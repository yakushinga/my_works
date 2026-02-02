from random import randint, choice
from string import ascii_uppercase
digits = "0123456789"
with open("tel.txt", "w") as f:
   s = ''
   while len(s) < 1000000:
     if randint(1,50) == 1:
       s += f'({randint(100, 999)})' + \
            f'{randint(100,999)}-{randint(1,99):02d}-{randint(1,99):02d}'
     s += choice(digits+'()'+ascii_uppercase)
   f.write(s)


