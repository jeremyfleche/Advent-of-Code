fichier=open('input.txt','r')
texte=fichier.read()
fichier.close()

t=[]
ligne=[]
temp=''
for i in texte:
	if i=='\n':
		t.append(ligne)
		ligne=[]
	elif i=='-' or i=='[' or i==']':
		if temp.isdigit():
			ligne.append(int(temp))
		else:
			ligne.append(temp)
		temp=''
	else:
		temp+=i

L=[]
for ligne in t:
	temp=''
	for i in range(len(ligne)-2):
		temp+=ligne[i]
	L.append([temp, ligne[len(ligne)-2], ligne[len(ligne)-1]])


def lettres_courantes(mot):
	d=dict()
	for lettre in mot:
		if lettre not in d:
			d[lettre]=1
		else:
			d[lettre]+=1

	nombre_max_lettre=0
	for lettre in d:
		if d[lettre]>nombre_max_lettre:
			nombre_max_lettre=d[lettre]

	t=[]
	while nombre_max_lettre!=0:
		temp=[]
		for lettre in d:
			if d[lettre]==nombre_max_lettre:
				temp.append(lettre)
		for i in sorted(temp):
			t.append(i)
		nombre_max_lettre-=1
	
	res=''
	for i in t:
		res+=i

	return res[:5]

res=0
a=0
for ligne in L:
	if lettres_courantes(ligne[0])==ligne[2]:
		res+=ligne[1]
		a+=1

print(f'Partie 1 : {res}')

#Partie 2

t=[]
ligne=[]
temp=''
for i in texte:
	if i=='\n':
		t.append(ligne)
		ligne=[]
	elif i=='-' or i=='[' or i==']':
		if temp.isdigit():
			ligne.append(int(temp))
		else:
			ligne.append(temp)
		temp=''
	else:
		temp+=i

def transforme(liste):
	res=''
	for mot in range(len(liste)-2):
		for lettre in liste[mot]:
			res+=chr((ord(lettre)-97+liste[len(liste)-2])%26+97)
		res+=' '
	return res

for ligne in t:
	temp=''
	for mot in range(len(ligne)-2):
		temp+=ligne[mot]
	if lettres_courantes(temp)==ligne[len(ligne)-1]:
		if 'northpole object storage' in transforme(ligne):
			print(f'Partie 2 : {ligne[len(ligne)-2]}')