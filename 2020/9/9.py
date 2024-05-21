with open("input.txt") as f:
	texte = f.read()

t = [int(i) for i in texte.strip().split()]

def valide(liste,i):
	for a in range(i-25,i):
		for b in range(i-25,i):
			if liste[a] + liste[b] == liste[i] and a != b:
				return True
	return False

for i in range(25,len(t)):
	if not valide(t,i):
		res = t[i]
		print("Partie 1:",res)
		break

# Partie 2

def solve(res):
	for a in range(len(t)):
		for b in range(a+1,len(t)):
			if sum(t[a:b]) == res:
				return max(t[a:b])+min(t[a:b])

print("Partie 2:",solve(res))