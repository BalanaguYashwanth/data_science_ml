import pandas as pd

csv_path = '/Users/yashwanth/other-projects/AI_ML/data_science/pandas_tutorial/test_table_data.csv'
df = pd.read_csv(csv_path)

print(df.loc[0:1]) # accessing from 0 row to 1st row
print('----------')
print(df.iloc[:, 1:4]) # accessing all rows with column from 1st to 3nd
print(df)
print('----------')
print(df['age'])
print('----------')
print('slicing: \n',df[1:2])
print('----------')
print(df.iloc[1,1:])
print('----------')
print(df['age'].min())