import time 
from selenium import webdriver 
from bs4 import BeautifulSoup
 
driver = webdriver.Chrome('./chromedriver')
url = 'https://music.bugs.co.kr/chart'
driver.get(url)
time.sleep(10)

html = driver.page_source
soup = BeautifulSoup(html, 'html.parser')
songs = soup.select('table.byChart > tbody > tr')

print(len(songs))
print(songs[0])

'''
song = songs[0]

title = song.select('p.title > a')[0].text
print(len(title))

singer = song.select('p.artist > a')[0].text.strip()
print(singer)
'''

song_data = []
rank = 1

for song in songs:
    title = song.select('p.title > a')[0].text
    singer = song.select('p.artist > a')[0].text 
    #print(title, singer, sep ='|')
    song_data.append(['Bugs',rank,title,singer])
    rank = rank + 1


import pandas as pd 

columns = ['서비스','순위','타이틀','가수']
pd_data = pd.DataFrame(song_data, columns=columns)

pd_data.to_csv('bugs.csv',index=False)