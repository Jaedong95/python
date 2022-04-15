import time
from selenium import webdriver
from bs4 import BeautifulSoup

driver = webdriver.Chrome('./chromedriver')
url = 'https://www.genie.co.kr/chart/top200'

driver.get(url)
time.sleep(10)

html = driver.page_source
soup = BeautifulSoup(html, 'html.parser')

songs = soup.select('table > tbody > tr')
print(len(songs))

'''
song = songs[0]

#title = song.select('a.title')
# print(len(title), title)

title = song.select('a.title')[0].text.strip()
print(title)

singer = song.select('a.artist')[0].text
print(singer)
'''

song_data = []
rank = 1

for song in songs:
    title = song.select('a.title')[0].text.strip()
    singer = song.select('a.artist')[0].text
    song_data.append(['Genie', rank, title, singer])
    rank = rank + 1 


import pandas as pd 

columns = ['서비스', '순위', '타이틀', '가수']
pd_data = pd.DataFrame(song_data, columns=columns)
pd_data.to_csv('Genie.csv',index=False)

