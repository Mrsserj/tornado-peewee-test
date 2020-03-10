from tornado.web import RequestHandler
from models import User


class VoteHandler(RequestHandler):
    def get(self):
        self.render("index.html", title="Список тестов")


class CreateUserHandler(RequestHandler):
    pass