import pandas as pd
from sklearn.datasets import load_iris
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from matplotlib import pyplot as plt 
import seaborn as sns

iris = load_iris()

df = pd.DataFrame({
    'sepal_length': iris.data[:,0],
    'sepal_width': iris.data[:,1],
    'petal_length': iris.data[:,2],
    'petal_width': iris.data[:,3],
    'species': iris.target
})
X = df[['sepal_length', 'sepal_width', 'petal_length', 'petal_width']]
y = df['species']

x_train, x_test, y_train, y_test = train_test_split(X, y, test_size=0.3)

rf = RandomForestClassifier(n_estimators=100)
rf.fit(x_train, y_train)
y_pred = rf.predict(x_test)
print(y_pred)

# Evals
accurancy_evals = accuracy_score(y_test, y_pred)
print("accurancy_evals:", accurancy_evals)

#Feature importance
feature_imp = pd.Series(rf.feature_importances_, index=iris.feature_names).sort_values(ascending=False)
print(feature_imp)

#Diagram


sns.barplot(x=feature_imp, y=feature_imp.index)
plt.legend()
plt.show()