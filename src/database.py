import sqlite3
import pandas as pd


def create_connection(db_name="phi_accessibility.db"):
    return sqlite3.connect(db_name)


def load_dataframe_to_db(df: pd.DataFrame, table_name="accessibility_posts"):
    conn = create_connection()

    df.to_sql(
        table_name,
        conn,
        if_exists="replace",
        index=False
    )

    conn.close()

    print(f"Loaded {len(df)} records into {table_name}")
