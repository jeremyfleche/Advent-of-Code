with open('input.txt','r') as f:
	texte = f.read()

t = [i.split() for i in texte.split('\n') if i!='']

def ajust(H, T):
	dx = abs(H[0]-T[0])
	dy = abs(H[1]-T[1])
	if dx > 1 and dy > 1:
		T = (H[0]-1 if T[0]<H[0] else H[0]+1, H[1]-1 if T[1]<H[1] else H[1]+1)
	elif dx > 1:
		T = (H[0]-1 if T[0]<H[0] else H[0]+1, H[1])
	elif dy > 1:
		T = (H[0] , H[1]-1 if T[1]<H[1] else H[1]+1 )
	return T

X = {'L':-1,'R':1,'U':0,'D':0}
Y = {'L':0,'R':0,'U':-1,'D':1}
H = (0,0)
T = [(0,0) for _ in range(9)]
P1 = set()
P2 = set()
for ligne in t:
	direction,valeur = ligne
	valeur = int(valeur)
	for _ in range(valeur):
		H = (H[0]+X[direction],H[1]+Y[direction])
		T[0] = ajust(H, T[0])
		for i in range(1,9):
			T[i] = ajust(T[i-1], T[i])
		P1.add(T[0])
		P2.add(T[8])

print('Partie 1 :',len(P1))
print('Partie 2 :',len(P2))