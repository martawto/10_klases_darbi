
import random

rindas, kolonas, = 4, 5,
# skaitli = [[None] * kolonas for i in range(rindas)]
skaitli2 = []


for j in range(0,10):
    for i in range(0,6):
        skaitli[i]=random.randrange(0,4,1)
print(skaitli)
skaitli2.append(skaitli)

vai

import random

arr2=[]

for j in range(0,10):
  arr = [random.randrange(10) for _ in range(6)]
  print(arr)
  arr2.append(arr)

print(arr2)

#   i,j: integer;
# begin
#   randomize;
#   for i:=1 to 4 do
#       for j:=1 to 5 do
#           t[i,j]:=random(99);

#   for i:=1 to 4 do
#       begin
#       for j:=1 to 5 do
#           write(t[i,j]:3);
#       writeln;
#       end;

# readln;
# end.


