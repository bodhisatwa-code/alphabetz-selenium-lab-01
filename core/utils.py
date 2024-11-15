import pandas as pd

def load_test_data_from_csv(file_path):
    df = pd.read_csv(f"test_data/{file_path}")
    return [tuple(row) for row in df.itertuples(index=False, name=None)], df.columns.tolist()
