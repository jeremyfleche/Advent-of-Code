from math import inf
from collections import deque

with open('input.txt','r') as f:
	texte = f.read()
"""
texte = '''
e => H
e => O
H => HO
H => OH
O => HH

HOHOHO
'''
"""
texte = texte.strip().split('\n\n')

temp = texte[0].split('\n')
temp = [ligne.split(' => ') for ligne in temp]

d = dict()
for ligne in temp:
	if ligne[0] in d:
		d[ligne[0]].append(ligne[1])
	else:
		d[ligne[0]] = [ligne[1]]

molecule = []
temp = ''
for i in texte[1]:
	if i.isupper() and temp != '':
		molecule.append(temp)
		temp = str(i)
	else:
		temp += i
if temp != '':
	molecule.append(temp)

def liste_to_str(liste):
	res = ''
	for i in liste:
		res += i
	return res

E = set()
for i in range(len(molecule)):
	try:
		for j in d[molecule[i]]:
			temp = molecule[:i] + [j] + molecule[i+1:]
			E.add(liste_to_str(temp))
	except:
		pass

print('Partie 1 :',len(E))

#Partie 2

def str_to_liste(element):
	res = []
	temp = ''
	for i in element:
		if i.isupper() and temp != '':
			res.append(temp)
			temp = str(i)
		else:
			temp += i
	if temp != '':
		res.append(temp)

	return res

d2 = dict()
for element in d:
	for i in d[element]:
		d2[i] = element

atomes = list(d2.keys())
for _ in range(len(atomes)-1):
	for i in range(len(atomes)-1):
		if len(atomes[i]) < len(atomes[i+1]):
			atomes[i],atomes[i+1] = atomes[i+1],atomes[i]

def minimum(q):
	mini = inf
	for i in q:
		if len(i) < mini:
			mini = len(i)
			res = i
	return res

def tri(q):
	for _ in range(len(q)-1):
		for i in range(len(q)-1):
			if len(q[i]) < len(q[i+1]):
				q[i],q[i+1] = q[i+1],q[i]

L = set()
molecule = texte[1]
q = deque([molecule])
while 'e' not in molecule:
	tri(q)
	s = q.popleft()
	print(s)
	for atome in atomes:
		i = s.find(atome)
		if i == -1:
			continue
		q.append(s[:i] + d2[atome] + s[i+len(atome):])
		