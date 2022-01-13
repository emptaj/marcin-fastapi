from pydantic import BaseModel
from typing import Optional

class Book(BaseModel):
    id: int
    title: str
    author: str

    class Config:
         orm_mode=True
    

class BookIn(BaseModel):
    title: Optional[str]
    author: Optional[str]

    class Config:
         orm_mode=True
