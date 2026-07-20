import sqlite3
import os


def load(df, table_name, db_path):
    """
    Load cleaned data into SQLite database.
    """

    print("=" * 50)
    print("STEP 3 : LOAD DATA")
    print("=" * 50)

    # Create database folder if it doesn't exist
    os.makedirs(os.path.dirname(db_path), exist_ok=True)

    # Connect to SQLite database
    connection = sqlite3.connect(db_path)

    print("Connected to SQLite Database.")

    # Save DataFrame into SQLite table
    df.to_sql(
        table_name,
        connection,
        if_exists="replace",
        index=False
    )

    print(f"Data loaded successfully into table '{table_name}'.")

    # Verify data
    cursor = connection.cursor()

    cursor.execute(f"SELECT COUNT(*) FROM {table_name}")

    total_rows = cursor.fetchone()[0]

    print(f"Total Rows Stored : {total_rows}")

    connection.close()

    print("Database Connection Closed.")