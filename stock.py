# Imports
import pandas as pd

# Reading the Data
stock_managing_data = pd.read_csv("Dataset/symbols_valid_meta.csv")

# Removing columns for easier organization (I may change which columns later but this should work for now)
stock_managing_data = stock_managing_data.drop(columns=['Nasdaq Traded','Listing Exchange','Market Category','Round Lot Size','Test Issue','Financial Status','CQS Symbol','NASDAQ Symbol','NextShares'])

# Seperates the ETF column into 2 columns. ETF_N and ETF_Y 
stock_managing_data = pd.get_dummies(stock_managing_data, columns=["ETF"])

# The data looks like this: print(stock_managing_data.head(3))
#   Symbol                            Security Name  ETF_N  ETF_Y
# 0      A  Agilent Technologies, Inc. Common Stock   True  False
# 1     AA          Alcoa Corporation Common Stock    True  False
# 2   AAAU             Perth Mint Physical Gold ETF  False   True

# for symbol in stock_managing_data["Symbol"]:
#     if stock_managing_data
#     data = pd.read_csv(f"Dataset/stocks/{symbol}.csv")
#     print(data.head(1))