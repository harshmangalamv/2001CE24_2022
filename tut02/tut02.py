import pandas as pd
import math
import os
from pathlib import Path
# df = pd.read_excel('input_octant_transition_identify.xlsx')
# the following part is copied from the previous tutorial work i.e. tut01: 
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

# what follows from here onwards is the major part that solves the problem of mod transition count:

# this function takes start, end (integral values for a specific mod range) and row, col integral values for uppermost left
# end of the table that solves a part of the problem

    def trans(st, en, row, col):
        df.iloc[row, col] = "Mod Transition Count"
        df.iloc[row+1, col] = f'{st} - {en}'
        df.iloc[row+2, col] = "Count"
        df.iloc[row+1, col+1] = "To"
        df.iloc[row+3, col-1] = "From"
        
        # preparing headers for transitions
        # kindly NOTE_ THE TRANSITION HEADS IN MY OUTPUT ARE DIFFERENT, AS THEY NEED NOT NECESSARILY BE IN THE SAME ORDER AS GIVEN IN THE SAMPLE
        head = -4
        for x in range(1, 9):
            if head != 0:
                df.iloc[row + 2, col + x] = head
            head += 1
            if head == 0:
                head += 1
        
        head = -4
        for x in range(3, 11):
            if head != 0:
                df.iloc[row + x, col] = head
            head += 1
            if head == 0:
                head += 1
        
        #   first stv, env collect transition "from" and "to" values, then their corresponding universal row and column values are computed
        #   and stored int them only
        #   then df.iat[stv, env], which tells the transition value corresponding to count of change from "stv" to "env", is ioncremented
        #   once correspondingly
        for x in range(st, en + 1):
            if x == 29744:
                break
            stv = df.at[x, 'Octant']
            env = df.at[x+1, 'Octant']
            stv = int(stv)
            env = int(env)
            ads = 5
            ade = 5
            if(env > 0):
                ade = 4
            if(stv > 0):
                ads = 4
            stv = row + stv + ads + 2
            env = col + env + ade
            df.iat[stv, env] += 1
        
    
    row = rowMax + 18
    col = 12
    st = 0
    en = mod - 1
    num = sz//(mod) + 1

    for i in range(num):
        trans(st, en, row, col)
        st = en + 1
        en = en + mod
        if en > 29740:
            en = 29744
        row = row + 13
    
    trans(0, sz-1, rowMax + 5, 12)


    if Path("octant_output22.csv").exists():
        os.remove("octant_output22.csv")
    df.to_csv('octant_output.csv')
octant_transition_count(5000)
