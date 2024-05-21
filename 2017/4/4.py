texte=open('input.txt','r').read()

t=[]
ligne=[]
temp=''
for i in texte:
	if i=='\n':
		ligne.append(temp)
		temp=''
		t.append(ligne)
		ligne=[]
	elif i==' ':
		ligne.append(temp)
		temp=''
	else:
		temp+=i

def valide(ligne):
	d=dict()
	for i in ligne:
		try:
			if d[i]==1:
				return False
		except:
			d[i]=1
	return True

res=0
for ligne in t:
	if valide(ligne):
		res+=1

print('Partie 1 :',res)

#Partie 2

def valide2(ligne):
	res=[]
	for mot in ligne:
		temp=dict()
		for i in mot:
			try:
				temp[i]+=1
			except:
				temp[i]=1
		if temp in res:
			return False
		res.append(temp)
	return True

res=0
for ligne in t:
	if valide2(ligne):
		res+=1

print('Partie 2 :',res)