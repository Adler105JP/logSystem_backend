from pydantic import BaseModel
from datetime import datetime
from uuid import UUID
from .log import Type_Severity

#-----------Log Schemas-----------

class LogBase(BaseModel):
    timestamp: datetime
    severity: Type_Severity
    source: str
    message: str | None = None

class LogCreate(LogBase):
    pass

class Log(LogBase):
    id: UUID
    user_id: UUID

    class Config:
        orm_mode = True


#-----------User Schemas-----------

class Token(BaseModel):
    access_token:str
    token_type:str
    username:str
    first_name:str
    last_name:str
    id:UUID

class UserBase(BaseModel):
    email: str
    user_name:str
    first_name:str
    last_name:str

class UserCreate(UserBase):
    password: str

class User(UserBase):
    id: UUID
    is_active: bool
    created_at: datetime
    updated_at: datetime
    logs: list[Log] = []

    class Config:
        orm_mode = True

