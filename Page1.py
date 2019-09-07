from selenium import webdriver
import time
from  random import randint
import tkinter

# 네이버 돌아다니는거 연습하려고 썻던 샘플 파일입니다.

def NaverSearch():
    count = 0
    driver.get('https://www.naver.com/')
    time.sleep(randint(4,8))
    driver.find_element_by_name('query').send_keys('네이버쇼핑')
    time.sleep(randint(4,10))
    driver.find_element_by_xpath('//*[@id="search_btn"]').click()
    time.sleep(randint(5,10))
    driver.find_element_by_xpath('//*[@id="main_pack"]/div[2]/ul/li/dl/dt/a').click()
    time.sleep(randint(7,10))
    last_tab = driver.window_handles[-1]
    driver.switch_to.window(window_name=last_tab)



    while True:
        time.sleep(randint(7,15))
        try:
            if driver.find_element_by_id('단어 찾기').size != 0 :
                break
        except Exception as e:
            
            time.sleep(randint(10,20))
            driver.find_element_by_class_name('next').click()
            count += 1
            print(count)
            if count == 100:
                print("no")
                break

    time.sleep(20)
    driver.close()
    last_tab = driver.window_handles[-1]
    driver.switch_to.window(window_name=last_tab)
    driver.close()
    last_tab = driver.window_handles[0]
    driver.switch_to.window(window_name=last_tab)
    driver.back()


def NaverNews():
    driver.get('https://www.naver.com/')
    time.sleep(randint(4,8))
    driver.find_element_by_xpath('//*[@id="PM_ID_serviceNavi"]/li[2]/a').click()

    time.sleep(randint(4,8))
    driver.find_element_by_xpath('//*[@id="today_main_news"]/div[2]/ul/li[1]/div[1]/a').click()
    time.sleep(randint(10,15))
    driver.back()
    driver.find_element_by_xpath('//*[@id="today_main_news"]/div[2]/ul/li[2]/div[1]/a').click()
    time.sleep(randint(10,15))
    driver.back()
    driver.find_element_by_xpath('//*[@id="today_main_news"]/div[2]/ul/li[3]/div[1]/a').click()
    time.sleep(randint(10,20))
    driver.back()
    driver.find_element_by_xpath('//*[@id="snb_wrap"]/ul/li[4]/a/img').click()
    time.sleep(randint(20, 27))
    driver.back()


    time.sleep(randint(4,6))
    driver.find_element_by_xpath('//*[@id="snb_wrap"]/ul/li[2]/a').click()
    time.sleep(randint(4,6))
    driver.find_element_by_xpath('//*[@id="lnbTopMenuUrl_4"]').click()
    time.sleep(randint(5,10))
    driver.find_element_by_xpath('//*[@id="lnbSubMenu_4_0"]/a/img').click()
    time.sleep(randint(10,15))
    '''
    driver.find_element_by_xpath('//*[@id="_newsList"]/ul/li[2]/a/img').click()
    time.sleep(randint(20,30))
    driver.back()
    driver.find_element_by_xpath('//*[@id="_newsList"]/ul/li[3]/a/img').click()
    time.sleep(randint(20,30))
    '''
    driver.back()

    driver.get('https://www.naver.com/')

def Youtube():
    time.sleep(randint(4,8))
    driver.find_element_by_name('query').send_keys('유튜브')
    time.sleep(randint(4,10))
    driver.find_element_by_xpath('//*[@id="search_btn"]').click()
    time.sleep(randint(5,10))
    driver.find_element_by_xpath('//*[@id="main_pack"]/div[2]/ul/li/dl/dt/a').click()
    time.sleep(randint(5,10))

    driver.close()
    last_tab = driver.window_handles[0]
    driver.switch_to.window(window_name=last_tab)
    a = randint(1, 2)
    if a == 1:
        time.sleep(1800)
        driver.delete_all_cookies()
    else:
        time.sleep(3200)
        driver.delete_all_cookies()

    driver.close()
    time.sleep(10)

def NaverMovie():
    driver.get('https://www.naver.com/')
    driver.find_element_by_xpath('//*[@id="PM_ID_serviceNavi"]/li[6]/a').click()
    time.sleep(randint(5,10))
    driver.find_element_by_xpath('//*[@id="scrollbar"]/div[1]/div/div/ul/li[3]/a').click()
    time.sleep(randint(5,10))
    driver.get('https://www.naver.com/')

while True:

    a = randint(1,2)
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument("--incognito")
    chrome_options.add_argument('122.154.214.231:8080')
    driver = webdriver.Chrome(chrome_options=chrome_options)
    driver.implicitly_wait(5)

    a = randint(1, 2)
    if a == 1:
        NaverSearch()
        NaverNews()
        NaverMovie()
    elif a == 2:
        NaverNews()
        NaverSearch()
        NaverMovie()
    else:
        NaverMovie()
        NaverNews()
        NaverSearch()
    Youtube()
