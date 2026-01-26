import time
from mymodules.aoc import *
from collections import deque
import os
os.chdir(os.path.dirname(__file__))

START_TIME = time.time()

texte = read_input("input")

a,b = texte.split("\n\n")

pattern = {int(line.split(":")[0]): [[eval(x) for x in c.split()] for c in line.split(":")[1].strip().split("|")] for line in a.splitlines()}
words = b.splitlines()


def generate_strings(rule):
	if (isinstance(rule, str)):
		return {rule}
	res = []
	for subrule in pattern[rule]:
		subresult = [""]
		for subrule_num in subrule:
			subsubresult = generate_strings(subrule_num)
			subresult = [s + r for s in subresult for r in subsubresult]
		res += subresult
	return res

words_0 = set(generate_strings(0))
res = 0
for w in words:
	if (w in words_0):
		res += 1
print("Partie 1 :", res)

print(f"[{int((time.time()-START_TIME)*1000)}ms]")
