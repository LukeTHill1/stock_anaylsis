# Imports
import pandas as pd

# Reading the Data
stock_managing_data = pd.read_csv("Dataset/symbols_valid_meta.csv")

# Removing columns for easier organization
stock_managing_data = stock_managing_data.drop(columns=['Nasdaq Traded','Listing Exchange','Market Category','ETF','Round Lot Size','Test Issue','Financial Status','CQS Symbol','NASDAQ Symbol','NextShares'])
# print(stock_managing_data.head())