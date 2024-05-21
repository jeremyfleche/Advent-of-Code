fichier=open('input.txt','r')
texte=fichier.read()
fichier.close()

A=10
B=11
C=12
D=13
E=14
F=15

def binaire(a):
    res=[0,0,0,0]
    x=a
    for i in range(3,-1,-1):
        if 2**i<=x:
            x-=2**i
            res[3-i]=1
    binaire=''
    for i in res:
        binaire+=str(i)
    return binaire

print(binaire(9))