with open("input.txt") as f:
	texte = f.read().strip().splitlines()

L = [i.split() for i in texte]

def iemeChiffre(n, i):
	return n//(10**i)%10

def algo(MONAD):
	i = 0
	d = {'w':0, 'x':0, 'y':0, 'z':0}
	for line in L:
		if line[0] == "inp":
			d[line[1]] = iemeChiffre(MONAD, i)
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

cache = {}
n = (10**14)-12
lc = 0
while True:
	MONAD -= 1
	for i in range(14):
		if iemeChiffre(MONAD, i) == 0:
			MONAD -= 10**i
	return MONAD