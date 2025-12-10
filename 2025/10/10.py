import time
from mymodules.aoc import *
import z3
import os
os.chdir(os.path.dirname(__file__))

START_TIME = time.time()

texte = read_input("input")

# texte = """[.##.] (3) (1,3) (2) (2,3) (0,2) (0,1) {3,5,4,7}
# [...#.] (0,2,3,4) (2,3) (0,4) (0,1,2) (1,2,3,4) {7,5,12,7,2}
# [.###.#] (0,1,2,3,4) (0,3,4) (0,1,2,4,5) (1,2) {10,11,11,5,10,5}"""

machines = []
for line in texte.splitlines():
	a,b,c = (line.split()[0][1:-1], line.split()[1:-1], line.split()[-1][1:-1])
	temp_a = [(0 if i=="." else 1) for i in a]
	temp_b = tuple((eval(i) if not isinstance(eval(i), int) else (eval(i),)) for i in b)
	temp_c = eval('[' + c + ']')
	machines.append((temp_a, temp_b, temp_c))

def solve1(goal, buttons, indicators_length):

	def toogle(indicators, button, n):
		for i in button:
			indicators ^= (1 << (n-i-1))
		return indicators

	def nb_press(indicators, buttons):

		if indicators == goal:
			return 0

		if buttons == tuple():
			return float("inf")

		no_press = nb_press(indicators, buttons[1:])
		press = 1 + nb_press(toogle(indicators, buttons[0], indicators_length), buttons[1:])

		return min(no_press, press)

	def dec(indicators):
		res = 0
		for i in indicators:
			res = (res<<1) + i
		return res

	goal = dec(goal)
	return nb_press(0, buttons)

def solve2(goal, buttons):
		
	variables = [z3.Int(f"b{i}") for i in range(len(buttons))]
	equations = []
	for i in range(len(goal)):
		line = []
		for j in range(len(buttons)):
			if i in buttons[j]:
				line.append(variables[j])
		eq = (sum(line) == goal[i])
		equations.append(eq)

	o = z3.Optimize()
	o.minimize(sum(variables))
	for eq in equations:
		o.add(eq)
	for v in variables:
		o.add(v >= 0)

	o.check()
	M = o.model()
	res = 0
	for d in M.decls():
		res += M[d].as_long()

	return res

res1 = 0
res2 = 0
for light_goal, buttons, counters_goal in machines:
	res1 += solve1(light_goal, buttons, len(light_goal))
	res2 += solve2(counters_goal, buttons)

print("Partie 1 :", res1)
print("Partie 2 :", res2)

print(f"[{int((time.time()-START_TIME)*1000)}ms]")
