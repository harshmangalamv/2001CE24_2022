import pandas as pd
import math
import os
from pathlib import Path
# df = pd.read_excel('input_octant_transition_identify.xlsx')
# the following part is copied from the previous tutorial work i.e. tut01:


def octant_longest_subsequence_count(mod=5000):
    ###Code
    try:
        df = pd.read_excel(r'input_octant_longest_subsequence.xlsx')
    except:
        print("Error: check if file name is correct, or input file is provided")
    df['U Avg'] = ''
    df['V Avg'] = ''
    df['W Avg'] = ''
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

    fun("U", "U Avg", "U'", sz)
    fun("V", "V Avg", "V'", sz)
    fun("W", "W Avg", "W'", sz)

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

    df["User Activity"] = ""
    df.at[2, "User Activity"] = "User Input->"
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

    # what follows from here onwards is the major part that solves the problem of octant_longest_subsequence_count():
    

octant_longest_subsequence_count()
