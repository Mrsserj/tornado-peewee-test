# coding=utf-8

from routes import url
import tornado.web
from peewee_async import Manager
import asyncio
from settings import db

loop = asyncio.new_event_loop()


application = tornado.web.Application(
    handlers = url,
    template_path = "templates"
)

application.objects = Manager(db, loop=loop)