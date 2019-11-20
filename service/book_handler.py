from typing import Optional, Awaitable

import tornado.web
import json
import entity.book_repository


class BookHandler(tornado.web.RequestHandler):
    book_repository: entity.book_repository.BookRepository

    def initialize(self, book_repository) -> None:
        """

        :type book_repository: entity.book_repository.BookRepository
        """
        self.book_repository = book_repository

    def prepare(self) -> Optional[Awaitable[None]]:
        if self.request.headers.get("Content-Type", "").startswith("application/json"):
            self.json_args = json.loads(self.request.body)
        else:
            self.json_args = None

    def get(self):
        author = self.get_arguments("author")

        if "author" in author:
            self.write(self.book_repository.find_books_by_author(author[0]))
        else:
            self.write(json.dumps(self.book_repository.get_all_books()))

    def post(self):
        author = self.json_args["author"]
        title = self.json_args["title"]
        book = self.book_repository.add_book(author, title)
        self.write(book)

    def data_received(self, chunk: bytes) -> Optional[Awaitable[None]]:
        pass

