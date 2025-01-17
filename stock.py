# Imports
import pandas as pd
import plotly_express as px
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn import metrics 
from sklearn.datasets import load_iris
from sklearn.metrics import accuracy_score
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

<<<<<<< HEAD
print(data.head(3))
# print("It worked")
=======

#stock_managed = pd.read_csv(f"{}")
#fig = px.line(
#    stock_managed,
#    x='Date',
#    y='Open'
#)
#fig2 = px.line(
#    stock_managing_data,
#    x='Date',
#    y='Close'
#)

# UI
print("\nStock Analysis")
print("--------------\n")

while True:
    user_input = input("Enter a NASDAQ Symbol (type \"exit\" to close): ").upper()
    if user_input.upper() == "EXIT":
        break
    if user_input in stock_managing_data["NASDAQ Symbol"].to_numpy():

        # Read Company Data
        company_info = []
        for c in stock_managing_data.to_numpy():
            if c[1] == user_input:
                company_info = c
                break
        folder = "etfs" if company_info[3] else "stocks"
        selected_stock = pd.read_csv(f"Dataset/{folder}/{user_input}.csv")

        # Display Company Data
        print(f"\n{company_info[0]} ({company_info[1]})\n")
        print("Stock History")
        print(selected_stock)

        # Display chart
        ## (code for displaying chart here)

    else:
        print(f"\"{user_input}\" - NASDAQ Symbol not found")
>>>>>>> 98185cce23eceb1166df728f759b9bd78cd16914
