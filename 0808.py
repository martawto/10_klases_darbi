#Sastādīt programmu, kas ģenerē nejaušu skaitļu masīvu A, kas satur n elementus.
#Noteikt, vai tajā ir negatīvi elementi. Skaitļu masīvu arī izvadīt uz ekrāna.

import random
a = []
n = int(input("Cik skaitļus ģenerēsim?"))
 
for i in range(n):
    a.append(random.randrange(-100,101))

print(a)
negativi = []
for x in a:
    if x < 0:
        negativi.append(x)
        
        

print("Negatīvie elementi ", negativi)