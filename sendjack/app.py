#!/usr/bin/env python
""" Module: app

Jackalope website to provide a sign up page.

"""
import tornado.httpserver
import tornado.ioloop
import tornado.web
from tornado.options import options

from settings import settings
from urls import url_patterns


class JackalopeApp(tornado.web.Application):

    """ The Tornado instance for Jackalope. """


    def __init__(self):
        """ Construct a Tornado application. """
        tornado.web.Application.__init__(self, url_patterns, **settings)


def main():
    """ main loop for Python script. """
    app = JackalopeApp()
    http_server = tornado.httpserver.HTTPServer(app)
    http_server.listen(options.port)
    tornado.ioloop.IOLoop.instance().start()


if __name__ == "__main__":
    main()
