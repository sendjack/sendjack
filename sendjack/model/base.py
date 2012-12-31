"""
    base api object
    ---------------

    Provide an interface and implementation for CRUD operations on database
    backed objects. All database backed API objects should subclass.

"""
from sqlalchemy.orm.exc import NoResultFound

from data.sqlalchemy_db import Session


class APIBase(object):


    @classmethod
    def create(class_, object_dict):
        """Return a newly created instance of `class_`."""
        session = Session()
        object_ = class_(**object_dict)
        session.add(object_)

        session.commit()
        return object_


    @classmethod
    def read(class_, id):
        """Return an instance of `class_`."""
        session = Session()
        object_ = session\
                .query(class_)\
                .get(id)

        if object_ is None:
            msg = "{} {} not found.".format(class_, id)
            raise NoResultFound(msg)

        session.expunge(object_)
        return object_


    @classmethod
    def update(class_, id, updated_dict):
        """Return an updated instance of `class_`."""
        session = Session()
        object_ = class_.read(id)
        session.add(object_)

        for k, v in updated_dict.items():
            setattr(object_, k, v)

        session.commit()
        return object_


    @classmethod
    def delete(class_):
        pass
