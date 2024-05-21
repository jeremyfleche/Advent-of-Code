from itertools import product

with open('input.txt','r') as f:
	texte=f.read()

def nombre(temp):
	if temp[0]=='-':
		return -nombre(temp[1:])
	if temp.isdigit():
		return int(temp)
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
	elif i=='=' or i=='x' or i=='y' or i=='z' or i=='.' or i==',' or i==' ':
		if temp!='':
			ligne.append(nombre(temp))
		temp=''
	else:
		temp+=i

def valide_ligne(ligne):
	if abs(ligne[1])<=50:
		return True
	return False

d=dict()
for ligne in t:
	if valide_ligne(ligne):
		x=[i for i in range(ligne[1],ligne[2]+1)]
		y=[i for i in range(ligne[3],ligne[4]+1)]
		z=[i for i in range(ligne[5],ligne[6]+1)]
		if ligne[0]=='on':
			for i in product(x,y,z):
				d[i]=1
		else:
			for i in product(x,y,z):
				d[i]=0

res=0
for i in d:
	if d[i]==1:
		res+=1

print(res)
