import os
import pandas as pd


def extract(csv_path):
    """
    Read data from CSV file.
    """

    print("=" * 50)
    print("STEP 1 : EXTRACT DATA")
    print("=" * 50)

    if not os.path.exists(csv_path):
        raise FileNotFoundError(
            f"CSV file not found: {csv_path}"
        )

    print("Reading CSV File...")

    df = pd.read_csv(csv_path)

    print(f"Rows Loaded : {len(df)}")
    print(f"Columns : {len(df.columns)}")

    print("\nFirst Five Records\n")

    print(df.head())

    return df