#6) Programma pieprasa n veselus skaitļus, 
# saglabā tos masīvā un izveido jaunu masīvu, kas
#satur dotā masīva negatīvos skaitļus.

saraksts= []
saraksts2 = []

n = int(input("Cik skaitļus saglabāsi?"))

for i in range(n):
    jaut = int(input("Ievadi skaitli: "))
    saraksts.append(jaut)

for x in saraksts:
    if x < 0:
        saraksts2.append(x)

print("Negatīvie skaitļi", saraksts2)