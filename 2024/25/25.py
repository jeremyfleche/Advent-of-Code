import time
START_TIME = time.time()

with open("input.txt") as f:
	texte = f.read().strip()

def heights(s):
	h = len(s)
	w = len(s[0])
	res = []
	for j in range(w):
		c = 0
		for i in range(h):
			if s[i][j] == '#':
				c += 1
		res.append(c-1)
	return res

temp = texte.split('\n\n')
keys = []
locks = []
for x in temp:
	y = [[j for j in i] for i in x.splitlines()]

	if y[0] == ['#']*len(y[0]):
		locks.append(heights(y))
	else:
		keys.append(heights(y))

def fit(lock, key):
	H = 7
	for i in range(len(lock)):
		if lock[i]+key[i]+2 > H:
			return False
	return True

res = 0
for key in keys:
	for lock in locks:
		if fit(lock, key):
			res += 1

print("Réponse :",res)
# != 58881
print(f"[{int((time.time()-START_TIME)*1000)}ms]")