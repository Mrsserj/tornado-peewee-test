# coding=utf-8


from handlers import TestListHandler, CreateUserHandler, UserLoginHandler, UserLogoutHandler

url = [
    (r'/', TestListHandler),
    (r'/login', UserLoginHandler),
    (r'/registry', CreateUserHandler),
    (r'/logout', UserLogoutHandler),
    #(r'.*', PageNotFoundHandler),
]