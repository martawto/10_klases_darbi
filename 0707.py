#Pieprasīt masīvu, kas satur N veselus skaitļus, paziņot, kādu skaitļu tajā vairāk: pāra vai nepāra.

import random
masivs = []

n = int(input("Cik skaitļus ģenerēsim?"))
 
for i in range(n):
    jaut = int(input("Ievadi skaitli: "))
    masivs.append(jaut)

masivs2 = [x for x in masivs if x % 2 == 0]
print(" Pāra skaitļi", masivs2)

masivs1 = [x for x in masivs if x % 2 != 0]
print(" Pāra skaitļi", masivs1)