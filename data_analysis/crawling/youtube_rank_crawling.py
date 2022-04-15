import time 
import pandas as pd 
from selenium import webdriver
from bs4 import BeautifulSoup

browser = webdriver.Chrome('./chromedriver')
'''
url = 'https://youtube-rank.com/board/bbs/board.php?bo_table=youtube&page=2'
browser.get(url)
time.sleep(100)

html = browser.page_source
soup = BeautifulSoup(html, 'html.parser')

channel_list = soup.select('form > table > tbody > tr')
print(len(channel_list),'\n')


channel = channel_list[0]
print(channel_list[0])

category = channel.select('p.category')[0].text.strip()
print(category)

title = channel.select('h1 > a')[0].text.strip()
print(title)

subscriber = channel.select('.subscriber_cnt')[0].text
view = channel.select('.view_cnt')[0].text
video = channel.select('.video_cnt')[0].text 

print(subscriber, view, video)
'''

results = []
for page in range(1, 11):
    url = f'https://youtube-rank.com/board/bbs/board.php?bo_table=youtube&page={page}'
    browser.get(url)
    time.sleep(5)
    html = browser.page_source
    soup = BeautifulSoup(html, 'html.parser')
    channel_list = soup.select('form > table > tbody > tr')

    for channel in channel_list: 
        title = channel.select('h1 > a')[0].text.strip()
        category = channel.select('p.category')[0].text.strip()
        subscriber = channel.select('.subscriber_cnt')[0].text
        view = channel.select('.view_cnt')[0].text
        video = channel.select('.video_cnt')[0].text
        # print(title, category, subscriber, view, video)
        data = [title, category, subscriber, view, video]
        results.append(data)

import pandas as pd 

df = pd.DataFrame(results)
df.columns = ['title', 'category', 'subscriber', 'view', 'video']
df.to_csv('./youtube_rank.csv', index=False)

