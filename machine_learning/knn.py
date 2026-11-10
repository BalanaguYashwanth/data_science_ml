import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split, cross_val_predict
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score, recall_score, precision_score
import seaborn as sns
from matplotlib import pyplot as plt

df = pd.read_csv("/Users/yashwanth/other-projects/AI_ML/data_science/data/frauddata.csv")
X = df.drop(columns=['fraud', 'id'])
y = df['fraud']

sns.scatterplot(x=X['dist_from_home'], y=X['purchase_price_ratio'], hue=df['fraud'])
plt.show()
x_train,x_test,y_train,y_test=train_test_split(X, y, test_size=0.2)
scalar=StandardScaler()
x_train=scalar.fit_transform(x_train)
x_test = scalar.transform(x_test)
knn = KNeighborsClassifier(n_neighbors=3)
knn.fit(x_train, y_train)
y_pred = knn.predict(x_test)

accuracy = accuracy_score(y_test, y_pred)
precision = precision_score(y_test, y_pred)
recall = recall_score(y_test, y_pred)
print("accuracy: ", accuracy)
print("precision: ", precision)
print('recall:', recall)
scores = []
k_values = [i for i in range(1,4)]

_scalar = StandardScaler()
X = _scalar.fit_transform(X)
for k in k_values:
    knn = KNeighborsClassifier(n_neighbors=k)
    score = cross_val_predict(knn, X, y, cv=5)
    scores.append(np.mean(score))

sns.lineplot(x=k_values, y=scores, markers='o')
plt.xlabel("K values")
plt.ylabel("Scores")
plt.show()