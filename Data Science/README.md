[Assignments]

○ Decision Tree 코드를 다음과 같이 수정 및 작성 

- target 변수를 lwvel로 수정하고, did_well은 입력변수로 사용 
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
