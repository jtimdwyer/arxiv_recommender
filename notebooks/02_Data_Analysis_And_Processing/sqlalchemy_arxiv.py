# This loads the table classes and sessionmaker for connecting
# to the postgres database serving all of the arxiv infomation

from sqlalchemy import create_engine, Column, String, Integer, DATE, BOOLEAN, Float, ARRAY, JSON
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

import json

Base = declarative_base()

class articles_base:
    id = Column(String, primary_key=True)
    created = Column(DATE)
    setspec = Column(String)
    title = Column(String)
    abstract = Column(String)
    
class articles_raw(Base, articles_base):
    __tablename__ = 'arxiv_raw'

class articles_detex(Base, articles_base):
    __tablename__ = 'arxiv_detex'
    title_converted = Column(BOOLEAN)
    abstract_converted = Column(BOOLEAN)

class articles_pandoc(Base, articles_base):
    __tablename__ = 'arxiv_pandoc'
    title_converted = Column(BOOLEAN)
    abstract_converted = Column(BOOLEAN)
    
class articles_similar(Base):
    __tablename__ = 'arxiv_similar'
    id = Column(String, primary_key=True)
    recs = Column(JSON)

    
class articles_vectors(Base):
    __tablename__ = 'arxiv_vectors'
    id = Column(String, primary_key=True)
    for num in range(300):
        exec(f"comp_{num} = Column(Float)")

def create_session_maker():
    with open('../../postgres.json') as pg_info:
        pg_json = json.load(pg_info)
        pg_username = pg_json['pg_username']
        pg_password = pg_json['pg_password']
        pg_ip = pg_json['pg_ip']

    engine = f'postgres://{pg_username}:{pg_password}@{pg_ip}:5432'
    engine = create_engine(engine)
    Session = sessionmaker(bind=engine)

    return Session

Session = create_session_maker()