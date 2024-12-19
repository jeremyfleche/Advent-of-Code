import time
START_TIME = time.time()

with open("input.txt") as f:
	texte = f.read().strip()

def part1(towels, patterns):
	cache = {}
	def isPossible(towel):
		if towel == "":
			return True
		if towel in cache:
			return cache[towel]
		res = False
		for p in patterns:
			n = len(p)
			if n <= len(towel) and p == towel[:n]:
				res = res or isPossible(towel[n:])
		cache[towel] = res
		return res

	return sum(isPossible(towel) for towel in towels)

def part2(towels, patterns):
	cache = {}
	def possibility(towel):
		if towel in cache:
			return cache[towel]
		if towel == "":
			return 1
		res = 0
		for p in patterns:
			n = len(p)
			if n <= len(towel) and p == towel[:n]:
				res += possibility(towel[n:])
		cache[towel] = res
		return res
	
	return sum(possibility(towel) for towel in towels)

patterns = texte.split("\n\n")[0].split(", ")
towels = texte.split("\n\n")[1].splitlines()

print("Partie 1 :", part1(towels, patterns))
print("Partie 2 :", part2(towels, patterns))

print(f"[{int((time.time()-START_TIME)*1000)}ms]")