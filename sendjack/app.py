#!/usr/bin/env python
"""
    Jackalope: SendJack
    -------------------

    Run Jackalope application.

"""
import tornado.httpserver
import tornado.ioloop
import tornado.web
from tornado.options import options

from redflag import redflag

import settings
from urls import url_patterns


class JackalopeApp(tornado.web.Application):

    """ The Tornado instance for Jackalope. """


    def __init__(self):
        """ Construct a Tornado application. """
        settings_dict = settings.settings
        tornado.web.Application.__init__(self, url_patterns, **settings_dict)

        self.initialize_mailer()


    def initialize_mailer(self):
        redflag.initialize(
                settings.MAILGUN_API_KEY,
                settings.MAILGUN_DOMAIN,
                "jack@sendjack.com")


def main():
    """ main loop for Python script. """
    app = JackalopeApp()
    http_server = tornado.httpserver.HTTPServer(app)
    http_server.listen(options.port)
    tornado.ioloop.IOLoop.instance().start()


if __name__ == "__main__":
    main()
