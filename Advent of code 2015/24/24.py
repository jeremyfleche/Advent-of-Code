with open('input.txt','r') as f:
	texte = f.read()
"""
texte = '''1
2
3
4
5
7
8
9
10
11'''
"""
t = sorted([int(i) for i in texte.strip().split('\n')])

poids = sum(t)//3

def taille_groupe(t):
	poids = sum(t)//3
	maxi = 0
	while sum(t[:maxi]) <= poids:
		maxi += 1
	temp = list(reversed(t))
	mini = 0
	while sum(temp[:mini]) <= poids:
		mini += 1
	return mini,maxi

