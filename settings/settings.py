import os
import sys

sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))

# define
HOST_ADDR = '127.0.0.1'  # localhost address
SERVER_PORT = 8100  # 서버 포트
DEBUG = False  # 디버그모드
MODE = os.environ.get('MODE')

# connect db
USER = 'postgres'  # username
PASSWOLRD = 'root'  # postgresql pw
DB_PORT = '5432'  # postgresql port
NAME = 'mobile_project'  # db name
DB_URI = f'postgresql://{USER}:{PASSWOLRD}@{HOST_ADDR}:{DB_PORT}/{NAME}'  # postgresql uri
SALT = b'$2b$12$tPrUCEr3KqxIcBEv0fx67e'
RDS_ENDPOINT = 'mp.cebsh5dyebyf.ap-northeast-2.rds.amazonaws.com'
# select operation mode
if MODE == 'TEST' or sys.argv[0].endswith('test'):  # use only pytest
    HOST_ADDR = '127.0.0.1'
    DEBUG = False
    NAME += '_test'
    DB_URI = f'postgresql://{USER}:{PASSWOLRD}@{HOST_ADDR}:{DB_PORT}/{NAME}'  # postgresql uri
elif MODE == 'DEV':  # mode - development
    HOST_ADDR = '127.0.0.1'
    DEBUG = True
elif MODE == 'RUN':  # mode - release
    HOST_ADDR = '0.0.0.0'
    DEBUG = False
    PASSWOLRD += '2628'
    DB_URI = f'postgresql://{USER}:{PASSWOLRD}@{RDS_ENDPOINT}:{DB_PORT}/{NAME}'  # postgresql uri
else:  # select not permission mode
    raise KeyError
