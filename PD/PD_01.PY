marta = 9 + 2 + 2006

print(marta)


import random
vainina = []

for i in range (marta) :
    vainina.append(random.randrange(-150, 150))



print(vainina)



for pos in vainina:
    if pos > 0:
        i = i+1
    
print("Pozitīvo skaitļu skaits,", i)


for neg in vainina:
    if neg < 0:
        i = i+ 1

print("Negatīvo skaitļu skaits, ", i)


for negativie in vainina:
    if negativie < 0:
        print(negativie , end= ", ")




va = sum(vainina) / len(vainina)
print("Vidējais aritmētiskais: ", round(va, 2))


#7

odds = []
for odd in vainina:
    if odd % 2 !=0:
       odds.append(odd) 

print("7 uzd",odds)
    




for dz_dat in vainina:
    if dz_dat == 9:
        print("Skaitlis ir sastopams", vainina.count(9), "reizes")
        break
    else:
        print("Tāda skaitļa nav") 
        break


#9
mazak_viejo = []

for x in vainina:
    if x < va:
        mazak_viejo.append(x)

print(mazak_viejo)

#10





#12
vainina.sort()
print("Elementi augošā secībā", vainina)


#13
vainina2 = []

for x in vainina:
    if x // 5 and 3:
        vainina2.append(x)

print("Dalās ar 3 un 5", vainina2)


#14
rows = 8
cols = 16
vainina3 = [[1]*cols]*rows

print( vainina3)