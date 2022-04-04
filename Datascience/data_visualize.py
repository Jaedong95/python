'''
colab에 Nanum 폰트 설치 
'''
!sudo apt-get install -y fonts-nanum 
!fc-cache -fv 
!rm ~/.cache/matplotlib -rf 

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

# 색상 옵션 
plt. 

# 1. 막대 그래프 
def plot_bar_vertical(x, y, title):   # x: list[], y: list[] 
  ''' 
  x축, y축에 들어갈 값을 입력으로 받아 수직 막대 그래프 출력
  ''' 
  plt.bar(x, y, tick_label=x)
  plt.title(title)
  plt.xticks(x, x)
  plt.show()
  
def plot_bar_horizon(x, y, title):   # x: list[], y: list[] 
  '''
  x축, y축에 들어갈 값을 입력으로 받아 수평 막대 그래프 출력 
  ''' 
  x = x[:20][::-1]   # 역순으로 정렬해야 보기 좋게 출력됨 
  plt.barh(x, y, tick_label=x)  
  plt.show()

  
# 2. 선 그래프 


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