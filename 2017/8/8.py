with open('input.txt','r') as f:
	texte=f.read()

def nombre(temp):
	try:
		return int(temp)
	except:
		return temp

t=[]
ligne=[]
temp=''
for i in texte:
	if i=='\n':
		ligne.append(nombre(temp))
		temp=''
		t.append(ligne)
		ligne=[]
	elif i==' ':
		ligne.append(nombre(temp))
		temp=''
	else:
		temp+=i

def inc_dec(a,inc_dec,nombre):
	global d
	if inc_dec=='inc':
		d[a]+=nombre
	else:
		d[a]-=nombre

def change(ligne):
	global d
	if ligne[5]=='==':
		if d[ligne[4]]==ligne[6]:
			inc_dec(ligne[0],ligne[1],ligne[2])
	elif ligne[5]=='<':
		if d[ligne[4]]<ligne[6]:
			inc_dec(ligne[0],ligne[1],ligne[2])
	elif ligne[5]=='<=':
		if d[ligne[4]]<=ligne[6]:
			inc_dec(ligne[0],ligne[1],ligne[2])
	elif ligne[5]=='>':
		if d[ligne[4]]>ligne[6]:
			inc_dec(ligne[0],ligne[1],ligne[2])
	elif ligne[5]=='>=':
		if d[ligne[4]]>=ligne[6]:
			inc_dec(ligne[0],ligne[1],ligne[2])
	else:
		if d[ligne[4]]!=ligne[6]:
			inc_dec(ligne[0],ligne[1],ligne[2])

def maximum(d):
	global res
	temp=max([i for i in d.values()])
	if temp>res:
		res=temp

d=dict()
for ligne in t:
	d[ligne[0]]=0
	d[ligne[4]]=0

res=0
for ligne in t:
	change(ligne)
	maximum(d)

print('Partie 1 :',max([i for i in d.values()]))
print('Partie 2 :',res)