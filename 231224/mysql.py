import pymysql 
import pandas as pd

class MyDB:
    # 서버의 정보를 인스턴스(self) 변수에 저장 
    # 클래스가 생성이 될때 최초로 한번만 실행이 되는 함수 (생성자 함수) __init__
    def __init__(
            self, 
            _host = '127.0.0.1', 
            _port = 3306, 
            _user = 'root', 
            _password = '1234', 
            _db = 'ezen2'
    ):
        self.host = _host
        self.port = _port
        self.user = _user
        self.password = _password
        self.db = _db
    # SQL Query를 입력받아 데이터베이스에 질의를 던지는 함수를 생성
    def sql_query(self, _sql, *_values):
        # 데이터베이스 서버와 연결
        _db = pymysql.connect(
            host = self.host, 
            port = self.port, 
            user = self.user, 
            password= self.password, 
            db = self.db
        )
        # 커서(가상 공간) 생성 
        cursor = _db.cursor(pymysql.cursors.DictCursor)
        # 입력받은 sql 쿼리문을 execute()
        cursor.execute(_sql, _values)
        # _sql이 select문이라면 
        if _sql.strip().upper().startswith('SELECT'):
            # data = cursor.fetchall()
            # result = pd.DataFrame(data)
            result = cursor.fetchall()
        # select문이 아니라면 
        else:
            _db.commit()
            result = 'Query OK'
        
        # 데이터베이스 서버와의 연결을 종료 
        _db.close()

        # 결과값을 리턴 
        return result
        