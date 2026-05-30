from src.transform import standardize_missing_values
import pandas as pd


def test_standardize_missing_values():

    df = pd.DataFrame({
        "value": ["unknown", "Apple Watch", ""]
    })

    transformed = standardize_missing_values(df)

    assert transformed["value"].isna().sum() == 2
