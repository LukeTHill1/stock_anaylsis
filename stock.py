# Imports
import pandas as pd
import plotly_express as px
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn import metrics 
from sklearn.datasets import load_iris
# Reading the Data
stock_managing_data = pd.read_csv("Dataset/symbols_valid_meta.csv")

# Removing columns for easier organization (I may change which columns later but this should work for now)
stock_managing_data = stock_managing_data.drop(columns=['Nasdaq Traded','Listing Exchange','Market Category','Round Lot Size','Test Issue','Financial Status','CQS Symbol','Symbol','NextShares'])

# Seperates the ETF column into 2 columns. ETF_N and ETF_Y 
stock_managing_data = pd.get_dummies(stock_managing_data, columns=["ETF"])

# The data looks like this: print(stock_managing_data.head(3))
#                              Security Name NASDAQ Symbol  ETF_N  ETF_Y
# 0  Agilent Technologies, Inc. Common Stock             A   True  False
# 1          Alcoa Corporation Common Stock             AA   True  False
# 2             Perth Mint Physical Gold ETF          AAAU  False   True

# Using the list of names it reads the data on each csv file using the symbol 
for row in range(len(stock_managing_data)):
    symbol = stock_managing_data["NASDAQ Symbol"][row]

    # PRN.csv is not a valid name. We will need a better work around later. I renamed the file to include a 1. Its hardcoded...
    if symbol == "PRN":
        symbol = "PRN1"

    if stock_managing_data["ETF_N"][row] == True:
        data = pd.read_csv(f"Dataset/stocks/{symbol}.csv")
    else:
        data = pd.read_csv(f"Dataset/etfs/{symbol}.csv")
    
# The data looks like this: print(data.head(3))
#          Date       Open       High        Low      Close  Adj Close    Volume
# 0  1999-11-18  32.546494  35.765381  28.612303  31.473534  27.068665  62546300
# 1  1999-11-19  30.713520  30.758226  28.478184  28.880543  24.838577  15234100
# 2  1999-11-22  29.551144  31.473534  28.657009  31.473534  27.068665   6577800

