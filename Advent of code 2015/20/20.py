from math import sqrt

def diviseurs(n):
	L=[]
	for i in range(1,int(sqrt(n)+1)):
		if n/i==n//i:
			L.append(int(n//i))
			if int(n//(n//i)) not in L:
				L.append(int(n//(n//i)))
	return sorted(L)

def nb_cadeaux(maison):
	return sum(diviseurs(maison))*10

maison=830000 						# après quelques tests on sait que le résultat est au dessus de 830000
while nb_cadeaux(maison)<36000000:
	maison+=1

print(f'Partie 1 : {maison}')

#Partie 2

def elfes_maison(maison):
	L=[]
	for elfe in diviseurs(maison):
		if maison//elfe<=50:
			L.append(elfe)
	return L

def nb_cadeaux2(maison):
	return sum(elfes_maison(maison))*11

maison=860000						# après quelques tests on sait que le résultat est au dessus de 860000
while nb_cadeaux2(maison)<36000000:
	maison+=1

print(f'Partie 2 : {maison}')