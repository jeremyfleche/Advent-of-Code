texte = [240920,789857]

def valide(number):
    temp = str(number)
    double = False
    decrease = False
    for i in range(len(temp)-1):
        if temp[i] == temp[i+1]:
            double = True
        if temp[i] > temp[i+1]:
            decrease = True
            break
    return double and not decrease

res = 0
for i in range(texte[0],texte[1]+1):
    res += valide(i)

print('Partie 1 :',res)

def valide2(number):
    temp = str(number)
    double = False
    decrease = False
    current_letter = temp[0]
    current_rep = 1
    for i in range(1,len(temp)):
        if temp[i] == current_letter:
            current_rep += 1
        if temp[i] != current_letter:
            if current_rep == 2:
                double = True
            current_rep = 1
            current_letter = temp[i]
        if temp[i-1] > temp[i]:
            decrease = True
            break
    if current_rep == 2:
        double = True
    return double and not decrease
   
res = 0
for i in range(texte[0],texte[1]+1):
    res += valide2(i)

print('Partie 2 :',res)
