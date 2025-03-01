from sqlalchemy import Column, String
from database import Base

class Word(Base):
    __tablename__ = "words"

    word = Column(String, primary_key=True, index=True)
    theme = Column(String, index=True)
