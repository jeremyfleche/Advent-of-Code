texte=open('input.txt','r').read()

t=[]
temp=''
for i in texte:
	if i=='\n':
		t.append(temp)
		temp=''
	else:
		temp+=i

def algo(s):
	deux=0
	trois=0
	d=dict()
	for i in s:
		try:
			d[i]+=1
		except:
			d[i]=1

	for i in d:
		if d[i]==2:
			deux=1
		if d[i]==3:
			trois=1

	return deux,trois

res_deux=0
res_trois=0
for ligne in t:
	deux,trois=algo(ligne)
	res_deux+=deux
	res_trois+=trois

print("Partie 1 :",res_deux*res_trois)

#Partie 2

def algo2(t):
	for i in t:
		for j in t:
			if i!=j:
				s=''
				for x in range(len(i)):
					if i[x]==j[x]:
						s+=i[x]
				if len(s)==len(i)-1:
					return s

print("Partie 1 :",algo2(t))				
