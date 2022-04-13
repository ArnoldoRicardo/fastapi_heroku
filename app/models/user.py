from app.db.base_class import Base
from sqlalchemy import Boolean, Column, Integer, String


class User(Base):
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True, nullable=False)
    hasshed_password = Column(String, nullable=False)
    disable = Column(Boolean, default=False)
