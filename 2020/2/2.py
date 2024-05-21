texte=open('input.txt','r').read()

def nombre(temp):
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
	elif i==' ' or i=='-' or i==':':
		if temp!='':
			ligne.append(nombre(temp))
			temp=''
	else:
		temp+=i

def valide(ligne):

	minimum=ligne[0]
	maximum=ligne[1]
	lettre=ligne[2]
	s=ligne[3]

	res=0
	for i in s:
		if i==lettre:
			res+=1

	if res<minimum or res>maximum:
		return False

	return True

res=0
for ligne in t:
	if valide(ligne):
		res+=1

print('Partie 1 :',res)

#Partie 2

def valide2(ligne):

	i=ligne[0]
	j=ligne[1]
	lettre=ligne[2]
	s=ligne[3]

	if (s[i-1]==lettre)+(s[j-1]==lettre)==1:
		return True

	return False

res=0
for ligne in t:
	if valide2(ligne):
		res+=1

print('Partie 2 :',res)