import time
from aoc import *
from collections import deque
import os
os.chdir(os.path.dirname(__file__))

START_TIME = time.time()

texte = read_input("input.txt")

grille = matrix(texte)

def initial_beam(grille):
	for i in range(len(grille)):
		for j in range(len(grille)):
			if grille[i][j] == 'S':
				return i+1, j

def solve1(grille):
	beams = [initial_beam(grille)]
	SEEN = set()
	res = 0
	while beams:
		y,x = beams.pop()
		if (y,x) in SEEN or y == len(grille)-1:
			continue
		if grille[y+1][x] == '.':
			beams.append((y+1,x))
		else:
			res += 1
			beams.append((y+1, x+1))
			beams.append((y+1, x-1))
		SEEN.add((y,x))
	return res

def solve2(grille):
	ys,xs = initial_beam(grille)
	beams = deque([(ys,xs)])
	ways = {(ys,xs):1}
	SEEN = set()
	while beams:
		y,x = beams.popleft()
		if (y,x) in SEEN or y == len(grille)-1:
			continue
		if grille[y+1][x] == '.':
			beams.append((y+1,x))
			ways[(y+1,x)] = ways.get((y+1, x), 0) + ways[(y,x)]
		else:
			ways[(y+1,x-1)] = ways.get((y+1, x-1), 0) + ways[(y,x)]
			beams.append((y+1, x+1))
			
			ways[(y+1,x+1)] = ways.get((y+1, x+1), 0) + ways[(y,x)]
			beams.append((y+1, x-1))

		SEEN.add((y,x))

	return sum([ways.get((len(grille)-1, x), 0) for x in range(len(grille[0]))])

print("Partie 1 :",solve1(grille))
print("Partie 2 :",solve2(grille))
print(f"[{int((time.time()-START_TIME)*1000)}ms]")