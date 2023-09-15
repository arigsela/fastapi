from fastapi import Body, FastAPI

app = FastAPI()

BOOKS = []

# GET Requests #


@app.get("/books")
def read_all_books():
    return BOOKS
