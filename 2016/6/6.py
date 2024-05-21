from math import inf

fichier=open('input.txt','r')
texte=fichier.read()
fichier.close()

t=[]
ligne=[]
for i in texte:
	if i=='\n':
		t.append(ligne)
		ligne=[]
	else:
		ligne.append(i)

def lettre_courante(liste):
	d=dict()
	for i in liste:
		if i not in d:
			d[i]=1
		else:
			d[i]+=1

	maximum=0
	for i in d:
		if d[i]>maximum:
			maximum=d[i]
			lettre_maximum=i

	return lettre_maximum

res=''
for j in range(len(t[0])):
	temp=[]
	for i in range(len(t)):
		temp.append(t[i][j])
	res+=lettre_courante(temp)

print(f'Partie 1 : {res}')

# Partie 2

def lettre_moins_courante(liste):
	d=dict()
	for i in liste:
		if i not in d:
			d[i]=1
		else:
			d[i]+=1

	minimum=inf
	for i in d:
		if d[i]<minimum:
			minimum=d[i]
			lettre_minimum=i

	return lettre_minimum

res=''
for j in range(len(t[0])):
	temp=[]
	for i in range(len(t)):
		temp.append(t[i][j])
	res+=lettre_moins_courante(temp)

print(f'Partie 2 : {res}')