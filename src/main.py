from src.extract import extract_csv_files
from src.transform import transform_data
from src.load import load_outputs

df = extract_csv_files()
df = transform_data(df)
load_outputs(df)
print("ETL process completed!")
