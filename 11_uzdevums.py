#Sastādīt tabulu jūdžu pārveidošanai kilometros, 
# attālumam no 5 līdz 7,5 jūdzēm ar soli h 
# (1 jūdze = 1,609 km).

h=float(input("Ievadi soļa lielumu: "))

judze = 1.609
x=5
b=7.5

print("jūdzes \t| km")
print("--------------")

while x <= b:
    print(round(x, 2), " \t| ",round( x * judze, 2))
    x += h