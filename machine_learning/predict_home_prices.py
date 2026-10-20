from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
import numpy as np
from sklearn.model_selection import train_test_split
import pandas as pd

df = pd.read_csv("/Users/yashwanth/other-projects/AI_ML/data_science/data/home_prices.csv")
x = df[['Area_sqft']]
y = df['Price_Lakhs']

# Train
x_train, x_test, y_train, y_test = train_test_split(x,y,train_size=0.8, test_size=0.2,random_state=42)
model = LinearRegression()
model.fit(x_train,y_train)
print("Slope:", model.coef_)
print("Intercept:", model.intercept_)

# Prediction
y_pred = model.predict(x_test)
print("predict_output:",y_pred)

results = pd.DataFrame({
    "area_sqft_actual": x_test['Area_sqft'].values,
    "price_lakhs_actual": y_test.values,
    "price_lakhs_predicted": y_pred
})
print('results:', results)

# Evluation
mae = mean_absolute_error(y_test, y_pred)
mse = mean_squared_error(y_test, y_pred)
rmse = np.sqrt(mse)
r2 = r2_score(y_test, y_pred)

print("MAE:", round(mae,2))
print("MSE:", round(mse,2))
print("RMSE:", round(rmse,2))
print("R2:", round(r2, 3))

