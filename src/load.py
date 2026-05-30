import pandas as pd
from database import load_dataframe_to_db


def load_to_csv(df: pd.DataFrame, output_path: str):

    df.to_csv(output_path, index=False)

    print(f"Dataset saved to {output_path}")


def load_to_database(df: pd.DataFrame):

    load_dataframe_to_db(df)
