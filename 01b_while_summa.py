# Atrast pirmo n saskaitāmo summu, ja n vērtību ievada no klaviatūras.
# S= 1 + 1* 2 + 1* 2* 3 + .... + 1* 2* 3 *.... *n

# ja piem n ir 4, tas summa ir 1 + 2 + 6 = 9


n = int(input("Ievadi skaitli n:"))
summa = 0 #te tiks saskaitī visi virknes skaitļi
x = 1 #saskaitamais
i = 1 # skitītājs, kurš sekos līdzi, cik virknes locekļi ir saskaitīti

while i <= n:
    x *=i # jeb x=x+3
    i +=1 #palielinas par 1
    summa += x# saskaitam skaitļus, summa = summa + x


print("Summa ir:", summa)