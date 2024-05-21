with open('input.txt','r') as f:
	texte=f.read()

file=['D H N Q T W V B','D W B','T S Q W J C','F J R N Z T P','G P V J M S T','B W F T N','B L D Q F H V N','H P F R','Z S M B L N P H']

def nombre(temp):
	if temp.isdigit():
		return int(temp)
	return temp

t=[]
ligne=[]
temp=''
for i in texte:
	if i=='\n':
		if temp!='':
			ligne.append(nombre(temp))
		temp=''
		t.append(ligne)
		ligne=[]
	elif i==' ':
		if temp!='':
			ligne.append(nombre(temp))
		temp=''
	else:
		temp+=i

for i in range(len(t)):
	t[i]=[t[i][1],t[i][3],t[i][5]]

pile = [i.split(' ') for i in file]

def instruction(ligne):
	global pile
	for i in range(ligne[0]):
		pile[ligne[2]-1].append(pile[ligne[1]-1][len(pile[ligne[1]-1])-1])
		pile[ligne[1]-1].pop()


for ligne in t:
	instruction(ligne)

res=''
for i in pile:
	res+=i[len(i)-1]

print('Partie 1 :',res)

pile=[i.split(' ') for i in file]

def instruction2(ligne):
	global pile
	temp=[]
	for i in range(ligne[0]):
		temp.append(pile[ligne[1]-1][len(pile[ligne[1]-1])-1-i])
	for i in range(ligne[0]):
		pile[ligne[1]-1].pop()
	temp=list(reversed(temp))
	for i in temp:
		pile[ligne[2]-1].append(i)

for ligne in t:
	instruction2(ligne)

res=''
for i in pile:
	res+=i[len(i)-1]

print('Partie 2 :',res)