import pandas as pd


fact_internet_sales = pd.read_csv('Homework11/fact_internet_sales.csv')
dim_product = pd.read_csv('Homework11/dim_product.csv')
dim_date = pd.read_csv('Homework11/dim_date.csv')
dim_customer = pd.read_csv('Homework11/dim_customer.csv')
dim_currency = pd.read_csv('Homework11/dim_currency.csv')

sales_with_date = fact_internet_sales.merge(dim_date, left_on='OrderDateKey', right_on='DateKey', how='inner')
sales_with_product = sales_with_date.merge(dim_product, left_on='ProductKey', right_on='ProductKey', how='inner')
full_data = sales_with_product.merge(dim_customer, left_on='CustomerKey', right_on='CustomerKey', how='inner')

filtered_data = full_data[
    (full_data['EnglishDayNameOfWeek'] == 'Sunday') &  
    (full_data['Color'] == 'Silver') &  
    (full_data['Size'].notna()) &  
    (full_data['Weight'] > 10) &  
    (full_data['YearlyIncome'] > 100000.0) &  
    (full_data['TotalChildren'] > 1)  
]

aggregated_data = (
    filtered_data
    .groupby(['CustomerKey', 'FirstName'], as_index=False)
    .agg(
        Total_TaxAmt=('TaxAmt', 'sum'),
        Avg_SalesAmount=('SalesAmount', 'mean'),
        Avg_TotalProductCost=('TotalProductCost', 'mean')
    )
)

result = aggregated_data.sort_values(by='FirstName').drop(columns=['CustomerKey'])


print("Sunday Sales Analysis for Silver Products:")
print(result)
