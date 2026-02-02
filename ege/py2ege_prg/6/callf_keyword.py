def F( a, b, c ):
  return a + b*c

#------------------------------

res = F( 1, 2, 3 )
print( res )

#------------------------------

res = F( c=3, b=2, a=1 )
print( res )

#------------------------------

names = [ 'c', 'b', 'a' ]
values = [ 3, 2, 1 ]
s = f"F( {names[0]}={values[0]}," + \
       f"{names[1]}={values[1]}," + \
       f"{names[2]}={values[2]} )"
res = eval( s )
print( res )

#------------------------------

args = { 'c': 3, 'b': 2, 'a': 1 }
res = F( **args )
print( res )

#------------------------------

names = [ 'c', 'b', 'a' ]
values = [ 3, 2, 1 ]

print( list( zip(names, values) ) )

args = dict( zip(names, values) )
res = F( **args )
print( res )

#------------------------------

def F( names, values ):
  var = dict( zip(names, values) )
  return var['a'] + var['b']*var['c']

names = [ 'c', 'b', 'a' ]
values = [ 3, 2, 1 ]
res = F( names, values )
print( res )
