import pandas as pd
import matplotlib.pyplot as plt
from utils import get_col
import numpy as np

class Analyzer:
    def __init__(self, symbols, start, end, index='^HSI'):
        self.index = index
        self.symbols = symbols
        self.dates = pd.date_range(start, end)
        self.prices = get_col(symbols, 'Adj Close', start, end, index)

    # Compute Bollinger Bands
    def get_bollinger_bands(self, rm, rstd):
        """Return upper and lower Bollinger Bands."""
        upper_band = rm + rstd * 2
        lower_band = rm - rstd * 2
        return upper_band, lower_band

    # daily return analysis
    def compute_daily_returns(self):
        """Compute and return the daily return values."""
        # Note: Returned DataFrame must have the same number of rows
        daily_returns = (self.prices / self.prices.shift(1)) - 1
        daily_returns.ix[0, :] = 0
        return daily_returns

    # visualization
    def plot_normalized(self, title="Stock prices"):
        """Plot stock prices with a custom title and meaningful axis labels."""
        normalized = self.prices / self.prices.ix[0,:]
        ax = normalized.plot(title=title, fontsize=12)
        ax.set_xlabel("Date")
        ax.set_ylabel("Price")
        plt.show()

    def show_bollinger(self, symbol, window):
        price = self.prices.ix[:,symbol]#[[symbol]]
        # Compute rolling mean
        rm = pd.rolling_mean(price, window)
        # Compute rolling standard deviation
        rstd = pd.rolling_std(price, window)
        # Compute upper and lower bands
        upper_band, lower_band = self.get_bollinger_bands(rm, rstd)
        ax = price.plot(title="Bollinger Bands", label=symbol)
        rm.plot(label='Rolling mean', ax=ax)
        upper_band.plot(label='upper band', ax=ax)
        lower_band.plot(label='lower band', ax=ax)
        # Add axis labels and legend
        ax.set_xlabel("Date")
        ax.set_ylabel("Price")
        ax.legend(loc='upper left')
        plt.show()

    def hist_daily_return(self, symbol):
        # Compute daily returns
        daily_returns = self.compute_daily_returns().ix[:,symbol]
        # select first column to compute
        dr_mean = daily_returns.mean()
        dr_std = daily_returns.std()
        kurtosis = round(daily_returns.kurtosis(), 3)
        daily_returns.hist(bins=30)
        plt.axvline(dr_mean, color='w', linestyle='dashed',linewidth=2)
        plt.axvline(dr_std, color='r', linestyle='dashed',linewidth=2)
        plt.axvline(-dr_std, color='r', linestyle='dashed',linewidth=2)
        plt.title(symbol)
        plt.annotate('Kurtosis = {}'.format(kurtosis), (0.05,1), (0, 10),
                     xycoords='axes fraction', textcoords='offset points', va='top')
        plt.show()

    # compare two columns
    def hist_compare_return(self, symbol1, symbol2):
        daily_returns = self.compute_daily_returns()
        daily_returns.ix[:,symbol1].hist(bins=50, label=symbol1, alpha=0.4)
        daily_returns.ix[:,symbol2].hist(bins=50, label=symbol2, alpha=0.4)
        plt.legend(loc='upper right')
        plt.show()

    def scatter_daily_return(self, symbol):
        daily_returns = self.compute_daily_returns()
        daily_returns.plot(kind='scatter', x=self.index, y=symbol)
        beta, alpha = np.polyfit(daily_returns[self.index], daily_returns[symbol], 1)
        corr = daily_returns[[self.index, symbol]].corr(method='pearson')[symbol][0]
        round_beta, round_alpha, round_corr = round(beta, 3), round(alpha, 5), round(corr, 3)
        plt.annotate('beta = {}\nalpha = {}\ncorrelation = {}'.format(round_beta, round_alpha, round_corr),
                     (0.05,0.95), (0, 0), xycoords='axes fraction', textcoords='offset points', va='top')
        plt.plot(daily_returns[self.index], daily_returns[self.index] * beta + alpha, '-', color='r')
        plt.show()
