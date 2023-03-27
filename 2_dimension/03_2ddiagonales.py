import random

x=0

while x < 2 or x > 20:
    x = int(input("Ievadi skaitli x, kurs bus gan kolonnu, gan diognalu skaits, x jābūt lielākam par 1 un mazākam par 21: "))
    if x < 2:
        print("Ievadi citu skaitli.")
    if x > 20:
        print("Ievadi citu skaitli.")
    

saraksts = [[None] * x for i in range(x)]
print(saraksts)

for i in range(x):
    for j in range(x):
        saraksts[i][j] = random.randint(0,9)

print(saraksts)

for m in saraksts:
    for u in m:
        print(u, end=" ")
    print()

sum = 0

for i in range(x):
    sum = sum + saraksts[i][i]

print(sum)