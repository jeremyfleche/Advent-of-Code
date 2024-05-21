from itertools import permutations
from math import inf

fichier=open('input.txt','r')
texte=fichier.read()
fichier.close()

t=[]
ligne=[]
mot=''
for i in texte:
	if i=='\n':
		ligne.append(mot)
		mot=''
		t.append(ligne)
		ligne=[]
	elif i==' ':
		ligne.append(mot)
		mot=''
	else:
		mot+=i

for ligne in t:
	ligne[4]=int(ligne[4])
	del ligne[3]
	del ligne[1]

villes=[]
for ligne in t:
	for i in range(2):
		if ligne[i] not in villes:
			villes.append(ligne[i])

def chemins_possibles(ville):
	global t
	res=[]
	for ligne in t:
		if ligne[0]==ville:
			res.append((ligne[1],ligne[2]))
		if ligne[1]==ville:
			res.append((ligne[0],ligne[2]))
	return res

graphe={}
for ville in villes:
	graphe[ville]={}
	for i in chemins_possibles(ville):
		graphe[ville][i[0]]=i[1]



routes=list(permutations(villes))

res=inf
for chemin in routes:
	x=0
	for i in range(1,len(chemin)):
		x+=graphe[chemin[i-1]][chemin[i]]
	if x<res:
		res=x

print(f'Partie 1 : {res}') #Cela marche car chaque ville est reliée à toutes les autres villes

routes=list(permutations(villes))

#Partie 2

res=0
for chemin in routes:
	x=0
	for i in range(1,len(chemin)):
		x+=graphe[chemin[i-1]][chemin[i]]
	if x>res:
		res=x

print(f'Partie 2 : {res}')