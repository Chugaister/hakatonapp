from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from db.config import *


engine = create_engine(DB_URL)
Session = sessionmaker(bind=engine)
