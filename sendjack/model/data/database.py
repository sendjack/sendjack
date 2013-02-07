"""

    database
    --------

    Provide an abstract database class and simple concrete subclasses. Also
    instantiate a couple of necessary database classes to make reference to
    instances and sessions simple and clean.

"""
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine

from jutil import environment


class Database(object):


    def __init__(self, tables):
        self._init_db()


    def _init_db(self):
        print 'OverrideRequiredError'
        # raise OverrideRequiredError()


# SQLAlchemy classes for managing database access in this package
DeclarativeBase = declarative_base()
Session = sessionmaker()


class SQLAlchemy(Database):

    _PROTOCOL = "postgres"
    _USER = environment.get_unicode(unicode("PGUSER"))
    _PASSWORD = environment.get_unicode(unicode("PGPASSWORD"))
    _HOST = environment.get_unicode(unicode("PGHOST"))
    _PORT = environment.get_integer(unicode("PGPORT"))
    _PATH = environment.get_unicode(unicode("PGDATABASE"))


    def _init_db(self):
        # TODO: use a url utility package for this sort of thing.
        url = "{}://{}:{}@{}:{}/{}".format(
                self._PROTOCOL,
                self._USER,
                self._PASSWORD,
                self._HOST,
                self._PORT,
                self._PATH)
        engine = create_engine(url, echo=True)

        # create_all must be called after the objects are imported.
        DeclarativeBase.metadata.create_all(engine)

        Session.configure(bind=engine)
