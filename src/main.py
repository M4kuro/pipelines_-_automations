from src.extract import extract_csv_files
# from transform_std import transform_data
from src.transform_vgsale import transform_sales_data
from src.load import load_outputs

df = extract_csv_files()
#df = transform_data(df)

df = transform_sales_data(df)
load_outputs(df)
print("ETL process completed!")
print(df.head())
print(df.dtypes)

