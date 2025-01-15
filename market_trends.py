# Imports
import pandas as pd
# import datetime as dt

from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split

### MAIN GOAL: Get Model to make predictions
### FUTURE PLANS: Make a csv file that is structured for a linear regression model using the mean market trend of each day.

stock_managing_data = pd.read_csv("Dataset/symbols_valid_meta.csv")

# Removing columns for easier organization (I may change which columns later but this should work for now)
stock_managing_data = stock_managing_data.drop(columns=['Nasdaq Traded','Listing Exchange','Market Category','Round Lot Size','Test Issue','Financial Status','CQS Symbol','Symbol','NextShares'])

# Possibly make 2 market trends, one for etf and one for stocks
market_trend_dataset = pd.DataFrame(columns=['Date','Open','High','Low','Close','Adj Close','Volume'])

aggregated_data = {}

for row in range(len(stock_managing_data)):
    symbol = stock_managing_data["NASDAQ Symbol"][row]

    # PRN.csv is not a valid name. We will need a better work around later. I renamed the file to include a 1. Its hardcoded...
    if symbol == "PRN":
        symbol = "PRN1"

    if stock_managing_data["ETF"][row] == 'N':
        data = pd.read_csv(f"Dataset/stocks/{symbol}.csv")
        data = data[data['Date'].dt.year >= 2000]

        for row_index in range(len(data)):
            date = data.at[row_index,'Date']
            if date in aggregated_data:
                aggregated_data[date]['Open'] += data.at[row_index,'Open'],
                aggregated_data[date]['High'] += data.at[row_index,'High'],
                aggregated_data[date]['Low'] += data.at[row_index,'Low'],
                aggregated_data[date]['Close'] += data.at[row_index,'Close'],
                aggregated_data[date]['Adj Close'] += data.at[row_index,'Adj Close'],
                aggregated_data[date]['Volume'] += data.at[row_index,'Volume'],
                aggregated_data[date]['Count'] += 1

            else:
                aggregated_data[date] = {
                    'Open' : data.at[row_index,'Open'],
                    'High' : data.at[row_index,'High'],
                    'Low' : data.at[row_index,'Low'],
                    'Close' : data.at[row_index,'Close'],
                    'Adj Close' : data.at[row_index,'Adj Close'],
                    'Volume' : data.at[row_index,'Volume'],
                    'Count' : 1
                }
    else:
        data = pd.read_csv(f"Dataset/etfs/{symbol}.csv")
        data = data[data['Date'].dt.year >= 2000]

        for row_index in range(len(data)):
            date = data.at[row_index,'Date']
            if date in aggregated_data:
                aggregated_data[date]['Open'] += data.at[row_index,'Open'],
                aggregated_data[date]['High'] += data.at[row_index,'High'],
                aggregated_data[date]['Low'] += data.at[row_index,'Low'],
                aggregated_data[date]['Close'] += data.at[row_index,'Close'],
                aggregated_data[date]['Adj Close'] += data.at[row_index,'Adj Close'],
                aggregated_data[date]['Volume'] += data.at[row_index,'Volume'],
                aggregated_data[date]['Count'] += 1

            else:
                aggregated_data[date] = {
                    'Open' : data.at[row_index,'Open'],
                    'High' : data.at[row_index,'High'],
                    'Low' : data.at[row_index,'Low'],
                    'Close' : data.at[row_index,'Close'],
                    'Adj Close' : data.at[row_index,'Adj Close'],
                    'Volume' : data.at[row_index,'Volume'],
                    'Count' : 1
                }

for date, values in aggregated_data.items():
    market_trend_dataset = pd.concat([market_trend_dataset,])

print(market_trend_dataset.head(3))


# market_trend_dataset.to_csv('market_trend_dataset.csv', index=False, header=True)

print("It is Finished")
# # Initializing the model 
# model = LinearRegression()

# # Running tests to learn the model. Will explain when I actually understand. Working with rows are weird
# test_data = pd.read_csv("Dataset/stocks/A.csv")
# test_data = test_data.drop(columns=['Date'], axis=1)
# # Not doing what I would like. With a closer look at the data its saying the next day, not past day.
# test_data['Previous_Close'] = test_data['Close'].shift(1)

# test_data = test_data.dropna()

# last_day = test_data[['Previous_Close']]
# target = test_data['Close']

# print(test_data)

# X_train, X_test, y_train, y_test = train_test_split(last_day, target, test_size=0.2, random_state=42)

# model.fit(X_train,y_train)

# last_close = test_data['Close'].iloc[-1]
# tomorrow_prediction = model.predict([[last_close]])
# print(f"Tomorrow's Predicted Closing Price: {tomorrow_prediction[0]}")