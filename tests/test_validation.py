import pandas as pd
from src.validate import validate_dataset


def test_validate_dataset_returns_correct_row_count():
    df = pd.DataFrame({
        "device_brand": ["Apple Watch", "Dexcom", "Fitbit"],
        "severity_label": ["High", "Medium", "Low"]
    })

    result = validate_dataset(df)

    assert result["rows"] == 3


def test_validate_dataset_returns_correct_column_count():
    df = pd.DataFrame({
        "device_brand": ["Apple Watch", "Dexcom"],
        "severity_label": ["High", "Medium"]
    })

    result = validate_dataset(df)

    assert result["columns"] == 2


def test_validate_dataset_detects_missing_values():
    df = pd.DataFrame({
        "device_brand": ["Apple Watch", None],
        "severity_label": ["High", "Medium"]
    })

    result = validate_dataset(df)

    assert result["missing_values"] == 1
