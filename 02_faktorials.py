#2) Atrast skaitļa n faktoriālu, ja n vērtību ievada no klaviatūras
#n! = 1* 2* 3* ... *n

n = int(input("Ievadi faktoriálu n: "))

f = 1
while n >= 1:
    f*=n # f=4
    n-=1 # n=4

print("Skaitļa faktoriāls:", f)