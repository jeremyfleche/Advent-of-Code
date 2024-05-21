from itertools import combinations

with open('input.txt','r') as f:
	texte=f.read()

t=[i.split(' ') for i in texte.split('\n') if i!='']

res1 = 0
res2 = 0
for ligne in t:
	bot,me = ligne

	res1 += {'X':1, 'Y':2, 'Z':3}[me]
	res1 += {('A', 'X') :3, ('A', 'Y') :6, ('A', 'Z') :0,
			('B', 'X') :0, ('B', 'Y') :3, ('B', 'Z') :6,
			('C', 'X') :6, ('C', 'Y') :0, ('C', 'Z') :3}[(bot,me)]

	res2 += {'X':0, 'Y':3, 'Z':6}[me]
	res2 += {('A', 'X') :3, ('A', 'Y') :1, ('A', 'Z') :2,
			('B', 'X') :1, ('B', 'Y') :2, ('B', 'Z') :3,
			('C', 'X') :2, ('C', 'Y') :3, ('C', 'Z') :1}[(bot,me)]

print('Partie 1 :',res1)
print('Partie 2 :',res2)