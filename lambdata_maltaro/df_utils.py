"""
utility functions for working with DataFrames
"""

import pandas
import numpy

TEST_DF = pandas.DataFrame([1, 2, 3])


def add_list_to_dataframe(mylist, df):
    """
    Adds a list to pandas dataframe as a new column. Then returns the extended
    dtaframe.

    """
    df["new_column"] = mylist
    return df


def count_zeros(df):
    """
    Transforms a dataframe to a np array, then counts how many 0s are in the
    array. The result will be printed out.
    """
    num_zeros = (df.values == 0).sum()
    print("Your Dataframe contains {} zeros".format(num_zeros))
