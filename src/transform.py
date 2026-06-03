import pandas as pd
import numpy as np

def clean_and_transform(df: pd.DataFrame) -> pd.DataFrame:

    # =============================
    # 0. Standardize columns
    # =============================
    df.columns = (
        df.columns.str.strip()
        .str.lower()
        .str.replace(".", "_")
        .str.replace(" ", "_")
    )

    # =============================
    # 1. Remove duplicates
    # =============================
    df = df.drop_duplicates()

    # =============================
    # 2. Convert numeric columns FIRST (IMPORTANT FIX)
    # =============================
    num_cols = ["sales", "profit", "discount"]

    for col in num_cols:
        df[col] = pd.to_numeric(df[col], errors="coerce")

    # Drop invalid numeric rows
    df = df.dropna(subset=num_cols)

    # =============================
    # 3. Convert dates safely for DB
    # =============================
    df["order_date"] = pd.to_datetime(df["order_date"], errors="coerce").dt.date
    df["ship_date"] = pd.to_datetime(df["ship_date"], errors="coerce").dt.date

    df = df.dropna(subset=["order_date", "ship_date"])

    # =============================
    # 4. Feature Engineering
    # =============================

    df["profit_margin"] = np.where(
        df["sales"] != 0,
        df["profit"] / df["sales"],
        0
    )

    df["shipping_delay_days"] = (
        pd.to_datetime(df["ship_date"]) - pd.to_datetime(df["order_date"])
    ).dt.days

    # FIXED BOOLEAN (IMPORTANT)
    df["is_high_value_order"] = np.where(df["sales"] > 500, True, False)

    df["discount_impact"] = df["sales"] * df["discount"]

    # =============================
    # 5. Business categorization
    # =============================
    df["profit_category"] = pd.cut(
        df["profit"],
        bins=[-np.inf, 0, 50, 200, np.inf],
        labels=["loss", "low_profit", "medium_profit", "high_profit"]
    )

    df["sales_category"] = pd.cut(
        df["sales"],
        bins=[0, 100, 500, 1000, np.inf],
        labels=["low", "medium", "high", "very_high"]
    )

    # =============================
    # 6. Final cleanup
    # =============================
    df = df[df["sales"] > 0]
    df = df.reset_index(drop=True)

    return df