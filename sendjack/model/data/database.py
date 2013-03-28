"""

    database
    --------

    Provide an abstract database class and simple concrete subclasses. Also
    instantiate a couple of necessary database classes to make reference to
    instances and sessions simple and clean.

"""
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy import create_engine

from jutil import environment
from jutil.errors import OverrideRequiredError


class Database(object):


    def __init__(self, tables):
        self._init_db()


    def _init_db(self):
        raise OverrideRequiredError()


# SQLAlchemy classes for managing database access in this package
DeclarativeModel = declarative_base()


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


        # our dev instance of PostGres only allows for 20 connections across
        # all applications (Jackalope, SendJack, Prod/Staging/Warman/Hammer)
        engine = create_engine(
                url,
                #echo=True,
                #echo_pool=True,
                # As we have a lot of clients connecting to a 20 connection DB
                # simulataneously.
                pool_size=2,
                max_overflow=1,
                # As we are getting an EOF OperationalError after long breaks
                # without queries.
                pool_recycle=120)

        # create_all must be called after the objects are imported.
        DeclarativeModel.metadata.create_all(engine)

        session_factory = sessionmaker(bind=engine)
        self.session_constructor = scoped_session(session_factory)


    def session(self):
        return self.session_constructor()


db_singleton = None


def set_db(database):
    global db_singleton

    if db_singleton is None:
        db_singleton = database
    else:
        raise RuntimeError()


def db():
    global db_singleton

    return db_singleton
