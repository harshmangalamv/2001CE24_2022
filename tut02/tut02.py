import pandas as pd
import math
import os
from pathlib import Path
# df = pd.read_excel('input_octant_transition_identify.xlsx')
def octant_transition_count(mod=5000):
    ###Code
    
    df = pd.read_excel(r'C:\Users\harsh\Documents\GitHub\2001CE24_2022\tut02\input_octant_transition_identify.xlsx')
    df['U Avg']=''
    df['V Avg']=''
    df['W Avg']=''
    df.loc[0, 'U Avg'] = df['U'].mean()
    df.loc[0, 'V Avg'] = df['V'].mean()
    df.loc[0, 'W Avg'] = df['W'].mean()
    df["U'"] = ''
    df["V'"] = ''
    df["W'"] = ''
    sz = len(df)
    def fun(a, b, c, sz):
        for i in range(sz):
            df.at[i, c] = df.at[i, a] - df.at[0, b]
    
    fun("U", "U Avg","U'", sz)
    fun("V", "V Avg","V'", sz)
    fun("W", "W Avg","W'", sz)

    for i in range(sz):
        if(df.at[i, "U'"]>=0 and df.at[i, "V'"]>=0 and df.at[i, "W'"]>=0):
            df.at[i, "Octant"] = 1
        if(df.at[i, "U'"]>=0 and df.at[i, "V'"]>=0 and df.at[i, "W'"]<0):
            df.at[i, "Octant"] = -1
        if(df.at[i, "U'"]<0 and df.at[i, "V'"]>=0 and df.at[i, "W'"]>=0):
            df.at[i, "Octant"] = 2
        if(df.at[i, "U'"]<0 and df.at[i, "V'"]>=0 and df.at[i, "W'"]<0):
            df.at[i, "Octant"] = -2
        if(df.at[i, "U'"]<0 and df.at[i, "V'"]<0 and df.at[i, "W'"]>=0):
            df.at[i, "Octant"] = 3
        if(df.at[i, "U'"]<0 and df.at[i, "V'"]<0 and df.at[i, "W'"]<0):
            df.at[i, "Octant"] = -3
        if(df.at[i, "U'"]>=0 and df.at[i, "V'"]<0 and df.at[i, "W'"]>=0):
            df.at[i, "Octant"] = 4
        if(df.at[i, "U'"]>=0 and df.at[i, "V'"]<0 and df.at[i, "W'"]<0):
            df.at[i, "Octant"] = -4
    
    df["User Activity"] = ""
    df.at[2, "User Activity"] = "User Input->"
    mod = 6000
    df["Octant ID"] = ''
    df.at[1, "Octant ID"] = "Overall Count"
    df.at[2, "Octant ID"] = f"mod {mod}"

    mn = 0 
    mx = mod - 1
    rowMax = sz // mod
    for i in range(3, rowMax + 4):
        if i is rowMax + 3:
            mx = sz - 1
        df.at[i, "Octant ID"] = f"{mn} - {mx}" 
        mn = mn + mod
        mx = mx + mod
    
    mn = 0


    mx = mod - 1
    for row in range(3, rowMax + 4):
        df = df.fillna(0)
        freq = {}
        for i in range(mn, mx):
            if(i >= 29745):
                break
            if(df.at[i, "Octant"] in freq):
                freq[df.at[i, "Octant"]] = freq[df.at[i, "Octant"]] + 1
            else:
                freq[df.at[i, "Octant"]] = 1

        for key, value in freq.items():
            df = df.fillna('')

            df.at[row, key] = int(value)

            if(df.at[1, key] == ''):
                df.at[1, key] = 0
            df = df.fillna(0)
            df.at[1, key] = int(df.at[1, key]) + int(value)
    
    mn = mn + mod
    mx = mx + mod

    

    if Path("octant_output22.csv").exists():
        os.remove("octant_output22.csv")
    df.to_csv('octant_output.csv')
octant_transition_count(5000)