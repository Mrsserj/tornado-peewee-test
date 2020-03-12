# coding=utf-8

from tornado.web import StaticFileHandler
from handlers import TestListHandler, CreateUserHandler, UserLoginHandler, UserLogoutHandler, QuestionHandler, \
    PageNotFoundHandler, ResultHandler

url = [
    (r'/', TestListHandler),
    (r'/login', UserLoginHandler),
    (r'/registry', CreateUserHandler),
    (r'/logout', UserLogoutHandler),
    (r'/quest', QuestionHandler),
    (r'/result', ResultHandler),
    (r'/(favicon.ico)', StaticFileHandler, {"path": "static"}),
    (r'.*', PageNotFoundHandler),
]