from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import TimeoutException
import requests
import pandas as pd
import os

executable_path = r'C:\Users\KJW\Desktop\python\py-ex\chromedriver.exe'
# os.environ["webdriver.chrome.driver"]=executable_path
# chrome_options =Options()
# chrome_options.add_extension(r'C:\Users\KJW\AppData\Local\Google\Chrome\User Data\Default\Extensions')
driver = webdriver.Chrome(executable_path = executable_path)
url = "http://www.vendorpia.com/"
# driver = webdriver.Ie(executable_path=r'C:\Users\KJW\Desktop\python\py-ex\IEDriverServer.exe')
# driver = webdriver.Chrome(r'C:\Users\PC\Desktop\개인\파이썬\chromedriver_win32\chromedriver.exe')
driver.get(url)

def vendor_login(id, pw):
    try :
        element = WebDriverWait(driver,10).until(
            EC.presence_of_element_located((By.ID, 'login_tbEmpNo'))
        )
        driver.find_element_by_id('login_tbEmpNo').send_keys(id)
        driver.find_element_by_id('login_tbPwd').send_keys(pw)
    except TimeoutException:
        print('Time Out')
    driver.find_element_by_id('login_btnLogin').click()
    driver.implicitly_wait(3)
    result = driver.find_elements_by_tag_name('frame')
    driver.switch_to_frame(result[1])
    result_iframe = driver.find_elements_by_tag_name('frame')
    driver.switch_to_frame(result_iframe[0])
    try :
        element = WebDriverWait(driver,10).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="UltraWebTree5_1_2_1"]/span[3]'))
        ) 
        driver.find_element_by_xpath('//*[@id="UltraWebTree5_1_2_1"]/span[3]').click()
    except TimeoutException:
        print('Time Out')
    driver.switch_to_default_content()
    driver.switch_to_frame(result[1])
    driver.switch_to_frame(result_iframe[1])
    try : 
        element = WebDriverWait(driver,10).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="G_oGrid"]/tbody'))
        )
        soup = BeautifulSoup(driver.page_source, 'lxml')
        table = soup.find(id='G_oGrid')
        tbody = table.find('tbody')
        tags_tr = tbody.find_all('tr') #tr tag all
        tags_tr_counts=len(tags_tr)
        page_td = soup.find('td', {'align': 'Center'})
        page_nos = page_td.find_all('a')
        page_default = page_td.find_all('b')
        page_all = page_default + page_nos
        # result_text = []
        # vd_df_result = pd.DataFrame()
        for page_no in page_all:
            if '1' in page_no.text:
                print('1페이지 크롤링 중입니다.')
                for tags_tr_count in range(tags_tr_counts)[:1]:
                    for i in range(39):
                        tag_nobr = tbody.find('tr').find('td', {'level':str(tags_tr_count)+'_'+str(i)})
                        if tag_nobr is not None:
                            # result_text.append(tag_nobr.text)
                            vd_df = pd.DataFrame(index=range(tags_tr_counts),columns=range(i)
                            vd_df.ix[tag_tr_count,i]=tag_nobr.text????
                            vd_df.append(vd_df)
                vd_df.to_excel('vd_df.xlsx',sheet_name="Sheet1")
            else:
                print(page_no.text+'페이지 크롤링 중입니다.')
                driver.find_element_by_xpath('//*[@id="form1"]/div[3]/div/table[2]/tbody/tr/td/a['+str(page_no.text)+']').click()
                for tags_tr_count in range(tags_tr_counts)[:1]:
                    for i in range(39):
                        tag_nobr = tbody.find('tr').find('td', {'level':str(tags_tr_count)+'_'+str(i)})
                        if tag_nobr is not None:
                            result_text.append(tag_nobr.text)
    except TimeoutException:
        print('Time Out')
        driver.quit()
 



vendor_login('wjddn0316', '0000')


def pd_vendor(*datas): 
    vendor_level_no = {
        'CS' : "0_2",
        '매출처' : "0_6",
        '생산처' : "0_7",
        '몰': "0_8",
        '주문번호':"0_10",
        '송장번호':"0_11",
        '주문자':"0_12",
        '수취인':"0_13",
        '전화':"0_14",
        '휴대폰':"0_15",
        '상태':"0_16",
        '상품명':"0_17",
        '상품옵션':"0_18",
        '수': "0_19",
        '박스':"0_21",
        '권역':"0_23",
        '주소':"0_25",
        '배송메시지':"0_26",
        '메모':"0_27",
        '배송사':"0_29",
        '선불비':"0_31",
        '착불비':"0_32",
        '제품비':"0_33",
        '배송예정일':"0_35",
        '등록일시':"0_36",
        '등록자':"0_37",
        '수정일시':"0_39"
    }
    find_vendor_no_all=[]
    for data in datas:
        if data in vendor_level_no.keys():
            find_vendor_no = vendor_level_no[data]
            find_vendor_no_all.append(find_vendor_no)
        else: print("존재하지 않는 데이터값입니다.")
    return find_vendor_no_all