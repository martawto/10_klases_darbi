import random
marta = []
n = int(input("Cik skaitļus ģenerēsim?"))
for i in range(n):
    #print(random.randrange(0,21), end=",")
    marta.append(random.randrange(0,21))

print(marta) 
print(type(marta))