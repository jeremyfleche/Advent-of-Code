nombre=open('input.txt','r').read()

t=''
for i in nombre:
	if i.isdigit():
		t+=i

nombre=t
res=0
for i in range(len(nombre)):
	if nombre[i]==nombre[(i+1)%len(nombre)]:
		res+=int(nombre[i])

print(f'Partie 1 : {res}')

#Partie 2

res=0
for i in range(len(nombre)):
	if nombre[i]==nombre[(i+len(nombre)//2)%len(nombre)]:
		res+=int(nombre[i])

print(f'Partie 2 : {res}')