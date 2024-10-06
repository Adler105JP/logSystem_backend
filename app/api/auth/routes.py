from typing import List
from fastapi import APIRouter, Depends, status, Response, HTTPException
from sqlalchemy.orm import Session
from app.db.database import get_db
from app.models import schemas, user
from datetime import datetime
from .ofuscator import get_password_hash, verify_password, create_access_token
from fastapi.security import OAuth2PasswordBearer
from fastapi.security import OAuth2PasswordRequestForm

router = APIRouter(
    prefix="/user",
    tags=["user"],
)

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="user/login")

@router.post('/login', response_model=schemas.Token)
def login(
    payload: OAuth2PasswordRequestForm = Depends(),
    db: Session = Depends(get_db)
):
    user = db.query(user.User).filter(
        (user.User.user_name == payload.username) or (user.User.email == payload.username)
    ).first()

    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid user credentials"
        )
    
    if not verify_password(payload.password, user.password):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid user credentials"
        )
    
    return {
        "access_token": create_access_token({
            "first_name":user.first_name,
            "last_name":user.last_name,
        }),
        "token_type": "bearer",
        "username":user.user_name,
        "first_name":user.first_name,
        "last_name":user.last_name,
        "id":user.id

    }

@router.post("/signup")
def create_user(request: schemas.UserCreate, db: Session = Depends(get_db)):
    new_user = user.User(
        email=request.email,
        password=get_password_hash(request.password),
        user_name=request.user_name,
        first_name=request.first_name,
        last_name = request.last_name
    )
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user


@router.get("/", response_model=List[schemas.User])
def all_fetch(
    token: str = Depends(oauth2_scheme),
    db: Session = Depends(get_db)
):
    users = db.query(user.User).all()
    return users


@router.get("/{id}", status_code=status.HTTP_200_OK, response_model=schemas.User)
def show(id, response: Response, db: Session = Depends(get_db)):
    user = db.query(user.User).filter(user.User.id == id).first()

    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"User with hte id={id} is not available."
        )

    return user




@router.put("/{id}", status_code=status.HTTP_202_ACCEPTED)
def update(id, request: schemas.UserBase, db: Session = Depends(get_db)):
    user = db.query(user.User).filter(user.User.id == id)

    if not user.first():
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"User with the id={id} is not found"
        )

    param = request.model_dump()
    param["update_at"] = datetime.now()

    user.update(param)
    db.commit()

    return "Updated"


@router.delete("/{id}", status_code=status.HTTP_202_ACCEPTED)
def delete(id, db: Session = Depends(get_db)):
    user = db.query(user.User).filter(user.User.id == id)

    if not user.first():
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"User with the id={id} is not found"
        )

    param = {"is_active": False}
    user.update(param)
    db.commit()

    return "Deleted"
