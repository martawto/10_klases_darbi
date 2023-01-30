#16) Sportists pirmajā dienā noskrien n km. 
# Katrā nākamajā dienā viņš noskrien par p%
# vairāk nekā iepriekšējā.
# a) Kurā dienā pēc treniņu sākuma viņš noskries vismaz k km?
# b) Cik dienās pēc treniņu sākuma viņš noskries vismaz k km?

n=float(input("Cik pirmajā dienā noskrēji km:"))
p=float(input("Par cik % vairāk noskrēji nākamajā dienā:"))
k=float(input("Cik jānoskrien vismaz: "))

dienas=1
i=1

while i < k:
    i = p * i 
    dienas = dienas + 1
print("Vismaz ", k, "km tika noskrieti", dienas,". dienās, noskrēja",dienas, "dienās.")

