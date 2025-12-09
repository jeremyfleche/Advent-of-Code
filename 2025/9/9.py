import time
from mymodules.aoc import *
import os
from shapely import Polygon

os.chdir(os.path.dirname(__file__))

START_TIME = time.time()

texte = read_input("input")
tiles = mapped_matrix(texte, sep=",")

def area(t1, t2):
	return (abs(t1[0]-t2[0])+1)*(abs(t1[1]-t2[1])+1)
	
def rectangle(t1, t2):
	return Polygon([t1,(t2[0],t1[1]),t2,(t1[0],t2[1])])

res1 = 0
res2 = 0
p = Polygon(tiles)
for i in range(len(tiles)):
	for j in range(i+1,len(tiles)):
		a = area(tiles[i], tiles[j])
		res1 = max(res1, a)
		if a > res2 and p.covers(rectangle(tiles[i], tiles[j])):
			res2 = a

print("Partie 1 :",res1)
print("Partie 2 :",res2)

print(f"[{int((time.time()-START_TIME)*1000)}ms]")
