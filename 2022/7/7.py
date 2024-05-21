with open('input.txt','r') as f:
	texte=f.read()

t=[]
ligne=[]
temp=''
for i in texte:
	if i=='\n':
		ligne.append(temp)
		temp=''
		t.append(ligne)
		ligne=[]
	elif i==' ' or i=='$':
		if temp!='':
			ligne.append(temp)
		temp=''
	else:
		temp+=i

def new_pointeur():
	global liste_pointeur
	liste_pointeur.pop()
	return liste_pointeur[len(liste_pointeur)-1]

d=dict()
liste_pointeur=[]
pointeur=d
for ligne in t:
	if ligne[0]=='cd':
		if ligne[1]=='..':
			pointeur=new_pointeur()
		elif ligne[1]!='..':
			try:
				pointeur=pointeur[ligne[1]]
				liste_pointeur.append(pointeur)
			except:
				pointeur[ligne[1]]=dict()
				pointeur=pointeur[ligne[1]]
				liste_pointeur.append(pointeur)
	if ligne[0]=='dir':
		try:
			pointeur[ligne[1]]=dict()
		except:
			pointeur=dict()
			pointeur[ligne[1]]=dict()
	if ligne[0].isdigit():
		pointeur[ligne[1]]=int(ligne[0])

def value(d):
	res=0
	for i in d:
		if type(d[i])==int:
			res+=d[i]
		if type(d[i])==dict:
			res+=value(d[i])
	return res

def partie1(d):
	global res
	for i in d:
		if type(d[i])==dict:
			if value(d[i])<=100000:
				res+=value(d[i])
			partie1(d[i])

res=0
partie1(d)
print('Partie 1 :',res)

def partie2(d):
	global liste
	for i in d:
		if type(d[i])==dict:
			liste.append(value(d[i]))
			partie2(d[i])

liste=[]
partie2(d)
liste=sorted(liste)

i=0
while value(d)-liste[i]>40000000:
	i+=1

print('Partie 2 :',liste[i])