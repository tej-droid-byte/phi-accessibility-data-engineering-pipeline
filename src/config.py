from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

DATA_DIR = BASE_DIR / "data"
OUTPUT_DIR = BASE_DIR / "outputs"

SAMPLE_DATA_PATH = DATA_DIR / "sample_phi_accessibility.csv"
PROCESSED_DATA_PATH = OUTPUT_DIR / "processed_phi_accessibility.csv"

REQUIRED_COLUMNS = [
    "source_subreddit",
    "subreddit_group",
    "device_brand",
    "primary_accessibility",
    "accessibility_taxonomy",
    "assistive_technology",
    "severity_label",
    "severity_score",
    "rq_category_v2",
    "topic_name_v2",
]
