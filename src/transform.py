import pandas as pd
import numpy as np


def clean_and_transform(df: pd.DataFrame) -> pd.DataFrame:

    # -----------------------------
    # 0. Standardize column names
    # -----------------------------
    df.columns = (
        df.columns
        .str.strip()
        .str.lower()
        .str.replace(".", "_")
        .str.replace(" ", "_")
    )

    # -----------------------------
    # 1. Remove duplicates
    # -----------------------------
    df = df.drop_duplicates()

    # -----------------------------
    # 2. Handle missing values
    # -----------------------------
    df = df.dropna(subset=["sales", "profit", "order_date", "ship_date"])

    # -----------------------------
    # 3. Convert date columns
    # -----------------------------
    df["order_date"] = pd.to_datetime(df["order_date"], errors="coerce")
    df["ship_date"] = pd.to_datetime(df["ship_date"], errors="coerce")

    # Drop invalid dates
    df = df.dropna(subset=["order_date", "ship_date"])

    # -----------------------------
    # 4. Feature Engineering
    # -----------------------------

    # Profit Margin
    df["profit_margin"] = np.where(
        df["sales"] != 0,
        df["profit"] / df["sales"],
        0
    )

    # Shipping delay in days
    df["shipping_delay_days"] = (df["ship_date"] - df["order_date"]).dt.days

    # High value order flag
    df["is_high_value_order"] = np.where(df["sales"] > 500, 1, 0)

    # Discount impact
    df["discount_impact"] = df["sales"] * df["discount"]

    # -----------------------------
    # 5. Business categorization
    # -----------------------------

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

    # -----------------------------
    # 6. Remove invalid rows
    # -----------------------------
    df = df[df["sales"] > 0]
    df = df[df["profit"].notnull()]

    # -----------------------------
    # 7. Reset index
    # -----------------------------
    df = df.reset_index(drop=True)

    return df