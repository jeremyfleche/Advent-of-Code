with open("input.txt") as f:
	texte = f.read()

liste = [int(i) for i in texte.strip().splitlines()]
print("Partie 1 :",sum(i//3-2 for i in liste))