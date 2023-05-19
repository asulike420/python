#!/usr/bin/env python3

import pandas as pd

# Specify the path to your Excel file
excel_file_path = 'file.xlsx'

# Read the Excel file into a DataFrame
data_frame = pd.read_excel(excel_file_path)

# Now you can work with the data in the DataFrame
# For example, you can print the contents of the DataFrame
print(data_frame)



# Specify the path to your Excel file
excel_file_path = 'file2.xlsx'

# Read all sheets from the Excel file into a dictionary of DataFrames
data_frames_dict = pd.read_excel(excel_file_path, sheet_name=None)

# Iterate over each sheet in the dictionary
for sheet_name, data_frame in data_frames_dict.items():
    # Now you can work with each DataFrame individually
    # For example, you can print the contents of each DataFrame
    print(f"Sheet Name: {sheet_name}")
    print(data_frame)
    print()  # Print an empty line to separate the output of each sheet