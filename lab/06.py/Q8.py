import pandas as pd

products_df = pd.read_csv('products.csv')
orders_df = pd.read_csv('orders.csv')

print("First 5 rows of products data:")
print(products_df.head())

print("\nLast 10 rows of products data:")
print(products_df.tail(10))

print("\nFirst 5 rows of orders data:")
print(orders_df.head())

print("\nLast 10 rows of orders data:")
print(orders_df.tail(10))

merged_df = pd.merge(orders_df, products_df, on='ProductID')
merged_df['Revenue'] = merged_df['Quantity'] * merged_df['Price']
total_revenue = merged_df['Revenue'].sum()
print(f"\nTotal revenue generated from all orders: ${total_revenue:.2f}")

product_sales = merged_df.groupby('ProductName')['Quantity'].sum().sort_values(ascending=False)
print("\nTop 5 best-selling products:")
print(product_sales.head(5))

print("\nTop 5 low-selling products:")
print(product_sales.tail(5))

top_5_products = product_sales.head(5).index
top_5_categories = merged_df[merged_df['ProductName'].isin(top_5_products)]['Category'].value_counts()
print("\nMost common product category among the top 5 best-selling products:")
print(top_5_categories.idxmax())

average_price_per_category = products_df.groupby('Category')['Price'].mean()
print("\nAverage price of products in each category:")
print(average_price_per_category)

merged_df['Order Date'] = pd.to_datetime(merged_df['Order Date'])
merged_df['Day'] = merged_df['Order Date'].dt.day
merged_df['Month'] = merged_df['Order Date'].dt.month
merged_df['Year'] = merged_df['Order Date'].dt.year

day_revenue = merged_df.groupby('Day')['Revenue'].sum()
month_revenue = merged_df.groupby('Month')['Revenue'].sum()
year_revenue = merged_df.groupby('Year')['Revenue'].sum()
print("\nDay with the highest total revenue:", day_revenue.idxmax())
print("Month with the highest total revenue:", month_revenue.idxmax())
print("Year with the highest total revenue:", year_revenue.idxmax())

monthly_revenue_df = merged_df.groupby('Month')['Revenue'].sum().reset_index()
print("\nTotal revenue for each month:")
print(monthly_revenue_df)

print("\nChecking for null values in products data:")
print(products_df.isnull().sum())
print("\nChecking for null values in orders data:")
print(orders_df.isnull().sum())
