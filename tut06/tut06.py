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

    count_of_total_classes_official = 18
    totalday_count=len(lectureday)
    df = pd.DataFrame(columns=['Roll','Name'] + lectureday)
    df.at[0,'Actual Lecture Taken']='Total monday+ thurs dynamic count'
    
    for i in range(221):
        temp_list = []
        roll = df_reg_stud['Roll No'][i]
        name = df_reg_stud['Name'][i]
        df_1 = pd.DataFrame(columns=['Dates'])
        k = 0
        for j in range(0, len(df_input_attend['Timestamp'])):
            a1 = type(df_input_attend.at[j, 'Attendance'])
            if(a1 == float):
                continue  # to skip some errors I faced, this fixed, idk how
            if (df_input_attend.at[j, 'Attendance'].split()[0] == roll):
                df_1.at[k, 'Dates'] = df_input_attend.at[j, 'Timestamp']
                k = k + 1
        df_1['Dates'] = pd.to_datetime(df_1['Dates'], dayfirst=True)

        x1="14"; x2="15"
        time1="14:00:00"; time2="15:00:00"
        lenp=len(df_1['Dates'])
        for r in range(lenp):
            p1=df_1['Dates'][r]; p1=str(p1); y = p1.split(" ")
            date1=y[0]; date1=str(date1); o=date1.split("-"); u1=o[2]+"/"+o[1] +"/"+o[0]
            f=y[1].split(':') # splitting time
            hour = f[0]; minute = f[1]  
            if (findDay(u1) == 'Monday') or (findDay(u1) == 'Thursday'):# pruning dates only when classes were done
                temp_list.append((p1))   
        check="tut06/output/{}".format(roll)+'.xlsx'
        if (os.path.exists("output")) == False:  # if path does not already exist then make a new directory
            os.mkdir("output")
        len_temp_list=len(temp_list)
        temp=pd.read_excel(check)#reading data of excel file with pathname check
        totalcountofreal=0#total real count 
        temp.at[0,'Name']=name; temp.at[0,'Roll']=roll; df.at[i+1,'Name']=name
        for j1 in range(totalday_count):
            list2=[]
            for k1 in range(len(temp_list)):
                st1=temp_list[k1]
                if(st1==""):
                    continue

                st2=st1.split(" ")
                r1=st2[0] #r1 stores date of submission of attendance
                if lectureday[j1]==r1:
                    list2.append(temp_list[k1])



attendance_report()




#This shall be the last lines of the code.
end_time = datetime.now()
print('Duration of Program Execution: {}'.format(end_time - start_time))
