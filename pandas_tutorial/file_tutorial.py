import pandas as pd

csv_path = '/Users/yashwanth/other-projects/AI_ML/data_science/pandas_tutorial/test_table_data.csv'
json_path = '/Users/yashwanth/other-projects/AI_ML/data_science/pandas_tutorial/test_data.json'
xslx_path = '/Users/yashwanth/other-projects/AI_ML/data_science/pandas_tutorial/temp1_data.xlsx'

csv_df = pd.read_csv(csv_path)
json_df = pd.read_json(json_path)
xlsx_df = pd.read_excel(xslx_path, sheet_name='Sheet2')


final_df = pd.concat([csv_df, json_df, xlsx_df], ignore_index=True)

print(final_df)
# print(df)
# print(df['age'])
# print('slicing: \n',df[1:2])
# print(df.iloc[1,1:])
# print(df['age'].min())