#Atrast skaitļa n faktoriālu, ja n vērtību ievada no klaviatūras
#n! = 1*2*3* ... *n
skaitlisn=int(input("Ievadi n vērtību:"))

faktorials=1
n=0
i=1
while i <= skaitlisn:
    n=faktorials*i
    i+=1
    print(n)
    
