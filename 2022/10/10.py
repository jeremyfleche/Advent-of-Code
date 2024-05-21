with open('input.txt','r') as f:
	texte = f.read()

liste = [i.split(' ') for i in texte.split('\n') if i!='']

def fonction(X, t):
	global res
	global afficheur
	t1 = t-1
	afficheur[t1//40][t1%40] = ('#' if abs(X-(t1%40))<=1 else ' ')
	if t in [20, 60, 100, 140, 180, 220]:
	    res += X*t

afficheur = [['?' for _ in range(40)] for _ in range(6)]
t = 0
X = 1
res = 0
for ligne in liste:
	if ligne[0] == 'noop':
		t += 1
		fonction(X, t)
	elif ligne[0] == 'addx':
		t += 1
		fonction(X, t)
		t += 1
		fonction(X, t)
		X += int(ligne[1])


print('Partie 1 :',res)
print('Partie 2 :')
for r in range(6):
    print(''.join(afficheur[r]))