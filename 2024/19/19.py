import time
START_TIME = time.time()

with open("input.txt") as f:
	texte = f.read().strip()

def isPossible(towel, patterns):
	Q = [towel]
	cache = set()
	while Q:
		remaining = Q.pop()
		if remaining == "":
			return True
		if remaining in cache:
			continue
		cache.add(remaining)
		for p in patterns:
			n = len(p)
			if n <= len(remaining):
				if p == remaining[:n]:
					Q.append(remaining[n:])
	return False

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
			if n <= len(towel):
				if p == towel[:n]:
					res += possibility(towel[n:])
		cache[towel] = res
		return res
	res = 0
	for i in towels:
		res += possibility(i)
	return res

patterns = texte.split("\n\n")[0].split(", ")
towels = texte.split("\n\n")[1].splitlines()

res1 = sum([isPossible(towel, patterns) for towel in towels])
print("Partie 1 :", res1)

res2 = part2(towels, patterns)
print("Partie 2 :", res2)

print(f"[{int((time.time()-START_TIME)*1000)}ms]")