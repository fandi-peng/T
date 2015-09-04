

from analyzer import Analyzer
from IPython.display import display, HTML
import datetime

def header(s, n):
    display(HTML(str('<h{}>' + s + '</h{}>').format(n,n)))

def get_report(symbols, start, end):
    header('Technical Report for Individual Stocks', 1)
    # initialize the analyzer
    # examine the performance since past one year from today
    analyzer = Analyzer(symbols, start, end)
    index = analyzer.index
    analyzer.plot_normalized()

    print 'The historical prices compared with HSI index. \n' \
          'All stock prices are normalized to 1 at the beginning of the time for easier comparison.\n'

    for symbol in symbols[1:]:
        header('{}'.format(symbol), 3)
        # 20-day moving average
        analyzer.show_bollinger(symbol, 20)
        print 'The Bollinger Bands for both stocks with 20-day moving average and 1 standard deviation.\n'

        analyzer.hist_daily_return(symbol)
        print 'Daily returns throughout the year plotted as histograms.\n'\
              'White dashed line denotes the mean and the red ones are standard deviations.\n'

        analyzer.hist_compare_return(index, symbol)
        print 'Daily returns of each stock against which of the HSI index.\n'

        analyzer.scatter_daily_return(symbol)
        print 'Beta, alpha and correlation of each stock.\n'
