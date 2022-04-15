''' Beautiful Soup 설치 '''
# pip install bs4 

from urllib.request import urlopen 
from bs4 import BeautifulSoup

''' 구문 분석 '''
# url을 이용한 구문 분석 
url = urlopen('http://python.org')
soup = BeautifulSoup(url.read(), 'html.parser')   # url을 호출하고, html parser를 통해 구문 분석 
print(soup.h1)   # soup에서 h1 부분만 출력 

# html 파일을 이용한 구문 분석 
# find_all(name, attrs, recursive, string, limit, **kwargs): 해당 하는 부분을 모두 찾아서 반환 
with open('example.html') as f:
    soup = BeautifulSoup(f, 'html.parser')  
    div = soup.find('div')   # div 부분 찾기 
    div_all = soup.find_all('div')   # div 부분 모두 찾기 
    div_id = soup.find_all('div', {'id': 'ABC_id'})   # <div id='ABC_id'>인 태그 속성 찾아 반환
    # div_text = soup.find('div', {'id': 'ABC_id'}).text    # 해당 태그에서 텍스트 추출 
    # print(div_text)


''' 크롤링: 영화 순위 가져오기 '''
from urllib.request import urlopen
from bs4 import BeautifulSoup

url = urlopen('https://movie.naver.com/movie/sdb/rank/rmovie.nhn')
soup = BeautifulSoup(url.read(), 'html.parser')
print(soup.title)

# 페이지 소스 분석하기
# Ctrl + F로 영화 부분 찾고, 반복되는 부분 확인 

# <tr>   
# <td class="ac"><img src="./랭킹 _ 네이버 영화_files/bullet_r_r01.gif" alt="01" width="14" height="13"></td>
# <td class="title">
#   <div class="tit3">
# 	    <a href="https://movie.naver.com/movie/bi/mi/basic.naver?code=154282" title="더 배트맨">더 배트맨</a>
# 	</div>
# </td>
# <!-- 평점순일 때 평점 추가하기  -->
# <!----------------------------------------->  
# <td class="ac"><img src="./랭킹 _ 네이버 영화_files/icon_na_1.gif" alt="na" width="7" height="10" class="arrow"></td>
# <td class="range ac">0</td>
# </tr>   

# 반복되는 부분 추출 
movie = soup.find_all('div', 'tit3')

# 영화 이름 추출 
# movie[0]   -> <div class='tit3'> <a href='/movie/ ~' title='영화제목1'>영화제목1</a></div>

rank = 1 
for a in movie: 
    movie_name = a.find('a').text
    print(f'{rank}위: {movie_name}')   # <a href="">영화제목</a>에서 텍스트만 추출 
    rank += 1 
    