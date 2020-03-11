import peewee
from settings import db
from peewee_extra_fields import SimplePasswordField
from datetime import datetime

#loop = asyncio.new_event_loop()
__all__ = ["User", "UserTest", "Question", "Answer", "UserAnswer"]

class BaseModel(peewee.Model):
    """A base model that will use our Postgresql database"""
    class Meta:
        database = db


class User(BaseModel):
    username = peewee.CharField(unique=True)
    password = SimplePasswordField('weqwe')
    first_name = peewee.CharField(null=True)
    last_name = peewee.CharField(null=True)
    age = peewee.IntegerField(null=True)
    is_superuser = peewee.BooleanField(default=False)


class UserTest(BaseModel):
    name = peewee.CharField()
    is_public = peewee.BooleanField(default=True)


class Question(BaseModel):
    test_ = peewee.ForeignKeyField(UserTest)
    order = peewee.IntegerField(default=10)
    text = peewee.CharField()

    def get_answer(self):
        return Answer.select().where(Answer.quest == self)


class Answer(BaseModel):
    quest = peewee.ForeignKeyField(Question)
    is_correct = peewee.BooleanField(default=False)
    text = peewee.CharField()


class UserAnswer(BaseModel):
    resp_date = peewee.DateTimeField(default=datetime.now())
    user_ = peewee.ForeignKeyField(User)
    quest = peewee.ForeignKeyField(Question)
    answer = peewee.BooleanField(null=True)


#objects = Manager(db, loop=loop)
#objects.database.allow_sync = False # this will raise AssertionError on ANY sync call