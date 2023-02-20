#5) Programma pieprasa n veselus skaitļus, saglabā tos masīvā un
#  paziņo, vai masīvā ir skaitlis,
#kas ir vienāds ar visu masīva elementu vidējo aritmētisko.


saraksts= []
saraksts2 = []

n = int(input("Cik skaitļus saglabāsi?"))

for i in range(n):
    jaut = int(input("Ievadi skaitli: "))
    saraksts.append(jaut)

videjais = sum(saraksts)// n 

for x in saraksts:
    if x == videjais:
        saraksts2.append(x)




print("Skaitļu skaits, kuri ir vienādi vidējo aritmētisko", videjais, "ir", len(saraksts2))