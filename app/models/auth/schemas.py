from pydantic import BaseModel
from datetime import datetime
from uuid import UUID

class Token(BaseModel):
    access_token:str
    token_type:str
    username:str
    first_name:str
    last_name:str

class UserBase(BaseModel):
    email: str
    user_name:str
    first_name:str
    last_name:str

class UserCreate(UserBase):
    password: str

class UserShow(UserBase):
    id: UUID
    is_active: bool
    created_at: datetime
    updated_at: datetime

    class Config:
        orm_mode = True