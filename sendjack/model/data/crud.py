"""
    CRUD
    ----

    Provide an interface and implementation for CRUD operations on database
    backed objects. All database-backed objects should subclass.

"""
from functools import wraps
from sqlalchemy.exc import DatabaseError, OperationalError, ResourceClosedError
from sqlalchemy.orm.exc import NoResultFound

from database import db


def retry(fun):

    @wraps(fun)
    def _inner(*args, **kwargs):
        max_retries = kwargs.pop("max_retries", 3)

        for retries in xrange(max_retries + 1):
            try:
                return fun(*args, **kwargs)
            except (DatabaseError, OperationalError):
                if retries + 1 > max_retries:
                    print "ERROR with too many retries."
                    raise

    return _inner


class CRUD(object):


    @classmethod
    @retry
    def create(class_, object_dict):
        """Return a newly created instance of `class_`."""
        session = db().session()
        object_ = class_(**object_dict)
        session.add(object_)
        session.commit()

        return object_


    @classmethod
    @retry
    def read(class_, id):
        """Return an instance of `class_`."""
        session = db().session()
        object_ = session.query(class_).get(id)
        session.commit()

        if object_ is None:
            msg = "{} {} not found.".format(class_, id)
            raise NoResultFound(msg)

        return object_


    @classmethod
    @retry
    def update(class_, id, updated_dict):
        """Return an updated instance of `class_`."""
        session = db().session()
        object_ = class_.read(id)
        session.add(object_)

        # update the object with the new attributes
        for k, v in updated_dict.items():
            # only update attributes that have changed
            try:
                if getattr(object_, k) != v:
                    setattr(object_, k, v)
            except AttributeError:
                setattr(object_, k, v)

        # TODO: Fix this error.
        # Currently there are no effects from it.
        # the events are first on 'after_flush' and the returned object_
        # works.
        # TODO: Check if all the flush events fire, which object this occurs
        # on, and when it happens.
        try:
            session.commit()
        except ResourceClosedError as e:
            print "The ResourceError was introduced with after_flush events."
            print "but doesn't cause any noticable problems right now."
            print e

        return object_


    @classmethod
    @retry
    def delete(class_, id):
        # session.close()
        raise NotImplementedError()
