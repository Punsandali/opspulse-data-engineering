import os
from sqlalchemy import create_engine
from urllib.parse import quote_plus

def save_and_load(df, path):
    # -------------------
    # 1. SAVE CSV
    # -------------------
    os.makedirs(os.path.dirname(path), exist_ok=True)
    df.to_csv(path, index=False)
    print(f"CSV saved at {path}")

    # -------------------
    # 2. LOAD TO POSTGRES
    # -------------------
    password = quote_plus("Punsandali@123")

    engine = create_engine(
        f"postgresql+psycopg2://postgres:{password}@localhost:5432/opspulse_db"
    )

    df.to_sql(
        "processed_superstore",
        engine,
        if_exists="replace",
        index=False
    )

    print("Data loaded to PostgreSQL successfully")