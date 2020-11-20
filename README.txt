# flask를 이용한 REST API서버  
```
Mobile Programing Team Project
수강신청 App Server Side
코드 작성자 20153159 김연수

서버주소 : http://3.34.158.76:8100/

코드는 api폴더안의 파일들과 api/README.md 파일 확인해주시면 됩니다
```
## 필요 패키지  
DB : PostgreSQL  
reference link - https://github.com/snowplow/snowplow/wiki/Setting-up-PostgreSQL

1. postgresql 설치할 때 비밀번호 `root`로 설정.  
2. postgresql에 database `mobile_project`로 생성`
3. `set MODE=DEV` 실행 -> 환경설정
4. 해당 폴더 안에서 `alembic upgrade head` 실행 -> 데이터 생성
5. 해당 폴더 안에서 `python run.py` 실행 -> 서버 실행

자세한 설정은 `settings.py` 참조.
```
https://www.postgresql.org/download/
다 next해서 설치

user : postgres
pw : root
database name : mobile_project
port : 5432
```
## 필요한 모듈 설치  
```
pip install -r requirments.txt  
```



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
404 장바구니에 담은 수업이 없음
```

[DELETE] /api/lecture/basket  
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
404 수강신청 성공한 수업이 없음
```