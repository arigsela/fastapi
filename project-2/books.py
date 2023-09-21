from fastapi import Body, FastAPI

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
