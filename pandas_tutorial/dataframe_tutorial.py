import pandas as pd

def plain_df():
    output = pd.DataFrame()
    print(output)

def array_df():
    output = pd.DataFrame([1,2,3])
    print('output: ', output)

def string_df():
    output = pd.DataFrame(['a', 'b', 'c'])
    print('output: ', output)

def array_with_columns_df():
    output = pd.DataFrame([['alex', 10], ['bish', 20], ['kiran', 30]], columns=['Name', 'Age'], index=['first', 'second', 'third'])
    print('output: \n', output)

def array_dtype():
    data = [['alex', 10], ['bish', 20], ['kiran', 30]]
    output = pd.DataFrame(data, dtype='float')
    print('output: \n', output) # Expected: Throw the error


def dict_df():
    output = pd.DataFrame({'name':['yash', 'nash', 'mash'], 'age':[20, 31, 23]})
    print(output)

def customize_index():
    output = pd.DataFrame({'name':['yash', 'nash', 'mash'], 'age': [20, 31, 23]}, index=['step1', 'step2', 'step3'])
    print(output)

def pd_series():
    df = pd.DataFrame({
    'sales': [10000, 15000, 12000]
    }, index=['Jan', 'Feb', 'Mar']) # ('\n Multi dimension execute always in 2D dimension: \n',df)

    output = pd.Series([10000, 15000, 12000], index=['Jan', 'Feb', 'Mar']) # ('\n Single series execute in 1D dimension: \n',output)

array_dtype()
