#2) Pieprasīt masīvu, kas satur N dažādus veselus skaitļus, atrast lielākās un mazākās vērtības
#starpību.

n = int(input("Cik skaitļus ievadīsiet? "))

saraksts = []

for i in range(n):
    jaut = int(input("Ievadi skaitli: "))
    saraksts.append(jaut)

print("Lielākās vērtīas ", max(saraksts), " un mazākās vērtīas ", min(saraksts), "starpība ir", max(saraksts) - min(saraksts) )