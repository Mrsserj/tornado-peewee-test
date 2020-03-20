# coding=utf-8

import tornado.ioloop
import tornado.options
import tornado.httpserver
import asyncio
import sys
from inspect import getmembers
from settings import db, PORT
import models
from models import *

from application import application


def main():
    db.create_tables([m[1] for m in getmembers(models) if m[0] in models.__all__])
    if User.select().count() == 0:
        User.create(
            username='test',
            password='test12345',
            first_name='test',
            last_name='test',
            age=18,
            is_superuser=True
        )
    if UserTest.select().count() == 0:
        for i in range(2):
            UserTest.create(name=f'Когнитивные способности #{i + 1}')

    for tst in UserTest.select().where(UserTest.is_public is True):
        if Question.select().where(Question.test_ == tst).count() == 0:
            for i in range(2):
                Question.create(test_=tst, text=f'Трудный вопрос №{i + 1}')
    for q in Question.select():
        if Answer.select().where(Answer.quest == q).count() == 0:
            Answer.create(quest=q, text="Правильный ответ", is_correct=True)
            Answer.create(quest=q, text="Неправильный ответ")

    tornado.options.parse_command_line()
    http_server = tornado.httpserver.HTTPServer(application)
    if sys.platform == 'win32':
        asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
    http_server.listen(PORT)
    print(f'server address is 0.0.0.0:{PORT}')
    tornado.ioloop.IOLoop.instance().start()


if __name__ == "__main__":
    main()
