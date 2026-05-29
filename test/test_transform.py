import pandas as pd
from src.transform import clean_and_transform


# -----------------------------
# Sample test data
# -----------------------------
def get_sample_data():
    return pd.DataFrame({
        "Order.Date": ["2023-01-01", None],
        "Ship.Date": ["2023-01-03", "2023-01-05"],
        "Sales": [100, 200],
        "Profit": [20, None],
        "Discount": [0.1, 0.2]
    })


# -----------------------------
# 1. Column existence test
# -----------------------------
def test_required_columns_exist():
    df = get_sample_data()
    result = clean_and_transform(df)

    expected_columns = [
        "sales",
        "profit",
        "order_date",
        "ship_date",
        "profit_margin",
        "shipping_delay_days"
    ]

    for col in expected_columns:
        assert col in result.columns


# -----------------------------
# 2. Null check test
# -----------------------------
def test_no_null_values_in_critical_columns():
    df = get_sample_data()
    result = clean_and_transform(df)

    assert result["sales"].isnull().sum() == 0
    assert result["profit"].isnull().sum() == 0
    assert result["order_date"].isnull().sum() == 0
    assert result["ship_date"].isnull().sum() == 0


# -----------------------------
# 3. Transformation validation test
# -----------------------------
def test_profit_margin_calculation():
    df = pd.DataFrame({
        "Order.Date": ["2023-01-01"],
        "Ship.Date": ["2023-01-03"],
        "Sales": [100],
        "Profit": [20],
        "Discount": [0.1]
    })

    result = clean_and_transform(df)

    expected_margin = 20 / 100

    assert abs(result["profit_margin"].iloc[0] - expected_margin) < 0.0001