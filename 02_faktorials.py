n = int(input("Ievadi faktoriálu n: "))

f = 1
while n >= 1:
    f*=n # f=4
    n-=1 # n=4

print("Skaitļa faktoriāls:", f)