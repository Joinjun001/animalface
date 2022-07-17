from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup

driver = webdriver.Chrome()
driver.get("https://naver.com")
driver.find_element(By.XPATH, '//*[@id="NM_FAVORITE"]/div[1]/ul[2]/li[8]/a').click()
driver.find_element(By.CSS_SELECTOR, '.Ntxt_webtoon').click()

for i in range(1,11):
    rank = driver.find_element(By.XPATH,'//*[@id="realTimeRankFavorite"]/li[{}]/a'.format(i)).text
    print(str(i)+"위: "+str(rank))

# writedata.py
f = open("새파일.txt", 'w',encoding='utf-8')
for i in range(1, 11):
    rank = driver.find_element(By.XPATH,'//*[@id="realTimeRankFavorite"]/li[{}]/a'.format(i)).text
    data = "{}위 : {}.\n".format(i, rank)
    f.write(data)
f.close()