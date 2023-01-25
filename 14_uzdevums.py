#Inta noguldīja bankā n latus. Pēc cik gadiem viņas noguldījums
# divkāršosies, ja
# pieaugums gadā ir p%?

n=float(input("Cik latus noguldīsi: "))
p=float(input("Kāds ir pieaugums gadā %: "))

gadi=0
sum=n

while sum < 2*n:
    sum = p * sum / 100 + sum
    gadi = gadi + 1
print("Summa pēc", gadi, "gadiem būs", sum)

