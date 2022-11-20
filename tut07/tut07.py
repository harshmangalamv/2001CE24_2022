# Writer:
# Harsh Mangalam Verma (IIT Patna) 
# For tut07
import pandas as pd
import math
import os
from pathlib import Path
input_dir = "input"

from datetime import datetime
start_time = datetime.now()

#Help
def octant_identification(mod = 4000):
    for file in os.listdir(input_dir):
        f = os.path.join(input_dir, file)
        file_name = file[:-5]
        print(file_name)
#         continue
        df = pd.read_excel(f)
            # creating and populating colums that store Avg values
        df.at[0, "U Avg"] = df["U"].mean()
        df.at[0, "V Avg"] = df["V"].mean()
        df.at[0, "W Avg"] = df["W"].mean()
        sz = len(df["T"])


        # this function calculates the differences required
        def fun(a, b, c, sz):
            for i in range(sz):
                df.at[i, c] = df.at[i, a] - df.at[0, b]

        # function calls for creating new columns that store, while calculating as per requirements at the same time
        fun("U", "U Avg", "U'", sz)
        fun("V", "V Avg", "V'", sz)
        fun("W", "W Avg", "W'", sz)
    #     df = df.fillna('')
        # df

        df.at[0, "Octant"] = ''


#This shall be the last lines of the code.
end_time = datetime.now()
print('Duration of Program Execution: {}'.format(end_time - start_time))
