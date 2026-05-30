import pandas as pd


def clean_text_columns(df: pd.DataFrame):
    """
    Strip whitespace and standardize text fields.
    """
    df = df.copy()

    text_columns = df.select_dtypes(include="object").columns

    for col in text_columns:
        df[col] = df[col].astype(str).str.strip()

    return df


def standardize_missing_values(df: pd.DataFrame):
    """
    Replace empty strings and unknown values with None.
    """
    df = df.copy()

    df = df.replace(
        ["", " ", "nan", "None", "unknown", "Unknown"],
        None
    )

    return df


def transform_dataset(df: pd.DataFrame):
    """
    Apply core transformations.
    """
    df = clean_text_columns(df)
    df = standardize_missing_values(df)

    print("Transformation completed")
    return df
