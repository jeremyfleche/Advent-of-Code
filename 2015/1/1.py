with open('input.txt','r') as f:
	texte = f.read()

res = 0
for i in texte:
	if i == '(':
		res += 1
	else:
		res -= 1

print('Partie 1 :',res)

#Partie 2

i = 0
niveau = 0
t = [i for i in texte.strip()]
while niveau != -1:
	if t[i] == '(':
		niveau += 1
	else:
		niveau -= 1
	i += 1

print('Partie 2 :',i)