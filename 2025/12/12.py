import time
from mymodules.aoc import *
from collections import deque
import os
os.chdir(os.path.dirname(__file__))

START_TIME = time.time()

texte = read_input("input")

temp = texte.split("\n\n")
regions = []
for a in temp[-1].splitlines():
	b,c = a.split(':')
	dimensions = list(map(int,b.strip().split("x")))
	quantities = list(map(int,c.strip().split()))
	regions.append((list(map(int,b.strip().split("x"))), list(map(int,c.strip().split()))))

res = 0
for dimensions,quantities in regions:
	total_present = sum(quantities) 
	if dimensions[0]*dimensions[1] >= total_present*9:
		res += 1

print(res)

print(f"[{int((time.time()-START_TIME)*1000)}ms]")