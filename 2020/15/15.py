texte = "18,11,9,0,5,1"

def incremente(last_spoken,tour):
	global d
	try:
		nombre, last_i, i = d[last_spoken]
		d[last_spoken] = (nombre+1, i, tour)
	except:
		d[last_spoken] = (1, 0, tour)

liste = [int(i) for i in texte.split(",")]
last_spoken = liste[-1]
d = {liste[i]:(1,0 ,i+1) for i in range(len(liste))}
tour = len(liste)

while tour != 2020:
	tour += 1
	if d[last_spoken][0] == 1:
		last_spoken = 0
		incremente(last_spoken,tour)
	else:
		nombre, last_i, i = d[last_spoken]
		x = i - last_i
		last_spoken = x
		incremente(x,tour)

print("Partie 1 :",last_spoken)

liste = [int(i) for i in texte.split(",")]
last_spoken = liste[-1]
d = {liste[i]:(1,0 ,i+1) for i in range(len(liste))}
tour = len(liste)

while tour != 30000000:
	tour += 1
	if d[last_spoken][0] == 1:
		last_spoken = 0
		incremente(last_spoken,tour)
	else:
		nombre, last_i, i = d[last_spoken]
		x = i - last_i
		last_spoken = x
		incremente(x,tour)

print("Partie 2 :",last_spoken)		# Attendre environ 45 sec pour le résultat