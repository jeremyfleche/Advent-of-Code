with open("input.txt") as f:
	texte = f.read().strip()

rules, updates = texte.split("\n\n")
rules = [[int(j) for j in i.split('|')] for i in rules.splitlines()]
updates = [[int(j) for j in i.split(',')] for i in updates.splitlines()]

d = {}
for a, b in rules:
	d[a] = d[a]|{b} if a in d else {b}

def correct(line):
	cache = set()
	for i in line:
		if i in d and d[i] & cache != set():
			return False
		cache.add(i)
	return True

def sort(line):
	for i in range(len(line)-1, 0, -1):
		for j in range(i):
			if line[j+1] in d and line[j] in d[line[j+1]]:
				line[j], line[j+1] = line[j+1], line[j]
	return line

res1 = 0
res2 = 0
for line in updates:
	if correct(line):
		res1 += line[len(line)//2]
	else:
		line = sort(line)
		res2 += line[len(line)//2]

print("Partie 1 :",res1)
print("Partie 2 :",res2)