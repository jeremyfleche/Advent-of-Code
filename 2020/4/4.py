with open("input.txt") as f:
    texte = f.read()

# texte = """pid:087499704 hgt:74in ecl:grn iyr:2012 eyr:2030 byr:1980
# hcl:#623a2f

# eyr:2029 ecl:blu cid:129 byr:1989
# iyr:2014 pid:896056539 hcl:#a97842 hgt:165cm

# hcl:#888785
# hgt:164cm byr:2001 iyr:2015 cid:88
# pid:545766238 ecl:hzl
# eyr:2022

# iyr:2010 hgt:158cm hcl:#b6652a ecl:blu byr:1944 eyr:2021 pid:093154719"""

t=texte.strip().split('\n\n')

def valide(ligne):
    for i in ['byr','iyr','eyr','hgt','hcl','ecl','pid']:
        if i not in ligne:
            return False
    return True

res=0
for ligne in t:
    if valide(ligne):
        res+=1

print("Partie 1 :",res)

#Partie 2

def separe(ligne):
    res=[]
    temp=''
    for i in ligne:
        if i=='\n' or i==' ':
            res.append(temp)
            temp=''
        else:
            temp+=i
    if temp != '':
        res.append(temp)
    return res

for i in range(len(t)):
    t[i] = {a:b for a,b in [i.split(':') for i in separe(t[i])]}

def valide2(d):
    try:
        if int(d['byr']) < 1920 or int(d['byr']) > 2002 or len(d['byr']) != 4:
            return False
    except:
        return False
    try:
        if int(d['iyr']) < 2010 or int(d['iyr']) > 2020 or len(d['iyr']) != 4:
            return False
    except:
        return False
    try:
        if int(d['eyr']) < 2020 or int(d['eyr']) > 2030 or len(d['eyr']) != 4:
            return False
    except:
        return False
    try:
        if d['hgt'][-2:] == 'cm':
            if int(d['hgt'][:-2]) < 150 or int(d['hgt'][:-2]) > 193:
                return False
        elif d['hgt'][-2:] == 'in':
            if int(d['hgt'][:-2]) < 59 or int(d['hgt'][:-2]) > 76:
                return False
        else:
            return False
    except:
        return False
    try:
        if d['hcl'][0] != "#" or len(d['hcl']) != 7:
            return False
        for i in d['hcl'][1:]:
            if i not in "0123456789abcdef":
                return False
    except:
        return False
    try:
        if d["ecl"] not in ['amb','blu','brn','gry','grn','hzl','oth']:
            return False
    except:
        return False
    try:
        if len(d["pid"]) != 9:
            return False
        for i in d["pid"]:
            if i.isdigit() == False:
                return False
    except:
        return False

    return True

res = 0
for i in t:
    if valide2(i):
        res += 1

print("Partie 2 :",res)