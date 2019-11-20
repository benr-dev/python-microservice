import tornado.ioloop
import tornado.web
from entity.book_repository import BookRepository

book_repo = BookRepository()


class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.write("Book Repository v1.0")


def make_app():
    return tornado.web.Application([
        (r"/v1", MainHandler)
    ])


if __name__ == "__main__":
    app = make_app()
    app.listen(8888)
    tornado.ioloop.IOLoop.current().start()
