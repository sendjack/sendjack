"""

    sqlalchemy_db
    -------------

    Provide database access by using SQLAlchemy.

"""
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from util import environment
from base import Database

# The SQLAlchemy classes that our api uses.
Base = declarative_base()
Session = sessionmaker()


class SQLAlchemy(Database):

    PG_PREFIX = "postgres"
    DB_HOST = environment.get_unicode(unicode("PGHOST"))
    DB_PORT = environment.get_integer(unicode("PGPORT"))
    DB_DATABASE = environment.get_unicode(unicode("PGDATABASE"))
    DB_USER = environment.get_unicode(unicode("PGUSER"))
    DB_PASSWORD = environment.get_unicode(unicode("PGPASSWORD"))
    DB_URL = "{}://{}:{}@{}:{}/{}".format(
            PG_PREFIX,
            DB_USER,
            DB_PASSWORD,
            DB_HOST,
            DB_PORT,
            DB_DATABASE)


    def _set_up_db(self):
        engine = create_engine(self.DB_URL, echo=True)
        # create_all must be called after the api objects are imported.
        Base.metadata.create_all(engine)
        Session.configure(bind=engine)
