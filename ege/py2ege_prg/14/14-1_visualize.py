data = []
for s in open('i/input_1.txt'):
  x, y = s.replace(',','.').split()
  data.append( (float(x), float(y)) )

from turtle import *
tracer(0)
up()
hideturtle()
scale, shiftX, shiftY = 50, 200, 250
for x, y in data:
  goto( x*scale-shiftX, y*scale-shiftY )
  dot( 3, 'black' )
done()
