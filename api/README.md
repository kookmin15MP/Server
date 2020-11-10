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

### lecture
[POST] /api/lecture/info  
수업 생성

요청
```
{
    "lecture_name": "mobile_project",
    "professor_name": "이창우 교수",
    "lecture_time": "10:30 - 12:00",
    "limited_people": 30
}
```

응답
```
{
    "lecture_id": 1,
    "lecture_name": "mobile_project",
    "professor_name": "이창우 교수",
    "lecture_time": "10:30 - 12:00",
    "limited_people": 30
}

200 ok
400 요청 형식 맞지 않음
```

[GET] /api/lecture/info  
모든 수업 불러오기

요청
```
{ }
```

응답
```
{
    "Lecture": [
        {
            "lecture_id": 1,
            "lecture_name": "mobile_project",
            "professor_name": "이창우 교수",
            "lecture_time": "10:30 - 12:00",
            "limited_people": 30
        }, ...
    ]
}

200 ok
400 요청 형식 맞지 않음
```

[POST] /api/lecture/basket  
장바구니에 추가

요청
```
{
    "user_id": 1,
    "lecture_id": 1
}
```

응답
```
{
    "basket_id": 1,
    "user_id": 1,
    "lecture_id": 1
}

200 ok
400 요청 형식 맞지 않음
```

[GET] /api/lecture/basket  
내 장바구니 불러오기

요청
```
{
    "user_id": 1
}
```

응답
```
{
    "Basket": [
        {
            "basket_id": 1,
            "user_id": 1,
            "lecture_id": 1
        }, ...
    ]
}

200 ok
400 요청 형식 맞지 않음
```

[PUT] /api/lecture/basket  
장바구니에서 수업 제거

요청
```
{
    "basket_id": 1
}
```

응답
```
{ }

200 ok
400 요청 형식 맞지 않음
```

[POST] /api/lecture/registration  
수강신청

요청
```
{
    "lecture_id": 1,
    "user_id": 1
}
```

응답
```
{
    "registration": 1,
    "user_id": 1,
    "lecture_id": 1
}

200 ok
400 요청 형식 맞지 않음
```

[GET] /api/lecture/registration
수강신청 성공 목록 불러오기

요청
```
{
    "user_id": 1
}
```

응답
```
{
    "Registration": [
        {
            "registration": 1,
            "user_id": 1,
            "lecture_id": 1
        }, ...
    ]
}

200 ok
400 요청 형식 맞지 않음
```