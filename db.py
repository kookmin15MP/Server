"""
Mobile Programing Team Project
수강신청 App Server Side
코드 작성자 20153159 김연수
"""
from sqlalchemy import create_engine, MetaData
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

from settings.settings import DB_URI

engine = create_engine(DB_URI, connect_args={'connect_timeout': 10})
Session = sessionmaker(bind=engine)
metadata = MetaData()
Base = declarative_base(metadata=metadata)


class Database:
    def __enter__(self):
        self.session = Session()
        return self.session

    def __exit__(self, type, value, traceback):
        self.session.close()
