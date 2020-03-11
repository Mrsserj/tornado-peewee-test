from tornado.web import RequestHandler, authenticated
from tornado.escape import url_escape, json_encode
from models import User, UserTest, Question, Answer, UserAnswer


class BaseHandler(RequestHandler):
    def get_current_user(self):
        return self.get_secure_cookie("user")

    def get_user_model(self):
        user = User.select().where(User.username == self.get_current_user().decode('utf-8').strip('"')).first()
        return user



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

        awnsw = question.get_answer()

        return self.render("question.html", question=question, q_ids=';'.join([str(i) for i in q_ids]), awnsw=awnsw)

    @authenticated
    async def post(self):
        q_ids = self.get_argument("q_ids", "")
        q_id = self.get_argument("q_id", "")
        answer_id = self.get_argument("answer", "")
        answ = None
        user = self.get_user_model()
        if q_id:
            current_quest = Question.select().where(Question.id == int(q_id)).first()
        if answer_id:
            answ = Answer.select().where(Answer.id == int(answer_id)).first()

            if answ:
                current_quest = answ.quest

        if user:
            u_answ = await self.application.objects.get_or_create(UserAnswer,
                user_=user,
                quest=current_quest,
            )
            if answ and u_answ[1]:
                u_answ[0].answer = answ.is_correct
                await self.application.objects.update(u_answ[0])
        if q_ids:
            next_q_id = q_ids.split(';').pop(0)
            question = await self.application.objects.execute(Question.select()
                                                           .join(UserTest, on=(Question.test_ == UserTest.id))
                                                           .where(Question.id == int(next_q_id)))
            next_ids = q_ids.split(';')[1:]
        else:
            return self.redirect(f'/result?t_id={current_quest.test_.id}')
        return self.render("question.html",
                           question=question[0],
                           q_ids=';'.join(next_ids),
                           awnsw=question[0].get_answer())


class ResultHandler(BaseHandler):
    @authenticated
    async def get(self):
        t_id = self.get_argument("t_id", "")
        answ = await self.application.objects.execute(UserAnswer.select().join(Question).join(UserTest)
                                                      .where(UserTest.id == int(t_id),
                                                             UserAnswer.user_ == self.get_user_model()))

        if not answ:
            return self.redirect(f'/quest?tid={t_id}')
        return self.render("result.html", answers=answ, title=answ[0].quest.test_.name if answ else 'Тест не пройден')

class PageNotFoundHandler(BaseHandler):

    @authenticated
    def get(self):
        self.render("404.html")