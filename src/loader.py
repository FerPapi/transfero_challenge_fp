import pandas as pd

def load_csv(filename):
    '''loads a csv file as dataframe'''

    df = pd.read_csv(filename)
    return df
