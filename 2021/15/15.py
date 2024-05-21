from math import inf

with open('input.txt','r') as f:
	texte = f.read()

t = [[int(i) for i in j] for j in texte.split()]

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

def minimum(Q,d):
	mini = inf
	sommet = -1
	for i in Q:
		if d[i] < mini:
			mini = d[i]
			sommet = i
	return sommet

def maj_dictance(d,s1,s2):
	try:
		if d[s2] > d[s1] + t[s2[0]][s2[1]]:
			d[s2] = d[s1] + t[s2[0]][s2[1]]
	except:
		pass

def Dijkstra():
	d = initialisation((0,0))
	q = Q()
	while len(q) != 0:
		s1 = minimum(q, d)
		q.remove(s1)
		for s2 in [(s1[0]+1,s1[1]),(s1[0],s1[1]+1)]:
			maj_dictance(d,s1,s2)
	return d

d = Dijkstra()
print('Partie 1 :',d[(len(t)-1,len(t[0])-1)])

#Partie 2

def ajoute(t, a):
	for i in range(len(t)):
		for j in range(len(t[i])):
			t[i][j] = (t[i][j]+a)%10
	return t

liste = [[0 for _ in range(5*len(t[0]))] for _ in range(5*len(t))]

