"""
    CRUD
    ----

    Provide an interface and implementation for CRUD operations on database
    backed objects. All database-backed objects should subclass.

"""
import json

from sqlalchemy.orm.exc import NoResultFound
from sqlalchemy.ext.declarative import DeclarativeMeta

from sqlalchemy_db import Session


class CRUD(object):


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
        object_ = session.query(class_).get(id)

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
    def delete(class_, id):
        raise NotImplementedError()


    @classmethod
    def search(class_, query):
        raise NotImplementedError()


    def json(self):
        return json.dumps(self, cls=SQLAlchemyEncoder(), check_circular=False)


#stackoverflow.com/questions/5022066/how-to-serialize-sqlalchemy-result-to-json
def SQLAlchemyEncoder():

    _visited_objects = []


    class _SQLAlchemyEncoder(json.JSONEncoder):

        def default(self, object_):
            if isinstance(object_.__class__, DeclarativeMeta):
                # don't re-visit self
                if object_ in _visited_objects:
                    return None
                _visited_objects.append(object_)

                # a SQLAlchemy class
                encodable = {}
                object_properties = [
                        x for x in dir(object_)
                        if not x.startswith('_') and x != 'metadata'
                        ]
                for key in object_properties:
                    encodable[key] = object_.__getattribute__(key)
                return encodable
            return json.JSONEncoder.default(self, object_)

    return _SQLAlchemyEncoder
