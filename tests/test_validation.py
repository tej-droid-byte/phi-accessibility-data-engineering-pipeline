import pandas as pd
from src.validate import validate_dataset


def test_validate_dataset():

    sample_data = pd.DataFrame({
        "device_brand": ["Apple Watch", "Dexcom"],
        "severity_label": ["High", "Medium"]
    })

    result = validate_dataset(sample_data)

    assert result["rows"] == 2
    assert result["columns"] == 2
    assert result["missing_values"] == 0
