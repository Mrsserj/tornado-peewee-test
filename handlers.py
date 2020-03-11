from tornado.web import RequestHandler, authenticated
from tornado.escape import url_escape, json_encode
from models import User, UserTest, Question, Answer


class BaseHandler(RequestHandler):
    def get_current_user(self):
        return self.get_secure_cookie("user")


class TestListHandler(BaseHandler):

    @authenticated
    async def get(self):
        tests = await self.application.objects.execute(UserTest.select().where(UserTest.is_public == True))
        self.render("index.html", title="Список тестов", items=tests)


class CreateUserHandler(BaseHandler):
    def get(self):
        self.render("registry.html")

    def post(self):
        username = self.get_argument("login", "")
        password = self.get_argument("password", "")
        last_name = self.get_argument("last_name", "")
        first_name = self.get_argument("first_name", "")
        age = self.get_argument("age", 18)
        #TODO сделать проверки
        User.create(
            username=username,
            password=password,
            first_name=first_name,
            last_name=last_name,
            age=int(age)
        )
        self.redirect(u"/login")


class UserLoginHandler(BaseHandler):
    def get(self):
        self.render("login.html")

    async def post(self):
        username = self.get_argument("login", "")
        password = self.get_argument("password", "")
        auth = await self.application.objects.execute(User.select().where(User.username==username,
                                                                          User.password==password))
        if auth:
            self.set_current_user(auth[0].username)
            self.redirect(self.get_argument("next", u"/"))
        else:
            error_msg = u"?error=" + url_escape("Login incorrect")
            self.redirect(u"/login" + error_msg)

    def set_current_user(self, user):
        if user:
            self.set_secure_cookie("user", json_encode(user))
        else:
            self.clear_cookie("user")


class UserLogoutHandler(BaseHandler):
        def get(self):
            self.clear_cookie("user")
            self.redirect(self.get_argument("next", "/login"))


class QuestionHandler(BaseHandler):

    @authenticated
    async def get(self):
        tid = self.get_argument("tid", 0)
        question = None
        q_ids = []
        for q in await self.application.objects.execute(Question.select()
                                                           .join(UserTest, on=(Question.test_ == UserTest.id))
                                                           .where(UserTest.id == tid)
                                                           .order_by(Question.order, Question.id)):
            if not question:
                question = q
            else:
                q_ids.append(q.id)

        awnsw = await self.application.objects.execute(Answer.select()
                                                       .where(Answer.quest == question))

        return self.render("question.html", question=question, q_ids=';'.join(str(q_ids)), awnsw=awnsw)

class PageNotFoundHandler(BaseHandler):

    @authenticated
    def get(self):
        self.render("404.html")