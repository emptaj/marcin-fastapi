import time
from fastapi import FastAPI, Response
from fastapi.middleware.cors import CORSMiddleware
from typing import List

from fastapi.exceptions import HTTPException
from models import Book, BookIn

BOOKS: List[Book] = [
    Book(id=0, title="Gruszki na wierzbie", author="Marcin Szyszka"),
    Book(id=1, title="Dziady", author="Adam Mickiewicz"),
    Book(id=2, title="Lalka", author="Bolesław Prus"),
    Book(id=3, title="Antygona", author="Sofokles"),
    Book(id=4, title="Chłopi", author="Władysław Stanisław Reymont"),
]

ID = 5

origins = [
    "http://localhost",
    "http://localhost:8000"
    "http://localhost:8080",
    "localhost",
    "null"
]

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/books")
async def get_books():
       return BOOKS


@app.get("/books/{id}")
async def get_book(id: int, response: Response):
       for book in BOOKS:
            if book.id == id:
                return book

       raise HTTPException(status_code=404,
                            detail="not found")


@app.post("/books/", status_code=201)
async def add_book(book: BookIn):
    global ID
    new_book = Book(id=ID, title=book.title, author=book.author)
    print(f"nowa ksiązka: {new_book}")
    BOOKS.append(new_book)
    ID += 1
    print(f"aktualnie książek: {ID}")
    time.sleep(0.5)
    return ID


@app.put("/books/{id}", status_code=201)
async def update_book(id: int, update_book: BookIn):
    for book in BOOKS:
        if book.id == id:
            if update_book.title:
                book.title = update_book.title 
            if update_book.author:
                book.author = update_book.author
            return book

    raise HTTPException(status_code=404,
    detail="not found")
