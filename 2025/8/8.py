import time
from aoc import *
from collections import deque
import os
os.chdir(os.path.dirname(__file__))

START_TIME = time.time()

texte = read_input("input")

L = [tuple(map(int,line)) for line in matrix(texte, ",")]

def distance(b1, b2):
	a,b,c = b1
	d,e,f = b2
	return (abs(a-d)**2+abs(b-e)**2+abs(c-f)**2)**(1/2)

d = {}
for i in range(len(L)):
	for j in range(i+1,len(L)):
		d[(i,j)] = distance(L[i], L[j])

sorted_distance = sorted(d, key=lambda kv: d[kv])

def solve1():
	circuits = []
	for i in range(1000):
		a,b = sorted_distance[i]
		new_c = {a,b}
		new_circuits = [c for c in circuits]
		for c in circuits:
			if new_c & c != set():
				new_c |= c
				new_circuits.remove(c)
		circuits = new_circuits + [new_c]

	temp = list(sorted([len(c) for c in circuits]))
	return temp[-1]*temp[-2]*temp[-3]

def solve2():
	i = 0
	circuits = []
	while len(circuits) != 1 or (len(circuits) == 1 and len(circuits[0]) != len(L)):
		a,b = sorted_distance[i]
		new_c = {a,b}
		new_circuits = [i for i in circuits]
		for c in circuits:
			if new_c & c != set():
				new_c |= c
				new_circuits.remove(c)
		circuits = new_circuits + [new_c]
		i += 1
	return L[a][0]*L[b][0]

print("Partie 1 :", solve1())
print("Partie 2 :", solve2())
print(f"[{int((time.time()-START_TIME)*1000)}ms]")
