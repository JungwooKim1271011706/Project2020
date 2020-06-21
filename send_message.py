import pandas as pd
import plotly.express as px
from datetime import datetime, date, timedelta
import tkinter
from tkinter import filedialog
import time

def file_open():
    root = tkinter.Tk()
    root.title = "대량 SMS 전송 - 미출 고객"
    root.filename = filedialog.askopenfilename(initialdir = "E:/Images",title = "choose your file",filetypes = (("csv files","*.csv"),("jpeg files","*.jpg"),("all files","*.*")))
    return root.filename

now_day = time.strftime('%y.%m.%d', time.localtime(time.time()))
day_a = datetime.today() - timedelta(days=5)
r_day = '.'.join(str(day_a)[2:10].split('-'))
df_t = pd.read_csv(file_open(), encoding = 'CP949')
path_save = r"C:\Users\KJW\Desktop\python\send_sms_" + time.strftime('%Y%m%d', time.localtime(time.time()))

def send_sms_csv(company):
    df_취소제거 = df_t[df_t['CS'].isnull()]
    if '주문등록일' in df_취소제거.columns:
        df_취소제거.rename(columns={"주문등록일" : "등록일"}, inplace = True)
    else:
        pass
    df_지연 = df_취소제거.등록일 <= r_day
    df_날짜=df_취소제거[df_지연]
    if '휴대전화' in df_날짜.columns:
        df_배송상태 = df_날짜[df_날짜.배송상태 == '지사출발']
        df_배송상태.rename(columns={"휴대전화" : "수취인휴대폰"}, inplace = True)
    else:
        df_배송상태 = df_날짜
    df_배송상테_공백제거 = df_배송상태[df_배송상태['수취인휴대폰'].notnull()]
    df_필터링 = df_배송상테_공백제거[df_배송상테_공백제거['수취인휴대폰'].str.startswith('010')]
    df_중복제거 = df_필터링.drop_duplicates('수취인휴대폰', keep='first')
    df_매출처 = df_중복제거[df_중복제거.매출처 == company]
    df_매출처_sms = df_매출처.loc[:,['수취인','CS','수취인휴대폰']]
    df_매출처_sms.to_csv(path_save + "_" + company + ".csv", encoding='euc-kr', index=False) #추출 데이터 저장
    #selenium으로 메이크샵 자동 문자보내기까지 핸들링
    #message 변수 기재하기

companys = ['바로방','퍼니','케어퍼니처']

for i in companys:
    send_sms_csv(i)