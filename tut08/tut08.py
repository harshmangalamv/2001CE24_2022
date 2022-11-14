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


	i_sc = int(0)
	pk_sc = int(0)
	m = 0
	ctr = int(0)
	# txts = ''''''
	fall_in = ''''''
	fall_pak = ''''''
	for para in content_pk:
		if(para == ""):
			continue
		m = re.search(r'[0-9]+\.[0-9]', para)
		b_b1 = re.search(r'([A-Z][a-z]*)[\s-](to)\s([A-Z][a-z]*)', para)
		b_b2 = re.search(
			r'([A-Z][a-z]*)[\s-]([A-Z][a-z]*)\s(to)\s([A-Z][a-z]*)', para)
		b_b3 = re.search(
			r'([A-Z][a-z]*)[\s-](to)\s([A-Z][a-z]*)\s([A-Z][a-z]*)', para)
		b_b4 = re.search(
			r'([A-Z][a-z]*)[\s-]([A-Z][a-z]*)+\s(to)\s([A-Z][a-z]*)\s([A-Z][a-z]*)', para)

		if(b_b1):
			b_b = b_b1
		if(b_b2):
			b_b = b_b2
		if(b_b3):
			b_b = b_b3
		if(b_b4):
			b_b = b_b4
		b_ = b_b[0].split("to")
		bowler = b_[0].strip()
		batsman = b_[1].strip()

		remark = re.search(f"{batsman},\s((no|1|2|3|4)\s(run|runs))", para)
		if remark:
			skore = (remark[0].split(','))[1].strip()
			if skore == "1 run":
				run_bat_pak[batsman] = run_bat_pak[batsman] + int(1)
				run_in[bowler] += int(1)
				cur_run_pk += int(1)
			elif skore == "2 run":
				run_bat_pak[batsman] = run_bat_pak[batsman] + int(2)
				run_in[bowler] += int(2)
				cur_run_pk += int(2)
			elif skore == "3 run":
				run_bat_pak[batsman] = run_bat_pak[batsman] + int(3)
				run_in[bowler] += int(3)
				cur_run_pk += int(3)
			elif skore == "4 run":
				run_bat_pak[batsman] = run_bat_pak[batsman] + int(4)
				run_in[bowler] += int(4)
				cur_run_pk += int(4)
			balls_pak[batsman] += int(1)
			over_in[bowler] += int(1)
			# print(skore)
		else:
			remark = re.search(f"{batsman},\s(SIX|FOUR)", para)
			if remark:
				skore = (remark[0].split(','))[1].strip()
				if skore == "SIX":
					run_bat_pak[batsman] = run_bat_pak[batsman] + int(6)
					run_in[bowler] += int(6)
					cur_run_pk += int(6)
					six_bat_pak[batsman] += int(1)
				if skore == "FOUR":
					run_bat_pak[batsman] = run_bat_pak[batsman] + int(4)
					run_in[bowler] += int(4)
					cur_run_pk += int(4)
					fours_bat_pak[batsman] += int(1)
				balls_pak[batsman] += int(1)
				over_in[bowler] += int(1)
			else:
				remark = re.search(f"{batsman},\s(out Bowled|out Lbw)", para)
				if remark:
					retby_pak[batsman] = f"b {bowler}"
					wkts_p += int(1)
					wicket_in[bowler] += int(1)
					balls_pak[batsman] += int(1)
					over_in[bowler] += int(1)
					fall_pak += (f"{cur_run_pk}-{wkts_p}({batsman},{m[0]}), ")
					ctr += 1
					if ctr == 4 or ctr == 8:
						fall_pak += f"\n"
				else:
					remark = re.search(f"{batsman},\swide", para)
					if remark:
						pk_sc += int(1)
						w_p += int(1)
						wd_in[bowler] += int(1)
						cur_run_pk += int(1)
						run_in[bowler] += int(1)
					else:
						remark = re.search(f"{batsman},\s[2-9]\swides", para)
						if remark:
							skore = remark[0].split(",")[1].strip()
							if skore == "2 wides":
								pk_sc += int(2)
								cur_run_pk += int(2)
								run_in[bowler] += int(2)
								w_p += int(2)
								wd_in[bowler] += int(2)
							if skore == "3 wides":
								pk_sc += int(3)
								cur_run_pk += int(3)
								run_in[bowler] += int(3)
								w_p += int(3)
								wd_in[bowler] += int(3)
						else:
							remark = re.search(f"{batsman},\sbyes", para)
							if remark:
								b_p += int(1)
								pk_sc += int(1)
								cur_run_pk += int(1)
								run_in[bowler] += int(1)
								over_in[bowler] += int(1)
							else:
								remark = re.search(
									f"{batsman},\sleg\sbyes,\s((1\srun)|[2-4]runs|FOUR),", para)
								if remark:
									typ = (remark[0].split(','))[1].strip()
									skore = ((remark[0].split(',')[2]).strip())
									over_pk[bowler] += int(1)
									if typ == "byes":
										if skore == "FOUR":
											pk_sc += int(4)
											cur_run_pk += int(4)
											run_in[bowler] += int(4)
											b_p += int(4)
										if skore == "1 run":
											pk_sc += int(1)
											cur_run_pk += int(1)
											run_in[bowler] += int(1)
											b_p += int(1)
										if skore == "2 run":
											pk_sc += int(2)
											cur_run_pk += int(2)
											run_in[bowler] += int(2)
											b_p += int(2)
										if skore == "3 run":
											pk_sc += int(3)
											cur_run_pk += int(3)
											run_in[bowler] += int(3)
											b_p += int(3)
									else:
										if skore == "FOUR":
											pk_sc += int(4)
											cur_run_pk += int(4)
											run_in[bowler] += int(4)
											lb_p += int(4)
										if skore == "1 run":
											pk_sc += int(1)
											cur_run_pk += int(1)
											run_in[bowler] += int(1)
											lb_p += int(1)
										if skore == "2 run":
											pk_sc += int(2)
											cur_run_pk += int(2)
											run_in[bowler] += int(2)
											lb_p += int(2)
										if skore == "3 run":
											pk_sc += int(3)
											cur_run_pk += int(3)
											run_in[bowler] += int(3)
											lb_p += int(3)
								else:
									remark = re.search(
										f"{batsman},\s(out Caught by)(\s\w[a-z]*)*", para)
									if remark:
										act = (remark[0].split(","))[
											1].split("by")[1].strip()
										wkts_p += int(1)
										wicket_in[bowler] += int(1)
										retby_pak[batsman] = f"c by {act} b {bowler}"
										fall_pak += (
											f"{cur_run_pk}-{wkts_p}({batsman},{m[0]}), ")
										balls_pak[batsman] += int(1)
										over_in[bowler] += int(1)
										ctr += 1
										if ctr == 4 or ctr == 8:
											fall_pak += f"\n"
									else:
										print(f"this {m[0]}")
										print(remark[0])
		if m[0] == "5.6":
			pwr_run_pk = cur_run_pk
	ov_pk = m[0]
	for batsman in team_pak:
		runs_pk += run_bat_pak[batsman]
	runs_pk += pk_sc
		
	m = 0
	fall_in = ''''''
	for para in content_in:
		if(para == ""):
			continue
		m = re.search(r'[0-9]+\.[0-9]', para)
		b_b1 = re.search(r'([A-Z][a-z]*)[\s-](to)\s([A-Z][a-z]*)', para)
		b_b2 = re.search(r'([A-Z][a-z]*)[\s-]([A-Z][a-z]*)\s(to)\s([A-Z][a-z]*)', para)
		b_b3 = re.search(r'([A-Z][a-z]*)[\s-](to)\s([A-Z][a-z]*)\s([A-Z][a-z]*)', para)
		b_b4 = re.search(r'([A-Z][a-z]*)[\s-]([A-Z][a-z]*)+\s(to)\s([A-Z][a-z]*)\s([A-Z][a-z]*)', para)
		
		if(b_b1):
			b_b = b_b1
		if(b_b2):
			b_b = b_b2
		if(b_b3):
			b_b = b_b3
		if(b_b4):
			b_b = b_b4
		b_ = b_b[0].split("to") 
		bowler = b_[0].strip()
		batsman = b_[1].strip()

		remark = re.search(f"{batsman},\s((no|1|2|3|4)\s(run|runs))", para)  
		if remark:
			skore = (remark[0].split(','))[1].strip()
			if skore == "1 run":
				run_bat_in[batsman] = run_bat_in[batsman] + int(1); run_pk[bowler] += int(1); cur_run_in += int(1)
			elif skore == "2 run":
				run_bat_in[batsman] = run_bat_in[batsman] + int(2); run_pk[bowler] += int(2); cur_run_in += int(2)
			elif skore == "3 run":
				run_bat_in[batsman] = run_bat_in[batsman] + int(3); run_pk[bowler] += int(3); cur_run_in += int(3)
			elif skore == "4 run":
				run_bat_in[batsman] = run_bat_in[batsman] + int(4); run_pk[bowler] += int(4); cur_run_in += int(4)
			balls_in[batsman] += int(1); over_pk[bowler] += int(1)
			# print(skore)
		else:
			remark = re.search(f"{batsman},\s(SIX|FOUR)", para)
			if remark:
				skore = (remark[0].split(','))[1].strip()
				if skore == "SIX":
					run_bat_in[batsman] = run_bat_in[batsman] + int(6); run_pk[bowler] += int(6); cur_run_in += int(6)
					six_bat_in[batsman] += int(1)
				if skore == "FOUR":
					run_bat_in[batsman] = run_bat_in[batsman] + int(4); run_pk[bowler] += int(4); cur_run_in += int(4)
					fours_bat_in[batsman] += int(1)
				balls_in[batsman] += int(1); over_pk[bowler] += int(1)
			else:
				remark = re.search(f"{batsman},\s(out Bowled|out Lbw)", para) 
				if remark:
					retby_in[batsman] = f"b {bowler}"
					wkts_i += int(1); wicket_pk[bowler] += int(1)
					balls_in[batsman] += int(1); over_pk[bowler] += int(1)
					fall_in += (f"{cur_run_in}-{wkts_i}({batsman},{m[0]}), ")
				else:
					remark = re.search(f"{batsman},\swide", para) 
					if remark:
						i_sc += int(1)
						w_i += int(1); wd_pk[bowler] += int(1)
						cur_run_in += int(1); run_pk[bowler] += int(1)
					else:
						remark = re.search(f"{batsman},\s[2-9]\swides", para)
						if remark:
							skore = remark[0].split(",")[1].strip()
							if skore == "2 wides":
								i_sc += int(2); cur_run_in += int(2); run_pk[bowler] += int(2)
								w_i += int(2); wd_pk[bowler] += int(2)
							if skore == "3 wides":
								i_sc += int(3); cur_run_in += int(3); run_pk[bowler] += int(3)
								w_i += int(3); wd_pk[bowler] += int(3)
						else:
							remark = re.search(f"{batsman},\sbyes", para)
							if remark:
								b_i += int(1)
								i_sc += int(1); cur_run_in += int(1); run_pk[bowler] += int(1); over_pk[bowler] += int(1)
							else:
								remark = re.search(f"{batsman},\sleg\sbyes,\s((1\srun)|[2-4]runs|FOUR),", para)
								if remark:
									typ = (remark[0].split(','))[1].strip()
									skore = ((remark[0].split(',')[2]).strip()); over_pk[bowler] += int(1)
									if typ == "byes":                                    
										if skore == "FOUR":
											i_sc += int(4); cur_run_in += int(4); run_pk[bowler] += int(4)
											b_i += int(4)
										if skore == "1 run":
											i_sc += int(1); cur_run_in += int(1); run_pk[bowler] += int(1)
											b_i += int(1)
										if skore == "2 run":
											i_sc += int(2); cur_run_in += int(2); run_pk[bowler] += int(2)
											b_i += int(2)
										if skore == "3 run":
											i_sc += int(3); cur_run_in += int(3); run_pk[bowler] += int(3)
											b_i += int(3)
									else:                                   
										if skore == "FOUR":
											i_sc += int(4); cur_run_in += int(4); run_pk[bowler] += int(4)
											lb_i += int(4)    
										if skore == "1 run":
											i_sc += int(1); cur_run_in += int(1); run_pk[bowler] += int(1)
											lb_i += int(1)
										if skore == "2 run":
											i_sc += int(2); cur_run_in += int(2); run_pk[bowler] += int(2)
											lb_i += int(2)    
										if skore == "3 run":
											i_sc += int(3); cur_run_in += int(3); run_pk[bowler] += int(3)
											lb_i += int(3)    
								else:
									remark = re.search(f"{batsman},\s(out Caught by)(\s\w[a-z]*)*", para)
									if remark:
										act = (remark[0].split(","))[1].split("by")[1].strip()
										wkts_i += int(1); wicket_pk[bowler] += int(1)
										retby_in[batsman] = f"c by {act} b {bowler}"; fall_in += (f"{cur_run_in}-{wkts_i}({batsman},{m[0]}), ")
										balls_in[batsman] += int(1); over_pk[bowler] += int(1)
									else:
										print(f"this {m[0]}")
										print(remark[0])
		if m[0] == "5.6":
			pwr_run_in = cur_run_in
	ov_i = m[0]
	for batsman in team_in:
		runs_i += run_bat_in[batsman]
	runs_i += i_sc                          






scorecard()

#This shall be the last lines of the code.
end_time = datetime.now()
print('Duration of Program Execution: {}'.format(end_time - start_time))
