import pandas.io.data as web
import pandas as pd


def get_col(symbols, col, start, end, index):
    if index not in symbols:
        symbols.insert(0, index)
    dates = pd.date_range(start, end)
    df = pd.DataFrame(index=dates)
    for symbol in symbols:
        df_temp = web.DataReader(symbol,  'yahoo', start, end)[[col]]
        df_temp = df_temp.rename(columns={col: symbol})
        df = df.join(df_temp)
        # drop dates market did not trade
        if symbol == index:
            df = df.dropna(subset=[index])
    # fill missing data
    df.fillna(method='ffill',inplace='TRUE')
    df.fillna(method='bfill',inplace='TRUE')
    return df