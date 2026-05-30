from extract import extract_csv
from transform import transform_dataset
from validate import validate_dataset
from load import load_to_csv
from config import PROCESSED_DATA_PATH
from load import load_to_csv, load_to_database


def run_pipeline():
    """
    Run the PHI accessibility data processing pipeline.
    """
    df = extract_csv()
    df = transform_dataset(df)
    validation_report = validate_dataset(df)

    PROCESSED_DATA_PATH.parent.mkdir(parents=True, exist_ok=True)
    load_to_csv(df, PROCESSED_DATA_PATH)
    load_to_database(df)

    print("Pipeline completed successfully")
    print(validation_report)


if __name__ == "__main__":
    run_pipeline()
