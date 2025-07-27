import matplotlib.pyplot as plt 
import pandas as pd 

def plot_bollinger_bands(df_symbol, symbol, window=20):
    """Plot Bollinger Bands for volatility analysis"""

    rolling_mean = df_symbol['Close'].rolling(window).mean()
    rolling_std = df_symbol['Close'].rolling(window).std()
    upper_band = rolling_mean + (2 * rolling_std)
    lower_band = rolling_mean - (2 * rolling_std)

    # Create a Matplotlib figure
    fig, ax = plt.subplots(figsize=(12, 6))
    ax.plot(df_symbol['Close'], label='Close Price', color='blue')
    ax.plot(rolling_mean, label='Rolling Mean', color='black')
    ax.plot(upper_band, label='Upper Band', color='red', linestyle='--')
    ax.plot(lower_band, label='Lower Band', color='green', linestyle='--')
    ax.fill_between(df_symbol.index, upper_band, lower_band, color='grey', alpha=0.1)
    ax.set_title(f'{symbol} - Bollinger Bands (Window={window})')
    ax.set_xlabel('Date')
    ax.set_ylabel('Price')
    ax.legend()
    ax.grid(True)

    return fig  # ✅ Return figure to be used with st.pyplot



#