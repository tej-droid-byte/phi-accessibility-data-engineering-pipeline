import pandas as pd
from src.transform import clean_text_columns, standardize_missing_values


def test_clean_text_columns_strips_whitespace():
    df = pd.DataFrame({
        "device_brand": [" Apple Watch ", " Dexcom "]
    })

    result = clean_text_columns(df)

    assert result["device_brand"].tolist() == ["Apple Watch", "Dexcom"]


def test_standardize_missing_values_replaces_unknown_values():
    df = pd.DataFrame({
        "device_brand": ["unknown", "Apple Watch", ""]
    })

    result = standardize_missing_values(df)

    assert result["device_brand"].isna().sum() == 2
