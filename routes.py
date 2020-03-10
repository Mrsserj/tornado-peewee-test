# coding=utf-8


from handlers import VoteHandler, CreateUserHandler

url = [
    (r'/', VoteHandler),
    #(r'/login', UserLoginHandler),
    (r'/register', CreateUserHandler),
    #(r'/logout', UserLogoutHandler),
    #(r'.*', PageNotFoundHandler),
]