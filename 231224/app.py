# 웹 프레임워크 flask 로드 
from flask import Flask, render_template, request, redirect
# mysql 모듈과의 연동 
import mysql as ms

import pandas as pd

# Flask 클래스를 생성
# __name__ : 현재 파일의 이름(파일명)
app = Flask(__name__)
# app = Flask('app.py')

# MyDB class를 생성 
mydb = ms.MyDB()

# api 구성 
@app.route('/')
# 네비게이터 함수 
# route에 있는 특정 주소와 아래의 함수를 연결 한다. 
# 특정 주소로 요청이 들어왔을때 아래의 함수를 호출하여 실행
# "/" -> 웹서버의 기본 루트 주소 뒤에 /를 추가한 주소 값을 의미
# 루트 주소 : localhost:3000
# 웹 브라우져에서 localhost:3000/ 요청 시 아래의 함수를 호출
def index():
    return "Hello World"

# 화면을 되돌려주는 api 생성
# localhost:3000/login 요청이 들어왔을때
@app.route('/login')
def login():
    # 특정한 html 파일을 되돌려준다. 
    return render_template('login.html')

# 로그인 ID PASSWORD를 받는 api 생성
@app.route('/signin')
def signin():
    # 유저가 보낸 데이터(id, password)를 변수에 대입
    # 유저가 서버에게 보낸 데이터는 request에 존재
    # request 기능을 로드 -> flask에서 가지고 온다. 
    # get 방식으로 데이터를 보내는 경우에는 request 안에 args에 데이터가 존재 
    print(f"request args message : {request.args}")
    # request.args는 dict형태의 데이터 
    # {
    #   _id : test, 
    #   _pass : 1111
    # }
    input_id = request.args['_id']
    input_pass = request.args['_pass']
    # id가 test이고 password가 1234인 경우 로그인 성공
    if (input_id == 'test') and (input_pass == '1234'):
        result = '로그인 성공'
    else:
        result = '로그인 실패'
    return result

# post
# localhost:3000/signin2  post형태의 url
@app.route('/signin2', methods=['post'])
def signin2():
    # post 형태로 데이터를 보낼때 
    # request안에 form이라는 곳에 데이터가 존재 
    print(f"request form message : {request.form}")
    # request.form 데이터도 데이터의 형태가 dict형태
    input_id = request.form['input_a']
    input_pass = request.form['input_b']
    # sql 쿼리문을 이용하여 user 테이블에 id, password가 모두 일치하는 데이터가 존재하는가?
    sql = """
        select 
        * 
        from 
        user 
        where 
        id = %s
        and 
        password = %s
    """
    sql_result = mydb.sql_query(sql, input_id, input_pass)
    # 로그인이 성공한 경우 -> sql_result -> [{id : xxxxx, password: xxxx, name: xxx, loc: xxx}]
    if sql_result:
        # 로그인이 성공했을때 특정 html 문서를 응답 메시지 보내준다. 
        # 로그인을 한 사람의 이름과 함께 html를 응답 메시지로 보내준다. 
        # result = '로그인 성공'
        # 로그인 한 사람의 이름을 변수에 대입 
        # sql_result -> [{id : xxxxx, password: xxxx, name: xxx, loc: xxx}]
        # sql_result[0] -> {id : xxxxx, password: xxxx, name: xxx, loc: xxx}
        # sql_result[0]['name'] -> xxx
        logind_name = sql_result[0]['name']
        return render_template('index.html', login = logind_name)
    # 로그인이 실패한 경우 -> sql_result -> []
    else:
        # result = '로그인 실패'
        # 로그인이 실패하는 경우에는 로그인 페이지로 되돌아간다. 
        return redirect("/login")
    
# corona 데이터를 이용하여 일일확진자의 수를 그래프로 표시하는 api를 생성
@app.route('/corona')
def corona():
    # corona data를 로드 
    df = pd.read_csv("../csv/corona.csv")
    # 첫번째 컬럼이 Unnamed: 0
    # 특정 컬럼을 제거
    df.drop(['Unnamed: 0', 'seq', 'accExamCnt', 'accDefRate'], axis=1, inplace=True)
    # 컬럼의 이름을 변경 
    # [등록일시, 누적사망자, 누적확진자, 기준일, 기준시간, 수정일시]
    df.columns = ['등록일시', '누적사망자', '누적확진자', '기준일', '기준시간', '수정일시']
    # '기준일'컬럼의 데이터를 오름차순 정렬
    df.sort_values('기준일', inplace=True)
    # 인덱스를 초기화 (기존의 인덱스를 제거)
    df.reset_index(drop=True, inplace=True)
    # 일일확진자라는 파생변수를 생성
    # (오늘의 누적확진자 - 어제의 누적확진자)
    df['일일확진자'] = df['누적확진자'].diff().fillna(0)
    # 가장 최근의 한달치 데이터를 추출
    df2 = df.tail(30)
    # 챠트에서 x축에 들어갈 데이터를 변수로 생성
    # x = df2.loc[:, '기준일']
    x = df2['기준일'].to_list()
    # y축에 들어갈 데이터를 변수로 생성
    y = df2['일일확진자'].to_list()

    # DataFrame을 dict형태로 데이터를 변환 
    data = df2.to_dict('records')
    # data는 [{col:value, col2:value2, ..}, ...]
    # 컬럼의 값들만 따로 변수에 저장
    cols = df2.columns
    # df2의 길이를 변수에 저장
    cnt = len(df2)
    print(data)

    return render_template('chart.html', 
                           chart_x = x, 
                           chart_y = y, 
                           data = data,
                           cols = cols, 
                           cnt = cnt)


    
    


# debug는 개발자모드를 사용할 것인가? False 기본값
# 파일이 수정이 될때마다 실행되고 있는 웹서버를 재시작을 자동
app.run(port = 3000, debug=True)