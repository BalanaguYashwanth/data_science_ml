import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score

df = pd.read_csv("/Users/yashwanth/other-projects/AI_ML/data_science/data/multi_linear_basic.csv")
x = df[['Study_hours', 'Practice_hours']]
y = df['Marks']

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.25, random_state=25)

model = LinearRegression()
model.fit(x_train, y_train)
print('coff:', model.coef_)
print('intercept:', model.intercept_)

y_predict = model.predict(x_test)
print('predict:', y_predict)

predict_df = pd.DataFrame(x_test)
predict_df['Actual_Marks'] = y_test
predict_df['Predict_Marks'] = y_predict
print('Predict\n', predict_df)

mae = mean_absolute_error(y_test, y_predict)
mse = mean_squared_error(y_test, y_predict)
rmse = np.sqrt(mse)
r2 = r2_score(y_test, y_predict)
print("mae:",mae)
print("mse:",mse)
print("rmse:",rmse)
print("r2:",r2)