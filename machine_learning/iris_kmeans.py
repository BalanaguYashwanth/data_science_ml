import pandas as pd
from matplotlib import pyplot as plt
from sklearn.metrics import silhouette_score, adjusted_rand_score
from sklearn.cluster import KMeans
from sklearn.model_selection import train_test_split
from sklearn.datasets import load_iris

iris = load_iris()
df = pd.DataFrame(iris.data, columns=iris.feature_names)
df.head()
x_train, x_test = train_test_split(df[['petal length (cm)','petal width (cm)']], test_size=0.1, random_state=42)
km=KMeans(n_clusters=3, random_state=1)
pred = km.fit_predict(x_train)
cluster = km.cluster_centers_

# plt.scatter(x_train.iloc[:,0], x_train.iloc[:,1], cmap='rainbow')
plt.scatter(x_train.iloc[:,0], x_train.iloc[:,1],c=km.predict(x_train), cmap='rainbow')
plt.scatter(cluster[:,0], cluster[:,1])
# plt.show()

train_pred = pd.DataFrame(x_train)
train_pred['pred'] = pred
print(train_pred.head(10))


score = silhouette_score(x_train, pred)
print("Silhouette Score:", score)

ari = adjusted_rand_score(x_train.index, pred)
print("Adjusted Rand Index:", ari)
