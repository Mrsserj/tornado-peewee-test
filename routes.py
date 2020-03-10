# coding=utf-8


from handlers import TestListHandler, CreateUserHandler

url = [
    (r'/', TestListHandler),
    #(r'/login', UserLoginHandler),
    (r'/register', CreateUserHandler),
    #(r'/logout', UserLogoutHandler),
    #(r'.*', PageNotFoundHandler),
]