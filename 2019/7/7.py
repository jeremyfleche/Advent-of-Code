with open("input.txt") as f:
	texte = f.read().strip()

liste = [int(i) for i in texte.split(",")]
print(liste)