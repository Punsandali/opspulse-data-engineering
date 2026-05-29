📊 OpsPulse - Data Engineering ETL Pipeline
📌 Project Overview

OpsPulse is a beginner-friendly Data Engineering project that simulates a real-world ETL (Extract, Transform, Load) pipeline using the Kaggle Global Superstore dataset.

The project focuses on:

Data ingestion from CSV
Data cleaning and transformation using Pandas
Feature engineering
Basic data validation using Pytest
Clean project structuring with Git version control
📂 Dataset Used

Kaggle Global Superstore Dataset

This dataset contains global retail transaction data including:

Sales and Profit
Customers and Orders
Product details
Shipping information
Regional and market data
⚙️ Project Workflow (ETL Pipeline)
1. Extract
Load raw CSV dataset using Pandas
2. Transform

Data cleaning and feature engineering:

Removed duplicate records
Handled missing values
Converted date columns (order_date, ship_date)
Created new features:
profit_margin
shipping_delay_days
discount_impact
sales_category
profit_category
is_high_value_order
3. Load
Saved cleaned dataset into data/processed/
🧠 Key Features Implemented
ETL pipeline structure (Extract → Transform → Load)
Data cleaning and preprocessing
Feature engineering for business insights
Data validation using Pytest
Modular Python project structure
🧪 Running Tests

Run all tests using:

python -m pytest tests/

Tests include:

Null value checks
Column existence validation
Transformation output verification
🚀 How to Run the Project
1. Install dependencies
pip install pandas numpy pytest
2. Run pipeline
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
│── tests/
│   ├── test_transform.py
│
│── main.py
│── README.md
🧠 What I Learned
Basics of Data Engineering pipelines
ETL vs ELT concepts
Data cleaning using Pandas
Feature engineering techniques
Writing basic unit tests with Pytest
Git and GitHub workflow for version control
📌 Future Improvements
Add SQL database integration (PostgreSQL/MySQL)
Build Airflow pipeline for orchestration
Deploy pipeline using Docker
Add real-time streaming version
👨‍💻 Author

Data Engineering Learning Project (OpsPulse)
