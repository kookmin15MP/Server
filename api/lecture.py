from flask import Blueprint, jsonify
from werkzeug.exceptions import BadRequest

from api.models.lecture import Lecture, Basket
from settings.serialize import serialize
from settings.utils import api

app = Blueprint('teach', __name__, url_prefix='/api/lecture')


@app.route('/info', methods=['POST'])
@api
def post_lecture_info(data, db):  # 수업 생성
    req_list = ['lecture_name', 'professor_name', 'lecture_time']

    for i in req_list:  # 필수 요소 검사
        if i not in data:
            raise BadRequest

    new_lecture = Lecture(lecture_name=data['lecture_name'],
                          professor_name=data['professor_name'],
                          lecture_time=data['lecture_time'], )
    db.add(new_lecture)
    db.commit()

    return jsonify(serialize(new_lecture))


@app.route('/info', methods=['GET'])
@api
def get_lecture_info(data, db):  # 모든 수업을 가져옴
    # 필요 인자 없음

    lectures = db.query(Lecture).all()

    return jsonify(serialize(lectures))


@app.route('/basket', methods=['POST'])
@api
def post_lecture_basket(data, db):  # 장바구니 추가
    req_list = ['user_id', 'lecture_id']

    for i in req_list:  # 필수 요소 검사
        if i not in data:
            raise BadRequest

    new_basket = Basket(lecture_id=data['lecture_id'],
                        user_id=data['user_id'], )
    db.add(new_basket)
    db.commit()

    return jsonify(serialize(new_basket))


@app.route('/basket', methods=['GET'])
@api
def get_lecture_basket(data, db):  # 장바구니 불러오기
    req_list = ['user_id']

    for i in req_list:  # 필수 요소 검사
        if i not in data:
            raise BadRequest

    baskets = db.query(Basket).filter(Basket.user_id == data['user_id'],
                                      Basket.is_valid is True, ).all()
    return jsonify(serialize(baskets))


@app.route('/basket', methods=['PUT'])
@api
def put_lecture_basket(data, db):  # 장바구니에서 무효화
    req_list = ['basket_id']

    for i in req_list:  # 필수 요소 검사
        if i not in data:
            raise BadRequest

    basket = db.query(Basket).filter(Basket.id == data['basket_id']).first()
    basket.is_valid = False
    db.commit()


