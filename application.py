# coding=utf-8

from routes import url
import tornado.web
from peewee_async import Manager
import asyncio
from settings import db, login_url

loop = asyncio.new_event_loop()


application = tornado.web.Application(
    handlers=url,
    template_path="templates",
    login_url=login_url,
    cookie_secret="sdfsd7f68sf6sdfd8f7f6s8df68sl",
)

application.objects = Manager(db, loop=loop)