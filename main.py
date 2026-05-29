from src.extract import load_data
from src.transform import clean_and_transform
from src.load import save_data

raw_path = "data/raw/superstore.csv"
output_path = "data/processed/cleaned.csv"

df = load_data(raw_path)
print(df.columns.tolist())
df_clean = clean_and_transform(df)
save_data(df_clean, output_path)

print("OpsPulse pipeline completed!")