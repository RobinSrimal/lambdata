"""
utility functions for working with DataFrames
"""

import pandas
import numpy

test_df = pandas.DataFrame([1, 2, 3])


class UtilityFunctions:

    def __init__(self, coolness = 5, swagfactor = 999):
        """
        init functions that sets coolness = 5 and swagfactor= 999 as default
        """
        self.coolness = coolness
        self.swagfactor = swagfactor

    def add_list_to_dataframe(self,mylist, df):
        """
        Adds a list to pandas dataframe as a new column. Then returns the extended
        dataframe.

        """
        df["new_column"] = mylist
        return df


    def count_zeros(self,df):
        """
        Transforms a dataframe to a np array, then counts how many 0s are in the
        array. The result will be printed out.
        """
        num_zeros = (df.values == 0).sum()
        print("Your Dataframe contains {} zeros".format(num_zeros))

    def raise_power_coolness(self,exponent):
        """
        raises the coolness by the power of the exponent that is given
        """
        self.coolness = self.coolness**exponent
        return self.coolness


    def raise_power(self, base,exponent):
        """
        given the base and the exponent it returns base**exponent
        """
        return base**exponent
