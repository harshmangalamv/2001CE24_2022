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
    
    # what follows from here onwards is the major part that solves the problem of octant_longest_subsequence_count():

    df['Count'] = ''
    df["Longest Subsequence Length"] = ''
    df["count"] = ''
    mp = {1: 1, 2: -1, 3: 2, 4: -2, 5: 3, 6: -3, 7: 4, 8: -4}
    for i in range(1, 9):
        df.at[i, 'Count'] = int(mp[i])

    ct = {1: 0, -1: 0, 2: 0, -2: 0, 3: 0, -3: 0, 4: 0, -4: 0}
    loc = {1: 0, -1: 1, 2: 2, -2: 3, 3: 4, -3: 5, 4: 6, -4: 7}
    ct_count = {1: 0, -1: 0, 2: 0, -2: 0, 3: 0, -3: 0, 4: 0, -4: 0}
    for i in range(1, 9):
        df.loc[i, "Longest Subsequence Length"] = int(0)
        df.loc[i, "count"] = int(0)
    for i in range(-4, 5):
        print("running at: ", i)
        if i == 0:
            continue
        temp_ct = int(0)
        for j in range(29744):
            if df.at[j, 'Octant'] == i:
                temp_ct += 1
            else:
                if df.at[1 + int(loc[i]), "Longest Subsequence Length"] == temp_ct:
                    df.at[1 + int(loc[i]), "count"] += 1
                # print(temp_ct, " ",
                #       df.loc[1 + int(loc[i]), "Longest Subsequence Length"])
                df.loc[1 + int(loc[i]), "Longest Subsequence Length"] = max(
                    int(temp_ct), df.loc[1 + int(loc[i]), "Longest Subsequence Length"])
                temp_ct = int(0)


    if Path("put_octant_longest_subsequence.xlsx").exists():
        os.remove("put_octant_longest_subsequence.xlsx")
    df.to_excel('put_octant_longest_subsequence.xlsx')
    print(df.head)

octant_longest_subsequence_count()
