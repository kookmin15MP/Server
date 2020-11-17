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

## API manual URL
``https://github.com/kookmin15MP/Server/tree/master/api``