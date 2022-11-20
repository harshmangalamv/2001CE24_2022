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

        # Populating the Octant column, that is created in first call itself, with corresponding row values of U' V' W'
        for i in range(sz):
            if(df.at[i, "U'"] >= 0 and df.at[i, "V'"] >= 0 and df.at[i, "W'"] >= 0):
                df.at[i, "Octant"] = 1
            if(df.at[i, "U'"] >= 0 and df.at[i, "V'"] >= 0 and df.at[i, "W'"] < 0):
                df.at[i, "Octant"] = -1
            if(df.at[i, "U'"] < 0 and df.at[i, "V'"] >= 0 and df.at[i, "W'"] >= 0):
                df.at[i, "Octant"] = 2
            if(df.at[i, "U'"] < 0 and df.at[i, "V'"] >= 0 and df.at[i, "W'"] < 0):
                df.at[i, "Octant"] = -2
            if(df.at[i, "U'"] < 0 and df.at[i, "V'"] < 0 and df.at[i, "W'"] >= 0):
                df.at[i, "Octant"] = 3
            if(df.at[i, "U'"] < 0 and df.at[i, "V'"] < 0 and df.at[i, "W'"] < 0):
                df.at[i, "Octant"] = -3
            if(df.at[i, "U'"] >= 0 and df.at[i, "V'"] < 0 and df.at[i, "W'"] >= 0):
                df.at[i, "Octant"] = 4
            if(df.at[i, "U'"] >= 0 and df.at[i, "V'"] < 0 and df.at[i, "W'"] < 0):
                df.at[i, "Octant"] = -4


        # df
        # Creating a column named "User Activity" then placing "User Input" at its place 
        # then creating and filling different values
        df[''] = ''
        df['mod1'] = ''
        df.at[2, "mod1"] = f"mod: {mod}"

        df["Overall Octant Count"] = ''
        df.at[1, "Overall Octant Count"] = "Octant ID"
        df.at[2, "Overall Octant Count"] = "Overall Count" 

        mn = 0
        mx = mod - 1
        rowMax = sz // mod

        # populating ranges of sizes mod starting from 0 to mod-1 till last interval max value hits df' max row value
        for i in range(3, rowMax + 4):
            if i is rowMax + 3:
                mx = sz - 1
            df.at[i, "Overall Octant Count"] = f"{mn} - {mx}" 
            mn = mn + mod
            mx = mx + mod
        df["1"]=''; df["-1"]=''; df["2"]='';df["-2"]='';df["3"]=''; df["-3"]=""; df["4"]=""; df["-4"]='';
        df["rank1"]=''; df["rank-1"]=''; df["rank2"]='';df["rank-2"]='';df["rank3"]=''; df["rank-3"]=""; df["rank4"]=""; df["rank-4"]='';
        df["rank1id"] = ''; df["rank1idname"] = ''; df['   ']=''
        mp = {1:1, 2:-1, 3:2, 4:-2, 5:3, 6:-3, 7:4, 8:-4}
        for i in mp:
            df.at[1, f"{mp[i]}"] = mp[i]
            df.at[1, f"rank{mp[i]}"] = f"Rank of {mp[i]}"


    #     # df.head(15)

        mn = 0
        mx = mod - 1


#This shall be the last lines of the code.
end_time = datetime.now()
print('Duration of Program Execution: {}'.format(end_time - start_time))
