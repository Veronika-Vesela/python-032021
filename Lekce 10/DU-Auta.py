import requests
import pandas
import numpy
import matplotlib.pyplot as plt

from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.preprocessing import StandardScaler
from sklearn.tree import DecisionTreeClassifier

auta = pandas.read_csv("auto.csv", na_values=["?"])
auta=auta.dropna()

auta_spotreba = pandas.pivot_table(auta, values="mpg", index="year", columns="origin", aggfunc="mean")
print(auta_spotreba)

auta_spotreba.plot(kind="line", title = "Průměrná spotřeba aut v jednotlivých regionech v letech 1970-1982")
plt.show()

X = auta.drop(columns=["origin", "name"])
y = auta["origin"]

X_train, X_test, y_train, y_test = train_test_split(X,y,test_size=0.7, random_state=42, stratify=y)



scaler = StandardScaler()
X_train=scaler.fit_transform(X_train)
X_test =scaler.transform(X_test)

model = DecisionTreeClassifier(random_state=42)
params ={'max_depth': [1,2,3,4,5,6,20], 'min_samples_leaf': [1,2,5,10,15]}
clf = GridSearchCV(model, params, scoring="f1_weighted")
clf.fit(X_train,y_train)
print(f"Nejlepší parametry jsou: {clf.best_params_}")
print(f"Nejlepší skore je {clf.best_score_}")

