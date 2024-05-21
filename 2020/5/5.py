with open("input.txt") as f:
    texte = f.read()

t = texte.strip().split()

def half(intervalle,a):
    if a == 'F' or a == 'L':
        return (intervalle[0],(intervalle[0]+intervalle[1])//2)
    if a == 'B' or a == 'R':
        return ((intervalle[0]+intervalle[1])//2,intervalle[1])

def seat_id(code):
    ligne = (0,127)
    colonne = (0,7)
    for i in range(7):
        ligne = half(ligne,code[i])
    for i in range(7,10):
        colonne = half(colonne,code[i])
    return 8*ligne[1]+colonne[1]

liste = []
for i in t:
    liste.append(seat_id(i))

print("Partie 1 :", max(liste))

# Partie 2

liste.sort()

for i in range(len(liste)-1):
    if liste[i] == liste[i+1]-2:
        print("Partie 2 :",liste[i]+1)
        break