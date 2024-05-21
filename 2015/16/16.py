fichier=open('input.txt','r')
texte=fichier.read()
fichier.close()

temp=''
ligne=[]
t=[]
for i in texte:
	if i=='\n':
		if temp.isdigit():
			ligne.append(int(temp))
			temp=''
		else:
			ligne.append(temp)
			temp=''
		t.append(ligne[1:])
		ligne=[]
	elif (i==' ' or i==':' or i==',') and temp!='':
		if temp.isdigit():
			ligne.append(int(temp))
			temp=''
		else:
			ligne.append(temp)
			temp=''
	elif i!=' ' and i!=':' and i!=',':
		temp+=i

emballage={'children': 3,
'cats': 7,
'samoyeds': 2,
'pomeranians': 3,
'akitas': 0,
'vizslas': 0,
'goldfish': 5,
'trees': 3,
'cars': 2,
'perfumes': 1}

d=dict()
for ligne in t:
	d[ligne[0]]={}
	for i in range(1,len(ligne),2):
		d[ligne[0]][ligne[i]]=ligne[i+1]


for tante in d:
	x=0
	for truc in d[tante]:
		if d[tante][truc]==emballage[truc]:
			x+=1
	if x==3:
		print(f'Partie 1 : {tante}')

#Partie 2

for tante in d:
	x=0
	for truc in d[tante]:
		if truc=='cats' or truc=='trees':
			if d[tante][truc]>emballage[truc]:
				x+=1
		elif truc=='pomeranians' or truc=='goldfish':
			if d[tante][truc]<emballage[truc]:
				x+=1
		else:
			if d[tante][truc]==emballage[truc]:
				x+=1
	if x==3:
		print(f'Partie 2 : {tante}')


