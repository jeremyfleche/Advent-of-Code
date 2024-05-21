with open('input.txt','r') as fichier:
	texte=fichier.read()

def nombre(temp):
	if temp.isdigit():
		return int(temp)
	return temp

t=[]
ligne=[]
temp=''
separateurs=' ()->,'
for i in texte:
	if i=='\n':
		if temp!='':
			ligne.append(nombre(temp))
			temp=''
		t.append(ligne)
		ligne=[]
	elif i in separateurs:
		if temp!='':
			ligne.append(nombre(temp))
		temp=''
	else:
		temp+=i

def longueur_branche(ligne):
	if len(ligne)==2:
		return 1
	liste=[]
	for i in ligne[2:len(ligne)]:
		for line in t:
			if i==line[0]:
				liste.append(line)
	return 1+max([longueur_branche(i) for i in liste])

longueur_max=0
programme=''
for ligne in t:
	if longueur_branche(ligne)>longueur_max:
		longueur_max=longueur_branche(ligne)
		programme=ligne[0]

print('Partie 1 :',programme)

#Partie 2

d=dict()
for ligne in t:
	d[ligne[0]]=ligne[1:len(ligne)]

def poids(branche):
	global d
	if len(d[branche])==1:
		return d[branche][0]
	return d[branche][0]+sum([poids(i) for i in d[branche][1:len(d[branche])]])

def partie2(branche):
	global d
	try:
		liste=[(i,poids(i)) for i in d[branche][1:len(d[branche])]]
	except:
		return poids(branche)
	temp=[i[1] for i in liste]
	for i in range(len(liste)):
		if temp.count(temp[i])==1:
			if type(partie2(liste[i][0]))==tuple:
				difference=max(temp)-min(temp)
				return d[liste[i][0]][0]-difference
			return partie2(liste[i][0])
	
	return poids(branche),liste

print('Partie 2 :',partie2(programme))
