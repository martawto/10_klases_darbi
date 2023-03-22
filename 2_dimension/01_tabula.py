
rindas, kolonas = 3, 4
burti = [[None] * kolonas for i in range(rindas)]


burti[0] = "A", "B", "C", "D"
burti[1] = "E", "F", "G", "H" 
burti[2] = "I", "J", "K", "L"

print(burti)

for i in burti:
    for e in i:
        print(e, end=" ")
    print()





