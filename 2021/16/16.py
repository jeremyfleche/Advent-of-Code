def binary(n):
    d = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, 'A': 10, 'B': 11, 'C': 12, 'D': 13, 'E': 14, 'F': 15}
    n = d[n]
    res = ""
    while n != 0:
        res = str(n%2) + res
        n //= 2
    while len(res) < 4:
        res = "0" + res
    return res

def dec(binaire):
    res = 0
    n = len(binaire)
    for i in range(n):
        res += int(binaire[i])* 2**(n-i-1)
    return res

def handler(trame, index=0):
    version = dec(trame[index:index+3])
    typeID = dec(trame[index+3:index+6])
    sommmeVersion = version
    index += 6
    if typeID == 4:
        temp = ""
        while trame[index] == "1":
            temp += trame[index+1:index+5]
            index += 5
        temp += trame[index+1:index+5]
        index += 5
    else:
        lengthID = trame[index]
        index += 1
        if lengthID == "0":
            lenght = dec(trame[index:index+15])
            index += 15
            end = index + lenght
            while index < end:
                temp, index = handler(trame, index)
                sommmeVersion += temp
        else:
            nb = dec(trame[index:index+11])
            index += 11
            for i in range(nb):
                temp, index = handler(trame, index)
                sommmeVersion += temp
    return sommmeVersion, index

def handler2(trame, index=0):
    version = dec(trame[index:index+3])
    typeID = dec(trame[index+3:index+6])
    index += 6
    if typeID == 4:
        temp = ""
        while trame[index] == "1":
            temp += trame[index+1:index+5]
            index += 5
        temp += trame[index+1:index+5]
        index += 5
        return dec(temp), index
    else:
        lengthID = trame[index]
        index += 1
        liste = []
        if lengthID == "0":
            lenght = dec(trame[index:index+15])
            index += 15
            end = index + lenght
            while index < end:
                temp, index = handler2(trame, index)
                liste.append(temp)
        else:
            nb = dec(trame[index:index+11])
            index += 11
            for i in range(nb):
                temp, index = handler2(trame, index)
                liste.append(temp)

        if typeID == 0:
            return sum(liste), index
        elif typeID == 1:
            res = 1
            for i in liste:
                res *= i
            return res, index
        elif typeID == 2:
            return min(liste), index
        elif typeID == 3:
            return max(liste), index
        elif typeID == 5:
            return 1 if liste[0]>liste[1] else 0, index
        elif typeID == 6:
            return 1 if liste[0]<liste[1] else 0, index
        elif typeID == 7:
            return 1 if liste[0]==liste[1] else 0, index

if __name__ == "__main__":
    with open("input.txt") as f:
        texte = f.read().strip()

    # texte = "9C0141080250320F1802104A08"

    trame = ""
    for bit in texte:
        trame += binary(bit)

    print("Partie 1 :",handler(trame)[0])
    print("Partie 2 :",handler2(trame)[0])