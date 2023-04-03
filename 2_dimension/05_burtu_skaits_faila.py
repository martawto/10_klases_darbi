MAPE = "2_dimension/"
f = open(MAPE + "teksts.txt", "r")
a = f.read()

#1.izvadam visu nolasīto uzreiz
print(a)

#2.izvadam nolasīto saturu pa 1 simbolam  - dotajā gadījumā katrs simbols jaunā rindā
for i in range(len(a)):
    print(a[i])

# 3. izvadam nolasīto saturu pa 1 simbolam - dotajā gadijumā simboli viens aiz otra
for i in range(len(a)):
    print(a[i], end="")

# 1.uzd atrisinājums

a_skaits = 0
print()
for i in range(len(a)):
    if(a[i].lower() == 'a'):
        a_skaits += 1
print("a vai A burti tekstā bija", a_skaits, "reizes.")

# 2) cik tekstā ir simboli kopā,
 
skaits=len(a)
print("Simbolu skaits failā", skaits)

# 3) Cik tekstā ir vārdu?

skaitsvardu = len(a.split())
print("Vārdu skaits:", skaitsvardu)

# 4) Cik tekstā ir pieturzīmes?
count=0
for i in range (0, len(a)):
    if a[i] in ('!', "," ,"\'" ,";" ,"\"", ".", "-" ,"?"): 
        count = count + 1
    
print("Pieturzīmes", count)