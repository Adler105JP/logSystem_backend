from fastapi import APIRouter, Depends, status, Response, HTTPException
from sqlalchemy import Enum
from sqlalchemy.orm import Session
from app.db.database import get_db
from app.models import schemas, log as Model
from fastapi.security import OAuth2PasswordBearer
from app.api.auth.ofuscator import verify_token

router = APIRouter(
    prefix="/api",
    tags=["api"],
)

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="user/login")

@router.get("/logs/{user_id}", status_code=status.HTTP_200_OK, response_model=list[schemas.Log])
def get_logs_from_user_id(
    user_id,
    token: str = Depends(oauth2_scheme),
    db: Session = Depends(get_db)
):
    verify_token (token)
    logs = db.query(Model.Log).filter(Model.Log.user_id == user_id).all()
    return logs

@router.post("/log/{user_id}", status_code=status.HTTP_201_CREATED, response_model=schemas.Log)
def create_log(
    user_id,
    item: schemas.LogCreate,
    token: str = Depends(oauth2_scheme),
    db: Session = Depends(get_db)
):
    verify_token (token)
    newLog = Model.Log(
        **item.model_dump(),
        user_id=user_id
    )

    db.add(newLog)
    db.commit()
    db.refresh(newLog)

    return newLog

@router.delete("/log/{id}/user/{user_id}", status_code=status.HTTP_202_ACCEPTED)
def delete_log(
    id,
    user_id,
    token: str=Depends(oauth2_scheme),
    db: Session = Depends(get_db)
):
    verify_token (token)
    logToUpdate = db.query(Model.Log).filter(Model.Log.id == id, Model.Log.user_id == user_id)

    if not logToUpdate.first():
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"User with the id={id} is not found"
        )
    
    logToUpdate.delete()
    db.commit()

    return { 
        "result":1, 
        "msg":"OK" 
    }


@router.put("/log/{id}/user/{user_id}", status_code=status.HTTP_202_ACCEPTED)
def update_log(
    id,
    user_id,
    payload: schemas.LogCreate,
    token: str=Depends(oauth2_scheme),
    db: Session = Depends(get_db)
):
    verify_token (token)
    logToUpdate = db.query(Model.Log).filter(Model.Log.id == id, Model.Log.user_id == user_id)

    if not logToUpdate.first():
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"User with the id={id} is not found"
        )
    
    params = payload.model_dump(exclude_unset=True)

    logToUpdate.update(params)
    db.commit()

    return { 
        "result":1, 
        "msg":"OK" 
    }
