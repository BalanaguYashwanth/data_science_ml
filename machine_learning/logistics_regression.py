import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix

df = pd.read_csv("/Users/yashwanth/other-projects/AI_ML/data_science/data/diabetes.csv")

feature_cols = ['Pregnancies', 'Glucose', 'Insulin', 'BMI', 'Age', 'BloodPressure','DiabetesPedigreeFunction']
x = df[feature_cols]
y = df['Outcome']
x_train, x_test, y_train, y_test = train_test_split(x,y, test_size=0.25, random_state=0)

model = LogisticRegression(solver='lbfgs', max_iter=1000)
model.fit(x_train, y_train)
y_pred=model.predict(x_test)
test_df = pd.DataFrame(x_test)
test_df['y_test'] = y_test
test_df['y_pred'] = y_pred
print(test_df.head(40))

#Evaluation
cnf_matrix = confusion_matrix(y_test, y_pred)
print('\n Evaluation: \n',cnf_matrix)


accuracy = (118 + 36) / (118 + 12 + 26 + 36)
precision = 36 / (36 + 12)
recall = 36 / (36 + 26)