""" Module: settings

Settings for Tornado project.

"""
import os
import tornado
import tornado.template
from tornado.options import define, options
from jinja2 import Environment, PackageLoader

from jutil import environment


# Make filepaths relative to settings.
path = lambda root, *a: os.path.join(root, *a)
ROOT = os.path.dirname(os.path.abspath(__file__))

EMBEDDABLE_DOMAIN = environment.get_unicode(unicode("EMBEDDABLE_DOMAIN"))
PORT = environment.get_integer(unicode("PORT"), 5000)

# tornado config
define("port", default=PORT, help="run on the given port", type=int)
define("config", default=None, help="tornado config file")
define("debug", default=True, help="debug mode")
tornado.options.parse_command_line()

MEDIA_ROOT = path(ROOT, 'media')
TEMPLATE_ROOT = path(ROOT, 'view/templates')

# settings dictionary
settings = {}
settings['debug'] = options.debug
settings['static_path'] = MEDIA_ROOT
settings['cookie_secret'] = (
        "\xee\x0ec\x9bl\x02\xeb/.\xd4\xeb\xc2(\xb0\xb1\x8a\x0b\xb5[^Tq\xecy")
settings['xsrf_cookies'] = False
settings['login_url'] = "/"
settings['template_loader'] = tornado.template.Loader(TEMPLATE_ROOT)
settings['ui_modules'] = {}

# SERVICES
STRIPE_PUBLISHABLE_KEY = environment.get_unicode(
        unicode("STRIPE_PUBLISHABLE_KEY"))
STRIPE_SECRET_KEY = environment.get_unicode(unicode("STRIPE_SECRET_KEY"))

MIXPANEL_TOKEN = environment.get_unicode(unicode("MIXPANEL_TOKEN"))

JINJA2_ENVIRONMENT = Environment(
        loader=PackageLoader('app', 'view/templates'),
        trim_blocks=True)
JINJA2_ENVIRONMENT.globals['stripe_key'] = STRIPE_PUBLISHABLE_KEY
JINJA2_ENVIRONMENT.globals['mixpanel_token'] = MIXPANEL_TOKEN

MAILGUN_API_KEY = environment.get_unicode(unicode("MAILGUN_API_KEY"))
MAILGUN_DOMAIN = environment.get_unicode(unicode("MAILGUN_DOMAIN"))

JACKALOPE_NAME = unicode("Jackalope")
JACKALOPE_EMAIL = environment.get_unicode(unicode("JACKALOPE_EMAIL"))
