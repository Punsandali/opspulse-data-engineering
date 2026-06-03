📊 OpsPulse – End-to-End Data Engineering ETL Pipeline
📌 Project Overview

OpsPulse is a beginner-to-intermediate Data Engineering project that simulates a real-world ETL (Extract, Transform, Load) pipeline using the Kaggle Global Superstore dataset.

The project demonstrates how raw data is transformed into analytics-ready data using Python and PostgreSQL.

🎯 Key Objectives
Build a modular ETL pipeline
Clean and transform raw retail data
Perform feature engineering for analytics
Load structured data into PostgreSQL
Run SQL-based analytics queries
Export query results using Python
Implement basic data validation tests using Pytest
📂 Dataset Used

Kaggle Global Superstore Dataset

It contains:

Sales and Profit
Customer and Order details
Product information
Shipping details
Region and Market data
⚙️ ETL Pipeline Workflow
1️⃣ Extract
Load raw CSV dataset using Pandas
2️⃣ Transform

Performed:

Removed duplicates
Handled missing values
Converted date columns (order_date, ship_date)
Feature engineering:
profit_margin
shipping_delay_days
discount_impact
sales_category
profit_category
is_high_value_order
3️⃣ Load
Cleaned dataset loaded into PostgreSQL
Using SQLAlchemy + psycopg2
Table: processed_superstore
🧠 SQL Analytics

Performed:

Aggregations (SUM, AVG, COUNT)
Filtering and grouping
Window functions (SUM OVER, RANK)
CTEs (Common Table Expressions)
Business KPIs:
Category-wise sales
Top customers
Profit segmentation
📊 Python + SQL Integration
SQL queries executed from Python
Query results exported as CSV
🧪 Testing

Run tests:

python -m pytest tests/

Includes:

Null checks
Column validation
Transformation checks

🚀 How to Run
Install dependencies
pip install pandas numpy sqlalchemy psycopg2-binary pytest
Run pipeline
python main.py

📁 Project Structure
OpsPulse/
│── data/
│   ├── raw/
│   ├── processed/
│
│── src/
│   ├── extract.py
│   ├── transform.py
│   ├── load.py
│
│── sql/
│   ├── analytics_queries.sql
│
│── tests/
│   ├── test_transform.py
│
│── main.py
│── README.md

🧠 Key Learnings
ETL pipeline design
Data cleaning & preprocessing
Feature engineering
SQL analytics (joins, window functions, CTEs)
PostgreSQL integration
Git & GitHub workflow

📌 Future Improvements
Apache Airflow orchestration
Docker containerization
Real-time streaming (Kafka)
BI dashboard (Power BI / Tableau)
Cloud deployment
👨‍💻 Author

OpsPulse – Data Engineering Learning Project
