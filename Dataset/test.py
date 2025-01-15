import pandas as pd

# Example DataFrame
data1 = pd.DataFrame({
    'Date': ['1999-12-31', '2000-01-01', '2001-06-15'],
    'Open': [10, 20, 30],
    'High': [10, 20, 30],
    'Low': [10, 20, 30],
    'Close': [10, 20, 30],
    'Adj Close': [10, 20, 30],
    'Volume': [10, 20, 30]
})

# Ensure 'Date' column is in datetime format
data1['Date'] = pd.to_datetime(data1['Date'])

# Filter rows where the year is 2000 or later
data = data1[data1['Date'].dt.year >= 2000]

print(data)
