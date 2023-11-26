#delaunay triangulation
import matplotlib.pyplot as plt
import random
import math
from math import *

defaultBounds = [[0, 200], [200, 0]]

baseDelaunayPoints = [[10, 10], [20,20], [10, 20], [20, 10]]

nPoints = 4#random.randint(3, 5)
points = []
triangles = []

def distance(x1, y1, x2, y2):
	return (((x1 - x2) ** 2) + ((y1 - y2) ** 2)) ** 0.5

def distanceTargetSort(target, array): 
		n = len(array)
	
		for i in range(n):
			for j in range(0, n - i - 1):
				point1 = array[j]
				point2 = array[j + 1]

				distance1 = distance(target[0], target[1], point1[0], point1[1])
				distance2 = distance(target[0], target[1], point2[0], point2[1])

				if distance1 > distance2:
					array[j], array[j + 1] = array[j + 1], array[j]

for i in range(0, nPoints):
	n1 = int(random.random() * 200)
	n2 = int(random.random() * 200)
	points.append([n1, n2])

n = len(points)
for i in range(n):
	for j in range(0, n - i - 1):
		if points[j][0] > points[j + 1][0]:
			points[j], points[j + 1] = points[j + 1], points[j]

for point1 in points:
	points2 = points.copy()
	distanceTargetSort(point1, points2)
	point2 = points2[1]
	point3 = points2[2]
	point4 = points2[3]
	p1p2Dist = distance(point1[0], point1[1], point2[0], point2[1])
	p1p3Dist = distance(point1[0], point1[1], point3[0], point3[1])
	p2p4Dist = distance(point2[0], point2[1], point4[0], point4[1])
	p3p4Dist = distance(point3[0], point3[1], point4[0], point4[1])
	
	if math.degrees(abs(math.atan2(p1p2Dist, p2p4Dist) - math.atan2(p1p3Dist, p3p4Dist))) <= 180:
		print("<= 180")		
		triangles.append([point1, point2, point4])
		triangles.append([point1, point3, point4])
	else:
		print("> 180")		
		triangles.append([point2, point3, point1])
		triangles.append([point2, point3, point4])




plt.figure(figsize=(7, 7))
plt.ylim(defaultBounds[1][1], defaultBounds[1][0])
plt.xlim(defaultBounds[0][0], defaultBounds[0][1])

for point in points:
	plt.plot(point[0], point[1], "ro")

for point in baseDelaunayPoints:
		plt.plot(point[0], point[1], "go")


if triangles.__len__() > 0:
	for tri in triangles:
		plt.plot([tri[0][0], tri[1][0], tri[2][0], tri[0][0]], [tri[0][1], tri[1][1], tri[2][1], tri[0][1]], "-yo")

plt.show()
