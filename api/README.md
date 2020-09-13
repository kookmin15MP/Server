# API manual

### authorization
[GET] /api/authorization/signup
회원가입 도중에 이메일 중복 확인

요청
```
{
    "email": "test@test.test"
}
```

응답
```
{
    "valid email": "test@test.test"
}

200 ok
400 요청 형식 맞지 않음
409 이미 존재하는 이메일
```

[POST] /api/authorization/signup
회원가입 처리

요청
```
{
    "email": "test@test.test",
    "pw": "test123!@#"
}
```

응답
```
{
    "id": 1,
    "email": "test@test.test"
}

200 ok
400 요청 형식 맞지 않음
```

[POST] /api/authorization/login
로그인 처리

요청
```
{
    "email": "test@test.test",
    "pw": "test123!@#"
}
```

응답
```
{
    "id": 1,
    "email": "test@test.test"
}

200 ok
400 요청 형식 맞지 않음
409 email or pw 오류
```