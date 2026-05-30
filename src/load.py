import pandas as pd

def load_to_csv(df: pd.DataFrame, output_path: str):
    """
    Save processed data to CSV.
    """
    df.to_csv(output_path, index=False)
    print(f"Dataset saved to {output_path}")
