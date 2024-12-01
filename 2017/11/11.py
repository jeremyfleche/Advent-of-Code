with open("input.txt") as f:
	texte = f.read().strip()

texte = "ne,ne,s,s"
L = texte.split(',')

def adjacent(s1, s2):
	direction = {'n':0,'ne':1,'se':2,'s':3,'sw':4,'nw':5}
	return

def algo(L):
	P = [L[0]]
	for s in L[1:]:

					
	return len(P)

print(algo(L))