# Calculate the average daily usage duration (in hours)
def average_daily_usage(df):
    return round(df['avg_daily_use_hours'].mean(), 2)

# Find the most frequently used device type
def most_common_device(df):
    return df['device_type'].mode()[0]

# Find the most common country among users
def most_common_country(df):
    return df['country'].mode()[0]

# Calculate the standard deviation of sync errors per device type
def sync_error_variation_by_device(df):
    return df.groupby('device_type')['sync_errors_weekly'].std().sort_values(ascending=False).round(2)

# Calculate the interquartile range (IQR) for user age
def age_interquartile_range(df):
    q1 = df['user_age'].quantile(0.25)
    q3 = df['user_age'].quantile(0.75)
    return q3 - q1