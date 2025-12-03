import time
START_TIME = time.time()

with open("input.txt") as f:
    texte = f.read().strip()

lines = texte.splitlines()

def find_max(number, size_to_chose):
    i = -1
    res = ""
    while size_to_chose > 0:
        maxi_i = i+1
        maxi = 0
        for j in range(i+1, len(number)-size_to_chose+1):
            if int(number[j]) > int(maxi):
                maxi = number[j]
                maxi_i = j
        res += maxi
        i = maxi_i
        size_to_chose -= 1
    return int(res)

res1 = sum([find_max(line, 2) for line in lines])
res2 = sum([find_max(line, 12) for line in lines])

print("Partie 1 :",res1)
print("Partie 2 :",res2)

print(f"[{int((time.time()-START_TIME)*1000)}ms]")
