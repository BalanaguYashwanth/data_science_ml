import pandas as pd
from matplotlib import pyplot as plt 
from sklearn.preprocessing import MinMaxScaler
from sklearn.model_selection import train_test_split
from sklearn.cluster import KMeans

df = pd.read_csv("/Users/yashwanth/other-projects/AI_ML/data_science/data/income.csv")
df = df.drop('Name', axis=1)

x_train, x_test = train_test_split(df[['Age', 'Income']], test_size=0.25, random_state=42)

km=KMeans(n_clusters=2)
cluster_pred = km.fit_predict(x_train)

# scatter plot (because inputs are very different ranges espically income, to normalize both in same values b/w 0 to 1)
scalar = MinMaxScaler()
x_train_scalar = scalar.fit_transform(x_train)

km_scalar = KMeans(n_clusters=3)
km_scalar.fit_predict(x_train_scalar)
cluster = km_scalar.cluster_centers_

plt.scatter(x_train_scalar[:,0], x_train_scalar[:,1])
plt.scatter(cluster[:,0], cluster[:,1])
plt.show()



