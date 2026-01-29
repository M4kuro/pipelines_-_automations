import pandas as pd

def transform_sales_data(df: pd.DataFrame) -> pd.DataFrame:
    # Keep only required columns
    df = df[
        [
            "Year",
            "Genre",
            "NA_Sales",
            "EU_Sales",
            "JP_Sales",
            "Other_Sales",
        ]
    ]

    # Drop rows with missing year
    df = df.dropna(subset=["Year"]) # type: ignore

    # Fix data types
    df["Year"] = df["Year"].astype(int)

    # Rename columns
    df = df.rename(
        columns={
            "Year": "year",
            "Genre": "genre",
            "NA_Sales": "NA",
            "EU_Sales": "EU",
            "JP_Sales": "JP",
            "Other_Sales": "Other",
        }
    )

    # Convert wide → long format
    df_long = df.melt(  # type: ignore
        id_vars=["year", "genre"],
        var_name="region",
        value_name="sales",
    )

    # Aggregate
    df_long = (
        df_long  # type: ignore
        .groupby(["year", "genre", "region"], as_index=False)
        .agg({"sales": "sum"})
        .sort_values("year")
    )

    return df_long
