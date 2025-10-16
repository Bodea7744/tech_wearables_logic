# Import data cleaning function
from clean_wearable_data import load_and_clean_data

# Import analysis functions
from wearable_metrics import (
    average_daily_usage,
    most_common_device,
    most_common_country,
    sync_error_variation_by_device,
    age_interquartile_range
)

# Load and clean the dataset
df = load_and_clean_data("tech_wearables_data.csv")

# 1. Display average daily usage duration
print("\n1. Average daily usage duration:", average_daily_usage(df), "hours")

# 2. Display most frequently used device type
print("\n2. Most common device type:", most_common_device(df))

# 3. Display most common user country
print("\n3. Most common country:", most_common_country(df))

# 4. Display variation in sync errors by device type
print("\n4. Sync error variation by device type:")
for device, std in sync_error_variation_by_device(df).items():
    print(f"   - {device}: {std} errors/week")

# 5. Display interquartile range (IQR) for user age
print("\n5. Interquartile range (IQR) for user age:", age_interquartile_range(df))