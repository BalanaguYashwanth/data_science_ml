import pandas as pd

df = pd.read_csv("/Users/yashwanth/other-projects/AI_ML/data_science/data/animal.csv", delimiter=';')

print(df.head())
# print(df.head(20)) #first 20 rows
# print(df.iloc[0]) # first row
# print(df.loc[0]) # first row
# print(df['animal']) # only animal rows
# print(df.loc[:'animal']) # accessing [all rows : only animal column]
# print(df.iloc[-1]) #last row
# print(df['water_need'].sum()) # sum of all rows
# print(df.water_need.sum()) # sum of all rows in different format
# print(df['water_need'].min()) #minimum least value
# print(df['water_need'].max()) #max least value
# print(df['water_need'].mean())
# print(df['water_need'].median())
# print(df[['water_need','animal']].groupby('animal').mean().sort_values(by='water_need', ascending=False))
# print(df['animal'].unique()) #unique of all animal characteristics
# print(df.iloc[[1,6],[0,1]]) #1st, 6th rows with selected 0th, 1st columns
# print(df.iloc[[1,6],:]) #all columns


# df.set_index("water_need", inplace=True) #making water_need as row index
# print(df.loc['Elephant':'Cow', :])
# print(df.loc['Elephant':'Cow', ['water_need']])
# print(df.loc[df['animal']=='Elephant', 'unique_id':'water_need'])
# print(df.loc['Elephant':'Cow'].iloc[:, -1])
# print(df.iloc[:]) # all rows with all columns
# print(df.iloc[:,:]) # all rows with all columns
# print(df.iloc[0,1:]) # first row & from 1st column to end

print(df['water_need'].describe())