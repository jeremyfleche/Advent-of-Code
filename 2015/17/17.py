from itertools import combinations
from itertools import permutations

fichier=open('input.txt','r')
texte=fichier.read()
fichier.close()

nombre=''
t=[]
for i in texte:
	if i=='\n':
		t.append(int(nombre))
		nombre=''
	else:
		nombre+=i

res=0
for i in range(len(t)):
	for j in combinations(t,i):
		if sum(j)==150:
			res+=1

print(f'Partie 1 : {res}')

#Partie 2
t=sorted(t)	
t=list(reversed(t))

min_element=0
x=0
while x<150:
	min_element+=1
	x=sum(t[:min_element])

res=0
for i in combinations(t,min_element):
	if sum(i)==150:
		res+=1

print(f'Partie 2 : {res}')
