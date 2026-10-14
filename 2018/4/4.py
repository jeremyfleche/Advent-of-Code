import time
from mymodules.aoc import *
from collections import deque
import os
os.chdir(os.path.dirname(__file__))

START_TIME = time.time()

texte = sorted(read_input("input").splitlines())

d = {}
current_id = 0
start_sleep = 0

for line in texte:
	temp = line.split()
	if temp[2] == "Guard":
		current_id = int(temp[3][1:])
		if current_id not in d:
			d[current_id] = []
	elif temp[2] == "falls":
		d[current_id].append(int(temp[1][3:5]))
	else:
		start_sleep = d[current_id][-1]
		end_sleep = int(temp[1][3:5])
		total = end_sleep - start_sleep
		d[current_id][-1] = [start_sleep, total]

total_max = 0
id_max = 0

for id in d:
	total = sum([i[1] for i in d[id]])
	if total > total_max:
		total_max = total
		id_max = id

minutes = {}
for id in d:
	minutes[id] = {}
	for start, duree in d[id]:
		for i in range(start, start+duree):
			minutes[id][i] = minutes[id].get(i,0)+1


max_minute = 0
minute = 0
for m in minutes[id_max]:
	if minutes[id_max][m] > max_minute:
		max_minute = minutes[id_max][m]
		minute = m

res1 = id_max * minute
print("Part 1 :", res1)

id_max = 0
minute_max = 0
maxi = 0

for id in d:
	for m in minutes[id]:
		if minutes[id][m] > maxi:
			maxi = minutes[id][m]
			id_max = id
			minute_max = m

res2 = id_max * minute_max
print("Part 2 :", res2)

print(f"[{int((time.time()-START_TIME)*1000)}ms]")
