from itertools import permutations
from math import inf

fichier=open('input.txt','r')
texte=fichier.read()
fichier.close()

temp=''
ligne=[]
t=[]
for i in texte:
	if i=='\n':
		t.append(ligne)
		ligne=[]
	elif i==' ' or i=='.':
		ligne.append(temp)
		temp=''
	else:
		temp+=i

L=[]
for ligne in t:
	temp=[]
	temp.append(ligne[0])
	if ligne[2]=='gain':
		temp.append(int(ligne[3]))
	else:
		temp.append(-int(ligne[3]))
	temp.append(ligne[len(ligne)-1])
	L.append(temp)



personnes=[]
for ligne in L:
	if ligne[0] not in personnes:
		personnes.append(ligne[0])
	if ligne[len(ligne)-1] not in personnes:
		personnes.append(ligne[len(ligne)-1])



bonheur={}
for personne in personnes:
	bonheur[personne]={}
	for ligne in L:
		if ligne[0]==personne:
			bonheur[personne][ligne[len(ligne)-1]]=ligne[1]

tables=list(permutations(personnes))

res=-inf
for table in tables:
	temp=0
	for i in range(len(table)):
		temp+=bonheur[table[i]][table[(i+1)%len(table)]]
		temp+=bonheur[table[i]][table[(i-1)%len(table)]]
	if temp>res:
		res=temp

print(f'Partie 1 : {res}')


# Partie 2

for personne in bonheur:
	bonheur[personne]['Moi']=0
bonheur['Moi']={}
for personne in bonheur:
	bonheur['Moi'][personne]=0

personnes.append('Moi')

tables=list(permutations(personnes))

res=-inf
for table in tables:
	temp=0
	for i in range(len(table)):
		temp+=bonheur[table[i]][table[(i+1)%len(table)]]
		temp+=bonheur[table[i]][table[(i-1)%len(table)]]
	if temp>res:
		res=temp

print(f'Partie 2 : {res}')

