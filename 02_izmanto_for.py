#2) Atrast skaitļa n faktoriālu, ja n vērtību ievada no klaviatūras
#n! = 1* 2* 3* ... *n

n = int(input("Ievadi faktoriálu n: "))

f=1

for i in range(1, n+1):
     f= f*i 
    
print(f)