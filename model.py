import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import yfinance as yf
from sklearn.linear_model import LinearRegression

# 1. Get Ethereum price data
eth = yf.download("ETH-USD", start="2016-01-01", auto_adjust=False)

# Flatten multi-level columns if they exist
if isinstance(eth.columns, pd.MultiIndex):
    eth.columns = [col[0] for col in eth.columns]

eth['Date'] = eth.index
eth['Price'] = eth['Close']


# 2. Approximate stock (total supply) and flow (new issuance)
# For simplicity, use approximate data — you can later replace with actual on-chain data.
# Assume initial supply and inflation rate
initial_supply = 72000000
annual_issuance_rate = 0.04  # 4% new ETH per year

eth['Year'] = eth['Date'].dt.year
eth['Stock'] = initial_supply * (1 + annual_issuance_rate) ** (eth['Year'] - eth['Year'].min())
eth['Flow'] = eth['Stock'].diff(365).fillna(method='bfill')
eth['S2F'] = eth['Stock'] / eth['Flow']

# 3. Drop invalid and zero values before regression
eth = eth.replace([np.inf, -np.inf], np.nan)
eth = eth.dropna(subset=['S2F', 'Price'])
eth = eth[eth['S2F'] > 0]
eth = eth[eth['Price'] > 0]

# 4. Log-transform safely
X = np.log(eth['S2F']).values.reshape(-1, 1)
y = np.log(eth['Price']).values.reshape(-1, 1)

# 5. Train model
from sklearn.linear_model import LinearRegression
model = LinearRegression()
model.fit(X, y)

a, b = model.intercept_[0], model.coef_[0][0]
print(f"Model: log(Price) = {a:.3f} + {b:.3f} * log(S2F)")

# 6. Predict and visualize
eth['Predicted_Price'] = np.exp(model.predict(X))

import matplotlib.pyplot as plt
plt.figure(figsize=(10, 6))
plt.scatter(eth['S2F'], eth['Price'], alpha=0.5, label="Actual")
plt.plot(eth['S2F'], eth['Predicted_Price'], color='red', label="Predicted (S2F Model)")
plt.xscale('log')
plt.yscale('log')
plt.xlabel('Stock-to-Flow Ratio (log scale)')
plt.ylabel('Price (USD, log scale)')
plt.title('Ethereum Stock-to-Flow Model')
plt.legend()
plt.show()
