import time
from mymodules.aoc import *
import os
os.chdir(os.path.dirname(__file__))

START_TIME = time.time()

texte = read_input("input")

G = {}
for line in texte.splitlines():
	x, temp = line.split(':')
	G[x] = []
	for voisin in temp.strip().split():
		G[x].append(voisin)

def solve():
	d = {}
	def chemin(a,b):
		if a == b:
			return 1
		if (a,b) in d:
			return d[(a,b)]
		d[(a,b)] = sum([chemin(v,b) for v in G.get(a, [])])
		return d[(a,b)]

	a = chemin("svr", "fft") * chemin("fft", "dac") * chemin("dac", "out")
	b = chemin("svr", "dac") * chemin("dac", "fft") * chemin("fft", "out")

	return chemin("you", "out"), a + b

res1, res2 = solve()
print("Partie 1 :", res1)
print("Partie 2 :", res2)
print(f"[{int((time.time()-START_TIME)*1000)}ms]")
