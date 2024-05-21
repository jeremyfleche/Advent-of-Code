fichier=open('input.txt','r')
texte=fichier.read()
fichier.close()

mot=''
ligne=[]
t=[]

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


def division_euclidienne(a,b):
	q=a//b
	r=a-b*q
	return q,r


def binaire(dec):
	res=''
	a=dec
	while division_euclidienne(a,2)[0]!=0:
		res+=str(division_euclidienne(a,2)[1])
		a=division_euclidienne(a,2)[0]
	res+=str(division_euclidienne(a,2)[1])
	return res[::-1]


def decimal(binaire):
	res=0
	for i in range(len(binaire)):
		res+=int(binaire[i])*2**(len(binaire)-1-i)
	return res


def et(dec1,dec2):
	b1=binaire(dec1)[::-1]
	b2=binaire(dec2)[::-1]
	longueur=max(len(b1),len(b2))
	for i in range(16-len(b1)):
		b1+='0'
	for i in range(16-len(b2)):
		b2+='0'
	b1=b1[::-1]
	b2=b2[::-1]
	res=''
	for i in range(len(b1)):
		if b1[i]==b2[i]=='1':
			res+='1'
		else:
			res+='0'
	return decimal(res)


def ou(dec1,dec2):
	b1=binaire(dec1)[::-1]
	b2=binaire(dec2)[::-1]
	for i in range(16-len(b1)):
		b1+='0'
	for i in range(16-len(b2)):
		b2+='0'
	b1=b1[::-1]
	b2=b2[::-1]
	res=''
	for i in range(len(b1)):
		if b1[i]=='1' or b2[i]=='1':
			res+='1'
		else:
			res+='0'
	return decimal(res)


def non(dec):
	b=binaire(dec)[::-1]
	for i in range(16-len(b)):
		b+='0'
	b=b[::-1]
	res=''
	for i in range(len(b)):
		res+=str(1-int(b[i]))
	return decimal(res)


def decale_g(dec,x):
	b=binaire(dec)[::-1]
	for i in range(16-len(b)):
		b+='0'
	b=b[::-1]
	res=''
	for i in range(x,len(b)):
		res+=b[i]
	for i in range(16-len(res)):
		res+='0'
	return decimal(res)


def decale_d(dec,x):
	b=binaire(dec)[::-1]
	for i in range(16-len(b)):
		b+='0'
	b=b[::-1]
	res=''
	for i in range(x):
		res+='0'
	for i in range(len(b)-x):
		res+=b[i]
	return decimal(res)

def double(s):
	if len(s)==2:
		return True
	return False

variables=[]
for ligne in t:
	for i in ligne:
		if i!='NOT' and i!='->' and i!='OR' and i!='RSHIFT' and i!='LSHIFT' and i!='AND' and i.isdigit()==False and i not in variables:
			variables.append(i)

d=dict()
while len(d)!=len(variables):
	for ligne in t:

		if ligne[1]=='->':
			if ligne[0].isdigit():
				d[ligne[2]]=int(ligne[0])
			elif ligne[0] in d:
				d[ligne[2]]=d[ligne[0]]

		if ligne[0]=='NOT' and ligne[1] in d:
			d[ligne[3]]=non(d[ligne[1]])

		if ligne[1]=='OR' and ligne[0] in d and ligne[2] in d:
			d[ligne[4]]=ou(d[ligne[0]],d[ligne[2]])

		if ligne[1]=='AND':
			if ligne[0].isdigit() and ligne[2] in d:
				d[ligne[4]]=et(int(ligne[0]),d[ligne[2]])
			if ligne[0] in d and ligne[2] in d:
				d[ligne[4]]=et(d[ligne[0]],d[ligne[2]])

		if ligne[1]=='RSHIFT' and ligne[0] in d:
			d[ligne[4]]=decale_d(d[ligne[0]],int(ligne[2]))

		if ligne[1]=='LSHIFT' and ligne[0] in d:
			d[ligne[4]]=decale_g(d[ligne[0]],int(ligne[2]))

a=d['a']
print('Partie 1 : '+str(a))

# Partie 2

for ligne in t:
    if ligne[1]=='->' and ligne[2]=='b':
        ligne[0]=str(a)

d=dict()
while len(d)!=len(variables):
	for ligne in t:

		if ligne[1]=='->':
			if ligne[0].isdigit():
				d[ligne[2]]=int(ligne[0])
			elif ligne[0] in d:
				d[ligne[2]]=d[ligne[0]]

		if ligne[0]=='NOT' and ligne[1] in d:
			d[ligne[3]]=non(d[ligne[1]])

		if ligne[1]=='OR' and ligne[0] in d and ligne[2] in d:
			d[ligne[4]]=ou(d[ligne[0]],d[ligne[2]])

		if ligne[1]=='AND':
			if ligne[0].isdigit() and ligne[2] in d:
				d[ligne[4]]=et(int(ligne[0]),d[ligne[2]])
			if ligne[0] in d and ligne[2] in d:
				d[ligne[4]]=et(d[ligne[0]],d[ligne[2]])

		if ligne[1]=='RSHIFT' and ligne[0] in d:
			d[ligne[4]]=decale_d(d[ligne[0]],int(ligne[2]))

		if ligne[1]=='LSHIFT' and ligne[0] in d:
			d[ligne[4]]=decale_g(d[ligne[0]],int(ligne[2]))

print('Partie 2 : '+str(d['a']))

