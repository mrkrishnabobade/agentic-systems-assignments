from fastapi import FastAPI,HTTPException
from pydantic import BaseModel
from typing import List
app= FastAPI()

class Book(BaseModel):
    title:str
    author:str
    year:int
    book_id:int

books:List[Book]=[]

#Lists the total books
@app.get("/books")
def get_books():
    return books
#adds the new book to the list
@app.post("/books")
def add_books(book:Book):
    books.append(book)
    return book
#return book based on the book id
@app.get("/book/{book_id}")
def get_book(book_id:int):
    if book_id<0 or book_id>=len(books):
        raise HTTPException(status_code=404,detail="Book not found ")
    return books[book_id]