import pandas as pd
import os

## 특정 경로의 파일들을 하나로 결합하여 데이터프레임을 생성을 하는 함수 
def data_load(_path, _end, _engine='utf-8'):
    # _path : 파일들이 존재하는 경로 
    # _end : 로드하려는 파일들의 확장자

    # _path에 입력된 값이 '/' 마지막에 존재하는가?
    if _path[-1] != '/':
        _path = _path + '/'
    # 입력받은 경로의 파일 목록을 로드 
    file_list = os.listdir(_path)

    # 비어있는 데이터프레임을 생성
    result = pd.DataFrame()

    # file_list를 기준으로 반복문을 실행
    for file in file_list:
        # if file.split('.')[-1] == _end:
        if file.endswith(_end):
            if _end == 'csv':
                df = pd.read_csv(_path+file, encoding=_engine)
            elif _end == 'json':
                df = pd.read_json(_path+file, encoding=_engine)
            elif _end == 'xml':
                df = pd.read_xml(_path + file, encoding=_engine)
            elif (_end == 'xlsx') | (_end == 'xls'):
                df = pd.read_excel(_path + file)
            else:
                # return은 함수를 강제 종료하고 결과값을 되돌려준다. 
                return "지원하지 않는 확장자입니다."
            result = pd.concat([result, df], axis=0, ignore_index=True)
    return result