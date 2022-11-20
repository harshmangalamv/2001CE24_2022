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

    #     # for every range, iterating and storing count of octant values by using a map, later updating the overall count
    #     # values of corresponding octant values in overall count row 
        freq1 = {}
        for row in range(3, rowMax + 4):
            freq = {} # intiating freq map
            pair_val_id = []
            for i in range(mn, mx):
                if(i >= sz):
                    break
                if(df.at[i, "Octant"] in freq):
                    freq[df.at[i, "Octant"]] = freq[df.at[i, "Octant"]] + 1 # incrementing the key value for the key
                else:
                    freq[df.at[i, "Octant"]] = 1 # initiating the key if not present
            freq = dict(sorted(freq.items(), key=lambda item: item[1]))
            ct = 8
            for i in freq:
                if ct == 1:
                    df.at[row, "rank1id"] = i
                df.at[row, f"rank{i}"] = ct; ct -= 1


            for i in mp:
                try:
                    df.at[row, f"{mp[i]}"] = freq[mp[i]]
                    df.at[2, f"{mp[i]}"] += freq[mp[i]]
                    freq1[mp[i]] = df.at[2, f"{mp[i]}"]
                except:
                    df.at[2, f"{mp[i]}"] = freq[mp[i]]


            mn = mn + mod
            mx = mx + mod
        freq1 = dict(sorted(freq1.items(), key=lambda item: item[1]))
        ct = 8
        for i in freq1:
            if ct == 1:
                    df.at[2, "rank1id"] = i
            df.at[2, f"rank{i}"] = ct; ct -= 1

        df[''] = ''
        df['frm'] = ''
        df.at[2, "frm"] = "From"
        df['Overall Transition Count'] = ''
        df.at[1, "Overall Transition Count"] = "Octant #"
        for i in range(0, 8):
            df.at[i+2, "Overall Transition Count"] = mp[i+1]
            df[f"{mp[i+1]}{mp[i+1]}"] = ''
            df.at[1, f"{mp[i+1]}{mp[i+1]}"] = mp[i+1]
    #     mp = {1:1, 2:-1, 3:2, 4:-2, 5:3, 6:-3, 7:4, 8:-4}
        def trans(st, en, row, col, str="Mod Transition Count"):
            df.iloc[row, col] = str
            df.iloc[row+1, col] = f'{st} - {en}'
            df.iloc[row+2, col] = "Octant #"
            df.iloc[row+1, col+1] = "To"
            df.iloc[row+3, col-1] = "From"

            # preparing headers for transitions
            # kindly NOTE_ THE TRANSITION HEADS IN MY OUTPUT ARE DIFFERENT, AS THEY NEED NOT NECESSARILY BE IN THE SAME ORDER AS GIVEN IN THE SAMPLE

            for x in range(1, 9):
#                 print(row + 2, f"{mp[x]}{mp[x]}")
                df.at[row + 2,f"{mp[x]}{mp[x]}"] = mp[x]

            for x in range(1, 9):
                df.at[row+2+x, "Overall Transition Count"] = mp[x]

            #   first stv, env collect transition "from" and "to" values, then their corresponding universal row and column values are computed
            #   and stored int them only
            #   then df.iat[stv, env], which tells the transition value corresponding to count of change from "stv" to "env", is ioncremented
            #   once correspondingly
    #         print("st: ", st, "en: ", en, "row: ", row, "col: ", col)
            mpp = {1:1, -1:2, 2:3, -2:4, 3:5, -3:6, 4:7, -4:8}
            for x in range(st, en + 1):
    #             df.fillna(0)
                if x == sz-1:
                    break
                stv = df.at[x, 'Octant']
                env = df.at[x+1, 'Octant']
                try:
                    df.at[row+2+mpp[stv], f"{env}{env}" ] += 1
                except:
                    df.at[row+2+mpp[stv], f"{env}{env}"] = 1
    #     trans(0, 4999, 14, 33)
        row = 14
        col = 34
        st = 0
        en = mod - 1
        num = sz//(mod) + 1

    #     print("rowMax: ", rowMax, "st: ", st)
        for i in range(num):
            trans(st, en, row, col)
            st = en + 1
            en = en + mod
            if en > sz:
                en = sz
            row = row + 14

        trans(0, sz-1, 1 , 33, "Overall Transition Count")

        df[' '] = ''
        df['Longest Subsequence Length'] = ''
        df.at[1, 'Longest Subsequence Length'] = "Octant #"
        for i in range(1, 9):
            df.at[i+1, 'Longest Subsequence Length'] = mp[i]
        df['lsl'] = ''
        df.at[1, 'lsl'] = 'Longest Subsequence Length'
        df['countt'] = ''

        # loc dictionary would help telling intergral coordintes required for calculation pruposes
        loc = {1: 0, -1: 1, 2: 2, -2: 3, 3: 4, -3: 5, 4: 6, -4: 7}
        # initiating "Longest Subsequence Length" and "count" columns with 0s
        df.at[1, 'countt'] = "Count"
        for i in range(1, 9):
            df.loc[i+1, 'lsl'] = int(0)
            df.loc[i+1, "countt"] = int(0)




        for i in range(-4, 5):
        #   print("runs ", i)
            if i == 0:
                continue
            temp_ct = int(0)
            for j in range(sz):
                if df.at[j, 'Octant'] == i:
                  temp_ct += 1
                else:
                  df.at[45, "lsl"] = max(temp_ct, df.at[loc[i]+2, "lsl"])
                  temp_ct = int(0)

    #   print("runs3")
        store = [[], [], [], [], [], [], [], []] # stores the last time stamp for longest sequence


#         print(df.head(30)) # printing top 30 rows to review
#         if Path("output/octant_output.xlsx").exists():
#             os.remove("output/octant_output.xlsx")
        df.to_excel(f'output/{file_name}_vel_octant_analysis_mod_{mod}.xlsx')
        # this part exports df to an output file if not present, otherwise it first deletes it first to avoid overwriting errors i faced in my system 


    #     print("mod: ", mod)

mod = 5000
octant_identification(mod)

#This shall be the last lines of the code.
end_time = datetime.now()
print('Duration of Program Execution: {}'.format(end_time - start_time))
