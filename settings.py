""" Module: settings

Settings for Tornado project.

"""
import tornado
import tornado.template
import os
from tornado.options import define, options


# Make filepaths relative to settings.
path = lambda root, *a: os.path.join(root, *a)
ROOT = os.path.dirname(os.path.abspath(__file__))

# tornado config
PORT = os.environ.get("PORT", 5000)
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
settings['xsrf_cookies'] = True
settings['login_url'] = "/"
settings['template_loader'] = tornado.template.Loader(TEMPLATE_ROOT)
settings['ui_modules'] = {}
