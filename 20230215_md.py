# 4) klases un mājas uzdevums līdz nākamai stundai:
# a) sastādīt programmu, kas ģenerē sarakstu, kas satur n nejaušus skaitļus (skaitļu diapazons no -50 līdz +50, n ievada lietotājs 0<n<100),
# b) iegūto sarakstu izvadīt, 
# c) lietotājam tiek pajautāts ievadīt skaitli x un programmai jāatrod pirmo saraksta elementu, kas ir mazāks par x un jāizvada to, kā arī jāizvada šī elementa kārtas numurs sarakstā, 
# d) izmest no saraksta visas nulles, ja tādas ir, un iegūto sarakstu izvadīt,
# e) izmest no saraksta visus skaitļus, kas atkārtojas un iegūto sarakstu izvadīt.
# f) papildināt sarakstu ar tādu skaitli no intervāla -50 līdz +50, kurš nav atrodams esošajā sarakstā un izvadīt šo pievienojamo skaitli un iegūto sarakstu.

import random
saraksts = []
n = int(input("Cik skaitļus ģenerēsim, jāievēro 0<n<100?"))

 
for i in range(n):
    saraksts.append(random.randrange(-50,50))


print(saraksts)

#c)

x = int(input("Ievadi skaitli x: "))

for mazakais in saraksts:
    if mazakais < x:
        print("Skaitlis, kas mazāks par ", x , "ir", mazakais , "tā indekss", saraksts.index(mazakais) )
        break

#d)

bez0 = [ele.lstrip('0') for ele in saraksts]

print("Jaunais saraksts bez 0" , bez0)


        

