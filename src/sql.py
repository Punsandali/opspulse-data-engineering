from sqlalchemy import create_engine
import pandas as pd
from urllib.parse import quote_plus

password = quote_plus("Punsandali@123")

engine = create_engine(
        f"postgresql+psycopg2://postgres:{password}@localhost:5432/opspulse_db"
    )


query = """
SELECT
    category,
    sales,
    SUM(sales) OVER (PARTITION BY category) AS category_total_sales
FROM processed_superstore;
"""

df = pd.read_sql(query, engine)
df.to_csv("category_sales.csv", index=False)

print("Export done")