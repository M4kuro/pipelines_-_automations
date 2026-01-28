from pathlib import Path
import pandas as pd

PROCESSED_PATH = Path("data/processed")
REPORTS_PATH = Path("reports")

def load_outputs(df: pd.DataFrame):
    PROCESSED_PATH.mkdir(parents=True, exist_ok=True)
    REPORTS_PATH.mkdir(parents=True, exist_ok=True)

    # Save cleaned data
    cleaned_file = PROCESSED_PATH / "cleaned_data.csv"
    df.to_csv(cleaned_file, index=False)

    # Simple summary report
    summary = df.describe(include="all")
    report_file = REPORTS_PATH / "summary_report.csv"
    summary.to_csv(report_file)
