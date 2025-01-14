# Imports
import pandas as pd

from sklearn.linear_model import SGDRegressor # I chose this model as it allows for Incremental Learning which will be needed for the multiple files
from sklearn.model_selection import train_test_split

### MAIN GOAL: Get Model to make predictions
### FUTURE PLANS: Make a csv file that is structured for a linear regression model using the mean market trend of each day.


# Initializing the model 
model = SGDRegressor()

# Running tests to learn the model. Will explain when I actually understand. Working with rows are weird
test_data = pd.read_csv("Dataset/stocks/A.csv")
test_data = test_data.drop(columns=['Date'], axis=1)
# Not doing what I would like. With a closer look at the data its saying the next day, not past day.
test_data['Previous_Close'] = test_data['Close'].shift(1)

test_data = test_data.dropna()

last_day = test_data[['Previous_Close']]
target = test_data['Close']

print(test_data)

X_train, X_test, y_train, y_test = train_test_split(last_day, target, test_size=0.2, random_state=42)

model.fit(X_train,y_train)

last_close = test_data['Close'].iloc[-1]
tomorrow_prediction = model.predict([[last_close]])
print(f"Tomorrow's Predicted Closing Price: {tomorrow_prediction[0]}")