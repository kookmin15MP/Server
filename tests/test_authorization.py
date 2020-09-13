def test_post_signup(client):  # 회원가입 테스트
    data = {
        'email': 'test@test.test',
        'pw': 'test123!@#',
    }
    res = client.post('/api/authorization/signup', data=data)
    assert res.status_code == 200
    assert res.get_json()['id'] == 1  # 유저 생성 확인


def test_get_signup(client):  # 이메일 중복 확인
    data = {
        'email': 'asdf@asdf.asdf',
        'pw': 'asdf123!@#',
    }
    res = client.get('/api/authorization/signup', query_string=data)
    assert res.status_code == 200  # 존재하지 않는 이메일

    res = client.post('/api/authorization/signup', data=data)
    assert res.status_code == 200  # 회원가입

    res = client.get('/api/authorization/signup', query_string=data)  # 동일한 이메일로 중복 확인
    assert res.status_code == 409  # 중복된 이메일 존재


def test_post_login(client):  # 로그인
    data = {
        'email': 'login@login.login',
        'pw': 'login123!@#',
    }
    res = client.post('/api/authorization/signup', data=data)
    assert res.status_code == 200  # 회원가입 정상적으로 완료

    res = client.post('/api/authorization/login', data=data)
    assert res.status_code == 200  # 로그인 정상적으로 완료
