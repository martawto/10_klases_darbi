MAPE = "2_dimension/" # šo nevajag, ja viņi neatrastos mapē apakšmapē. Ja atrastos galvenajā mapē - viss izvadītos.

f = open(MAPE + "teksts.txt", "r", encoding="utf-8") # encoding atļauj izvadīt tekstus ar garumzīmēm un mīkstinājumiem.
# print(f.read()) # => izvada visu uzreiz.
# print(f.read(8)) => izvada noteiktu elementu skaitu.
# print(f.readline()) => pa rindiņām

for i in f: # rindas var izvadīt ciklā
    print(i, end="") 

print("\nTekstā burts 'a' sastopams:", i.count("a"), "reizes.")

#for j in f:
#    print(j[1], end="") => izvada pēc indeksa no katras rinads, piemēram, 1. elementu.

f.close() # beidz darbu ar failu.

