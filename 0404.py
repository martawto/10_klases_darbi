#4) Programma pieprasa n veselus skaitļus, saglabā tos masīvā un paziņo to skaitļu skaitu, kas
#ir mazāki par vidējo aritmētisko.

saraksts= []
saraksts2 = []

n = int(input("Cik skaitļus saglabāsi?"))

for i in range(n):
    jaut = int(input("Ievadi skaitli: "))
    saraksts.append(jaut)

videjais = sum(saraksts)// n 

for x in saraksts:
    if x < videjais:
        saraksts2.append(i)




print("Skaitļu skaits, kuri ir mazāki par vidējo aritmētisko", videjais, "ir", len(saraksts2))
