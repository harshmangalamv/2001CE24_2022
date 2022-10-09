import pandas as pd
import math
import os
from pathlib import Path
from datetime import datetime
start_time = datetime.now()

print("runs")

#Help https://youtu.be/H37f_x4wAC0


def octant_longest_subsequence_count_with_range():
  ###Code
  # df
  # try:
  df = pd.read_excel(r'input_octant_longest_subsequence_with_range.xlsx')
  # except:
  #     print("Error: check if file name is correct, or input file is provided")
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

  print("runs1")

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

  print("runs2")

octant_longest_subsequence_count_with_range()


# This shall be the last lines of the code.
end_time = datetime.now()
print('Duration of Program Execution: {}'.format(end_time - start_time))
