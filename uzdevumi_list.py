# 1. Definēsim jaunu sarakstu un aizpildīsim to ar n 
#nejaušiem skaitļiem no 1-20, n jāpajautā ievadīt lietotājam
import random
marta = []
n = int(input("Cik skaitļus ģenerēsim?"))
 
for i in range(n):
    #print(random.randrange(0,21), end=",")
    marta.append(random.randrange(0,21))

print(marta) 
print(type(marta))

# 2. Izvadīsim iegūto sarakstu
print(marta) 
print(type(marta))


# 3. Izvadīsim 1-mo saraksta elementu
print(marta[0]) 

# 4. Izvadīsim pēdējo saraksta elementu
print(marta[-1])

# 5. Izvadīsim iepriekšpēdējo saraksta elementu
print(marta[-2])

# 6. Pievienosim sarakstam lietotāja ievadītu skaitli X
x = int(input("Ievadi skaitli: "))
marta.append(x)

# 7. Izvadīsim iegūto sarakstu ar jauno skaitli
print(marta)

# 8. Izdzēsīsim no saraksta pirmo elementu
marta.pop(0)

# 9. Izvadīsim tagad iegūto sarakstu 
print(marta)

# 10. Izvadīsim katru trešo saraksta elementu
print("Katrais trešais saraksta elements", marta[0::3])
# 11. Izveidosim jaunu sarakstu, kur ir tikai pāra skaitļi no sākuma saraksta un beigās izvadīsim to summu 
marta1 = [x for x in marta if x % 2 == 0]
print(" Pāra skaitļi", marta1, "Summa", sum(marta1))
# 12. Izveidosim jaunu sarakstu, kur ir tikai nepāra skaitļi no sākuma saraksta un beigās izvadīsim to summu 
marta2 = [x for x in marta if x % 2 != 0]
print(" Pāra skaitļi", marta2, "Summa", sum(marta2))

# 13. Izvadīsim tikai tos skaitļus, kas dalās ar 3 
marta3 = [x for x in marta if x % 3 == 0]
print(" Pāra skaitļi", marta1, "Summa", sum(marta3))

# 14. Visu saraksta skaitļu summu
print("Skaitļu summa: ", sum(marta))
# 15. Visu saraksta skaitļu vidējo aritmētisko, noapaļotu līdz 2 zīmēm aiz komata
va = sum(marta) / len(marta)
print("Vidējais aritmētiskais: ", round(va, 2))
# 16. Cik reizes sarakstā ir sastopams skaitlis `7`
print("Cik ir skaitļu 7:", marta.count(7))
# 17. Izvadīsim visus saraksta elementus sakārtotā augošā secībā 
marta.sort()
print("Elementi augošā secībā", marta)
# 18. Izvadīsim visus saraksta elementus sakārtotā dilstošā secībā
marta.sort(reverse = True)
print("Elementi dilstošā secībā", marta)