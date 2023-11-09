from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from . import schemas


Base = declarative_base()


class Job(Base):
    __tablename__ = "jobs"

    id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String(128))
    location = Column(String(128))
    description = Column(String(1024))
    salary = Column(String(128))
    disable_category = Column(String(128))
