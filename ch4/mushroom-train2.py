import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn import metrics
from sklearn.model_selection import train_test_split

# 데이터 읽기
mr = pd.read_csv("mushroom.csv", header=None)

# 데이터 내부의 기호를 숫자로 변환하기
label = []
data = []
attr_list = []

for row_index, row in mr.iterrows():
    label.append(row.ix[0])
    exdata = []
    for col_index, col in enumerate(row.ix[1:]):
        if row_index == 0:
            attr = {"dic": {}, "cnt":0}
            attr_list.append(attr)
        else:
            attr = attr_list[col_index]
            if row_index == 100:
                print("attr({})={}".format(col_index,attr))
# 버섯의 특징 기호를 배열로 나타내기
        d = [0,0,0,0,0,0,0,0,0,0,0,0]
        if col in attr["dic"]:
            idx = attr["dic"][col]
        else:
            idx = attr["cnt"]
            attr["dic"][col] = idx
            attr["cnt"] += 1
        d[idx] += 1
        exdata += d
    data.append(exdata)

# 학습 전용과 테스트 전용 데이터로 나누기
data_train, data_test, label_train, label_test = train_test_split(data, label)

clf = RandomForestClassifier()
clf.fit(data_train, label_train)

predict = clf.predict(data_test)

ac_score = metrics.accuracy_score(label_test, predict)
cl_report = metrics.classification_report(label_test, predict)
print("score =", ac_score)
print("report =\n")
print(cl_report)
