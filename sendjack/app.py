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

    # xheaders=True is critical to the health of our production site. it makes
    # sure the originating client IP, protocol, and port are included in the
    # request object instead of those set by the reverse proxy (heroku).
    http_server = tornado.httpserver.HTTPServer(app, xheaders=True)
    http_server.listen(options.port)

    tornado.ioloop.IOLoop.instance().start()


if __name__ == "__main__":
    main()
