import bcrypt
from flask import blueprints, jsonify
from werkzeug.exceptions import BadRequest, Conflict

from api.models.user import User
from settings.serialize import serialize
from settings.settings import SALT
from settings.utils import api

app = blueprints('authorization', __name__, url_prefix='/api/authorization')


def encoder(pw):
    password_hash = bcrypt.hashpw(pw.encode(), SALT)  # hash 암호화
    return password_hash


@app.route('/signup', methods=['POST'])
@api
def post_signup(data, db):  # 회원가입 수행 함수
    req_list = ['email', 'pw']
    for i in req_list:  # 필수 요소 검사
        if i not in data:
            raise BadRequest

    password_hash = encoder(data['pw'])  # 암호화

    new_user = User(email=data['email'],
                    pw=password_hash,
                    )

    db.add(new_user)
    db.commit()

    return jsonify(serialize(new_user))


@app.route('/signup', methods=['GET'])
@api
def get_signup(data, db):  # 이메일 중복 체크
    req_list = ['email']
    for i in req_list:  # 필수 요소 검사
        if i not in data:
            raise BadRequest

    query = db.query(User).filter(User.email == data['email']).first()  # email이 존재하는지 검색
    if query:  # 이미 존재하는 이메일
        raise Conflict

    return jsonify({'valid email': data['email']})


@app.route('/login', methods=['POST'])
@api
def post_login(data, db):  # 이메일과 패스워드로 로그인
    req_list = ['email', 'pw']
    for i in req_list:  # 필수 요소 검사
        if i not in data:
            raise BadRequest

    password_hash = encoder(data['pw'])  # 암호화
    query = db.query(User).filter(User.email == data['email'],
                                  User.pw == password_hash,
                                  ).first()
    if not query:  # id 또는 pw 오류
        raise Conflict

    return jsonify(serialize(query))
