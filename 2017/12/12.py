import time
START_TIME = time.time()

with open("input.txt") as f:
    texte = f.read().strip()

pipes = {}
for line in texte.splitlines():
    src, dests = line.split("<->")
    src = int(src)
    pipes[src] = set()
    for dest in dests.split(","):
        pipes[src].add(int(dest))

def is_accessible(a,b):
    Q = [a]
    SEEN = set()
    while Q:
        x = Q.pop()
        if x == b:
            return True
        if x in SEEN:
            continue
        SEEN.add(x)
        for y in pipes[x]:
            Q.append(y)
    return False

def part1():
    res = 0
    for i in pipes:
        if is_accessible(i,0):
            res += 1
    return res

def part2():
    Q = [i for i in pipes]
    SEEN = set()
    res = 0
    for i in Q:
        if i in SEEN:
            continue
        E = [i]
        while E:
            x = E.pop()
            if x in SEEN:
                continue
            SEEN.add(x)
            for y in pipes[x]:
                E.append(y)
        res += 1
    return res


print("Partie 1 :", part1())
print("Partie 2 :", part2())

print(f"[{int((time.time()-START_TIME)*1000)}ms]")