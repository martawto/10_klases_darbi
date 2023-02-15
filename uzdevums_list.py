#1) izveidot sarakstu (masīva elementa indekss sakrīt ar kalendāra datumu), kurā jāsaglabā janvāra mēneša prognozētās temperatūras (var izmantot datus, kurus var sameklēt internetā),

temperatura_diena = [0, 8, 9, 9, 2, -1, -11, -8, -3, -2, 2, 2, 6, 7, 6, 5, 5, 4, 4, 2, 3, 0, -2, -1, 0, 2, 2, 1, -1, -1, 2, 0]
temperatura_nakts = [0, 3, 2, 1, -1, -12, -14, -14, -8, -4, -3, 1, 1, 5, 4, 3, 2, 1, 0, -1, -2, -4, -6, -3, -3, 0, 1, -2, -3, -1, 2, 0 ]
temperatura = [] # temperatura dienas un nakts, tas ir diennakts vidējā

#2) vēlams saglabāt gan dienas, gan nakts temperatūru sarakstus (katru savā sarakstā) un rēķināt dienu vidējās temperatūras, kuras izmantotu tālāk uzdevumu risināšanā, 

for i in range(len(temperatura_diena)):
    temperatura.append(temperatura_diena[i] + temperatura_nakts[i]/2)
    print(i + 1, ". diena - ", temperatura[i]) 





sum = 0
for i in temperatura_diena:
    sum+= i

d = len(temperatura_diena)

diena=sum/d
print("Summa ", sum)
print("Mēneša vidēja dienas temperatūra ir", diena)

#3) aprēķināt mēneša vidējo temperatūru,

sum2 = 0
for i in temperatura_nakts:
    sum2+= i

d2 = len(temperatura_nakts)

nakts=sum2/d
print("Summa ", sum2)
print("Vidēja nakts temperatūra ir", nakts)

print("Mēneša vidējā temperatūra ir",  )


#4) siltāko dienu, 
#5) aukstāko dienu,
#6) izvadīt tikai katras nedēļas nogales dienu temperatūras (sestdienas, svētdienas) (uzdevuma risinājumā ir jāizmanto cikls),
for i in range (6, 10, 7):
    if i > 31:
        break
    print(i + 1,"diena"  , saraksts [i])
    print(i + 2,"diena"  , saraksts [i+1])

#7) noskaidrot siltāko nedēļas nogali un vēsāko, t.i. jāsalīdzina nedēļas nogaļu vidējās temperatūras.

