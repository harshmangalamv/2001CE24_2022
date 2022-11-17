# importing different requirements
import pandas as pd
from numpy import nan
import numpy as np
import os
import calendar
import math
import datetime
start_time = datetime.datetime.now()

pd.options.mode.chained_assignment = None  # default='warn'

#function to calcualate the day of the week when we give the input in format of string as dd/mm/yy

def findDay(date):
    day, month, year = (int(i) for i in date.split('/'))
    born = datetime.date(year, month, day)
    return born.strftime("%A")

def attendance_report():
###Code
    df_reg_stud = pd.read_csv('tut06\input_registered_students.csv')
    df_input_attend = pd.read_csv('tut06\input_attendance.csv')

    # (before running for updated attendance list, update this manunally) to store dates of lecture in yy-mm-dd
    lectureday = ['2022-07-28', '2022-08-01', '2022-08-04', '2022-08-08',
        '2022-08-12', '2022-08-15', '2022-08-18', '2022-08-22',
        '2022-08-25','2022-08-29','2022-09-01', '2022-09-05',
        '2022-09-08','2022-09-12','2022-09-15',
        '2022-09-19','2022-09-22','2022-09-26','2022-09-29']
 

attendance_report()




#This shall be the last lines of the code.
end_time = datetime.now()
print('Duration of Program Execution: {}'.format(end_time - start_time))
