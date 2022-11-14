import os
import re
import py
import math
from datetime import datetime
start_time = datetime.now()

f_in = open(r'C:\Users\harsh\Documents\GitHub\trash_lol\tut08\india_inns2.txt', 'r')
f_pk = open(r'C:\Users\harsh\Documents\GitHub\trash_lol\tut08\pak_inns1.txt', 'r')
op = open(r'C:\Users\harsh\Documents\GitHub\trash_lol\tut08\Scorecard.txt', 'w')

# Harsh MangalM Verma
# 2001CE24
def scorecard():
	search_in =f_in.read()
	search_pk =f_pk.read()
	content_in = search_in.split('\n')
	content_pk = search_pk.split('\n')

	team_in = ["Rohit", "Rahul", "Kohli", "Jadeja", "Suryakumar Yadav", "Hardik Pandya", "Karthik", \
		"Bhuvneshwar Kumar", "Avesh Khan", "Yuzvendra Chahal", "Arshdeep Singh"]
	bowler_in = ["Bhuvneshwar", "Arshdeep Singh", "Hardik Pandya", "Avesh Khan", "Chahal", "Jadeja"]
	team_pak = ["Rizwan", "Babar Azam", "Fakhar Zaman","Iftikhar Ahmed","Khushdil","Shadab Khan","Asif Ali", "Mohammad Nawaz",  "Haris Rauf", "Naseem Shah", "Dahani"]
	bowler_pak = ["Naseem Shah", "Dahani", "Haris Rauf", "Shadab Khan", "Mohammad Nawaz"]
	# print(bowler_pak, '\n')
	run_bat_in = {}
	ball_bat_in = {}
	fours_bat_in = {}
	six_bat_in = {}
	sr_bat_in = {}
	retby_in = {}
	balls_in ={}

	run_bat_pak = {}
	ball_bat_pak = {}
	fours_bat_pak = {}
	six_bat_pak = {}
	sr_bat_pak = {}
	retby_pak = {}
	balls_pak ={}

	for batsman in team_in:
		run_bat_in[batsman]     = int(0)
		ball_bat_in[batsman]    = int(0)
		fours_bat_in[batsman]   = int(0)
		six_bat_in[batsman]     = int(0)
		sr_bat_in[batsman]      = int(0)
		balls_in[batsman]       = int(0)
		retby_in[batsman]       = "not out"
		

	for batsman in team_pak:
		run_bat_pak[batsman]    = int(0)
		ball_bat_pak[batsman]   = int(0)
		fours_bat_pak[batsman]  = int(0)
		six_bat_pak[batsman]    = int(0)
		sr_bat_pak[batsman]     = int(0)
		balls_pak[batsman]      = int(0)
		retby_pak[batsman]      = "not out"

	over_in = {}; maiden_in = {}; run_in = {}; wicket_in = {}; nb_in = {}; wd_in = {}; eco_in = {} # run_in - > it is run against a bowler
	over_pk = {}; maiden_pk = {}; run_pk = {}; wicket_pk = {}; nb_pk = {}; wd_pk = {}; eco_pk = {}

	for bowler in bowler_in:
		over_in[bowler] = int(0); maiden_in[bowler] = int(0); run_in[bowler] = int(0); wicket_in[bowler] = int(0); nb_in[bowler] = int(0); wd_in[bowler] = int(0); eco_in[bowler] = int(0)
	for bowler in bowler_pak:
		over_pk[bowler] = int(0); maiden_pk[bowler] = int(0); run_pk[bowler] = int(0); wicket_pk[bowler] = int(0); nb_pk[bowler] = int(0); wd_pk[bowler] = int(0); eco_pk[bowler] = int(0)


	lb_i = 0; b_i = 0; w_i = 0; nb_i = 0; p_i = 0; wkts_i = 0; ov_i = 0; runs_i = 0; cur_run_in = 0; pwr_run_in = int(0)
	lb_p = 0; b_p = 0; w_p = 0; nb_p = 0; p_p = 0; wkts_p = 0; ov_pk = 0; runs_pk = 0; cur_run_pk = 0; pwr_run_pk = int(0)


scorecard()

#This shall be the last lines of the code.
end_time = datetime.now()
print('Duration of Program Execution: {}'.format(end_time - start_time))
