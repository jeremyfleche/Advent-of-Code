from itertools import product

with open("input.txt") as f:
	texte = f.read().strip()

# texte = """???.### 1,1,3
# .??..??...?##. 1,1,3
# ?#?#?#?#?#?#?#? 1,3,1,6
# ????.#...#... 4,1,1
# ????.######..#####. 1,6,5
# ?###???????? 3,2,1"""

def nb_possibilites(s, pattern):
	if s == "":
		return 1 if pattern == () else 0
	if pattern == ():
		return 1 if "#" not in s else 0

	res = 0
	if s[0] in ".?":
		res += nb_possibilites(s[1:], pattern)
	if s[0] in "#?":
		if pattern[0] <= len(s) and "." not in s[:pattern[0]] and (len(s) == pattern[0] or s[pattern[0]] != "#"):
			res += nb_possibilites(s[pattern[0]+1:],pattern[1:])

	return res

res = 0
for ligne in texte.splitlines():
	s, temp = ligne.split()
	pattern = tuple(map(int, temp.split(",")))
	res += nb_possibilites(s, pattern)

print("Partie 1 :",res)

# Partie 2

cache = dict()

def nb_possibilites(s, pattern):
	if s == "":
		return 1 if pattern == () else 0
	if pattern == ():
		return 1 if "#" not in s else 0

	key = (s,pattern)
	if key in cache:
		return cache[key]

	res = 0
	if s[0] in ".?":
		res += nb_possibilites(s[1:], pattern)
	if s[0] in "#?":
		if pattern[0] <= len(s) and "." not in s[:pattern[0]] and (len(s) == pattern[0] or s[pattern[0]] != "#"):
			res += nb_possibilites(s[pattern[0]+1:],pattern[1:])
			
	cache[key] = res
	return res

res = 0
for ligne in texte.splitlines():
	s, temp = ligne.split()
	pattern = tuple(map(int, temp.split(",")))
	res += nb_possibilites("?".join([s]*5), pattern*5)

print("Partie 2 :",res)