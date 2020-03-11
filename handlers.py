from tornado.web import RequestHandler, authenticated
from tornado.escape import url_escape, json_encode
from models import User, UserTest
import asyncio


class BaseHandler(RequestHandler):
    def get_current_user(self):
        return self.get_secure_cookie("user")


class TestListHandler(BaseHandler):

    @authenticated
    async def get(self):
        tests = await self.application.objects.execute(UserTest.select().where(UserTest.is_public == True))
        self.render("index.html", title="Список тестов", items=tests)


class CreateUserHandler(BaseHandler):
    pass


class UserLoginHandler(BaseHandler):
    def get(self):
        self.render("login.html")

    async def post(self):
        username = self.get_argument("login", "")
        password = self.get_argument("password", "")
        auth = await self.application.objects.get(User, username=username, password=password)
        if auth:
            self.set_current_user(auth.username)
            self.redirect(self.get_argument("next", u"/"))
        else:
            error_msg = u"?error=" + url_escape("Login incorrect")
            self.redirect(u"/login" + error_msg)

    def set_current_user(self, user):
        if user:
            self.set_secure_cookie("user", json_encode(user))
        else:
            self.clear_cookie("user")


