from sqlalchemy import Column, Integer, String, Unicode

from db import Base


class User(Base):
    __tablename__ = 'User'

    id = Column(Integer, primary_key=True, autoincrement=True)
    email = Column(String, unique=True, nullable=False)
    pw = Column(String, nullable=False)
