import time
import re
from aoc import *

START_TIME = time.time()

texte = read_input("input.txt")

# texte = """123 328  51 64 
#  45 64  387 23 
#   6 98  215 314
# *   +   *   + """

L = []
for i,line in enumerate(texte.splitlines()):
	L.append([])
	for e in line.split(" "):
		if e != "":
			L[i].append(e)

def part1():
	res = [0 if L[-1][j] == "+" else 1 for j in range(len(L[-1]))]


	for i in range(len(L)-1):
		for j in range(len(L[i])):
			if not L[i][j].isdigit():
				continue
			if L[-1][j] == "+":
				res[j] += int(L[i][j])
			else:
				res[j] *= int(L[i][j])
	return sum(res)

print("Partie 1 :",part1())

L = [[e for e in line] for line in texte.splitlines()]


def part2():
	res = ["" for j in range(len(L[0]))]

	for i in range(len(L)-1):
		for j in range(len(L[0])):
				res[j] += L[i][j]

	somme = 0
	i = 0
	j = 0
	while i < len(res):
		temp = 0 if L[-1][i] == "+" else 1
		j = 0
		op = L[-1][i]
		while i+j < len(res) and res[i+j].strip().isdigit():
			if op == "+":
				temp += int(res[i+j].strip())
			else:
				temp *= int(res[i+j].strip())
			j += 1
		i += j + 1
		somme += temp
	return somme

print("Partie 2 :",part2())

print(f"[{int((time.time()-START_TIME)*1000)}ms]")