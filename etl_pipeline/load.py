import pandas as pd

def load_csv_data():
    csv_file_path = '/Users/yashwanth/other-projects/AI_ML/data_science/etl_pipeline/sales_data.csv'
    df = pd.read_csv(csv_file_path)
    return df
