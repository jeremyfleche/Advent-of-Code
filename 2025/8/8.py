import time
from mymodules.aoc import *
from collections import deque
import os
from mymodules.structures import UnionFind

os.chdir(os.path.dirname(__file__))

START_TIME = time.time()

texte = read_input("input")

lines = mapped_matrix(texte, ",")

def distance(b1, b2):
	a,b,c = b1
	d,e,f = b2
	return (abs(a-d)**2+abs(b-e)**2+abs(c-f)**2)**(1/2)

distances = {}
for i in range(len(lines)):
	for j in range(i+1,len(lines)):
		distances[(i,j)] = distance(lines[i], lines[j])

sorted_by_distance = sorted(distances, key=lambda x: distances[x])

def solve():
	UF = UnionFind()
	wire = 0
	while UF.count != 1 or UF.total_elements != len(lines):
		w1, w2 = sorted_by_distance[wire]
		UF.union(w1, w2)
		wire += 1
		if wire == 1000:
			sizes = list(sorted(UF.size.values()))
			res1 = sizes[-1]*sizes[-2]*sizes[-3]
	return res1, lines[w1][0]*lines[w2][0]
			

res1, res2 = solve()
print("Partie 1 :", res1)
print("Partie 2 :", res2)

print(f"[{int((time.time()-START_TIME)*1000)}ms]")
