import pandas as pd

def load_and_clean_data(filepath):
    # Load the dataset from CSV
    df = pd.read_csv(filepath)

    # Remove rows that are completely empty
    df.dropna(how='all', inplace=True)

    # Remove duplicate entries
    df.drop_duplicates(inplace=True)

    # Drop rows missing critical columns needed for analysis
    df.dropna(subset=['user_age', 'device_type', 'avg_daily_use_hours', 'sync_errors_weekly', 'country'], inplace=True)

    # Convert relevant columns to numeric types (if not already)
    df['user_age'] = pd.to_numeric(df['user_age'], errors='coerce')
    df['avg_daily_use_hours'] = pd.to_numeric(df['avg_daily_use_hours'], errors='coerce')
    df['sync_errors_weekly'] = pd.to_numeric(df['sync_errors_weekly'], errors='coerce')

    # Drop rows with missing values after conversion
    df.dropna(subset=['user_age', 'avg_daily_use_hours', 'sync_errors_weekly'], inplace=True)

    # Return the cleaned DataFrame
    return df