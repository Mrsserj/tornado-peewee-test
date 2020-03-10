# coding=utf-8

import tornado.ioloop
import tornado.options
import tornado.httpserver
import asyncio
import os
import sys
from inspect import getmembers
from settings import db
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

    tornado.options.parse_command_line()
    http_server = tornado.httpserver.HTTPServer(application)
    if sys.platform == 'win32':
        asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
    port = int(os.environ.get("PORT", 5000))
    http_server.listen(port)
    print("server address is 0.0.0.0:", str(port))
    tornado.ioloop.IOLoop.instance().start()


if __name__ == "__main__":
    main()
