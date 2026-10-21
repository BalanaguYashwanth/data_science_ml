from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
import numpy as np
from sklearn.model_selection import train_test_split
import pandas as pd

df = pd.read_csv("/Users/yashwanth/other-projects/AI_ML/data_science/data/home_prices.csv")
x = df[['Area_sqft']]
y = df['Price_Lakhs']

# Pandas DataFrame Display

#First 5 records
first_five = df.head(5)
print("First five: \n",first_five)

#Last 5 records
last_five = df.tail(5)
print("Last five: \n",last_five)

#Number of rows and columns
print('Rows x Columns:', df.shape)

#Column names
print('Columns:',df.columns)

#Data types
print('data types: \n', df.dtypes)

#Missing values
print("Data has null:",df.isnull().sum())


######################

# Exploratory data analysis

#⁠Average house area
print('Average sqft:',df['Area_sqft'].mean())

#⁠Minimum house area
print('Minimum sqft:',df['Area_sqft'].min())

#⁠Maximum house area
print('Maximum sqft:',df['Area_sqft'].max())

#⁠Average house price
print('Maximum sqft:',df['Price_Lakhs'].mean())

#⁠Minimum house price
print('Maximum sqft:',df['Price_Lakhs'].min())

#####################

# Describe
print("Describe: \n",df.describe())

######################

# Train
x_train, x_test, y_train, y_test = train_test_split(x,y,train_size=0.8, test_size=0.2,random_state=42)
model = LinearRegression()
model.fit(x_train,y_train)
slope = model.coef_[0]
intercept = model.intercept_
print("Slope:", slope)
print("Intercept:", intercept)

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

######################

# Prediction of few more sqft's with custom dataset

# Calculating actual value
file_source_path = "/Users/yashwanth/other-projects/AI_ML/data_science/data/predict_home_prices.csv"
df = pd.read_csv(file_source_path)
df['Price_Lakhs'] = df['Area_sqft'] * slope + intercept
df.to_csv(file_source_path,index=False)

# Predict
y_pred = model.predict(df[['Area_sqft']])
df['Predict_Price_Lakhs'] = y_pred
df.to_csv(file_source_path, index=False)

df['Error'] = df['Price_Lakhs']-df['Predict_Price_Lakhs']
df.to_csv(file_source_path, index=False)

df['mae'] = mean_absolute_error(y_true=df['Price_Lakhs'],y_pred=df['Predict_Price_Lakhs'])
df['mse'] = mean_squared_error(y_true=df['Price_Lakhs'],y_pred=df['Predict_Price_Lakhs'])
df['rmse'] = np.sqrt(df['mse'])
df['r2'] = r2_score(y_true=df['Price_Lakhs'], y_pred=df['Predict_Price_Lakhs'])
df.to_csv(file_source_path, index=False)

