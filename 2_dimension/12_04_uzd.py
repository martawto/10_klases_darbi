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
skaitli = []
n = int(input("Cik nejaušus skaitļus ģenerēsi? "))

for i in range(n): skaitli.append(random.randint(0, 99))
print(skaitli)

darbsk = int(input("Kādu darbību izmantosi, '+' '-''/''**' ?"))