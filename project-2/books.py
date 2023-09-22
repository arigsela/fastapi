from typing import Optional
from fastapi import FastAPI
from pydantic import BaseModel, Field

app = FastAPI()


class Book:
    id: int
    title: str
    author: str
    description: str
    rating: int

    def __init__(self, id, title, author, description, rating):
        self.id = id
        self.title = title
        self.author = author
        self.description = description
        self.rating = rating


class BookRequest(BaseModel):
    id: Optional[int] = Field(title="id is not needed")
    title: str = Field(min_length=3)
    author: str = Field(min_length=1)
    description: str = Field(min_lenth=1, max_length=100)
    rating: int = Field(gt=1, lt=6)


class Config:
    json_schema_extra = {

    }

BOOKS = [
    Book(1, "Computer Science PRo", "CodingWithRoby", "Very nice book", 5),
    Book(2, "Fast Api", "CodingWithRoby", "Very great book", 5),
    Book(3, "Master Endpoints", "CodingWithRoby", "Very awesome book", 5),
    Book(4, "HP1", "author 1", "book description 4 ", 2),
    Book(5, "HP2", "author 2", "book description 5", 3),
    Book(6, "HP3", "author 3", "book description 6", 1),
]

# GET Requests #


@app.get("/books")
async def read_all_books():
    return BOOKS


# POST requests #


@app.post("/create-book")
async def create_book(book_request: BookRequest):
    # Converting request to Book object
    new_book = Book(**book_request.model_dump())
    BOOKS.append(find_book_id(new_book))


def find_book_id(book: Book):
    #Ternary operator
    #book.id = 1 if len(BOOKS) == 0 else BOOKS[-1].id + 1

    if len(BOOKS) > 0:
        # Grab the last element in the list
        book.id = BOOKS[-1].id + 1
    else:
        book.id = 1

    return book
