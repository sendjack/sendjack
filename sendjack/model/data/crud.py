"""
    CRUD
    ----

    Provide an interface and implementation for CRUD operations on database
    backed objects. All database-backed objects should subclass.

"""
from sqlalchemy.orm.exc import NoResultFound

from database import Session


class CRUD(object):


    @classmethod
    def create(class_, object_dict):
        """Return a newly created instance of `class_`."""
        session = Session()
        object_ = class_(**object_dict)
        session.add(object_)

        # the next line is where the OperationalError is happening.
        session.commit()
        session.close()
        return object_


    @classmethod
    def read(class_, id):
        """Return an instance of `class_`."""
        session = Session()
        # the next line is where the OperationalError is happening.
        object_ = session.query(class_).get(id)

        if object_ is None:
            msg = "{} {} not found.".format(class_, id)
            raise NoResultFound(msg)

        session.expunge(object_)
        session.close()
        return object_


    @classmethod
    def update(class_, id, updated_dict):
        """Return an updated instance of `class_`."""
        session = Session()

        # TODO: this seems inefficient. we should probably be doing something
        # like INSERT...ON DUPLICATE KEY UPDATE....
        object_ = class_.read(id)
        session.add(object_)

        for k, v in updated_dict.items():
            setattr(object_, k, v)

        session.commit()
        session.close()
        return object_


    @classmethod
    def delete(class_, id):
        # session.close()
        raise NotImplementedError()
