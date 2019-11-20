import json


class BookRepository:

    def __init__(self):
        self.books = []

    def add_book(self, author, title):
        book = {"Author": author, "Title": title}
        self.books.append(book)
        print("Book: {0}".format(book))
        return json.dumps(book)

    def find_books_by_author(self, author):
        response = []
        for idx, book in enumerate(self.books):
            if book["Author"] == author:
                response.append(book)
        return response

    def remove_book(self, title):
        found = False
        for idx, book in enumerate(self.books):
            if book["Title"] == title:
                found = True
                del self.books[idx]
        print("Books: {0}".format(json.dumps(self.books)))
        return found

    def get_all_books(self):
        return self.books

    def json_list(self):
        return json.dumps(self.books)
