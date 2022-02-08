import time 
from selenium import webdriver
from bs4 import BeautifulSoup

driver = webdriver.Chrome('./chromedriver')
url = 'http://www.melon.com/chart/index.htm'

driver.get(url)
time.sleep(10)

html = driver.page_source
soup = BeautifulSoup(html, 'html.parser')

song_data = []
rank = 1
songs = soup.select('table > tbody > tr')

for song in songs:
    title = song.select('div.rank01 > span > a')[0].text
    singer = song.select('div.rank02 > a')[0].text
    song_data.append(['Melon', rank, title, singer])
    rank = rank + 1

# song_data 리스트를 이용해 데이터 프레임 만들기
import pandas as pd 

columns = ['서비스','순위','타이틀','가수']
pd_data = pd.DataFrame(song_data, columns = columns)
print(pd_data.head())

pd_data.to_csv('./melon.csv', index=False) 