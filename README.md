# Purchase_Analysis

This repository contains a Python script for analyzing customer purchase history from an online retail store. The script performs data preparation, customer segmentation, and time series analysis to provide valuable insights into customer behavior and trends.

## Table of Contents

- [Introduction](#introduction)
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Customer Segmentation](#customer-segmentation)
- [Time Series Analysis](#time-series-analysis)
- [Contributing](#contributing)
- [License](#license)

## Introduction

The Online Retail Store Analysis script allows you to gain meaningful insights into customer purchase behavior and trends. By analyzing the customer purchase history, the script provides valuable information on customer segmentation and the trend of total purchase amount over time. With these insights, you can make informed decisions to optimize marketing strategies, customer targeting, and overall business performance.

## Features

- Data preparation by handling missing values, sorting the data, and calculating the total purchase amount.
- Customer segmentation based on total purchase amount to identify high, medium, and low spenders.
- Time series analysis to understand the trend of total purchase amount over different time periods.
- Exporting the prepared data, customer segmentation, and trend analysis to separate Excel files for further analysis.
- Summary report generation to provide a quick overview of the trend analysis.

## Installation

1. Clone the repository to your local machine using `git clone https://github.com/your-username/online-retail-analysis.git`.
2. Navigate to the project directory with `cd online-retail-analysis`.
3. Install the required dependencies by running `pip install -r requirements.txt`.

## Usage

1. Prepare your dataset by placing it in the project directory and updating the file path in the code (`df = pd.read_excel('retail_data_v1.xlsx')`).
2. Run the script using `python analysis_script.py`.
3. The script will perform data preparation, customer segmentation, time series analysis, and generate Excel files with the results.
4. The prepared data, customer segmentation, and trend analysis files will be saved as `Final_data.xlsx`, `Customer_Segmentation.xlsx`, and `Trend.xlsx`, respectively.
5. The summary report of the trend analysis will be saved as `Summary_of_Trend.xlsx`.
6. The customer segmentation, trend analysis, and summary report will be displayed in the console.

## Customer Segmentation

The script segments customers based on their total purchase amount into three categories: high spenders, medium spenders, and low spenders. This segmentation provides insights into different customer segments and their contribution to the total purchase amount. Understanding the spending patterns of different customer segments can help tailor marketing campaigns, loyalty programs, and personalized offers to maximize customer satisfaction and drive revenue growth.

## Time Series Analysis

The time series analysis focuses on understanding the trend of the total purchase amount over time. By examining the total purchase amount on a monthly basis, the script identifies patterns, seasonal trends, and any changes in customer spending behavior. This analysis provides valuable insights into the overall business performance, helps identify potential growth opportunities, and assists in making data-driven decisions for future strategies.

## Contributing

Contributions to this project are welcome. If you find any issues or have suggestions for improvements, please open an issue or submit a pull request. Feel free to contribute new features, enhance existing functionality, or provide bug fixes. Together, we can improve the analysis script and make it more powerful and versatile for the online retail community.

## License

This project is licensed under the [MIT License](LICENSE).

