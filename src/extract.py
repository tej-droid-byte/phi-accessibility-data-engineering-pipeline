import pandas as pd
from config import SAMPLE_DATA_PATH


def extract_csv(file_path=SAMPLE_DATA_PATH):
    """
    Extract data from a CSV file.
    """
    df = pd.read_csv(file_path)
    print(f"Extracted {len(df)} rows from {file_path}")
    return df
