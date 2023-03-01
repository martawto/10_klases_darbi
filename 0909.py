#Sastādīt programmu, kas ģenerē nejaušu skaitļu masīvu, kas satur skaitļus diapazonā no –
#10 līdz +10. Iegūto masīvu izvadīt ekrānā.

import random
a = []

for i in range(-10, 10):
    a.append(random.randrange(-10,10))

print(a)