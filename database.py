from datetime import datetime, date
from sqlalchemy import Date

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.orm import sessionmaker

engine = create_engine('sqlite:///todo.db?check_same_thread=False')

Session = sessionmaker(bind=engine)
session = Session()

Base = declarative_base()


# creating the table
class Table(Base):
    __tablename__ = "task"

    id = Column(Integer, primary_key=True)
    task = Column(String, default='default_value')
    deadline = Column(Date, default=date.today())

    def __repr__(self):
        return self.string_field


Base.metadata.create_all(engine)
