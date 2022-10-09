import pandas as pd
import math
import os
from pathlib import Path
from datetime import datetime
start_time = datetime.now()

# print("runs")
# NOTE: THIS PROGRAM TOOK 2 MIN 29 SEC TO RUN ON MY LOCAL MACHINE
#       THERE ARE A NUMBER OF PRINT STATEMENTS COMMENTED ALREADY FOR BETTER DEBUGGING - THE LEAST THEY TELL: WHERE(THE LINE) IS THE PROGRAM RUNNING RN! 

#Help https://youtu.be/H37f_x4wAC0
def octant_longest_subsequence_count_with_range():
  ###Code
  # df
  try:
    df = pd.read_excel(r'input_octant_longest_subsequence_with_range.xlsx')
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

#   print("runs1")

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

#   print("runs2")

# what follows from here onwards is the major part that solves the problem of octant_longest_subsequence_with_range():
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
    #   print("runs ", i)
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

#   print("runs3")
  store = [[], [], [], [], [], [], [], []] # stores the last time stamp for longest sequence

# calculations for count of total number of "longest subsequence length"
  # if temp_ct, that stores count of octant number "i", equals "Longest Subsequence Length"
  # corresponding count for "i" is incremented
  for i in range(-4, 5):
    #   print("runs ", i)
      if i == 0:
          continue
      temp_ct = int(0)
      for j in range(29744):
          if df.at[j, 'Octant'] == i:
              temp_ct += 1
          else:
              if temp_ct == df.loc[1 + int(loc[i]), "Longest Subsequence Length"]:
                  df.at[1 + int(loc[i]), "count"] += 1
                  store[loc[i]].append(df.at[j, "Time"])
              temp_ct = int(0)

  df['Octant.'] = ''
  df['Longest Subsequence Length.'] = ''
  df['Count.'] = ''

  row = 1 # for traversing through rows
#   idea: using mp and loc dictionaries, i filled the corresponding sequence values with use of for loop
#         evry for loop's first 3 lines fill in "Longest Subsequence Length", count for a given octant
#         then 'time', 'from' and 'to' are filled in next row
#         then row incremented by 1
#         another embedded for loop fills in start and end time stamps corresponding to those longest subsequences
#         since "store" for any octant value stores only "to" values, "from" values are derived by subtracting the (size of correspnding subsequence MINUS 1)*(0.01)
#         so next lines fill the "from" and "to" values correspondingly 
  for i in range(1, 9):
      df.loc[row, "Octant."] = mp[i]
    #   print(df.at[loc[mp[i]]+2, "Longest Subsequence Length"])
      df.loc[row, "Longest Subsequence Length."] = df.at[int(loc[mp[i]])+1, "Longest Subsequence Length"]
      df.loc[row, "Count."] = df.at[int(loc[mp[i]])+1, "count"]
      df.loc[row + 1, "Octant."] = "Time"
      df.loc[row + 1, "Longest Subsequence Length."] = "From"
      df.loc[row + 1, "Count."] = "To"
      row += 1
      for j in range(1, len(store[loc[mp[i]]]) + 1):
          df.loc[row + j, "Longest Subsequence Length."] = store[loc[mp[i]]][j - 1] - (int(df.at[int(loc[mp[i]])+1, "Longest Subsequence Length"]) - 1)*0.01
          df.loc[row + j, "Count."] = store[loc[mp[i]]][j - 1]

      row += (len(store[loc[mp[i]]]) + 1)

#   print("runs4")

  if Path("output_octant_longest_subsequence_with_range.xlsx").exists():
    os.remove("output_octant_longest_subsequence_with_range.xlsx")
  df.to_excel("output_octant_longest_subsequence_with_range.xlsx")
#   print(df)

octant_longest_subsequence_count_with_range()
print("well, it runs, really!!")

# This shall be the last lines of the code.
end_time = datetime.now()
print('Duration of Program Execution: {}'.format(end_time - start_time))