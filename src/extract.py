from pathlib import Path
import pandas as pd

RAW_DATA_PATH = Path("./data/raw")

def extract_csv_files():
    csv_files = list(RAW_DATA_PATH.glob("*.csv"))

    if not csv_files:
        raise FileNotFoundError("No CSV files found in data/raw")

    df_list = []
    for file in csv_files:
        df = pd.read_csv(file)
        df["source_file"] = file.name
        df_list.append(df)

    combined_df = pd.concat(df_list, ignore_index=True)
    return combined_df
