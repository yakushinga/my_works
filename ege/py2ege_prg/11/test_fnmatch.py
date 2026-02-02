from fnmatch import fnmatch

files = [ 'rock.wav', 'moon.cab', 'gem.html', 'good.cpp' ]

for f in files:
  print( fnmatch( f, "g*.c??" ) )