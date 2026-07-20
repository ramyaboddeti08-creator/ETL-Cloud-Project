import pandas as pd


def transform(df):
    """
    Clean and transform the extracted data.
    """

    print("=" * 50)
    print("STEP 2 : TRANSFORM DATA")
    print("=" * 50)

    # Convert column names to snake_case
    df.columns = (
        df.columns
        .str.strip()
        .str.lower()
        .str.replace(" ", "_")
    )

    print("Column names converted to snake_case.")

    # Remove duplicate rows
    duplicates = df.duplicated().sum()
    if duplicates > 0:
        print(f"Removing {duplicates} duplicate rows.")
        df = df.drop_duplicates()
    else:
        print("No duplicate rows found.")

    # Fill missing amount values with 0
    df["amount"] = df["amount"].fillna(0)

    # Convert amount to numeric
    df["amount"] = pd.to_numeric(df["amount"], errors="coerce")

    # Convert exchange_rate to numeric
    df["exchange_rate"] = pd.to_numeric(
        df["exchange_rate"],
        errors="coerce"
    )

    # Convert order_date to datetime
    df["order_date"] = pd.to_datetime(
        df["order_date"],
        errors="coerce"
    )

    # Create a new calculated column
    df["amount_usd"] = df["amount"] * df["exchange_rate"]

    print("\nTransformation Completed Successfully.")

    print("\nCleaned Data Preview:\n")
    print(df.head())

    return df