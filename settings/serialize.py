"""
Mobile Programing Team Project
수강신청 App Server Side
코드 작성자 20153159 김연수
"""
from typequery import GenericMethod

from api.models.lecture import Lecture, Basket, Registration
from api.models.user import User

serialize = GenericMethod('serialize')


@serialize.of(bool)
@serialize.of(type(None))
@serialize.of(int)
@serialize.of(float)
@serialize.of(str)
def serialize(value, **kwargs):
    return value


@serialize.of(list)
def serialize(input_list, **kwargs):
    class_name = input_list[0].__class__.__name__
    result_list = list()
    for i in input_list:
        result_list.append(serialize(i))

    result = {
        class_name: result_list
    }
    return result


@serialize.of(User)
def serialize(user, **kwargs):
    result = {
        'id': user.id,
        'email': user.email,
    }
    return result


@serialize.of(Lecture)
def serialize(lecture, **kwargs):
    result = {
        'lecture_id': lecture.id,
        'lecture_name': lecture.lecture_name,
        'professor_name': lecture.professor_name,
        'lecture_time': lecture.lecture_time,
        'limited_people': lecture.limited_people,
    }
    return result


@serialize.of(Basket)
def serialize(basket, **kwargs):
    result = {
        'basket_id': basket.id,
        'user_id': basket.user_id,
        'lecture_id': basket.lecture_id,
    }
    return result


@serialize.of(Registration)
def serialize(registration, **kwargs):
    result = {
        'registration_id': registration.id,
        'user_id': registration.user_id,
        'lecture_id': registration.lecture_id,
    }
    return result
