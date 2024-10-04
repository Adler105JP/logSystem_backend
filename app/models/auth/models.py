
from sqlalchemy import Table, Boolean, Column, Integer, String, DateTime
from sqlalchemy_utils import UUIDType
from app.db.database import Base
import uuid
from datetime import datetime

class User(Base):
    __tablename__ = 'user'

    id = Column(UUIDType(binary=False), primary_key=True, default=uuid.uuid4)
    user_name = Column(String(50), unique=True, nullable=False)
    email = Column(String(255), unique=True)
    password = Column(String(255))
    is_active = Column(Boolean, default=True)
    created_at = Column(DateTime, default=datetime.now)
    updated_at = Column(DateTime, default=datetime.now)
    first_name = Column(String(100))
    last_name = Column(String(100))