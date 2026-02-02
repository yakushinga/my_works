from random import choice
with open("data.txt", "w") as f:
   s = []
   for i in range(1000000):
     s += [choice("АЕЁИОУЫЭЮЯБВГДЖЗЙКЛМНПРСТФХЧЦШЩ")]
   f.write("".join(s))


