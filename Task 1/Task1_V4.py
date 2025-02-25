import pandas as pd
import numpy as np


df = pd.read_csv("D:/stuff/Stuff/Task 1/yellow_tripdata_2024-01.csv")
# 1
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

# 2
numerical_columns = ['trip_distance', 'fare_amount', 'tip_amount', 'total_amount']
numeric_summary = df[numerical_columns].describe()
print("Summary Statistics for Numerical Columns:")
print(numeric_summary, "\n")


vendor_distribution = df['VendorID'].value_counts().reset_index()
vendor_distribution.columns = ['VendorID', 'Count']
payment_distribution = df['payment_type'].value_counts().reset_index()
payment_distribution.columns = ['Payment Type', 'Count']

print("Distribution of Trips by VendorID:")
print(vendor_distribution, "\n")
print("Distribution of Trips by Payment Type:")
print(payment_distribution, "\n")

# 3
average_trip_distance = df['trip_distance'].mean()
df['pickup_datetime'] = pd.to_datetime(df['pickup_year'] + '-' + df['pickup_month'] + '-' + df['pickup_day'] + ' ' + df['pickup_hour'])
df['dropoff_datetime'] = pd.to_datetime(df['dropoff_year'] + '-' + df['dropoff_month'] + '-' + df['dropoff_day'] + ' ' + df['dropoff_hour'])
df['trip_duration'] = (df['dropoff_datetime'] - df['pickup_datetime']).dt.total_seconds() / 60
average_trip_duration = df['trip_duration'].mean()

print("Average Trip Distance:", average_trip_distance)
print("Average Trip Duration (minutes):", average_trip_duration, "\n")


busiest_pickup = df['PULocationID'].value_counts().reset_index()
busiest_pickup.columns = ['PULocationID', 'Count']
busiest_dropoff = df['DOLocationID'].value_counts().reset_index()
busiest_dropoff.columns = ['DOLocationID', 'Count']

print("Busiest Pickup Locations:")
print(busiest_pickup.head(), "\n")
print("Busiest Dropoff Locations:")
print(busiest_dropoff.head(), "\n")


ratecode_distribution = df['RatecodeID'].value_counts().reset_index()
ratecode_distribution.columns = ['RateCodeID', 'Count']
print("Distribution of Trips by RateCodeID:")
print(ratecode_distribution, "\n")

# 4
total_revenue = df['total_amount'].sum()
average_fare_payment = df.groupby('payment_type')[['fare_amount', 'total_amount']].mean().reset_index()


if 'congestion_surcharge' in df.columns and 'Airport_fee' in df.columns:
    impact_surcharge_airport = df.groupby(['congestion_surcharge', 'Airport_fee'])['total_amount'].mean().reset_index()
    print("Impact of Congestion Surcharge and Airport Fee on Total Fare:")
    print(impact_surcharge_airport, "\n")
else:
    print("Columns 'congestion_surcharge' and 'Airport_fee' not found in dataset.\n")

print("Total Revenue Generated:", total_revenue, "\n")
print("Average Fare and Total Amount by Payment Type:")
print(average_fare_payment, "\n")

# 5
df['pickup_hour'] = pd.to_datetime(df['pickup_datetime']).dt.hour
df['pickup_Weekday'] = pd.to_datetime(df['pickup_datetime']).dt.day_name()
trip_counts_by_hour = df['pickup_hour'].value_counts().sort_index()
trip_counts_by_day = df['pickup_Weekday'].value_counts().sort_index()

print("Trips by Hour of Day:")
print(trip_counts_by_hour.to_string(), "\n")
print("Trips by Day of the Week:")
print(trip_counts_by_day.to_string(), "\n")


peak_hours = trip_counts_by_hour.idxmax()
print(f"Peak Hour for Taxi Trips: {peak_hours}:00")

# 6
df['tipped'] = df['tip_amount'] > 0
tip_percentage = df['tipped'].mean() * 100
print(f"Percentage of Trips with Tips: {tip_percentage:.2f}%")


correlation = df[['trip_distance', 'fare_amount']].corr()
print("Correlation Between Trip Distance and Fare Amount:")
print(correlation, "\n")


store_flag_distribution = df['store_and_fwd_flag'].value_counts()
print("Distribution of Store_and_fwd_flag:")
print(store_flag_distribution, "\n")

# unnecessary columns
df.drop(columns=['pickup_UTC', 'pickup_hour', 'tpep_pickup_datetime', 'dropoff_UTC', 'dropoff_hour', 'tpep_dropoff_datetime'], inplace=True)

print('------------------------------------------------------------------------------------------------------------\n')
print(df.head())