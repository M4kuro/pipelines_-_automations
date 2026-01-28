from pathlib import Path
import pandas as pd
import shutil # for file operations; Useful for copying/moving files sending to archive

RAW_DATA_PATH = Path("./data/raw")
ARCHIVE_PATH = Path("./data/archive")

def extract_csv_files():
    csv_files = list(RAW_DATA_PATH.glob("*.csv"))

    if not csv_files:
        raise FileNotFoundError("No CSV files found in data/raw")

    df_list = []
    
    for file in csv_files:
        df = pd.read_csv(file) # type: ignore
        df["source_file"] = file.name
        df_list.append(df) # type: ignore

        # Move processed file to archive
        ARCHIVE_PATH.mkdir(parents=True, exist_ok=True)
        shutil.move(str(file), ARCHIVE_PATH / file.name)
        
    combined_df = pd.concat(df_list, ignore_index=True) # type: ignore
    return combined_df
