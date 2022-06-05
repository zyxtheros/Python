import matplotlib.pyplot as plt
import numpy
import pandas as pd


# # ↓↓ DEPRECATED ↓↓ # #
# def readfile(source):
# 	data = open(source, "r")  # Open the file in read mode
# 	if data.mode == "r":  # We use the mode function in the code to check that the file is in open mode. If yes, we proceed ahead
# 		return data.read()  # Use f.read to read file data and store it in variable content
#
#
# cast_iron = readfile("Cast Iron.csv")
# def header(msg):
# 	print("-" * 50)
# 	print("[" + msg + " ]")
#
#
# filename = "Cast Iron.csv"
# dataframe = pd.read_csv(filename, index_col='Time (sec)')
# dataframe.drop([0, 1, 2], axis=0)
# print(dataframe)
# print(dataframe.dtypes)

# dataframe.plot(x="Extension (in)", y="Load (lbf)")
# plt.show()
# # ↑↑ DEPRECATED ↑↑ # #


file1 = 'Excel Files/309-902 Cast Iron.xlsx'
iron_df = pd.read_excel(file1, skiprows=[0, 1, 2, 3, 5], index_col='Time (sec)') # Use skiprows to ignore metadata
# # ↓↓ DEPRECATED ↓↓ # #
# new_header = iron_df.iloc[0] # Set the header as the new top row
# iron_df = iron_df[1:] # Make the dataframe the same as the dataframe w/o the header row
# iron_df.columns = new_header # set the header again
# iron_df_adj = iron_df.drop(iron_df.index[[0, 2]]) # how to drop rows from your dataframe
# print(iron_df_adj)
# print(iron_df_adj.dtypes)
# # ↑↑ DEPRECATED ↑↑ # #

print(iron_df)
# print(iron_df.dtypes)
iron_df.plot(x="Extension (in)", y="Load (lbf)")
# plt.show()
print("-" * 53)

iron_df_meta = pd.read_excel(file1, nrows=2)


def null_header(frame): # Sets all the headers to an empty string
	frame_dict = dict.fromkeys(frame.columns, '')
	frame.rename(columns=frame_dict)


# null_header(iron_df_meta) # get rid of the header

iron_df_meta.insert(0, '', "|", allow_duplicates=True)
pd.set_option("display.max_columns", None, 'display.max_rows', None)
print(iron_df_meta)
# null_header(iron_df_meta)
