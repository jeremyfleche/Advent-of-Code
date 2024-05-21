from math import inf
from collections import deque

with open('input.txt','r') as f:
	texte = f.read()
"""
texte = '''Valve AA has flow rate=0; tunnels lead to valves DD, II, BB
Valve BB has flow rate=13; tunnels lead to valves CC, AA
Valve CC has flow rate=2; tunnels lead to valves DD, BB
Valve DD has flow rate=20; tunnels lead to valves CC, AA, EE
Valve EE has flow rate=3; tunnels lead to valves FF, DD
Valve FF has flow rate=0; tunnels lead to valves EE, GG
Valve GG has flow rate=0; tunnels lead to valves FF, HH
Valve HH has flow rate=22; tunnel leads to valve GG
Valve II has flow rate=0; tunnels lead to valves AA, JJ
Valve JJ has flow rate=21; tunnel leads to valve II'''
"""
#----------------------------------------------------------------------------------------------------------------------- formatage de l'input
t = [[j for j in i.split(' ')] for i in texte.split('\n')if i!='']

for ligne in range(len(t)):
	t[ligne] = [t[ligne][1],int(t[ligne][4][5:-1])]+[i[:-1] for i in t[ligne][9:-1]]+[t[ligne][-1]]
#-----------------------------------------------------------------------------------------------------------------------

#----------------------------------------------------------------------------------------------------------------------- Calcul distance entre deux valves
def init(s_debut):
	global t
	d = dict()
	q = []
	for ligne in t:
		d[ligne[0]] = inf
		q.append(ligne[0])
	d[s_debut] = 0
	return d,q

def minimum(q, d):
	mini = inf
	sommet = -1
	for i in q:
		if d[i] < mini:
			mini = d[i]
			sommet = i
	return sommet

def maj_dictance_min(d,s1,s2):
	try:
		if d[s2] > d[s1] + 1:
			d[s2] = d[s1] + 1
	except:
		pass

def chemins(t):
	d = dict()
	for ligne in t:
		d[ligne[0]] = []
		for i in range(2,len(ligne)):
			d[ligne[0]].append(ligne[i])
	return d

def distance(s1,s2):
	d,q = init(s1)
	c = chemins(t)
	while q:
		s1 = minimum(q,d)
		q.remove(s1)
		for i in c[s1]:
			maj_dictance_min(d,s1,i)
	return d[s2]
#-----------------------------------------------------------------------------------------------------------------------

def pression(t):
	pression = dict()
	for ligne in t:
		pression[ligne[0]] = ligne[1]
	return pression

def tunnels(t):
	res = dict()
	for ligne in t:
		res[ligne[0]]=[]
		for i in range(2,len(ligne)):
			res[ligne[0]].append(ligne[i])
	return res

p = pression(t)

non_vide = []
for i in tunnels(t):
	if p[i]!=0:
		non_vide.append(i)

valves = dict()
for i,valve in enumerate(non_vide):
	valves[valve] = i

dist = dict()
for i in tunnels(t):
	dist[i] = dict()
	for j in valves:
		dist[i][j] = distance(i,j)

cache = dict()
def solve(t,valve,opened):
	if (t,valve,opened) in cache:
		return cache[(t,valve,opened)]
	best = 0
	for voisin in dist[valve]:
		temp = 1 << valves[voisin]
		if opened & temp:
			continue
		t_restant = t - dist[valve][voisin] - 1
		if t_restant <= 0:
			continue
		best = max(best,solve(t_restant,voisin,opened|temp)+p[voisin]*t_restant)

	cache[(t,valve,opened)] = best
	return best

print('Partie 1 :',solve(30,'AA',0))

opended = (1 << len(non_vide)) - 1

best = 0
for i in range((opended+1)//2):
	best = max(best, solve(26,'AA',i) + solve(26,'AA',opended^i))

print('Partie 2 :',best)