'''
colab에 Nanum 폰트 설치 
'''
!sudo apt-get install -y fonts-nanum 
!fc-cache -fv 
!rm ~/.cache/matplotlib -rf 
sa
# 이후 런타임 재시작, 해당 셸 스킵 후 코드 실행 

'''
필요 라이브러리 Import 
'''
from wordcloud import WordCloud, STOPWORDS   
from PIL import Image

import numpy as np  
import matplotlib as mpl 
import matplotlib.pyplot as plt 
import matplotlib.font_manager as fm  
import seaborn as sns 
  
%matplotlib inline

# 마이너스 폰트 깨짐 방지 
mpl.rcParams['axes.unicode_minus'] = False   

# 한글 폰트 설정 
plt.rc('font', family='NanumBarunGothic') 

# 워드클라우드 한글 폰트 설정 
from wordcloud import WordCloud   

font_path = '/usr/share/fonts/truetype/nanum/NanumSquareR.ttf'
wordcloud = WordCloud(font_path=font_path, max_font_size=60)

# 0. 여러 옵션들 
1) 색상 옵션 
plt. 

2) size 옵션 
plt.rcParams['figure.figsize'] = [10, 8] 

3) title, label 옵션 
plt.title(title)
plt.xlabel('x label') 
plt.ylabe('y label') 

4) 축 옵션 
# axis(): 보여줄 축의 범위 지정 
plt.axis([0, 3, 2, 5])   # x축: 0~3, y축: 2~5까지 보여줌 

5) subplots 
# subplot: 여러 axes의 집합, figure: subplot을 모두 포함하는 오브젝트 
# subplot(행의 수, 열의 수, 만들고자 하는 subplot의 Index) 
plt.subplot(1, 2, 1) 
plt.plot(x, y, color='green')
plt.title(title) 

plt.subplot(1, 2, 2) 
plt.plot(x, y, coloer='steelblue')
plt.title(title) 
plt.show() 

5-1) subplot adjust 
# subplot_adjust(): subplot의 margin 조정. 
# left, right, bottom, top, wspace: subplots의 수평 간격, hspace: subplots의 수직 간격 
# ... 앞의 코드 생략 
plt.subplots_adjust(bottom=0.2, hspace=0.25) ) 
plt.show() 

6) Legends 옵션 
# legend(): 그래프 모서리에 작은 모달을 달아 각 라벨이 무엇을 의미하는지 알려줌 
# loc 0: best, 1: upper right, 2: upper left, 3: lower left, ... 10: center 

6-1) legend() 함수 이용 
plt.legend(['parabola', 'cubic'], loc= 0)    
plt.show() 

6-2) label 옵션 이용 
plt.plot(x, y, label='parabola')
plt.plot(x, y, label='cubic') 
plt.legend()   # 꼭 호출해주어야 함 
plt.show() 

7) tick 옵션 
# figure는 여러 subplot을 보유하기 때문에, tick을 수정할 subplot 명시 
# ax: axes 오브젝트
1) subplot 이용 
ax = plt.subplot(1, 1, 1)  # 수정할 subplot 명시 

ax = plt.subplot()
ax.set_xticks([1, 2, 4])  # x축에 보여지는 값 수정 

plt.plot(x, y, 'o')   # 'o': scatter 그래프 
ax.set_yticks([0.1, 0.6, 0.8])   # y축에 보여지는 값 수정 
ax.set_yticklabels(['10%', '60%', '80%'])   # y축 라벨 지정 

2) subplot 이용 x 
xs = df['x'].to_list()
xlabels = df['x'].apply(lambda x: x[4:]).to_list()   # YYYYMMDD의 경우 MMDD만 label로 표시
plt.plot(xs, y)
plt.xticks(xs, xlabels, rotation=45)
plt.xlabel('2020 Daily Trend') 
# parameter nbins: 출력할 개수 지정 
plt.locator_params(axis='x', nbins=len(xlabels) / 2)   

8) figure 옵션 
# figure(): 새로운 figure 생성 
plt.figure(figsize=(4, 10))   # 가로, 세로 길이 지정 
plt.savefig('cori.png')   # png 파일로 저장 


9) close 옵션 
plt.close('all')   # 기존에 존재하는 모든 그래프 삭제 

# 1. 막대 그래프 
def plot_bar_vertical(x, y):   # x: list[], y: list[] 
  ''' 
  x축, y축에 들어갈 값을 입력으로 받아 수직 막대 그래프 출력
  ''' 
  plt.bar(x, y, tick_label=x)
  plt.xticks(x, x)
  plt.show()
  
def plot_bar_horizon(x, y):   # x: list[], y: list[] 
  '''
  x축, y축에 들어갈 값을 입력으로 받아 수평 막대 그래프 출력 
  ''' 
  x = x[:20][::-1]   # 역순으로 정렬해야 보기 좋게 출력됨 
  plt.barh(x, y, tick_label=x)  
  plt.show()


# 2. 선 그래프 
def plot_line(x, y):  # x: list[int], y: list[int]
  ''' 
  x축, y축에 들어갈 값을 입력으로 받아 선 그래프 출력 
  '''
  plt.plot(x, y) 
  plt.show() 

def plot_mulit_line(x, y1, y2):  # x: list[], y1: list[int], y2: list[int]
  '''
  x축, y축에 들어갈 값을 입력으로 받아 여러개의 선 그래프 출력 
  # linestyle: '--', ':', ' ' ...  
  # marker: 'o', '*', 's' ... 
  ''' 
  plt.plot(x, y1, color='green')
  plt.plot(x, y2, color='blue', linestyle=':', marker='o')  
  plt.show() 


# 3. 히트맵 
# 0) create pivot table 
def create_matrix(table):
  '''
  입력받은 테이블의 index와 columns를 설정해서 matrix 생성
  ''' 
  rating_matrix = table.pivot(index='m_no', columns='goodsno', values='point')
  return rating_matrix
 
# pivot table -> heatmap 
def create_heatmap(rating_matrix):
  fig, ax = plt.subplots(figsize=(12, 6))  # 크기 지정 
  sns.heatmap(rating_matrix, annot=False, ax=ax, cmap='Blues') 
  plt.show() 


# 4. 워드클라우드 
# 형태소 분석기 설치 
!python3 -m pip install konlpy 

# 워드 클라우드 설치 
!pip install wordcloud 

# 워드클라우드 생성 
def plot_wordCloud(sentence_list):
  '''
  문장 리스트를 입력으로 받으면, 입력받은 데이터에 대한 워드클라우드 출력 
  '''
  stopwords = set(STOPWORDS)   # 제외할 단어 등록 
  stopwords.add('정말')
  stopwords.add('내가')
  stopwords.add('그리고')
  stopwords.add('그래서')
  
  # 문장 리스트를 join() 함수를 이용하여 하나의 str로 변환 후 워드클라우드 생성 
  wordcloud = WordCloud(font_path=font_path, max_font_size=60, stopwords=stopwords).generate(" ".join(sentence_list))
  print(f'wordcloud shape: {wordcloud.to_array().shape}')   

  plt.axis('off')
  # bilinear 보간법 적용 후 이미지 출력 
  plt.imshow(wordcloud, interpolation='bilinear')   
  plt.show() 

def plot_wordCloud_frequencies(word_dict):
  '''
  단어: 빈도수 형태의 dictionary를 입력으로 받으면, 이에 대한 WordCloud 출력 
  '''
  # 빈도 수 기준 워드클라우드 생성 
  wordcloud = WordCloud(font_path=font_path, max_font_size=60).generate_from_frequencies(word_dict)  
  
  plt.figure()
  plt.axis("off")
  # bilinear 보간법 적용 후 이미지 출력 
  plt.imshow(wordcloud, interpolation="bilinear")   
  plt.show()
 
 def plot_wordCloud_img(word_dict, img):
  '''
  단어: 빈도수 형태의 dictionary와 배경으로 사용할 img를 입력으로 받고, 
  이에 대한 WordCloud 출력  
  '''
  img = np.array(Image.open('.png'))  # Image를 numpy 배열로 변환 
  wc = WordCloud(background_color="white", # 배경색 지정
               max_words=30, # 출력할 최대 단어 수
               mask=img, # 배경으로 사용할 이미지
               contour_width=3,  # 테두리선의 크기
               contour_color='steelblue') # 테두리선의 색

  wc.generate_from_frequencies(word_dict) # 워드 클라우드 생성

  wc.to_file(".png") # 결과를 이미지 파일로 저장

  # 화면에 결과를 출력
  plt.figure()
  plt.axis("off")
  plt.imshow(wc, interpolation='bilinear')
  plt.show()