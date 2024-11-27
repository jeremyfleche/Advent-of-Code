with open("input.txt") as f:
	texte = f.read().strip()

texte = "ne,ne,ne"
L = texte.split(',')

def get(s,i):
	try:
		return s[i]
	except:
		return -1

def algo(L):
	P = []
	res = 1
	P = [L[0]]
	for d in L[1:]:
		print(P,res)
		if P[-1][0] != d[0]:
			res -= 1
			P.pop()
		else:
			res += 1
			P.append(d)
	return len(P)

print(algo(L))