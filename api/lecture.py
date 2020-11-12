"""
Mobile Programing Team Project
수강신청 App Server Side
코드 작성자 20153159 김연수
"""
from flask import Blueprint, jsonify
from werkzeug.exceptions import NotFound, Conflict

from api.models.lecture import Lecture, Basket, Registration
from settings.serialize import serialize
from settings.utils import api, check_data

app = Blueprint('teach', __name__, url_prefix='/api/lecture')


@app.route('/info', methods=['POST'])
@api
def post_lecture_info(data, db):  # 수업 생성
    req_list = ['lecture_name', 'professor_name', 'lecture_time', 'limited_people']
    check_data(data, req_list)  # 필수 파라미터 들어있는지 검사

    new_lecture = Lecture(lecture_name=data['lecture_name'],  # 새로운 수업을 생성함
                          professor_name=data['professor_name'],
                          lecture_time=data['lecture_time'],
                          limited_people=data['limited_people'])
    db.add(new_lecture)
    db.commit()

    return jsonify(serialize(new_lecture))


@app.route('/info', methods=['GET'])
@api
def get_lecture_info(data, db):  # 모든 수업을 가져옴
    # 필요 인자 없음

    lectures = db.query(Lecture).all()  # 모든 수업을 불러옴

    return jsonify(serialize(lectures))


@app.route('/basket', methods=['POST'])
@api
def post_lecture_basket(data, db):  # 장바구니 추가
    req_list = ['user_id', 'lecture_id']
    check_data(data, req_list)  # 필수 파라미터 들어있는지 검사

    new_basket = Basket(lecture_id=data['lecture_id'],  # 장바구니에 새로운 수업을 생성함
                        user_id=data['user_id'], )
    db.add(new_basket)
    db.commit()

    return jsonify(serialize(new_basket))


@app.route('/basket', methods=['GET'])
@api
def get_lecture_basket(data, db):  # 장바구니 불러오기
    req_list = ['user_id']
    check_data(data, req_list)  # 필수 파라미터 들어있는지 검사

    baskets = db.query(Basket).filter(Basket.user_id == data['user_id'],  # 해당 유저의 장바구니를 가져옴
                                      Basket.is_valid.is_(True), ).all()
    if not baskets:  # 장바구니에 담긴게 없음
        raise NotFound
    return jsonify(serialize(baskets))


@app.route('/basket', methods=['DELETE'])
@api
def delete_lecture_basket(data, db):  # 장바구니에서 무효화
    req_list = ['basket_id']
    check_data(data, req_list)  # 필수 파라미터 들어있는지 검사

    basket = db.query(Basket).filter(Basket.id == data['basket_id']).first()  # 해당 장바구니 수업을 가져옴
    basket.is_valid = False  # 해당 수업을 장바구니에서 무효화함
    db.commit()

    return jsonify({})


@app.route('/registration', methods=['POST'])
@api
def post_registration(data, db):  # 수강신청
    req_list = ['lecture_id', 'user_id']
    check_data(data, req_list)  # 필수 파라미터 들어있는지 검사

    lecture = db.query(Lecture).filter(Lecture.id == data['lecture_id']).first()  # 수강신청할 수업을 가져옴
    if not lecture:  # 해당 수업이 존재하지 않음
        raise NotFound

    registrations = db.query(Registration).filter(
        Registration.lecture_id == data['lecture_id']).all()  # 수강신청한 사람들을 모두 가져옴
    if len(registrations) >= lecture.limited_people:  # 수강신청 인원 초과
        raise Conflict

    new_registration = Registration(user_id=data['user_id'],  # 수강신청을 성공함
                                    lecture_id=data['lecture_id'], )
    db.add(new_registration)
    db.commit()

    basket = db.query(Basket).filter(Basket.user_id == data['user_id'],  # 장바구니에서 해당 수업을 가져옴
                                     Basket.lecture_id == data['lecture_id'], ).first()
    if basket:  # 해당 수업이 장바구니에 존재함
        basket.is_valid = False  # 해당 수업을 장바구니에서 무효화시킴
        db.commit()

    return jsonify(serialize(new_registration))


@app.route('/registration', methods=['GET'])
@api
def get_registration(data, db):  # 내가 수강신청한 목록 불러오기 ( 수업목록 )
    req_list = ['user_id']
    check_data(data, req_list)  # 필수 파라미터 들어있는지 검사

    registrations = db.query(Registration).filter(Registration.user_id == data['user_id']).all()  # 수강신청 성공한 목록을 가져옴

    if not registrations:  # 수업신청 성공한 수업이 존재하지 않음
        raise NotFound

    return jsonify(serialize(registrations))
