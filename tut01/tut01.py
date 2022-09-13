import pandas as pd
import pandas as pd

# UPD: original code from tutorial that checked python version removed - not needed anymore
df = pd.read_csv("octant_input.csv")

df.at[0, "U Avg"] = df["U"].mean()
df.at[0, "V Avg"] = df["V"].mean()
df.at[0, "W Avg"] = df["W"].mean()
df.at[0, "U Avg"] = df["U"].mean()
df = df.fillna()
sz = len(df)

# this function calculates the differences required
def fun(a, b, c, sz):
    for i in range(sz):
        df.at[i, c] = df.at[i, a] - df.at[0, b]

# df.drop("W'=W - W avg", inplace=True, axis=1)

# function calls for meking changes as pre requirement for the columns
fun("U", "U Avg", "U'", sz)
fun("V", "V Avg", "V'", sz)
fun("W", "W Avg", "W'", sz)

# df

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

df

# def nanToZero(a):
#     for i in range(sz):
#         if(df.at[i, a]=="NaN"):
#             df.at[i, a]=0
# nanToZero("U Avg")
# nanToZero("V Avg")
# nanToZero("W Avg")

# df["U Avg"].dropna
# df["V Avg"].dropna
# df["W Avg"].dropna
# df.dropna()
