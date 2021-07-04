import pandas as pd
import os

# print configuration
pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)

# file_path = os.getcwd() + "\input_data\Master Report_1526790692.xlsx"
file_path = os.getcwd() + "\input_data\movies.xls"

# sheet_name = "CM REPORT"
sheet_name = "2010s"


# read excel file
dfs = pd.read_excel(file_path, sheet_name=sheet_name)

# print pandas dataframe
# with pd.option_context('display.max_rows', None, 'display.max_columns', None):  # more options can be specified also
# #     print(dfs)

# multiply aspect ration with budget
dfs['aspect_ration_budget_multiply'] = dfs['Aspect Ratio'] * dfs['Budget']

dfs['aspect_ration_budget_multiply'].fillna(1, inplace=True)
# print pandas dataframe
print(dfs.head(n=40))