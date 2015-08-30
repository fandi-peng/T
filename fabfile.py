from fabric.api import local, warn_only


def download():
    for i in range(1, 10000):
        id = '0000'
        s = str(i)
        stock_id = id[:(len(id)-len(s))] + s
        # skip the stock ids that are not listed
        with warn_only():
            local('wget -O data/{}.csv "http://real-chart.finance.yahoo.com/table.csv?s={}.HK"'
                  .format(stock_id, stock_id) )
