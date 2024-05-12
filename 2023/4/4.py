with open('input.txt') as f:
	texte = f.read()

t = [[i for i in ligne.split(" ") if i != ''] for ligne in texte.splitlines()]

res = 0
d = {i:1 for i in range(len(t))}
for ligne in range(len(t)):
	match = len(set(t[ligne][2:12]) & set(t[ligne][13:]))			# Intersection des deux ensembles -> nombre de matchs
	res += 2**(match-1) if match > 0 else 0							# Ajout du nombre de point à res
	for k in range(ligne+1, min(ligne+match+1,len(t))):				# Pour tous les n (= match) dictionnaires suivants (qui sont dans d)
		d[k] += d[ligne]											# On ajoute d[ligne] copies

print("Partie 1 :",res)
print("Partie 2 :",sum(d.values()))