import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler

# Load the data
source = 'D:/stuff/Stuff/Task 4/train.csv'
url="https://media.githubusercontent.com/media/Ibragim21/Stuff/refs/heads/main/Task%204/train.csv"
df = pd.read_csv(url)

# Clean missing values and standardize columns
df.dropna(inplace=True)
df.columns = df.columns.str.lower().str.replace(' ', '_')
numerical_cols = df.select_dtypes(include=[np.number]).columns


print(df.head())

# Calculate total sale for each product
total_sales_per_product = df.groupby('product_name')['sales'].sum().reset_index()
print(total_sales_per_product)

# Identify top-selling products and regions using groupby
top_selling_product = df.groupby('product_name')['sales'].sum().idxmax()
top_selling_product_sales = df.groupby('product_name')['sales'].sum().max()
print('Top selling product is', top_selling_product,' With total sale amount =' , top_selling_product_sales,'\n')

top_selling_region = df.groupby('region')['sales'].sum().idxmax()
top_selling_region_sales = df.groupby('region')['sales'].sum().max()
print('Top selling region is', top_selling_region, ' With total sale amount =', top_selling_region_sales)
