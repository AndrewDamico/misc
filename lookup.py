#!/usr/bin/env python
# coding: utf-8

# # V-Lookup for Python
# Andrew D'Amico
# 09/10/2021

# This workbook creates a Pandas dataframe (DF) containing two feature sets such that each of the items in column A are also in column B. The objective is to lookup the value of column A, find the same value in column B, and return the value in column A which is in the same row as the value in column B as Column C.
#
# It needs to be noted that this will only find the first matching value; subsequent matching values (e.g., multiple records which contain items in column B that match the search value in column A) are ignored.

# # Libraries

import pandas as pd


# # Create Sample Data
# Create a Pandas dataframe comprised of two columns: A and B. Each column containes the same values in different rows.

df = pd.DataFrame(data = {'A': ['Item 1','Item 2','Item 3'], 'B':['Item 3','Item 1','Item 2']})
df


# # Lambda Function
# We can use a lambda function to iterate through the rows, finding the location of the value x in columns B, and returning the subsequent value in column A.

df['C'] = df['A'].apply(lambda x: df['A'].loc[df['B'] == x].values[0])
df


# # Iterate through rows
# The following performs the same operations, but in a non-lambda format (i.e., a for loop). This will find the first location of the value in column A in column B, and will then return the value in column A corresponding to the row in column B


for index in df.iterrows():
    df.at[index[0],'C'] = df.loc[df['B'] == df.iloc[index[0]]['A'], 'A'].values[0]
df


# # An Easier Breakdown to see what is happening

for index in df.iterrows():
    value_looking_for = df.iloc[index[0]]['A']
    lookup_column = df['B']
    column_to_return = 'A'
    df.at[index[0],'C'] = df.loc[lookup_column == value_looking_for, column_to_return].values[0]

df

