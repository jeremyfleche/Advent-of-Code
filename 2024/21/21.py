import time
START_TIME = time.time()

from collections import deque
from itertools import product
from functools import cache, partial

def affichage_keypad(keypad):
	for j in range(len(keypad[0])):
		print("+---" if keypad[0][j]!=' ' else ' '*4, end="")
	print('+')
	for i in range(len(keypad)):	
		for j in range(len(keypad[i])):
			print(f"| {keypad[i][j]} " if keypad[i][j]!=' ' else ' '*4, end="")
		print("|")
		if i != len(keypad)-1:
			print("+---"*len(keypad[i])+'+')
	for j in range(len(keypad[-1])):
		print("+---" if keypad[-1][j]!=' ' else ' '*4, end="")
	print('+')

with open("input.txt") as f:
	texte = f.read().strip()

# texte = """029A
# 980A
# 179A
# 456A
# 379A"""

numeric_keypad = [['7','8','9'],['4','5','6'],['1','2','3'],[None,'0','A']]
directional_keypad = [[None,'^','A'],['<','v','>']]

def precompute(keypad):
	buttons = {}
	for i in range(len(keypad)):
		for j in range(len(keypad[i])):
			if keypad[i][j] is not None:
				buttons[keypad[i][j]] = (i,j)
	res = {}
	for start in buttons:
		for end in buttons:
			if start == end:
				res[(start,end)] = ["A"]
				continue
			paths = []
			Q = deque([(buttons[start], "")])
			dist = float("inf")
			while Q:
				(l,c), move = Q.popleft()
				for nl, nc, new_move in [(l-1,c,'^'),(l+1,c,'v'),(l,c-1,'<'),(l,c+1,'>')]:
					if not (0<=nl<len(keypad) and 0<=nc<len(keypad[0])) or keypad[nl][nc] is None:
						continue
					if keypad[nl][nc] == end:
						if dist < len(move) + 1:
							break
						dist = len(move) + 1
						paths.append(move+new_move+'A')
					else:
						Q.append(((nl,nc), move+new_move))
				else:
					continue
				break
			res[(start,end)] = paths
	return res

def combinaisons(seq, precomputed_paths):
	seqs = [precomputed_paths[(x, y)] for x, y in zip("A" + seq, seq)]
	return ["".join(x) for x in product(*seqs)]

num_PC = precompute(numeric_keypad)
dir_PC = precompute(directional_keypad)
paths_lengths = {key: len(value[0]) for key, value in dir_PC.items()}
codes = texte.splitlines()

@cache
def algo(seq, depth):
	if depth == 1:
		return sum(paths_lengths[(i,j)] for i,j in zip('A'+seq, seq))
	res = 0
	for i, j in zip('A'+seq, seq):
		res += min(algo(x, depth-1) for x in dir_PC[(i,j)])
	return res

def solve():
	res1, res2 = 0, 0
	algo1 = partial(algo, depth=2)
	algo2 = partial(algo, depth=25)
	for code in codes:
		robot = combinaisons(code, num_PC)
		temp1 = min(map(algo1, robot))
		temp2 = min(map(algo2, robot))
		res1 += temp1 * int(code[:-1])
		res2 += temp2 * int(code[:-1])
	return res1, res2

res1, res2 = solve()
print("Partie 1 :", res1)
print("Partie 2 :", res2)

print(f"[{int((time.time()-START_TIME)*1000)}ms]")