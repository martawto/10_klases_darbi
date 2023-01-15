# Atrast pirmo n saskaitāmo summu, ja n vērtību ievada no klaviatūras.
#  S= 3 + 6 + 9 + ...

n = int(input("Ievadi skaitli n:"))
summa = 0 #te tiks saskaitī visi virknes skaitļi
x = 3 #saskaitamais
i = 1 # skitītājs, kurš sekos līdzi, cik virknes locekļi ir saskaitīti

while i <= n:
    summa += x# saskaitam skaitļus, summa = summa + x
    x +=3 # jeb x=x+3
    i +=1 #palielinas par 1

print("Summa ir:", s)