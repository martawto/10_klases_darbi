#4) Dotai naturālai x vērtībai, ko ievada no klaviatūras Atrast
# s=1 + 1/2 + 1/4 + 1/8  ..... + 1/2^n

n = int(input("Ievadi n: "))

sum=0

for i in range(n+1):
    sum = sum + 1/2**i

print("Summa ir ", sum)

#parbaude: s = 0, i = 0, s = 0 + 1 =1
#          s = 1, i = 1, ja i >= n, tad cikls beidz darbu, lidz ar to atbilde 1 nav pareizi
# labot var beigu vērtību n+1
# #parbaude: s = 0, i = 0, s = 0 + 1 =1
#          s = 1, i = 1, ja i >= n, tad tiek turpinats cikls, jo 1< 2
# cikla range beigu vertiba ir 2, jo n bija 2 un 1+ 1 = 2
