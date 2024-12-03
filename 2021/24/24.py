with open("input.txt") as f:
	texte = f.read().strip().splitlines()

L = [i.split() for i in texte]

def instructions(MONAD):
	i = 0
	d = {'w':0, 'x':0, 'y':0, 'z':0}
	for line in L:
		if line[0] == "inp":
			d[line[1]] = MONAD[i]
			i += 1
		elif line[0] == "add":
			b = d[line[2]] if line[2] in d else int(line[2])
			d[line[1]] += b
		elif line[0] == "mul":
			b = d[line[2]] if line[2] in d else int(line[2])
			d[line[1]] *= b
		elif line[0] == "div":
			b = d[line[2]] if line[2] in d else int(line[2])
			if b == 0:
				return -1
			d[line[1]] //= b
		elif line[0] == "mod":
			b = d[line[2]] if line[2] in d else int(line[2])
			if b == 0:
				return -1
			d[line[1]] %= b
		else:
			d[line[1]] = 1 if d[line[1]] == (d[line[2]] if line[2] in d else int(line[2])) else 0
	return d['z']

def algo(MONAD):
	print(len(cache))
	if MONAD in cache:
		return cache[MONAD], MONAD
	if len(MONAD) == 14:
		z = instructions(MONAD)
		cache[MONAD] = z==0
		return cache[MONAD], MONAD
	for i in range(9, 0, -1):
		new_MONAD = MONAD + (i,)
		temp, M = algo(new_MONAD)
		if temp:
			cache[MONAD] = True 
			return True, MONAD
	cache[MONAD] = False
	return False, MONAD

cache = {}
print(algo(tuple()))