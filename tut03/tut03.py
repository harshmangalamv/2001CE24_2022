import pandas as pd
import math
import os
from pathlib import Path

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
    
    # what follows from here onwards is the major part that solves the problem of octant_longest_subsequence_count():

    # initializing required column headers
    df['Count'] = ''
    df["Longest Subsequence Length"] = ''
    df["count"] = ''
    mp = {1: 1, 2: -1, 3: 2, 4: -2, 5: 3, 6: -3, 7: 4, 8: -4}
    for i in range(1, 9):
        df.at[i, 'Count'] = int(mp[i])

    # loc dictionary would help telling intergral coordintes required for calculation pruposes
    loc = {1: 0, -1: 1, 2: 2, -2: 3, 3: 4, -3: 5, 4: 6, -4: 7}
    # initiating "Longest Subsequence Length" and "count" columns with 0s
    for i in range(1, 9):
        df.loc[i, "Longest Subsequence Length"] = int(0)
        df.loc[i, "count"] = int(0)
    
    # calculating for longest subsequnce length
    # i is for octant values, j runs over all rows 
    # if df.at[j, 'Octant'] matches with i ie the "octant" number, increment, else update 
    # longest subsequence length and reset the corresponding count stored as temp_ct
    for i in range(-4, 5):
        if i == 0:
            continue
        temp_ct = int(0)
        for j in range(29744):
            if df.at[j, 'Octant'] == i:
                temp_ct += 1
            else:
                df.loc[1 + int(loc[i]), "Longest Subsequence Length"] = max(
                    int(temp_ct), df.loc[1 + int(loc[i]), "Longest Subsequence Length"])
                temp_ct = int(0)

    # calculations for count of total number of "longest subsequence length" 
    # if temp_ct, that stores count of octant number "i", equals "Longest Subsequence Length"
    # corresponding count for "i" is incremented 
    for i in range(-4, 5):
        if i == 0:
            continue
        temp_ct = int(0)
        for j in range(29744):
            if df.at[j, 'Octant'] == i:
                temp_ct += 1
            else:
                if temp_ct == df.loc[1 + int(loc[i]), "Longest Subsequence Length"]:
                    df.at[1 + int(loc[i]), "count"] += 1
                temp_ct = int(0)

    if Path("output_octant_longest_subsequence.xlsx").exists():
        os.remove("output_octant_longest_subsequence.xlsx")
    df.to_excel('output_octant_longest_subsequence.xlsx')

octant_longest_subsequence_count()