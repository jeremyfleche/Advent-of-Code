with open('input.txt','r') as f:
	texte = f.read()

ligne=[]
temp=''
t2=[]
for i in range(len(texte)-1):
	if texte[i]+texte[i+1]=='\n\n':
		ligne.append(temp)
		temp=''
		t2.append(ligne)
		ligne=[]
		t1=t2
		x=i+2
		break
	elif texte[i]=='\n':
		ligne.append(temp)
		temp=''
		t2.append(ligne)
		ligne=[]
	elif texte[i]==' ':
		ligne.append(temp)
		temp=''
	else:
		temp+=texte[i]

for i in t1:
	del i[1]

t2=[]
temp=''
for i in range(x,len(texte)):
	if texte[i].isupper():
		temp+=texte[i]
		if texte[i+1].isupper():
			t2.append(temp)
			temp=''
	elif texte[i]=='\n':
		continue
	else:
		temp+=texte[i]
		t2.append(temp)
		temp=''
if temp!='':
	t2.append(temp)

L=set()
for i in range(len(t2)):
	for j in t1:
		if t2[i]==j[0]:
			t=[]
			temp=''
			for k in j[1]:
				if k.isupper():
					if temp.isupper():
						t.append(temp)
						temp=''
					temp+=k
				else:
					temp+=k
					t.append(temp)
					temp=''
			if temp!='':
				t.append(temp)
			L.add(str(t2[:i]+t+t2[i+1:]))

print(f'Partie 1 : {len(L)}')

#Partie 2

instructions=[]
for i in t1:
	instructions.append([])
	instructions[len(instructions)-1].append(i[1])
	instructions[len(instructions)-1].append(i[0])

L=[]
for i in range(len(instructions)):
	for j in range (len(instructions)):
		if i<j and len(instructions[i][0])<len(instructions[j][0]):
				instructions[i],instructions[j]=instructions[j],instructions[i]


molecule=''
for i in t2:
	molecule+=i

def tri(L):
	for i in range(len(L)):
		for j in range (len(L)):
			if i<j and len(L[i])>len(L[j]):
				L[i],L[j]=L[j],L[i]


def algorithme(liste):
	global instructions
	L=[]
	for instruction in instructions:
		for i in range(len(molecule)-len(instruction)+1):
			if molecule[i:i+len(instruction)]==instruction[0]:
				if molecule[:i]+instruction[1]+molecule[i+len(instruction):] not in L:
					L.append(molecule[:i]+instruction[1]+molecule[i+len(instruction):])
	return L


L=[molecule]
cible=molecule
nb_etape=0
while cible!='e':
	t=[]
	for i in L:
		t+=algorithme(i)
	tri(t)
	L=[t[i] for i in range(len(t)) if len(t[i])==len(t[0])]
	cible=L[0]
	nb_etape+=1
	print(nb_etape)
