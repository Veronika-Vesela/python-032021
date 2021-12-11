import pandas
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.preprocessing import StandardScaler

water=pandas.read_csv("water-potability.csv")
water=water.dropna()

X=water.drop(columns=["Potability"])
y=water["Potability"]

X_train, X_test, y_train, y_test = train_test_split(X,y,test_size=0.3, random_state=42 )

scaler=StandardScaler()
X_train=scaler.fit_transform(X_train)
X_test=scaler.transform(X_test)

clf=KNeighborsClassifier()
clf.fit(X_train,y_train)



