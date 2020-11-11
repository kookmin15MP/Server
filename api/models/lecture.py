from sqlalchemy import Column, Integer, String, ForeignKey, Boolean

from db import Base


class Lecture(Base):
    __tablename__ = 'lecture'

    id = Column(Integer, primary_key=True, autoincrement=True)
    lecture_name = Column(String, nullable=False, unique=False)  # 강의명
    professor_name = Column(String, nullable=False, unique=False)  # 교수
    lecture_time = Column(String, nullable=False, unique=False)  # 수업 시간
    limited_people = Column(Integer, nullable=False, unique=False)  # 최대 수용 인원


class Basket(Base):
    __tablename__ = 'basket'

    id = Column(Integer, primary_key=True, autoincrement=True)
    user_id = Column(Integer, ForeignKey('user.id'))  # 유저 아이디
    lecture_id = Column(Integer, ForeignKey('lecture.id'))  # 강의 아이디
    is_valid = Column(Boolean, nullable=False, unique=False, default=True)  # 수강신청 성공이나 삭제시 무효화


class Registration(Base):
    __tablename__ = 'registration'

    id = Column(Integer, primary_key=True, autoincrement=True)
    user_id = Column(Integer, ForeignKey('user.id'))  # 유저 아이디
    lecture_id = Column(Integer, ForeignKey('lecture.id'))  # 강의 아이디
