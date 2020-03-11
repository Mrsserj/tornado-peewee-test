# coding=utf-8


from handlers import TestListHandler, CreateUserHandler, UserLoginHandler, UserLogoutHandler, QuestionHandler, \
    PageNotFoundHandler

url = [
    (r'/', TestListHandler),
    (r'/login', UserLoginHandler),
    (r'/registry', CreateUserHandler),
    (r'/logout', UserLogoutHandler),
    (r'/quest', QuestionHandler),
    (r'.*', PageNotFoundHandler),
]