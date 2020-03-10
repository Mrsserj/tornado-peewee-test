from tornado.web import RequestHandler
from models import User, UserTest
import asyncio


class TestListHandler(RequestHandler):
    async def get(self):
        tests = await self.application.objects.execute(UserTest.select().where(UserTest.is_public == True))
        self.render("index.html", title="Список тестов", items=tests)


class CreateUserHandler(RequestHandler):
    pass