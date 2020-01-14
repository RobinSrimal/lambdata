"""
utility functions for working with DataFrames
"""

import pandas
import numpy

TEST_DF = pandas.DataFrame([1,2,3])


def add_list_to_dataframe(mylist,df):
    df["new_column"] = mylist
    return df


def count_zeros(df):
    num_zeros = (df.values==0).sum()
    print("Your Dataframe contains this amount of zeros:", num_zeros)
    
