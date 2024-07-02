from fastapi import FastAPI
from pydantic import BaseModel, Field, field_validator
from datetime import datetime
from typing import Any


app = FastAPI()


class Book(BaseModel):
    id: int
    title: str
    year: int = Field(..., gt=1500, le=datetime.now().year)
    isbn: int = None


    @field_validator('isbn')
    @classmethod
    def check_isbn(cls, value: Any):
        if value is not None and len(value) != 13:
            raise ValueError('Value must contain of 13 digits')
        if value is not None and not value.isdigit():
            raise ValueError('Value must be digit')
        return value


books = []


@app.get('/books/')
def all_books():
    return books


@app.post('/books/', status_code=201)
def create_book(book: Book):
    book_id = len(books) + 1
    new_book = Book(id=book_id, **book.dict())
    books.append(new_book)
    return new_book
