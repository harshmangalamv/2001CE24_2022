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


for row in range(3, 9):
    freq = {}
#     if(row>10):
#         break
    if(row == 3):
        mn = 0
        mx = mod
    for i in range(mn, mx):
        if(i >= 29745):
            break
        if(df.at[i, "Octant"] in freq):
            freq[df.at[i, "Octant"]] = freq[df.at[i, "Octant"]] + 1
        else:
            freq[df.at[i, "Octant"]] = 1
    for key, value in freq.items():
        df.at[row, key] = value
        if(df.at[1, key] == ''):
            df.at[1, key] = 0
        df.at[1, key] = df.at[1, key] + value

    if(row == 3):
        mn = mod+1
        mx = 2*mod
    if(row > 3):
        mn = mn + mod
        mx = mx + mod


# for i in range(1, 5000):
#     if(df.at[i, "Octant"]==1.0):
#         count1 = count1+1

# count1
df = df.fillna('')
df.head(15)
# df

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
