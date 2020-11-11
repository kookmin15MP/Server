def test_post_lecture_info(client):
    data = {
        'lecture_name': 'test_lecture',
        'professor_name': '김연수',
        'lecture_time': '10:30 - 11:45',
        'limited_people': 30,
    }

    res = client.post('/api/lecture/info', data=data)
    assert res.status_code == 200


def test_get_lecture_info(client):
    data = {

    }

    res = client.get('/api/lecture/info', query_string=data)
    assert res.status_code == 200


def test_post_lecture_basket(client, user):
    data = {
        'user_id': user.id,
        'lecture_id': 1,
    }

    res = client.post('/api/lecture/basket', data=data)
    assert res.status_code == 200


def test_get_lecture_basket(client, user):
    data = {
        'user_id': user.id,
        'lecture_id': 1,
    }

    res = client.post('/api/lecture/basket', data=data)
    assert res.status_code == 200  # 장바구니 추가

    res = client.get('/api/lecture/basket', query_string=data)
    assert res.status_code == 200  # 장바구니 불러오기


def test_delete_lecture_basket(client):
    data = {
        'basket_id': 1,
    }

    res = client.delete('/api/lecture/basket', query_string=data)
    assert res.status_code == 200


def test_post_registration(client, user):
    data = {
        'user_id': user.id,
        'lecture_id': 1,
    }

    res = client.post('/api/lecture/registration', data=data)
    assert res.status_code == 200


def test_get_registration(client, user):
    data = {
        'user_id': user.id,
        'lecture_id': 1,
    }

    res = client.post('/api/lecture/registration', data=data)
    assert res.status_code == 200  # 수강신청 성공

    res = client.get('/api/lecture/registration', query_string=data)
    assert res.status_code == 200
