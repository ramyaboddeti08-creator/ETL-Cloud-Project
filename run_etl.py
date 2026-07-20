import os
from dotenv import load_dotenv

from etl.extractor import extract
from etl.transformer import transform
from etl.loader import load
from etl.viz import create_report


def main():

    print("=" * 60)
    print(" ETL CLOUD PROJECT ")
    print("=" * 60)

    # Load environment variables
    load_dotenv(".env.example")

    csv_path = os.getenv("CSV_PATH")
    db_path = os.getenv("DB_PATH")

    # STEP 1 - Extract
    raw_df = extract(csv_path)

    # STEP 2 - Transform
    cleaned_df = transform(raw_df)

    # STEP 3 - Load
    load(
        cleaned_df,
        "sales_data",
        db_path
    )

    # STEP 4 - Generate Report
    report = create_report(
        cleaned_df,
        "reports"
    )

    print("\n")
    print("=" * 60)
    print("PROJECT COMPLETED SUCCESSFULLY")
    print("=" * 60)

    print(f"Report Location : {report}")
    print(f"Database Location : {db_path}")


if __name__ == "__main__":
    main()