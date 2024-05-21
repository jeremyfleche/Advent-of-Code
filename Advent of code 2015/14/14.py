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
	temp.append(int(ligne[3]))
	temp.append(int(ligne[6]))
	temp.append(int(ligne[len(ligne)-2]))
	L.append(temp)


def division_euclidienne(a,b):
	q=a//b
	r=a-b*q
	return q,r

def distance(L):
	temps_final=2503
	q,r=division_euclidienne(temps_final,L[2]+L[3])
	if r>=L[2]:
		return L[1]*L[2]*(q+1)
	else:
		return L[1]*L[2]*q+r*L[1]
	

res=-inf
for ligne in L:
	if distance(ligne)>res:
		res=distance(ligne)

print(f'Partie 1 : {res}')

#Partie 2

def distance2(L,temps_final):
	q,r=division_euclidienne(temps_final,L[2]+L[3])
	if r>=L[2]:
		return L[1]*L[2]*(q+1)
	else:
		return L[1]*L[2]*q+r*L[1]

temps_final=0
t=[]
while temps_final!=2503:
	temps_final+=1
	res=-inf
	renne=''
	for ligne in L:
		if distance2(ligne,temps_final)>res:
			res=distance2(ligne,temps_final)
			renne=ligne[0]
	t.append(renne)

d={}
for ligne in L:
	d[ligne[0]]=0

for renne in t:
	d[renne]+=1

res=-inf
for renne in d:
	if d[renne]>res:
		res=d[renne]

print(f'Partie 2 : {res}')