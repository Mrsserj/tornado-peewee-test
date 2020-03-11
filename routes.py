# coding=utf-8


from handlers import TestListHandler, CreateUserHandler, UserLoginHandler, UserLogoutHandler, QuestionHandler, \
    PageNotFoundHandler, ResultHandler

url = [
    (r'/', TestListHandler),
    (r'/login', UserLoginHandler),
    (r'/registry', CreateUserHandler),
    (r'/logout', UserLogoutHandler),
    (r'/quest', QuestionHandler),
    (r'/result', ResultHandler),
    (r'.*', PageNotFoundHandler),
]