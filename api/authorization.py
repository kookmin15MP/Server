"""
Mobile Programing Team Project
수강신청 App Server Side
코드 작성자 20153159 김연수
"""
import bcrypt
from flask import Blueprint, jsonify
from werkzeug.exceptions import Conflict

from api.models.user import User
from settings.serialize import serialize
from settings.settings import SALT
from settings.utils import api, check_data

app = Blueprint('authorization', __name__, url_prefix='/api/authorization')


def encoder(pw):  # 패스워드를 해시 함수를 이용해 암호화 해주는 함수
    password_hash = bcrypt.hashpw(pw.encode(), SALT).decode()  # hash 암호화
    return password_hash


@app.route('/signup', methods=['POST'])
@api
def post_signup(data, db):  # 회원가입 수행 함수
    req_list = ['email', 'pw']
    check_data(data, req_list)  # 필수 파라미터 들어있는지 검사

    password_hash = encoder(data['pw'])  # 암호화

    new_user = User(email=data['email'],
                    pw=password_hash,
                    )  # 새로운 유저 생성

    db.add(new_user)
    db.commit()

    return jsonify(serialize(new_user))


@app.route('/signup', methods=['GET'])
@api
def get_signup(data, db):  # 이메일 중복 체크
    req_list = ['email']
    check_data(data, req_list)  # 필수 파라미터 들어있는지 검사

    query = db.query(User).filter(User.email == data['email']).first()  # email이 존재하는지 검색
    if query:  # 이미 존재하는 이메일
        raise Conflict

    return jsonify({'valid email': data['email']})


@app.route('/login', methods=['POST'])
@api
def post_login(data, db):  # 이메일과 패스워드로 로그인
    req_list = ['email', 'pw']
    check_data(data, req_list)  # 필수 파라미터 들어있는지 검사

    password_hash = encoder(data['pw'])  # 암호화
    query = db.query(User).filter(User.email == data['email'],
                                  User.pw == password_hash,
                                  ).first()  # 이메일과 암호화된 패스워드로 존재하는지 검사함
    if not query:  # id 또는 pw 오류
        raise Conflict

    return jsonify(serialize(query))
