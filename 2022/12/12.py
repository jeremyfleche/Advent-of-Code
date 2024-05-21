from math import inf

with open('input.txt','r') as f:
	texte = f.read()



S = (0,0)
E = (0,0)

t = [[i for i in j] for j in texte.split()]

for i in range(len(t)):
	for j in range(len(t[i])):
		if t[i][j] == 'E':
			E = (i,j)
		if t[i][j] == 'S':
			S = (i,j)

t = [[ord(i)-ord('a')+1 for i in j] for j in texte.split()]
t[S[0]][S[1]] = 0
t[E[0]][E[1]] = 26

def Q():
	global t
	Q = []
	for i in range(len(t)):
		for j in range(len(t[i])):
			Q.append((i,j))
	return Q

def initialisation(s_debut):
	global t
	d=dict()
	for i in range(len(t)):
		for j in range(len(t[i])):
			d[(i,j)] = inf
	d[s_debut] = 0
	return d

def minimum(q,d):
	mini = inf
	sommet = -1
	for i in q:
		if d[i] <= mini:
			mini = d[i]
			sommet = i
	return sommet

def maj_dictance(d,s1,s2):
	try:
		if d[s2] > d[s1] + 1:
			d[s2] = d[s1] + 1
	except:
		pass

def Dijkstra(S):
	global E
	global t
	d = initialisation(S)
	q = Q()
	while q:					# signifie : tant que q n'est pas une liste vide
		s1 = (minimum(q, d))
		q.remove(s1)
		for s2 in [(s1[0]+1,s1[1]),(s1[0],s1[1]+1),(s1[0]-1,s1[1]),(s1[0],s1[1]-1)]:
			try:
				if t[s1[0]][s1[1]] >= t[s2[0]][s2[1]] or t[s1[0]][s1[1]] == t[s2[0]][s2[1]] - 1:
					maj_dictance(d,s1,s2)
			except:
				pass

	return d[E]

print('Partie 1 :',Dijkstra(S))

mini = inf
for i in range(len(t)):
	for j in range(len(t[i])):
		if j == 0:						# les seuls a qui peuvent sortir de leur position se trouvent sur la première colonne
			temp = Dijkstra((i,j))
			if temp < mini:
				mini = temp

print('Partie 2 :',mini) # attendre environ 35 secondes pour le résultat (pas trop optimisé 🙄)
