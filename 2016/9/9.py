fichier=open('input.txt','r')
texte=fichier.read()
fichier.close()

def decompresse(texte):
	res=0
	i=0
	while i<len(texte):
		if texte[i]=='(':
			liste=[]
			temp=''
			while texte[i]!=')':
				if texte[i].isdigit():
					temp+=texte[i]
				elif temp!='':
					liste.append(int(temp))
					temp=''
				i+=1
			i+=1
			liste.append(int(temp))
			temp=''
			for x in range(i,i+liste[0]):
				temp+=texte[x]
			res+=liste[1]*len(temp)
			i+=liste[0]
		elif texte[i]!='\n':
			res+=1
			i+=1
		else:
			i+=1
	return res

print(f'Partie 1 : {decompresse(texte)}')

# Partie 2


def decompresse2(texte):
	res=0
	i=0
	while i<len(texte):
		if texte[i]=='(':
			liste=[]
			temp=''
			while texte[i]!=')':
				if texte[i].isdigit():
					temp+=texte[i]
				elif temp!='':
					liste.append(int(temp))
					temp=''
				i+=1
			i+=1
			liste.append(int(temp))
			temp=''
			for x in range(i,i+liste[0]):
				temp+=texte[x]
			res+=liste[1]*decompresse2(temp)
			i+=liste[0]
		elif texte[i]!='\n':
			res+=1
			i+=1
		else:
			i+=1
	return res

print(f'Partie 2 : {decompresse2(texte)}')
