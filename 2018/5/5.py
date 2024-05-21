from math import inf

with open('input.txt','r') as f:
	texte = [i for i in f.read().strip()]


def reaction(m):
	for i in range(len(m)-1):
		if m[i] == m[i+1]:
			pass
		elif m[i].upper() == m[i+1] or m[i].lower() == m[i+1]:
			m[i] = '0'
			m[i+1] = '0'
	return [i for i in m if i != '0']

while len(texte) != len(reaction(texte)):
	texte = reaction(texte)

print(len(texte))

with open('input.txt','r') as f:
	texte = [i for i in f.read().strip()]

alphabet = 'abcdefghijklmnopqrstuvwxyz'

def partie2(m):
	global alphabet
	minimum = inf
	for lettre in alphabet:
		print(lettre)
		for i in range(len(m)-1):
			if m[i] == lettre or m[i] == lettre.upper():
				if m[i] == m[i+1]:
					pass
				elif m[i].upper() == m[i+1] or m[i].lower() == m[i+1]:
					m[i] = '0'
					m[i+1] = '0'
		temp = [i for i in m if i != '0']
		while len(temp) != len(reaction(temp)):
			temp = reaction(temp)
		if len(temp) < minimum:
			minimum = len(temp)
	return minimum

print(partie2(texte))