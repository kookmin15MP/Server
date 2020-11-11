from pytest import fixture
from sqlalchemy import create_engine

from api.models.user import User
from db import Base, Database
from settings.settings import DB_URI, NAME, PASSWOLRD, DB_PORT, HOST_ADDR
from settings.wsgi import create_wsgi

app = create_wsgi()

ID_NUM = 1234


@fixture()
def client(init_database):  # pytest용 클라이언트
    return app.test_client()


@fixture(scope='session')
def database():  # pytest용 일회용 데이터베이스
    engine = create_engine(f'postgresql://postgres:{PASSWOLRD}@{HOST_ADDR}:{DB_PORT}',
                           connect_args={'connect_timeout': 10})
    conn = engine.connect()
    conn.execute("COMMIT")

    conn.execute(f"DROP DATABASE IF EXISTS {NAME}")
    conn.execute("COMMIT")
    conn.execute(f"CREATE DATABASE {NAME}")
    conn.execute("COMMIT")
    conn.close()


@fixture()
def init_database(database):
    engine = create_engine(DB_URI, connect_args={'connect_timeout': 10})
    Base.metadata.create_all(engine)


@fixture()
def user(client):
    global ID_NUM
    ID_NUM = ID_NUM + 1
    with Database() as db:
        new_user = User(email=f'user{ID_NUM}@user.user',
                        pw='user123!@#', )
        db.add(new_user)
        db.commit()
        db.refresh(new_user)
        db.expunge(new_user)
    return new_user
