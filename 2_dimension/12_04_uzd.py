# Sastādīt programmu, kas lietotājam piedāvā risināt matemātiskos uzdevumus,
# piem. skaitļi varētu tikt ģenerēti nejauši
# tiktu piedāvāta kāda no darbībām, piem. +,-, *, /, kāpināšana
# piem. 7 * 3 = , lietotājam jāievada atbilde.
# Ja ievada 21, tad programmas izvada PAREIZI, ja nē, tad var rīkoties dažādi - izvada NEPAREIZI,
# vai arī neizvada neko un piedāvā nākamo uzdevumu vai arī izvada nepareizi un piedāvā ievadīt atkārtoti u.tml.
# Būtiski ir lietotājam pajautāt kādā apjomā piedāvāt skaitļus, piem. līdz 10 vai 100 vai citādi
# Programmas beigās izvada pareizo un nepareizo atbilžu skaitu, iegūti vērtējumu %.
# Programma varētu piedāvāt uzdevumus līdz lietotājs atbild, ka vēlas beigt darbu.
# Visi uzdevumi un atbildes jāizvada gan uz ekrāna gan failā.
# Uzdevuma risinājumā jāpielieto funkcijas.
# Visu pārējo funkcionalitāti katrs var papildināt pats.

import random

def summa(x, y):
    rezult = x + y
    return rezult
def starpiba(x, y):
    rezult = x - y
    return rezult

def reizinajums(x, y):
    rezult = x * y
    return rezult

def dalijums(x, y):
    rezult = x / y
    return rezult

def kapinasana(x, y):
    rezult = x ** y
    return rezult





apjoms = 0

cik = int(input("Cik uzdevumus vēlies risināt?"))

while apjoms != 1 and apjoms != 2:
    print("Kādā apjomā vēlaties risināt? Ievadi 1 ja no 0-9 vai 2 ja no 0-20")
    apjoms = int(input("1 vai 2: "))

    if apjoms < 1:
         print("Esi ievadījis pārāk mazu skaitli! Ievadi atkārtoti!")
    if apjoms > 2:
         print("Esi ievadījis pārāk mazu skaitli! Ievadi atkārtoti!")


if apjoms == 1:
   apjoms = 9
if apjoms == 2:
    apjoms ==20

for i in range(cik):
    a= random.randint(0,apjoms)
    b = random.randint(0,apjoms)
    d = random.randint(1,3)


    if d == 1:
        print("Cik ir", a, " + ", b, "=")
        atb = int(input("Atbilde: "))

        if summa(a,b) == atb:
            print("Pareizi!")
        else:
            print("Nepareizi! Pareizā atbilde ir", summa(a, b))

    if d == 2:
        print("Cik ir", a, " - ", b, "=")
        atb = int(input("Atbilde: "))

        if starpiba(a,b) == atb:
            print("Pareizi!")
        else:
            print("Nepareizi! Pareizā atbilde ir", starpiba(a, b))

    if d == 3:
        print("Cik ir", a, " + ", b, "=")
        atb = int(input("Atbilde: "))

        if reizinajums(a,b) == atb:
            print("Pareizi!")
        else:
            print("Nepareizi! Pareizā atbilde ir", reizinajums(a, b))

    if d == 4:
        print("Cik ir", a, " : ", b, "=")
        atb = int(input("Atbilde: "))

        if reizinajums(a,b) == atb:
            print("Pareizi!")
        else:
            print("Nepareizi! Pareizā atbilde ir", reizinajums(a, b))