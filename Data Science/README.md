[Decision Tree]

○ Decision Tree 코드를 다음과 같이 수정 및 작성 

- target 변수를 level로 수정하고, did_well은 입력변수로 사용 
- 필요에 따라 Candidate class의 정의 수정 
- lang = 'Java', tweets = True, phd = False, did_well = True인 경우의 분류결과 출력 
- lang = 'Python', tweets = False, phd = False, did_well = False인 경우의 분류결과 출력 

○ wine 분류 데이터를 얻는 API (https://scikit-learn.org/stable/modules/generated/sklearn.datasets.load_wine.html 와 
  의사결정나무를 생성/활용하는 API (https://scikit-learn.org/stable/modules/generated/sklearn.tree.DecisionTreeClassifier.html#sklearn.tree.DecisionTreeClassifier) 를
  활용하여 다음 질문에 답하는 프로그램을 작성하여 제출

- 의사결정나무를 criterion = 'entropy', random_state = 0 외에는 모두 default로 설정하여 생성 
- [0.4, 10.7, 20.3, 10.6, 12, 2.8, 3, 0.1, 2.5, 5.1, 1.0, 3.2, 123] 입력데이터의 와인 종류 출력
- [0.4, 10.7, 20.3, 10.6, 12, 2.8, 3, 0.1, 2.5, 5.1, 1.0, 3.2, 123] 입력데이터의 예측확률 출력
- 의사결정 나무의 리프의 수 출력
- 의사결정 높이 (깊이) 출력

[KNN]

○ 기간별_일평균_대기환경_정보_2018년.csv 파일의 data cleaning 

- 측정값이 모두 0으로 들어간 결측치 값이 들어간 행을 삭제한 파일을 data1.csv로 저장 및 제출 
- 주어진 csv 파일의 컬럼명을 cdate, acode, aname, scode,sname,fdust,ufdust,ozone, nd, cm, sagas와 같이 변경 

○ data1.csv 파일 조작 

- 공기질 airquality 컬럼을 추가하여, 다음과 같이 미세미세 앱의 기준과 영어단어에 따라 값을 부여 
- 미세미세 앱의 6가지 조건 중 가장 낮은 공기품질로 결정 
  ex) 모두 0이고, 미세먼지가 50이면 보통 
- 초미세먼지 컬럼을 제거하고, data2.csv를 만들어 제출 

○ K-NN 분석 

- 초미세먼지 컬럼이 없는 data2.csv 파일을 기반으로 k-NN 알고리즘을 이용하여 공기질을 예측하는 파이썬 프로그램 작성하여 제출 
- 데이터를 저장된 순서대로 7:3으로 나누어, recall(1점), precision(1점), f-score(1.8점) 값ㅇㄹ 출력한 화면을 캡처하여 제출 
- f-score는 값에 따른 등급별 점수 부여 

[Linear Regression]

○ 기간별_일평균_대기환경_정보_2018년.csv 파일의 data cleaning 

- 측정값이 모두 0으로 들어간 결측치 값이 들어간 행을 삭제한 파일을 data1.csv로 저장 및 제출 
- 주어진 csv 파일의 컬럼명을 cdate, acode, aname, scode,sname,fdust,ufdust,ozone, nd, cm, sagas와 같이 변경 

○ data1.csv 파일 조작 

- 필요에 따라, 데이터 정규화, 제곱, 다양한 결합값 등을 컬럼으로 추가한 data2.csv 파일을 만들어 제출 (data1.csv 파일의 데이터만 사용)

○ 선형회귀분석 

- 초미세먼지 값을 구하기 위한 data2.csv 컬럼을 이용하여, 선형회귀분석식의 beta와 R^2를 출력하는 파이썬 프로그램 작성하여 제출
- R^2 값에 따라 등급별 점수 부여 
