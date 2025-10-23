# Project-3

## Introduction

The goal of this project is to apply the Stock-to-Flow (S2F) model to predict the price of Ethereum (ETH), the second-largest cryptocurrency by market capitalization. The Long Short-Term memory (LSTM) model, it takes the last 60 prices (as input) and learns a relationship between them to guess what the next price might be.T his makes LSTM great for financial predictions, where patterns often repeat.

## Long Short-Term Memory Model

An LSTM regression model (Long Short-Term Memory) is a type of neural network designed to learn patterns and relationships from time-dependent data, such as cryptocurrency prices. Unlike regular regression models that treat each data point independently, an LSTM can “remember” information from previous time steps, making it ideal for analyzing sequences. This memory feature helps the model understand how past values influence future ones. 

In the context of predicting Ethereum’s price, an LSTM regression model takes in a series of past prices and learns the underlying trends, fluctuations, and patterns in how the price moves over time. It then uses this knowledge to predict the next price or future values. Because Ethereum’s price is affected by market trends, trading activity, and historical patterns, an LSTM model is especially useful since it can capture the temporal dependencies and complex nonlinear relationships in the data, leading to more accurate and realistic price predictions than simpler models.

## Data Understanding

The Ethereum dataset obtained from Yahoo Finance contains daily market information with columns such as Open, High, Low, Close, Adj Close, and Volume, each representing different aspects of Ethereum’s trading activity in U.S. dollars. The Open, High, Low, and Close prices are usually highly correlated since they all describe Ethereum’s value within the same day, while Volume reflects the total amount of trading and can sometimes indicate strong buying or selling pressure before major price movements. By analyzing this data, we can identify important patterns such as overall upward or downward trends, short-term volatility spikes, and periods of increased trading activity.

<img src="./price-of-ethereum.png" alt="price of ethereum">

## Data Pre-Processing

Before running the Ethereum price data through an LSTM (Long Short-Term Memory) model, several data preprocessing steps are necessary to prepare the dataset for effective learning. First, missing or null values in the data (such as Open, Close, High, Low, or Volume) must be checked and handled—either by removing or imputing them. Next, the data should be sorted by date to maintain the correct time sequence since LSTMs depend on temporal order. Then, the feature scaling step is crucial—usually applying MinMaxScaler or StandardScaler to normalize numerical values between 0 and 1 so that the model can train efficiently without bias toward larger numbers. After scaling, the data is split into training and testing sets, often with 70–80% for training and the rest for testing. Finally, because LSTM expects sequential input, the data is reshaped into time windows.These steps ensure the model can capture temporal dependencies and patterns in Ethereum’s price movements effectively.

## Data Modeling

<img src="model-prediction.png" alt="picture of model prediction">

## Evaluation

The LSTM model’s predicted Ethereum prices differ from the actual prices by about $159.75. RMSE is a common metric for regression tasks that measures the square root of the average squared differences between predicted and true values, so it gives an overall sense of the model’s prediction error. A lower RMSE indicates that the predictions are closer to the real prices, while a higher RMSE means larger deviations. In practical terms, an RMSE of 159.75 USD means that, on average, the model’s daily price predictions are off by around $160.

## Impact

RMSE measures the average size of the errors in the model’s predictions, so it tells us how far off, on average, the predicted prices are from the actual prices. If Ethereum is trading at a high value, such as $10,000, an average error of $160 represents only about 1.6%, which may be acceptable given the inherent volatility of cryptocurrencies. However, if Ethereum is trading at a lower price, like $2,000, the same error would be around 8%, which could be significant and less useful for precise forecasting. Overall, the RMSE indicates the model’s performance quantitatively, and while some error is expected in volatile markets, lower RMSE values are always better because they mean the predictions are closer to the actual prices.

## Conclusion

I have learned a lot about linear regression and how it works and the math behind it. However, for this project I was predicting the closing value of the Ethereum crypto. This is not something a linear regression model can handle well due to the non-linear and volatile nature of cryptocurrency prices. So I went with an LSTM model, a deep learning model that is well-suited for time series data because it can analyze previous price trends to make predictions. I have observed that*preprocessing steps such as scaling the data and structuring it into sequences of past days were crucial for the model to learn effectively. Additionally, experimenting with feature selection, such as including only the closing price versus adding high, low, and volume data, showed that while additional features sometimes added more context, the model performed reasonably well even with just the closing price. I also learned that splitting data into training and testing sets and using metrics like RMSE helps evaluate how well the model generalizes to unseen data. Overall, this project taught me the importance of data preparation, sequence modeling, and carefully choosing evaluation metrics when working with volatile financial data.

## References

LSTM Model: https://www.geeksforgeeks.org/deep-learning/deep-learning-introduction-to-long-short-term-memory/

code: https://github.com/DarkerKin/project-3

data: Yahoo finance

coding help: chatgpt