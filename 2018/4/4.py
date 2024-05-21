with open('input.txt','r') as fichier:
	texte=fichier.read()

texte = '''[1518-11-01 00:00] Guard #10 begins shift
[1518-11-01 00:05] falls asleep
[1518-11-01 00:25] wakes up
[1518-11-01 00:30] falls asleep
[1518-11-01 00:55] wakes up
[1518-11-01 23:58] Guard #99 begins shift
[1518-11-02 00:40] falls asleep
[1518-11-02 00:50] wakes up
[1518-11-03 00:05] Guard #10 begins shift
[1518-11-03 00:24] falls asleep
[1518-11-03 00:29] wakes up
[1518-11-04 00:02] Guard #99 begins shift
[1518-11-04 00:36] falls asleep
[1518-11-04 00:46] wakes up
[1518-11-05 00:03] Guard #99 begins shift
[1518-11-05 00:45] falls asleep
[1518-11-05 00:55] wakes up'''

t = [i for i in texte.strip().split('\n')]
# 17 inclus
for i in range(len(t)):
	t[i] = [int(t[i][1:5]),int(t[i][6:8]),int(t[i][9:11]),int(t[i][12:14]),int(t[i][15:17])] + t[i][19:].split(' ')

def temps(temps_debut,temps_fin): # format -> temps_debut = (heures,minutes)
	h1,m1 = temps_fin
	h,m = temps_debut
	res = [temps_debut]
	while (h,m) != (h1,m1):
		m += 1
		if m == 60:
			h = (h+1)%24
			m = 0
		res.append((h,m))
	return res

asleep = dict()
d = dict()
current_guard = 0
for ligne in t:
	if ligne[5] == 'Guard':
		current_guard = ligne[6][1:]
	elif ligne[5] == 'falls':
		try:
			if asleep[current_guard] == 0:
				asleep[current_guard] = (ligne[3],ligne[4])
		except:
			pass
	else:
		try:
			temps_debut = asleep[current_guard]
			temps_fin = (ligne[3],ligne[4])
			for i in temps(temps_debut,temps_fin):
				try:
					d[i].add(current_guard)
				except:
					d[i] = {current_guard}
			asleep[current_guard] = 0
		except:
			pass

print(d)