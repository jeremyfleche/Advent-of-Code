import time
START_TIME = time.time()

with open("input.txt") as f:
    texte = f.read().strip()

def concate(i, j):
    res = ""
    for k in range(j):
        res += str(i)
    return int(res)

def in_range(i,values):
    return values[0]<=i<=values[1]

def add_all_repeat_for_i(i, values, SEEN, borne):
    j = 2
    res = 0
    while (concate(i,j) <= values[1] and (borne == 0 or j <= borne)):
        if in_range(concate(i,j),values):
            SEEN.add(concate(i,j))
        j += 1
    return res

def invalidIDs(values, borne):
    SEEN = set()
    i = 1
    repeat = 2
    while concate(i, 2) <= values[1]:
        add_all_repeat_for_i(i, values, SEEN, borne)
        i += 1
    return sum(SEEN)

res1 = 0
res2 = 0
for line in texte.split(','):
    values = list(map(int, line.split('-')))
    
    res1 += invalidIDs(values, 2)
    res2 += invalidIDs(values, 0)


print("Partie 1 :",res1)
print("Partie 2 :",res2)
print(f"[{int((time.time()-START_TIME)*1000)}ms]")