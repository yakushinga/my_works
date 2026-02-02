from random import randint, choice
digits = "0123456789"
rus = "АЕЁИОУЫЭЮЯБВГДЖЗЙКЛМНПРСТФХЧЦШЩ"
rusauto = "АВЕКМНОРСТУХ"
with open("auto.txt", "w") as f:
   s = ''
   while len(s) < 1000000:
     if randint(1,50) == 1:
       s += f'{choice(rusauto)}' + \
            f'{randint(100,999)}{choice(rusauto)}{choice(rusauto)}'
     s += choice(digits+rus)
   f.write(s)


