"""
Mobile Programing Team Project
수강신청 App Server Side
코드 작성자 20153159 김연수
"""
import functools

from flask import request
from werkzeug.exceptions import BadRequest

from db import Database


def api(f):  # 함수의 쿼리스트링 또는 바디데이터를 같은 포멧으로 사용할 수 있게 해주는 함수
    @functools.wraps(f)
    def deco(*args, **kwargs):
        if request.method in ['GET', 'DELETE']:
            data = request.args.to_dict()
        elif request.method in ['POST', 'PUT']:
            data = request.form
        else:
            data = {}
        with Database() as db:  # 디비를 편하게 사용하게함
            return f(data, db, *args, **kwargs)

    return deco


def check_data(data, req_list):  # request에 파라미터가 다 들어있는지 확인하는 함수
    for i in req_list:  # 필수 요소 검사
        if i not in data:  # 없으면 400
            raise BadRequest
