import pandas as pd
import os

DATA_FILE = 'data/styles.csv'

def main():
    if not os.path.exists(DATA_FILE):
        print(f"Error: {DATA_FILE} not found. Did you run download_data.sh?")
        return

    try:
        # OnError_bad_lines=skip is used because some CSVs have malformed rows
        df = pd.read_csv(DATA_FILE, on_bad_lines='skip')
        print("CSV Loaded Successfully!")
        print("-" * 30)
        print("Columns found:")
        print(df.columns.tolist())
        print("-" * 30)
        print("First 5 rows:")
        print(df.head())
        print("-" * 30)
        print("Unique values in 'gender':")
        print(df['gender'].unique())
        print("-" * 30)
        print("Unique values in 'masterCategory':")
        print(df['masterCategory'].unique())
    except Exception as e:
        print(f"Error reading CSV: {e}")

if __name__ == "__main__":
    main()
