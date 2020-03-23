# coding=utf-8

from tornado.web import StaticFileHandler, url
from handlers import TestListHandler, CreateUserHandler, UserLoginHandler, UserLogoutHandler, QuestionHandler, \
    PageNotFoundHandler, ResultHandler

urls = [
    url(r'/', TestListHandler),
    url(r'/login', UserLoginHandler),
    url(r'/registry', CreateUserHandler),
    url(r'/logout', UserLogoutHandler, name='UserLogoutHandler'),
    url(r'/quest', QuestionHandler),
    url(r'/result', ResultHandler, name='ResultHandler'),
    url(r'/(favicon.ico)', StaticFileHandler, {"path": "static"}),
    url(r'.*', PageNotFoundHandler),
]
