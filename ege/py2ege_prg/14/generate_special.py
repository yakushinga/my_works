from random import uniform
from math import sqrt, sin, cos, log, pi, radians

import math

def rotate_point( x, y, cx, cy, angle_degrees ):
    angle_radians = radians(angle_degrees)
    dx = x - cx
    dy = y - cy
    x_new = cx + dx * cos(angle_radians) - dy * sin(angle_radians)
    y_new = cy + dx * sin(angle_radians) + dy * cos(angle_radians)
    return (x_new, y_new)

def in_ellipse_uniform( x0, y0, a, b, N, angle = 0, Rbend = 0 ):
  points = []
  while len(points) < N:
    x = uniform( x0 - a, x0 + a)
    y = uniform( y0 - b, y0 + b)
    if ((x-x0)** 2)/(a**2) + ((y-y0)**2)/(b**2) <= 1:
      if Rbend:
        x, y = rotate_point( x, y, 0, 0, (x/Rbend)*180/pi )
      x, y = rotate_point( x, y, x0, y0, angle )
      points.append( (x, y) )
  return points

# Box-Muller Transform
# https://en.wikipedia.org/wiki/Box%E2%80%93Muller_transform
def normal( average, dispersion ):
  u1 = uniform(0, 1)
  u2 = uniform(0, 1)
  return average + dispersion*sqrt(-2*log(u1)) * cos(2*pi*u2)

def in_ellipse_normal(x0, y0, a, b, num_points, angle = 0, Rbend = 0):
  points = []
  d = sqrt(a**2 + b**2)
  while len(points) < num_points:
     # Generate random radius values based on a probability distribution
    r = normal(0, d/2 if num_points < 100 else d )  # Normal distribution, mean 0, std 1
    r = normal(0, 100 )  # Normal distribution, mean 0, std 1
    theta = uniform(0, 2*pi)  # Random angle
     # Compute Cartesian coordinates from polar coordinates
    x = r * cos(theta)
    y = r * sin(theta)
     # Apply the ellipse transformation
    x_ellipse = (a*x) / (d + 1e-10)  # Avoid division by zero
    y_ellipse = (b*y) / (d + 1e-10)

     # Check if the point is inside the ellipse
    if ((x_ellipse**2) / (a**2) + (y_ellipse**2) / (b**2)) <= 1:
      if Rbend:
        x_ellipse, y_ellipse = rotate_point( x_ellipse, y_ellipse, 0, 0,
                                            (x_ellipse/Rbend)*180/pi )
      x_ellipse, y_ellipse = rotate_point( x_ellipse, y_ellipse, 0, 0, angle )
      points.append((x0+x_ellipse, y0+y_ellipse))

  return points

def rotateAll( points, xCenter, yCenter, angle ):
  for i, p in enumerate(points):
    points[i] = rotate_point( p[0], p[1], xCenter, yCenter, angle )

def writePoints( points, fName ):
  with open( fName, "w" ) as F:
    #print( "X\tY", file = F )
    for p in points:
      s = f"{p[0]}\t{p[1]}".replace('.',',')
      print( s, file = F )

def cloudsXYSeparable( clouds ):
  def separ123( i0, i1, i2 ):
    sep1x = r[i0] < min(l[i1], l[i2]) or l[i0] > max(r[i1],r[i2])
    sep1y = t[i0] < min(b[i1], b[i2]) or b[i0] > max(t[i1],t[i2])
    sep23y = t[i1] < b[i2] or t[i2] < b[i1]
    sep23x = l[i1] > r[i2] or l[i2] > r[i1]
    return (sep1x and sep23y) or (sep1y and sep23x)
  K = len(clouds)
  l = [ clouds[i][0]-clouds[i][2] for i in range(K) ]
  r = [ clouds[i][0]+clouds[i][2] for i in range(K) ]
  t = [ clouds[i][1]+clouds[i][3] for i in range(K) ]
  b = [ clouds[i][1]-clouds[i][3] for i in range(K) ]
  if K == 2:
    sep1x = r[0] < l[1] or l[0] > r[1]
    sep1y = t[0] < b[1] or b[0] > t[1]
    return sep1x or sep1y
  else:
    return separ123(0, 1, 2) or separ123(1, 0, 2) or separ123(2, 0, 1)

def cloudsIntersect( cloud1, cloud2 ):
  x1, y1, a1, b1 = cloud1
  x2, y2, a2, b2 = cloud2
  d = ((x2 - x1)**2 + (y2 - y1)**2) ** 0.5
  r_horizontal = a1 + a2
  r_vertical = b1 + b2
  if K == 2:
    return d < 1.5*r_horizontal and d < 1.5*r_vertical
  else:
    return d < 1.2*r_horizontal and d < 1.2*r_vertical

def cloudsNotIntersected( clouds ):
  K = len(clouds)
  for i in range(K):
    for j in range(i+1, K):
      if cloudsIntersect( clouds[i], clouds[j] ):
        return False
  return True

def genClouds( x0, y0, K ):
  clouds = [ [0, 0, 0, 0] for i in range(K) ]
  while True:
    for k in range(K):
      clouds[k][0] = uniform( x0-3, x0+3 )
      clouds[k][1] = uniform( y0-3, y0+3 )
      clouds[k][2] = uniform( 1, 1.5 )
      clouds[k][3] = uniform( 1, 1.5 )
    #if cloudsXYSeparable( clouds ):
    if not cloudsXYSeparable( clouds ) and cloudsNotIntersected( clouds ):
       print( clouds )
       return clouds

from random import shuffle, randint

no = 99

for i, let in enumerate('ab'):
  N = [1000, 10000][i]
  K = [2, 3][i]
  if i == 0:
    clouds = [ [8, 4, 5, 1],
               [1, 5, 5, 1]   ]
    angles = [ 100, 300 ]
    Rbend = [ 7, 7 ]
    rotation = [4, 5, -50]

    clouds = [ [2.9, 8.7, 6, 1],
               [6.25, 1.8, 5, 1]   ]
    angles = [ 20, 0 ]
    Rbend = [ -5, 4 ]
    rotation = [0, 0, 0]

    # Задания для самостоятельной работы
    clouds = [
               [7, 4.7, 2.5, 0.75],
               [2, 6.3, 6, 1],
             ]
    angles = [ 50, 70 ]
    Rbend = [ 3, -7 ]
    rotation = [4, 4, 170]

    clouds = [
               [4, 3, 7, 1],
               [5.5, 6, 7, 1],
             ]
    angles = [ 0, 0 ]
    Rbend = [ -15, 15 ]
    rotation = [4, 4.5, -45]

    K = 1
    clouds = [
               [2, 2, 1, 1],
             ]
    angles = [ 0 ]
    Rbend = [ 0 ]
    rotation = [0, 0, 0]

  else:
    clouds = [
               [3.3, 8.5, 1.5, 1.5],
               [1.5, 1.5, 1.5, 1.5],
               [6.6, 5, 1.2, 1.5],
             ]
    angles = [ 0, 0, 0 ]
    Rbend = [ 0, 0, 0 ]
    clouds = [
               [2, 5, 2, 1],
               [3, 8, 4, 1],
               [4.5, 3.5, 3, 0.75],
             ]
    angles = [ -75, -75, 65 ]
    Rbend = [ 0, 0, 0 ]
    clouds = [
               [8, 5.7, 2.5, 0.75],
               [2, 6.3, 5.5, 1],
               [5.4, 2.6, 4.5, 0.75],
             ]
    angles = [ 50, 70, -30 ]
    Rbend = [ 3, -7, 4.5 ]
    rotation = [0, 0, 0]
    clouds = [
               [2, 4, 1, 3.2],
               [4, 9, 4, 1],
               [6, 6, 2.5, 0.8],
             ]
    angles = [ 0, 0, 0 ]
    Rbend = [ 0, 0, 0 ]
    rotation = [0, 0, 0]
    # Задачи для самостоятельного решения
    clouds = [
               [3.3, 8.5, 2, 2],
               [1.5, 2.5, 2, 2],
               [7.3, 5, 2, 2],
             ]
    angles = [ 0, 0, 0 ]
    Rbend = [ 0, 0, 0 ]
    rotation = [4, 4, 45]

    clouds = [
               [8, 5.7, 2.5, 0.75],
               [2, 6.3, 5.5, 1],
               [5.4, 2.6, 4.5, 0.75],
             ]
    angles = [ 50, 70, -30 ]
    Rbend = [ 3, -7, 4.5 ]
    rotation = [4, 4, 45]

    K = 4
    clouds = [
               [0, 3, 5, 1],
               [2, -2, 5, 1],
               [-4, -4, 7, 1],
               [5.5, 6, 7, 1],
             ]
    angles = [ 45, 45, -70, -70 ]
    Rbend = [ 0, 0, -15, 15 ]
    rotation = [5, 5, 90]

    K = 3
    clouds = [
               [8, 5.7, 2.5, 0.75],
               [2, 6.3, 5.5, 1],
               [5.4, 2.6, 4.5, 0.75],
             ]
    angles = [ 50, 70, -30 ]
    Rbend = [ 3, -7, 4.5 ]
    rotation = [4, 4, 90]

    K = 3
    clouds = [
               [8, 5.7, 2, 1],
               [2, 6.3, 1, 2],
               [5.4, 2.6, 2, 2],
             ]
    angles = [ 0, 0, 0 ]
    Rbend = [ 0, 0, 0 ]
    rotation = [0, 0, 00]

  points = []
  for k in range(K):
    points.extend( in_ellipse_normal( clouds[k][0], clouds[k][1],
                               clouds[k][2], clouds[k][3], N//K,
                               angles[k], Rbend[k] ) )
  for i, p in enumerate(points):
    points[i] = ( p[0]*8/10, p[1] )
  rotateAll( points, *rotation )
  shuffle( points )
  writePoints( points, f'{no}\\27-{no}{let}.txt' )
