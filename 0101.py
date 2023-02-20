#1) Programma pieprasa n veselus skaitļus, saglabā tos masīvā un paziņo: vismazāko skaitli un
#tā indeksu (kārtas numuru).

n = int(input("Cik skaitļus ievadīsiet? "))

saraksts = []

for i in range(n):
    jaut = int(input("Ievadi skaitli: "))
    saraksts.append(jaut)

print("Mazākais skaitlis ir ", min(saraksts), ", indekss ", saraksts.index(min(saraksts)) )