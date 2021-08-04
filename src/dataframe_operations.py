import pandas as pd

def remove_col_from_dataframe(df, column):
    """
        removes column from input dataframe
    """

    df = df.drop(column, axis=1)
    return df


def standardize_timestamp_column(df, col, unit=None, format=None, utc=False):
    """
        Standardizes a datastamp column for a given dataframe
    """
    df['datastamp'] = pd.to_datetime(df[col], unit=unit, format=format, utc=utc)
    return df


def create_ohlcv_df(df_trades, freq='1Min'):
    """
        Creates an open, high, low, close, volume dataset based on trades dataset.
        open, high, low, close columns are given by resample() method from pandas
        volumn is the sum of amount of trades in period
        Inputs:
            df_trades: dataframe which contains all trades in period, with standardized datastam column
            freq: the frequency to resample and aggregated the rows
        Outputs:
            dataframe [datastamp, open, high, low, close, volume]
    """

    # first create ohlc columns from pandas resample() method
    df_ohlcv = df_trades.set_index('datastamp')['price'].resample(freq).ohlc()
    # then define volume as the sum of ocurrences on the interval
    df_ohlcv['volume'] = df_trades.set_index('datastamp')['amount'].resample(freq).sum()
    # reset index
    df_ohlcv.reset_index(inplace=True)

    return df_ohlcv

def asof_join(df_left, df_right, on='datastamp', direction='forward',allow_exact_matches=False):
    """
        Creates a table based on the merge_asof() method from pandas
    """
    merge_asof_df = pd.merge_asof(df_left, df_right, on=on,  direction=direction, allow_exact_matches=allow_exact_matches)
    return merge_asof_df



def create_moving_average_feature(df, moving_average_name_col, data_col, window_size):
    """
        Uses pandas rolling() method to perform a simple rolling average
    """
    df[moving_average_name_col] = df[data_col].rolling(window=window_size).mean()
    return df


def open_close_binary_classification(df, col_name):
    """
        
    """
    rows = df.shape[0]
    for i in range(rows):
        df.loc[i, col_name] = 1 if df['close'][i] >= df['open'][i] else 0

    return df
