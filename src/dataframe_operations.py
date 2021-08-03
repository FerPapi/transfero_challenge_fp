import pandas as pd

def remove_col_from_dataframe(df, column):
    '''removes column from input dataframe'''

    df = df.drop(column, axis=1)
    return df
