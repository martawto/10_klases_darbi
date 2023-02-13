# 1. Definēsim jaunu sarakstu un aizpildīsim to ar n nejaušiem skaitļiem no 1-20, n jāpajautā ievadīt lietotājam
import random
valerija = []
n = int(input("Cik skaitļus ģenerēsim?"))
 
for i in range(n):
    #print(random.randrange(0,21), end=",")
    valerija.append(random.randrange(0,21))

print(valerija) 
print(type(valerija))

# 2. Izvadīsim iegūto sarakstu
print(valerija) 
print(type(valerija))


# 3. Izvadīsim 1-mo saraksta elementu
print(valerija[0]) 

# 4. Izvadīsim pēdējo saraksta elementu
print(valerija[-1])

# 5. Izvadīsim iepriekšpēdējo saraksta elementu
print(valerija[-2])

# 6. Pievienosim sarakstam lietotāja ievadītu skaitli X
x = int(input("Ievadi skaitli: "))
valerija.append(x)

# 7. Izvadīsim iegūto sarakstu ar jauno skaitli
print(valerija)

# 8. Izdzēsīsim no saraksta pirmo elementu
valerija.pop(0)

# 9. Izvadīsim tagad iegūto sarakstu 
print(valerija)

# 10. Izvadīsim katru trešo saraksta elementu
print("Katrais trešais saraksta elements", valerija[0::3])
# 11. Izveidosim jaunu sarakstu, kur ir tikai pāra skaitļi no sākuma saraksta un beigās izvadīsim to summu 
valerija1 = [x for x in valerija if x % 2 == 0]
print(" Pāra skaitļi", valerija1, "Summa", sum(valerija1))
# 12. Izveidosim jaunu sarakstu, kur ir tikai nepāra skaitļi no sākuma saraksta un beigās izvadīsim to summu 
valerija2 = [x for x in valerija if x % 2 != 0]
print(" Pāra skaitļi", valerija2, "Summa", sum(valerija2))

# 13. Izvadīsim tikai tos skaitļus, kas dalās ar 3 
valerija3 = [x for x in valerija if x % 3 == 0]
print(" Pāra skaitļi", valerija1, "Summa", sum(valerija3))

# 14. Visu saraksta skaitļu summu
print("Skaitļu summa: ", sum(valerija))
# 15. Visu saraksta skaitļu vidējo aritmētisko, noapaļotu līdz 2 zīmēm aiz komata
va = sum(valerija) / len(valerija)
print("Vidējais aritmētiskais: ", round(va, 2))
# 16. Cik reizes sarakstā ir sastopams skaitlis `7`
print("Cik ir skaitļu 7:", valerija.count(7))
# 17. Izvadīsim visus saraksta elementus sakārtotā augošā secībā 

# 18. Izvadīsim visus saraksta elementus sakārtotā dilstošā secībā