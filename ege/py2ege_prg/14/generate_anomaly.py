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

def in_ellipse_uniform( x0, y0, a, b, N, angle = 0 ):
  points = []
  while len(points) < N:
    x = uniform( x0 - a, x0 + a)
    y = uniform( y0 - b, y0 + b)
    if ((x-x0)** 2)/(a**2) + ((y-y0)**2)/(b**2) <= 1:
      x, y = rotate_point( x, y, x0, y0, angle )
      points.append( (x, y) )
  return points

# Box-Muller Transform
# https://en.wikipedia.org/wiki/Box%E2%80%93Muller_transform
def normal( average, dispersion ):
  u1 = uniform(0, 1)
  u2 = uniform(0, 1)
  return average + dispersion*sqrt(-2*log(u1)) * cos(2*pi*u2)

def in_ellipse_normal(x0, y0, a, b, num_points, angle = 0):
  points = []
  d = sqrt(a**2 + b**2)
  while len(points) < num_points:
     # Generate random radius values based on a probability distribution
    r = normal(0, 0.5*d)  # Normal distribution, mean 0, std 1
    theta = uniform(0, 2*pi)  # Random angle
     # Compute Cartesian coordinates from polar coordinates
    x = r * cos(theta)
    y = r * sin(theta)
     # Apply the ellipse transformation
    x_ellipse = x0 + (a*x) / (d + 1e-10)  # Avoid division by zero
    y_ellipse = y0 + (b*y) / (d + 1e-10)

     # Check if the point is inside the ellipse
    if (((x_ellipse - x0)**2) / (a**2) + ((y_ellipse - y0)**2) / (b**2)) <= 1:
      x_ellipse, y_ellipse = rotate_point( x_ellipse, y_ellipse, x0, y0, angle )
      points.append((x_ellipse, y_ellipse))

  return points

def writePoints( points, fName ):
  with open( fName, "w" ) as F:
    #print( "X\tY", file = F )
    for p in points:
      s = f"{p[0]}\t{p[1]}".replace('.',',')
      print( s, file = F )

def readPoints( fName ):
  points = []
  for s in open( fName ):
    x, y = s.replace(',','.').split()
    points.append( (float(x), float(y)) )
  return points

from random import shuffle, randint

no = 99

for i, let in enumerate('ab'):
  #if i == 0: continue
  fName = f'{no}\\27-{no}{let}.txt'
  points = readPoints( fName )
  centers = []
  if i == 0:
    cntAnomaly = [8, 6]
    centers = [ (0, 2), (7, 8) ]
  else:
    cntAnomaly = [4, 3, 2, 5]
    centers = [ (1.2, 2.5), (4, 7), (8, 8.5), (7.5, 2.5) ]
  na = len(cntAnomaly)
  points = points[:len(points)-sum(cntAnomaly )]
  for k in range(na):
    points.extend( in_ellipse_normal( centers[k][0], centers[k][1], 1, 1, cntAnomaly[k] ) )
  shuffle( points )
  writePoints( points, fName )
