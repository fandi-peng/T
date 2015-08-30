from analyzer import Analyzer
import datetime

def main():
    start = datetime.datetime(2014, 8, 29)
    end = datetime.datetime(2015, 8, 29)
    analyzer = Analyzer(['0400.HK', '1717.HK'], start, end)
    #analyzer.plot_data('0400.HK')
    #analyzer.show_bollinger('1717.HK')
    #analyzer.hist_daily_return('1717.HK')
    #analyzer.hist_compare_return('^HSI', '1717.HK')
    #analyzer.hist_compare_return('^HSI', '0400.HK')
    #analyzer.scatter_daily_return('0400.HK')
    #analyzer.scatter_daily_return('1717.HK')

main()