# Importing all the necessay libraries
import pandas as pd
import numpy as np
from sklearn.preprocessing import scale

# Loading the dataset
df = pd.read_csv('household_power_consumption.txt', parse_dates={'DateTime' : ['Date', 'Time']}, infer_datetime_format=True, 
                 low_memory=False, na_values=['nan','?'], sep=';')
# Dropping the null values
df.dropna(inplace = True)
# Selecting all the columns except for datetime column
df1 = df.loc[:, 'Global_active_power':'Sub_metering_3']
# Scaling whole data and converting it into dataframe
X = scale(df1)
df1 = pd.DataFrame(X)
# Selecting all the columns except for Cluster column
final_df = df1.round(3)
# Saving the final data into text file
np.savetxt(r'dataset.txt', final_df, fmt = '%1.3f', delimiter = ', ')
