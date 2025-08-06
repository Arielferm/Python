
import pandas as pd
import yfinance as yf
import datetime
from datetime import date, timedelta
import plotly.graph_objects as go
import plotly.express as px
today = date.today()

d1 = today.strftime("%Y-%m-%d")
end_date = d1
d2 = date.today() - timedelta(days=365)
d2 = d2.strftime("%Y-%m-%d")
start_date = d2

# Collecting the stock price data of H&M using the yfinance API of Yahoo Finance.
data = yf.download('HM-B.ST', start=start_date,
                              end=end_date,
                              progress=False)

print(data.head())

# Flatten the MultiIndex columns
data.columns = ['_'.join(col).strip() for col in data.columns.values]
print(data.columns)

# "Date" is index in this dataset. Below is how to convert this index into column.
data["Date"] = data.index
data = data[["Date", "Open_HM-B.ST", "High_HM-B.ST", "Low_HM-B.ST", "Close_HM-B.ST", "Volume_HM-B.ST"]]
data.reset_index(drop=True, inplace=True)
print(data.head())

# Candlestick shart of H&M's stock prices
figure = go.Figure(data=[go.Candlestick(x=data["Date"], open=data["Open_HM-B.ST"], high=data["High_HM-B.ST"], low=data["Low_HM-B.ST"], close=data["Close_HM-B.ST"])])
figure.update_layout(title = "H&M Stock Price Analysis", xaxis_rangeslider_visible=False)
figure.show()

# Bar plot which shows the close prices of H&M's stock
figure = px.bar(data, x= "Date", y= "Close_HM-B.ST")
figure.show()

# Time period selectors are like buttons and show the graph of a specific time period
figure = px.line(data, x='Date', y='Close_HM-B.ST', title='Stock Market Analysis with Time Period Selectors')

figure.update_xaxes(
    rangeselector = dict(
        buttons = list([
            dict(count=1, label="1m", step="month", stepmode="backward"),
            dict(count=6, label="6m", step="month", stepmode="backward"),
            dict(count=3, label="3m", step="month", stepmode="backward"),
            dict(count=1, label="1y", step="year", stepmode="backward"),
            dict(step="all")
        ])
    )
)
figure.show()
