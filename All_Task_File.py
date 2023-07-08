import pandas as pd
import numpy as np

# Task 1: Data Preparation

# Read the dataset
df = pd.read_excel('retail_data_v1.xlsx')

# Drop rows with missing values
df.dropna(inplace=True)

# Sort the data based on customer ID and Date
df.sort_values(['CustomerID', 'Date'], inplace=True)

# Create a new column named TotalAmount
df['TotalAmount'] = df['Quantity'] * df['UnitPrice']


# Task 2: Customer Segmentation

# Calculate the total purchase amount for each customer
total_purchase = df.groupby('CustomerID')['TotalAmount'].sum()

# Calculate the percentiles
high_limit = np.percentile(total_purchase, 90)
low_limit = np.percentile(total_purchase, 50)

# Segment customers based on their total purchase amount
customer_segment = []
for amount in total_purchase:
    if amount > high_limit:
        customer_segment.append('High Spenders')
    elif amount > low_limit:
        customer_segment.append('Medium Spenders')
    else:
        customer_segment.append('Low Spenders')

# Create a new DataFrame for customer segmentation
segmentation_df = pd.DataFrame({'CustomerID': total_purchase.index, 'Segment': customer_segment})

# Task 3: Time Series Analysis

# Create a new column named 'Month' which contains the month of each purchase
df['Month'] = df['Date'].dt.to_period('M')

# Create a new DataFrame that contains the total purchase amount for each month
monthly_purchase = df.groupby('Month')['TotalAmount'].sum()

# Analyze the trend of total purchase amount over time
trend = pd.DataFrame(monthly_purchase)
trend.reset_index(inplace=True)
trend['GrowthRate'] = (trend['TotalAmount'] - trend['TotalAmount'].shift(1)) / trend['TotalAmount'].shift(1)

#Summary of the trend
summary_report = trend.describe()


# Output the results

# Save the prepared data to an Excel file
df.to_excel('Final_data.xlsx', index=False)


segmentation_df.to_excel('Customer_Segmentation.xlsx', index=False)

trend.to_excel('Trend.xlsx', index=False)

summary_report.to_excel('Summary_of_Trend.xlsx')


# Display the customer segmentation
print("Customer Segmentation:")
print(segmentation_df)

# Display the trend analysis
print("\nTrend Analysis:")
print(trend)

# Summary of the Trend
print("\nTrend Summary of Trends:")
print(summary_report)