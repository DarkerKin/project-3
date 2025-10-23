import yfinance as yf
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.preprocessing import MinMaxScaler
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import LSTM, Dense

# 1️⃣ Load Ethereum historical data
data = yf.download("ETH-USD", start="2020-01-01", end="2025-01-01")
prices = data[['Close']]

#This shows the price of ethereum overtime
plt.figure(figsize=(10,5))
plt.plot(data['Close'], label='Ethereum Closing Price')
plt.title("Ethereum Price Over Time")
plt.xlabel("Date")
plt.ylabel("Price (USD)")
plt.legend()
plt.savefig("price-of-ethereum.png")

# 2️⃣ Normalize the data
scaler = MinMaxScaler(feature_range=(0, 1))
scaled_data = scaler.fit_transform(prices)

# 3️⃣ Create training dataset
X_train, y_train = [], []
time_step = 60  # use past 60 days to predict next day
for i in range(time_step, len(scaled_data)):
    X_train.append(scaled_data[i-time_step:i, 0])
    y_train.append(scaled_data[i, 0])
X_train, y_train = np.array(X_train), np.array(y_train)
X_train = np.reshape(X_train, (X_train.shape[0], X_train.shape[1], 1))

# 4️⃣ Build LSTM model
model = Sequential([
    LSTM(50, return_sequences=True, input_shape=(X_train.shape[1], 1)),
    LSTM(50),
    Dense(1)
])
model.compile(optimizer='adam', loss='mean_squared_error')
model.fit(X_train, y_train, epochs=10, batch_size=32, verbose=1)

# 5️⃣ Make predictions
train_predict = model.predict(X_train)
train_predict = scaler.inverse_transform(train_predict.reshape(-1, 1))
actual_prices = scaler.inverse_transform(y_train.reshape(-1, 1))

# 6️⃣ Visualization
plt.figure(figsize=(10,6))
plt.plot(actual_prices, color='blue', label='Actual ETH Price')
plt.plot(train_predict, color='red', label='Predicted ETH Price')
plt.title("Ethereum Price Prediction (LSTM)")
plt.xlabel("Time")
plt.ylabel("Price (USD)")
plt.legend()
plt.savefig("model-prediction.png")
