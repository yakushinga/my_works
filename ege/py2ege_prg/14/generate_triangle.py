from random import uniform, random
from math import sqrt, sin, cos, log, pi, radians

import math

def rotate_point( x, y, cx, cy, angle_degrees ):
    angle_radians = radians(angle_degrees)
    dx = x - cx
    dy = y - cy
    x_new = cx + dx * cos(angle_radians) - dy * sin(angle_radians)
    y_new = cy + dx * sin(angle_radians) + dy * cos(angle_radians)
    return (x_new, y_new)

# Box-Muller Transform
# https://en.wikipedia.org/wiki/Box%E2%80%93Muller_transform
def normal( average, dispersion ):
  u1 = uniform(0, 1)
  u2 = uniform(0, 1)
  return average + dispersion*sqrt(-2*log(u1)) * cos(2*pi*u2)

def point_in_triangle(pt1, pt2, pt3):
    """
    Random point on the triangle with vertices pt1, pt2 and pt3.
    """
    x, y = random(), random()
    q = abs(x - y)
    s, t, u = q, 0.5 * (x + y - q), 1 - 0.5 * (q + x + y)
    return (
        s * pt1[0] + t * pt2[0] + u * pt3[0],
        s * pt1[1] + t * pt2[1] + u * pt3[1],
    )

def dist( pt1, pt2 ):
  return ((pt1[0]-pt2[0])**2 + (pt1[1]-pt2[1])**2) ** 0.5

def point_in_triangle_normal(pt1, pt2, pt3):
   xc = (pt1[0] + pt2[0] + pt3[0]) / 3
   yc = (pt1[1] + pt2[1] + pt3[1]) / 3
   sigma = max( dist((xc,yc), p) for p in [pt1, pt2, pt3] ) / 3 * 1.5
   x = normal(xc, sigma)
   y = normal(yc, sigma)
   return (x, y)

def in_triangle_uniform( pt1, pt2, pt3, num_points ):
  points = [ point_in_triangle(pt1, pt2, pt3)
             for _ in range(num_points) ]
  return points

def is_in_triangle( pt, pt1, pt2, pt3 ):
  x1, y1 = pt1; x2, y2 = pt2; x3, y3 = pt3; xp, yp = pt
  # Calculate the cross products (c1, c2, c3) for the point relative to each edge of the triangle
  c1 = (x2 - x1) * (yp - y1) - (y2 - y1) * (xp - x1)
  c2 = (x3 - x2) * (yp - y2) - (y3 - y2) * (xp - x2)
  c3 = (x1 - x3) * (yp - y3) - (y1 - y3) * (xp - x3)
  # Check if all cross products have the same sign (inside the triangle) or different signs (outside the triangle)
  return (c1 < 0 and c2 < 0 and c3 < 0) or (c1 > 0 and c2 > 0 and c3 > 0)

def in_triangle_normal( pt1, pt2, pt3, num_points ):
  points = []
  while len(points) < num_points:
     pt = point_in_triangle_normal(pt1, pt2, pt3)
     if is_in_triangle( pt, pt1, pt2, pt3 ):
       points.append( pt )
  return points

def rotateAll( points, xCenter, yCenter, angle ):
  for i, p in enumerate(points):
    points[i] = rotate_point( p[0], p[1], xCenter, yCenter, angle )

def shiftAll( points, xCenter, yCenter ):
  for i, p in enumerate(points):
    points[i] = p[0]+xCenter, p[1]+yCenter

def writePoints( points, fName ):
  with open( fName, "w" ) as F:
    #print( "X\tY", file = F )
    for p in points:
      s = f"{p[0]}\t{p[1]}".replace('.',',')
      print( s, file = F )

from random import shuffle, randint

no = 99

for i, let in enumerate('ab'):
  N = [5000, 10000][i]
  K = [2, 3][i]
  if i == 0:
    pts = [ [(-1, 2), (-2, 10), (4, 10)],
            [(-1, 1.5), (4.2, 9.5), (3.5, 3.5)],
            ]
    shift = [0, 0]
    rotation = [3, 3, 160]
  else:
    pts = [ [(0, 2), (0, -2), (4, 0)],
            [(-1, 3), (5, 7), (-4, 8)],
            [(-1, 1), (-2, -4), (-7, 3)],
            ]
    shift = [0, 0]
    rotation = [4, 4, 0]
    K = 4
    pts = [ [(-1, -1), (6, -1), (2.5, 5)],
            [(-1, -0.5), (2.4, 5.2), (0.5, 7)],
            [(6, -0.5), (2.6, 5.2), (4.5, 7)],
            [(2.5, 5.5), (0.5, 7.3), (4.5, 7.3)],
            ]
    shift = [0, 0]
    rotation = [4, 4, -45]
  points = []
  for k in range(K):
    points.extend( in_triangle_normal( *pts[k], N//K) )
  rotateAll( points, *rotation )
  shiftAll( points, *shift )
  shuffle( points )
  writePoints( points, f'{no}\\27-{no}{let}.txt' )
