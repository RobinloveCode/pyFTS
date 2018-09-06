"""
Bitcoin to USD quotations

Daily averaged index, by business day, from 2010 to 2018.

Source: https://finance.yahoo.com/quote/BTC-USD?p=BTC-USD
"""


from pyFTS.data import common
import pandas as pd
import numpy as np


def get_data():
    """
    Get the univariate time series data.

    :return: numpy array
    """
    dat = get_dataframe()
    return np.array(dat["Avg"])


def get_dataframe():
    """
    Get the complete multivariate time series data.

    :return: Pandas DataFrame
    """
    df = pd.read_csv('https://query.data.world/s/72gews5w3c7oaf7by5vp7evsasluia')

    return df

