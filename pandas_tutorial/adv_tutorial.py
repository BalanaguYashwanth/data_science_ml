import pandas as pd

data = {'one':[11,21,31], 'two':[24,25,26]}
data_2 = {'one':[31,32,33], 'two':[41,42,43]}

df = pd.DataFrame(data)
df_2 = pd.DataFrame(data_2)

# print(df['one']) #first index
# print(df.pop('one')) #pop
# del df['one'] #del
# print(df)
# output = pd.concat([df, df_2], ignore_index=True) #concat
# print(output)