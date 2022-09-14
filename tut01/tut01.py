# Writer:
# Harsh Mangalam Verma (IIT Patna) 
# For tut01

def octant_identification(mod = 4000):
    import pandas as pd
    import math
    import os
    from pathlib import Path

    df = pd.read_csv("tut01\octant_input.csv")

    # creating and populating colums that store Avg values
    df.at[0, "U Avg"] = df["U"].mean()
    df.at[0, "V Avg"] = df["V"].mean()
    df.at[0, "W Avg"] = df["W"].mean()
    df.at[0, "U Avg"] = df["U"].mean()
    sz = len(df)

    # this function calculates the differences required
    def fun(a, b, c, sz):
        for i in range(sz):
            df.at[i, c] = df.at[i, a] - df.at[0, b]

    # function calls for creating new columns that store, while calculating as per requirements at the same time
    fun("U", "U Avg", "U'", sz)
    fun("V", "V Avg", "V'", sz)
    fun("W", "W Avg", "W'", sz)
    df = df.fillna('')
    # df

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
    df["User Activity"] = ""
    df.at[2, "User Activity"] = "User Input->"
    df["Octant ID"] = ''
    df.at[1, "Octant ID"] = "Overall Count"
    df.at[2, "Octant ID"] = f"mod: {mod}"

    mn = 0
    mx = mod - 1
    rowMax = sz // mod

    # populating ranges of sizes mod starting from 0 to mod-1 till last interval max value hits df' max row value
    for i in range(3, rowMax + 4):
        if i is rowMax + 3:
            mx = sz - 1
        df.at[i, "Octant ID"] = f"{mn} - {mx}" 
        mn = mn + mod
        mx = mx + mod

    # df.head(15)

    mn = 0
    mx = mod - 1

    # for every range, iterating and storing count of octant values by using a map, later updating the overall count
    # values of corresponding octant values in overall count row 
    for row in range(3, rowMax + 4):
        freq = {} # intiating freq map
        for i in range(mn, mx):
            if(i >= 29745):
                break
            if(df.at[i, "Octant"] in freq):
                freq[df.at[i, "Octant"]] = freq[df.at[i, "Octant"]] + 1 # incrementing the key value for the key
            else:
                freq[df.at[i, "Octant"]] = 1 # initiating the key if not present

        for key, value in freq.items():
            df = df.fillna('')

            df.at[row, key] = int(value) # filling the value corresponding to every octant value (key) and row range (row)

            df = df.fillna(0)
            df.at[1, key] = int(df.at[1, key]) + int(value) # updating the verall count (row 1) and octant value (key) 

        # df = df.fillna('')

        mn = mn + mod
        mx = mx + mod

    print(df.head(30)) # printing top 30 rows to review

    # this part exports df to an output file if not present, otherwise it first deletes it first to avoid overwriting errors i faced in my system 
    if Path("tut01/octant_output.csv").exists():
        os.remove("tut01/octant_output.csv")
    df.to_csv('tut01/octant_output.csv')

    print("mod: ", mod)

mod = 300
octant_identification(mod)