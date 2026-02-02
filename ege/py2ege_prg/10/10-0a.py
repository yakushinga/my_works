F = open("i/input_0.txt")
s = F.read()
F.close()
print( s )

print( '-----------------------' )
with open("i/input_0.txt") as F:
  s = F.read()
print( s )

print( '-----------------------' )
with open("i/input_0.txt") as F:
  while True:
    s = F.readline()
    if not s: break
    print( s )

print( '-----------------------' )
for s in open("i/input_0.txt"):
  print( s )

print( '-----------------------' )
for s in open("i/input_0.txt"):
  print( s.rstrip() )



