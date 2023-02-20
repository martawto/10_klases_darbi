#3) Sastādīt programmu, kas pieprasa ievadīt 10 skaitļus un paziņo kurš no skaitļiem ir
#mazākais (ievadīto skaitļu vērtības saglabāt masīvā).


saraksts = []

for i in range(10):
    jaut = int(input("Ievadi skaitli: "))
    saraksts.append(jaut)

print("Mazākais skaitlis ir ", min(saraksts))