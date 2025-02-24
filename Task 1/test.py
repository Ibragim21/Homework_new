import pandas as pd
import numpy as np

# Load the dataset
df = pd.read_csv("yellow_tripdata_2024-01.csv")

# Split datetime columns
df_split=df['tpep_pickup_datetime'].str.split(' ',expand=True)
df['pickup_Weekday']=df_split[0]
df['pickup_day']=df_split[2]
df['pickup_month']=df_split[1]
df['pickup_hour']=df_split[3]
df['pickup_UTC']=df_split[4]
df['pickup_time']=df['pickup_hour']+' '+df['pickup_UTC']
df['pickup_year']=df_split[5]

df_split=df['tpep_dropoff_datetime'].str.split(' ',expand=True)
df['dropoff_Weekday']=df_split[0]
df['dropoff_day']=df_split[2]
df['dropoff_month']=df_split[1]
df['dropoff_hour']=df_split[3]
df['dropoff_UTC']=df_split[4]
df['dropoff_time']=df['dropoff_hour']+' '+df['dropoff_UTC']
df['dropoff_year']=df_split[5]

# Descriptive Statistics
numerical_columns = ['trip_distance', 'fare_amount', 'tip_amount', 'total_amount']
numeric_summary = df[numerical_columns].describe()
print("Summary Statistics for Numerical Columns:")
print(numeric_summary, "\n")

# Determine the distribution of trips by VendorID and Payment_type
vendor_distribution = df['VendorID'].value_counts().reset_index()
vendor_distribution.columns = ['VendorID', 'Count']
payment_distribution = df['payment_type'].value_counts().reset_index()
payment_distribution.columns = ['Payment Type', 'Count']

print("Distribution of Trips by VendorID:")
print(vendor_distribution, "\n")
print("Distribution of Trips by Payment Type:")
print(payment_distribution, "\n")

# Trip Analysis
average_trip_distance = df['trip_distance'].mean()
df['pickup_datetime'] = pd.to_datetime(df['pickup_year'] + '-' + df['pickup_month'] + '-' + df['pickup_day'] + ' ' + df['pickup_hour'])
df['dropoff_datetime'] = pd.to_datetime(df['dropoff_year'] + '-' + df['dropoff_month'] + '-' + df['dropoff_day'] + ' ' + df['dropoff_hour'])
df['trip_duration'] = (df['dropoff_datetime'] - df['pickup_datetime']).dt.total_seconds() / 60
average_trip_duration = df['trip_duration'].mean()

print("Average Trip Distance:", average_trip_distance)
print("Average Trip Duration (minutes):", average_trip_duration, "\n")

# Identify the busiest pickup and dropoff locations
busiest_pickup = df['PULocationID'].value_counts().reset_index()
busiest_pickup.columns = ['PULocationID', 'Count']
busiest_dropoff = df['DOLocationID'].value_counts().reset_index()
busiest_dropoff.columns = ['DOLocationID', 'Count']

print("Busiest Pickup Locations:")
print(busiest_pickup.head(), "\n")
print("Busiest Dropoff Locations:")
print(busiest_dropoff.head(), "\n")

# Analyze the distribution of trips by RateCodeID
ratecode_distribution = df['RatecodeID'].value_counts().reset_index()
ratecode_distribution.columns = ['RateCodeID', 'Count']
print("Distribution of Trips by RateCodeID:")
print(ratecode_distribution, "\n")

# Financial Analysis
total_revenue = df['total_amount'].sum()
average_fare_payment = df.groupby('payment_type')[['fare_amount', 'total_amount']].mean().reset_index()

# Check if congestion_surcharge and Airport_fee exist before grouping
if 'congestion_surcharge' in df.columns and 'Airport_fee' in df.columns:
    impact_surcharge_airport = df.groupby(['congestion_surcharge', 'Airport_fee'])['total_amount'].mean().reset_index()
    print("Impact of Congestion Surcharge and Airport Fee on Total Fare:")
    print(impact_surcharge_airport, "\n")
else:
    print("Columns 'congestion_surcharge' and 'Airport_fee' not found in dataset.\n")

print("Total Revenue Generated:", total_revenue, "\n")
print("Average Fare and Total Amount by Payment Type:")
print(average_fare_payment, "\n")

# Time-Based Analysis
trip_counts_by_hour = df['pickup_hour'].value_counts().sort_index()
trip_counts_by_day = df['pickup_Weekday'].value_counts().sort_index()

print("Trips by Hour of Day:")
print(trip_counts_by_hour, "\n")
print("Trips by Day of the Week:")
print(trip_counts_by_day, "\n")

# Peak hours (hours with highest trip counts)
peak_hours = trip_counts_by_hour.idxmax()
print(f"Peak Hour for Taxi Trips: {peak_hours}:00")

# Advanced Analysis
# 1. Percentage of Trips with Tips
df['tipped'] = df['tip_amount'] > 0
tip_percentage = df['tipped'].mean() * 100
print(f"Percentage of Trips with Tips: {tip_percentage:.2f}%")

# 2. Correlation Between Trip Distance and Fare Amount
correlation = df[['trip_distance', 'fare_amount']].corr()
print("Correlation Between Trip Distance and Fare Amount:")
print(correlation, "\n")

# 3. Store_and_fwd_flag Analysis
store_flag_distribution = df['store_and_fwd_flag'].value_counts()
print("Distribution of Store_and_fwd_flag:")
print(store_flag_distribution, "\n")

# Drop unnecessary columns
df.drop(columns=['pickup_UTC', 'pickup_hour', 'tpep_pickup_datetime', 'dropoff_UTC', 'dropoff_hour', 'tpep_dropoff_datetime'], inplace=True)

print('------------------------------------------------------------------------------------------------------------\n')
print(df.head())
