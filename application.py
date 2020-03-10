# coding=utf-8

from routes import url
import tornado.web

application = tornado.web.Application(
    handlers = url,
    template_path = "templates"
)
