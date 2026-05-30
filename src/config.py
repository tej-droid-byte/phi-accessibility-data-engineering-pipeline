import pandas as pd

def validate_dataset(df: pd.DataFrame):
    """
    Basic data quality checks.
    """

    print(f"Rows: {len(df)}")
    print(f"Columns: {len(df.columns)}")

    missing = df.isnull().sum().sum()

    print(f"Missing Values: {missing}")

    return {
        "rows": len(df),
        "columns": len(df.columns),
        "missing_values": int(missing)
    }
