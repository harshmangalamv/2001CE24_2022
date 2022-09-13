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

# df

# mod = int(input("Enter the alue of mod:\n"))
mod = 5000
df["Octant ID"] = ''
df.at[1, "Octant ID"] = "Overall Count"
df.at[2, "Octant ID"] = f"mod: {mod}"

mn = 5001
mx = 10000

for i in range(3, 9):
    if(i == 3):
        df.at[i, "Octant ID"] = "0000-5000"
    else:
        df.at[i, "Octant ID"] = f"{mn} - {mx}"
        mn = mn + 5000
        mx = mx + 5000

# df.head(15)

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
