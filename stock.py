# Imports
import pandas as pd
import numpy as np
import tkinter as tk
from tkinter import messagebox
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
        symbol = "PRIN"

    if stock_managing_data["ETF_N"][row] == True:
        data = pd.read_csv(f"Dataset/stocks/{symbol}.csv")
    else:
        data = pd.read_csv(f"Dataset/etfs/{symbol}.csv")
    
# Function to check if the input is in the specified column of the CSV file
def check_value():
    user_input = entry.get()  # Get the input from the user
    column_name = 'Security Name'
    
    # Load the CSV file into a pandas DataFrame
    try:
        stock_managing_data = pd.read_csv('Dataset/symbols_valid_meta.csv')  # Replace with your actual CSV file path
    except FileNotFoundError:
        messagebox.showerror('Error', 'CSV file not found.')
        return
    
    # Check if the input is in the specified column
    if user_input in stock_managing_data[column_name].values:
        messagebox.showinfo('Result', f'{user_input} is found in the column!')
    else:
        messagebox.showinfo('Result', f'{user_input} is NOT found in the column.')

# Create the main window for the GUI
window = tk.Tk()
window.title('CSV Value Checker')

# Add a label and an entry box for the user input
label = tk.Label(window, text='Enter a value to check in the CSV:')
label.pack(pady=10)

entry = tk.Entry(window, width=30)
entry.pack(pady=10)

# Add a button to trigger the check_value function
button = tk.Button(window, text='Check', command=check_value)
button.pack(pady=10)

# Run the main loop to keep the window open
window.mainloop()