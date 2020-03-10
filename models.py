from peewee_async import Manager
import peewee
from settings import db
import asyncio

loop = asyncio.new_event_loop()
__all__ = ["User", "UserTest", "Question", "Answer", "UserAnswer"]

class BaseModel(peewee.Model):
    """A base model that will use our Postgresql database"""
    class Meta:
        database = db


class User(BaseModel):
    username = peewee.CharField()
    password = peewee.CharField()
    first_name = peewee.CharField()
    last_name = peewee.CharField()
    age = peewee.IntegerField()


class UserTest(BaseModel):
    name = peewee.CharField()
    is_public = peewee.BooleanField(default=True)


class Question(BaseModel):
    test_ = peewee.ForeignKeyField(UserTest)
    order = peewee.IntegerField(default=10)
    text = peewee.CharField()


class Answer(BaseModel):
    quest = peewee.ForeignKeyField(Question)
    is_correct = peewee.BooleanField(default=False)
    text = peewee.CharField()


class UserAnswer(BaseModel):
    user_ = peewee.ForeignKeyField(User)
    answer = peewee.ForeignKeyField(Answer)


objects = Manager(db, loop=loop)
objects.database.allow_sync = False # this will raise AssertionError on ANY sync call