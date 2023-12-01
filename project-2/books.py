from typing import Optional
from fastapi import FastAPI, Path, Query, HTTPException
from pydantic import BaseModel, Field

app = FastAPI()


class Book:
    id: int
    title: str
    author: str
    description: str
    rating: int
    published_date: int

    def __init__(self, id, title, author, description, rating, published_date):
        self.id = id
        self.title = title
        self.author = author
        self.description = description
        self.rating = rating
        self.published_date = published_date


class BookRequest(BaseModel):
    id: Optional[int] = Field(title="id is not needed")
    title: str = Field(min_length=3)
    author: str = Field(min_length=1)
    description: str = Field(min_lenth=1, max_length=100)
    rating: int = Field(gt=1, lt=6)
    published_date: int = Field(gt=1900, lt=2099)

    class Config:
        json_schema_extra = {
            'example': {
                'id': None,
                'title': 'A new book',
                'author': 'codingwithroby',
                'description': 'A new desctiption of the book',
                'rating': 5,
                'published_date': 2000
            }
        }


BOOKS = [
    Book(1, "Computer Science PRo", "CodingWithRoby", "Very nice book", 5, 2012),
    Book(2, "Fast Api", "CodingWithRoby", "Very great book", 5, 2000),
    Book(3, "Master Endpoints", "CodingWithRoby", "Very awesome book", 5, 1999),
    Book(4, "HP1", "author 1", "book description 4 ", 2, 2023),
    Book(5, "HP2", "author 2", "book description 5", 3, 2022),
    Book(6, "HP3", "author 3", "book description 6", 1, 1982),
]

# GET Requests #


@app.get("/books")
async def read_all_books():
    return BOOKS


@app.get("/books/")
async def read_book_by_rating(book_rating: int = Query(gt=0, lt=6)):
    books_to_return = []
    for book in BOOKS:
        if book.rating == book_rating:
            books_to_return.append(book)
    return books_to_return


@app.get("/books/{book_id}")
async def read_book(book_id: int = Path(gt=0)):
    for book in BOOKS:
        if book.id == book_id:
            return book
    raise HTTPException(status_code=404, detail="Item not found")


@app.get("/books/publish/")
async def read_book_by_published_date(published_date: int = Query(gt=1900, lt=2099)):
    books_to_return = []
    for book in BOOKS:
        if book.published_date == published_date:
            books_to_return.append(book)
    return books_to_return



# POST requests #


@app.post("/create-book")
async def create_book(book_request: BookRequest):
    # Converting request to Book object
    new_book = Book(**book_request.model_dump())
    BOOKS.append(find_book_id(new_book))


# PUT Requests


@app.put("/books/update_book")
async def update_book(book: BookRequest):
    book_changed = False
    for i in range(len(BOOKS)):
        if BOOKS[i].id == book.id:
            BOOKS[i] = book
            book_changed = True
    if not book_changed:
        raise HTTPException(status_code=404, detail="Item not found")


# DELETE Requests


@app.delete("/books/{book_id}")
async def delete_book(book_id: int = Path(gt=0)):
    book_changed = False
    for i in range(len(BOOKS)):
        if BOOKS[i].id == book_id:
            BOOKS.pop(i)
            book_changed = True
            break
    if not book_changed:
        raise HTTPException(status_code=404, detail="Item not found")


def find_book_id(book: Book):
    #Ternary operator
    #book.id = 1 if len(BOOKS) == 0 else BOOKS[-1].id + 1

    if len(BOOKS) > 0:
        # Grab the last element in the list
        book.id = BOOKS[-1].id + 1
    else:
        book.id = 1

    return book
