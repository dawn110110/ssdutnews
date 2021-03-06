#!/usr/bin/env python
#encoding=utf-8
'''db'''
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base
import config
import tornado.database

NewsDatabase = tornado.database.Connection(
    "127.0.0.1:3306",
    "ssdutnews",
    "ssdutnews",
    "ssdutnewsplayswell",
)

engine = create_engine(config.db_config,
                       pool_recycle=1)
db_session = scoped_session(sessionmaker(autocommit=False,
                                         autoflush=False,
                                         bind=engine))
ses = db_session  # short name

Base = declarative_base()
Base.query = db_session.query_property()


def init_db():
    import models
    Base.metadata.create_all(bind=engine)
