from sqlalchemy import Column, String, DateTime, ForeignKey, Enum
from sqlalchemy_utils import UUIDType
from app.db.database import Base
import uuid
from datetime import datetime
from sqlalchemy.orm import relationship
from enum import Enum as Py_Enum

class Type_Severity(Py_Enum):
    LOW = 0
    NORMAL = 1
    HIGTH = 2
    IMMEDIATE = 3

class Log(Base):
    __tablename__ = "log"
    __table_args__= {
        "mysql_engine":"InnoDB"
    }

    id = Column(UUIDType(binary=False), primary_key=True, default=uuid.uuid4)
    user_id = Column(UUIDType(binary=False), ForeignKey("user.id", ondelete="CASCADE"), nullable=False)
    timestamp = Column(DateTime, default=datetime.now)
    severity = Column(Enum(Type_Severity), default=Type_Severity.NORMAL)
    source = Column(String(100))
    message = Column(String(500))

    owner_user = relationship("User", back_populates="logs")