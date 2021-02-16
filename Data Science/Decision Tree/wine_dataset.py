import sklearn
from sklearn.datasets import load_wine
from  sklearn.model_selection import train_test_split

dataset = load_wine()

# print(dataset.DESCR)
# print(dataset.feature_names)
# print(dataset.target_names)
# print(dataset.frame)  -> error
X_train, X_test, y_train, y_test = train_test_split(dataset.data, dataset.target, test_size=0.30, random_state = 45)

# print(X_train)
# print(X_test)
# print(y_test)

from sklearn import tree
classifier = tree.DecisionTreeClassifier(criterion='entropy',random_state=0)
classifier = classifier.fit(X_train,y_train)

input_data = [[0.4, 10.7, 20.3, 10.6, 12, 2.8, 3, 0.1, 2.5, 5.1, 1.0, 3.2, 123]]
predict_data = classifier.predict(input_data)
print("입력 데이터: ", input_data)
print("입력 데이터의 와인 종류: ", dataset.target_names[predict_data])

prediction = classifier.predict(X_test)
# train_predict = classifier.predict(X_train)
# print(train_predict)
# test_predict = classifier.predict(X_test)

tree_depth = classifier.get_depth()
print("이 트리의 높이: ",tree_depth)

tree_leaf_count = classifier.get_n_leaves()
print("이 트리의 리프 수: ", tree_leaf_count)

# print(train_predict)
accuracy = sklearn.metrics.accuracy_score(prediction,y_test)

print("입력 데이터의 예측 확률: ", '%.2f'% (accuracy*100),"%")


