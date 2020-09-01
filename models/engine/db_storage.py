#!/usr/bin/python3
""" Doc """
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from os import getenv
from models.base_model import Base
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review


class DBStorage:
    """ class db storage """
    __engine = None
    __session = None

    def __init__(self):
        """initilize"""
        DBStorage.__engine = create_engine("mysql+mysqldb://{}:{}@{}/{}"
                                           .format(getenv("HBNB_MYSQL_USER"),
                                                   getenv("HBNB_MYSQL_PWD"),
                                                   getenv("HBNB_MYSQL_HOST"),
                                                   getenv("HBNB_MYSQL_DB")),
                                           pool_pre_ping=True)
        if getenv('HBNB_ENV') == "test":
            Base.metadata.drop_all(bind=DBStorage.__engine)

    def all(self, cls=None):
        """see all"""
        if cls:
            o_query = DBStorage.__session.query(cls).all()
            objs = {}
            for obj in o_query:
                objs.update({obj.to_dict()['__class__'] + '.' + obj.id: obj})
            return objs
        else:
            o_query = DBStorage.__session.query(User, State, City, Amenity,
                                                Place, Review).all()
            objs = {}
            for obj in o_query:
                objs.update({obj.to_dict()['__class__'] + '.' + obj.id: obj})
            return objs

    def new(self, obj):
        """ Doc """
        self.__session.add(obj)

    def save(self):
        """ Doc """
        self.__session.commit()

    def update(self, obj=None):
        """ update """
        if obj:
            self.__session.delete(obj)

    def reload(self):
        """ reload db"""
        Base.metadata.create_all(self.__engine)
        session_factory = sessionmaker(bind=DBStorage.__engine,
                                       expire_on_commit=False)
        Session = scoped_session(session_factory)
        DBStorage.__session = Session()

    def close(self):
        self.__session.close()
