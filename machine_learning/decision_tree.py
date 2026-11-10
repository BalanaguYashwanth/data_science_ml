import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import classification_report, confusion_matrix

df = pd.read_csv("/Users/yashwanth/other-projects/AI_ML/data_science/data/decision_tree.csv")
X = df.drop('Class', axis=1)
y = df['Class']
x_train, x_test, y_train, y_test = train_test_split(X,y, test_size=0.20)
decision_tree=DecisionTreeClassifier()
decision_tree.fit(x_train, y_train)
y_pred = decision_tree.predict(x_test)
test_df = pd.DataFrame(x_test)
test_df['Predit'] = y_pred
print("Confusion matrix: \n",confusion_matrix(y_test, y_pred))
print("Classification report:\n",classification_report(y_test, y_pred))
