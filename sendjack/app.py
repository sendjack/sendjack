#!/usr/bin/env python
"""
    Jackalope: SendJack
    -------------------

    Run Jackalope's SendJack application.

"""
import tornado.httpserver
import tornado.ioloop
import tornado.web
from tornado.options import options

from redflag import redflag

import settings
from url.patterns import url_patterns
from event import event


class SendJackApp(tornado.web.Application):

    """ The Tornado instance for SendJack. """


    def __init__(self):
        """ Construct a Tornado application. """
        settings_dict = settings.settings
        tornado.web.Application.__init__(self, url_patterns, **settings_dict)

        self.initialize_mailer()
        event.initialize()

    def initialize_mailer(self):
        redflag.initialize(
                settings.MAILGUN_API_KEY,
                settings.MAILGUN_DOMAIN,
                settings.JACKALOPE_EMAIL,
                settings.JACKALOPE_NAME)


def main():
    """ main loop for Python script. """
    app = SendJackApp()
    http_server = tornado.httpserver.HTTPServer(app)
    http_server.listen(options.port)
    tornado.ioloop.IOLoop.instance().start()


if __name__ == "__main__":
    main()
