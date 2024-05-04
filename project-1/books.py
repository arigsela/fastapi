from fastapi import Body, FastAPI


app = FastAPI()

BOOKS = [
    {"Title": "Book one", "Author": "Author one", "Category": "Science"},
    {"Title": "Book two", "Author": "Author two", "Category": "Science"},
    {"Title": "Book three", "Author": "Author three", "Category": "Math"},
    {"Title": "Book four", "Author": "Author four", "Category": "history"},
    {"Title": "Book five", "Author": "Author five", "Category": "history"},
    {"Title": "Book six", "Author": "Author six", "Category": "history"}
]

# GET Requests #


@app.get("/books")
def read_all_books():
    return BOOKS


# Path parameters
@app.get("/books/{book_title}")
def read_book(book_title: str):
    for book in BOOKS:
        if book.get('Title').casefold() == book_title.casefold():
            return book


# Query parameters
@app.get("/books/")
def read_category_by_query(category: str):
    books_to_return = []
    for book in BOOKS:
        if book.get('Category').casefold() == category.casefold():
            books_to_return.append(book)

    return books_to_return


@app.get("/books/{book_author}/")
async def read_category_by_query(book_author: str, category: str):
    books_to_return = []
    for book in BOOKS:
        if (book.get('Author').casefold() == book_author.casefold() and
                book.get('Category').casefold() == category.casefold()):
            books_to_return.append(book)

    return books_to_return

# POST Requests #


@app.post("/books/create_book")
async def create_book(new_book=Body()):
    BOOKS.append(new_book)


# PUT Requests #


@app.put("/books/update_book")
async def update_book(updated_book=Body()):
    for i in range(len(BOOKS)):
        if BOOKS[i].get('Title').casefold() == updated_book.get('Title').casefold():
            BOOKS[i] = updated_book
