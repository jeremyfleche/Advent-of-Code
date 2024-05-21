with open('input.txt','r') as f:
    texte=f.read()

t=[]
ligne=[]
for i in texte:
    if i=='\n':
        t.append(ligne)
        ligne=[]
    else:
        ligne.append(i)

if ligne!=[]:
    t.append(ligne)

def nb_arbre(t,pente_x,pente_y):
    x,y=0,0
    res=0
    while y<len(t)-1:
        x=(x+pente_x)%len(t[0])
        y+=pente_y
        if t[y][x]=='#':
            res+=1
    return res
   
print('Partie 1 :',nb_arbre(t,3,1))
print('Partie 2 :',nb_arbre(t,1,1)*nb_arbre(t,3,1)*nb_arbre(t,5,1)*nb_arbre(t,7,1)*nb_arbre(t,1,2))
