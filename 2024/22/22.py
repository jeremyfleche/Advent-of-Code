import time
START_TIME = time.time()

with open("input.txt") as f:
	texte = f.read().strip()

# texte = """1
# 2
# 3
# 2024"""

def prune(x):
	return x % 16777216

def mix(x, secret_number):
	return x ^ secret_number

def part1():
	L = [int(i) for i in texte.splitlines()]
	res = 0
	for i in L:
		temp = 0
		for _ in range(2000):
			# print(i%10)
			i = prune(mix(i, i*64))
			i = prune(mix(i, i//32))
			i = prune(mix(i, i*2048))
		res += i
	return res

def bananas(buyer,sequence):
	i = 0
	for j in range(1, len(buyer)):
		if buyer[j]-buyer[j-1] == sequence[i]:
			i += 1
		else:
			i = 0
		if i>3:
			return buyer[j]
	return 0

def part2():
	L = [int(i) for i in texte.splitlines()]
	M = []
	for i in L:
		temp = [i%10]
		for _ in range(2000):
			i = prune(mix(i, i*64))
			i = prune(mix(i, i//32))
			i = prune(mix(i, i*2048))
			temp.append(i%10)
		M.append(temp)
	cache = {}
	for i, buyer in enumerate(M):
		cache[i] = {}
		sequence = [buyer[j]-buyer[j-1] for j in range(1,5)]
		cache[i][tuple(sequence)] = buyer[4]
		for j in range(5, len(buyer)):
			sequence = sequence[1:] + [buyer[j]-buyer[j-1]]
			if tuple(sequence) not in cache[i]:
				cache[i][tuple(sequence)] = buyer[j]
	return max(sum(cache[i].get((a,b,c,d),0) for i in range(len(M))) for a in range(-9,10) for b in range(-9,10) for c in range(-9,10) for d in range(-9,10))

print("Partie 1 :", part1())
print("Partie 2 :", part2()) # ~90s avec pypy3
print(f"[{int((time.time()-START_TIME)*1000)}ms]")