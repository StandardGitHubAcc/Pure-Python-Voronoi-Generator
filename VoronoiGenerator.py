#https://stackoverflow.com/questions/28504737/how-to-plot-a-single-point-in-matplotlib
#https://www.geeksforgeeks.org/create-2d-pixel-plot-in-python/
#https://stackoverflow.com/questions/66238749/how-to-find-the-closest-coordinate-from-a-list-of-points
#https://www.geeksforgeeks.org/sorting-algorithms-in-python/

import numpy as np
import matplotlib.pyplot as plt
#import math

defaultBounds = [[0, 200], [200, 0]]

points = [(50, 50), (25, 25), (75, 75), (98, 70)]
#points = [(50, 50), (25, 25), (75, 75)]
data = []
#cell = []
cell = {}
intersection3Points = {}

def distance(x1, y1, x2, y2):
	return (((x1 - x2) ** 2) + ((y1 - y2) ** 2)) ** 0.5

def bubbleSort(arr): #Not used but a good template
     
    n = len(arr)
 
    # For loop to traverse through all 
    # element in an array
    for i in range(n):
        for j in range(0, n - i - 1):
             
            # Range of the array is from 0 to n-i-1
            # Swap the elements if the element found 
            #is greater than the adjacent element
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

def distanceTargetSort(target, array):
	n = len(array)
	
	for i in range(n):
		for j in range(0, n - i - 1):
			point1 = array[j]["midpoint"]
			point2 = array[j + 1]["midpoint"]

			distance1 = distance(target[0], target[1], point1[0], point1[1])
			distance2 = distance(target[0], target[1], point2[0], point2[1])

			if distance1 > distance2:
				array[j], array[j + 1] = array[j + 1], array[j]
			

def intersectSolver(line1, line2):
	midPt1 = line1["midpoint"]
	midPt2 = line2["midpoint"]

	slope1 = line1["slope"]
	slope2 = line2["slope"]

	if slope1 != slope2:

		#x = (midPt1[0] * slope1) - (midPt2[0] * slope2) - midPt1[1] + midPt2[1]
		#y = slope1 * (x - midPt1[0]) + midPt1[1]

		#x = ( (slope1 * midPt1[0]) - (slope2 * midPt2[0]) + midPt1[1] - midPt2[1]) / (slope1 - slope2)
		#y = slope1 * (x - midPt1[0]) + midPt1[1]

		yInt1 = (slope1 * -1 * midPt1[0]) + midPt1[1]
		yInt2 = (slope2 * -1 * midPt2[0]) + midPt2[1]

		x = (yInt2 - yInt1) / (slope1 - slope2)
		y = (slope1 * x) + yInt1

		#print(f"intersect of y = {slope1}(x - {midPt1[0]}) + {midPt1[1]} and y = {slope2}(x - {midPt2[0]}) + {midPt2[1]} is ({x}, {y})")
		
		if (x > line1["boundA"][0] and x < line1["boundB"][0] and y < line1["boundA"][1] and y > line1["boundB"][1]) and (x > line2["boundA"][0] and x < line2["boundB"][0] and y < line2["boundA"][1] and y > line2["boundB"][1]):
			return x, y
		else:
			#print(f'intersection is out of bounds ({line1["boundA"][0]}, {line1["boundA"][1]}) ({line1["boundB"][0]}, {line1["boundB"][1]}) or ({line2["boundA"][0]}, {line2["boundA"][1]}) ({line2["boundB"][0]}, {line2["boundB"][1]})')
			return (None, None)
	else:
		#print(f"there is no interesection of y = {slope1}(x - {midPt1[0]}) + {midPt1[1]} and y = {slope2}(x - {midPt2[0]}) + {midPt2[1]} or they are the same equation")
		return (None, None)


def equationToPoint(equation, x):
	return equation["slope"] * (x - equation["midpoint"][0]) + equation["midpoint"][1]
	
def setDefaultBounds(slope, mPtX, mPtY, givenBounds):#, lineBounds):
	leftBound = givenBounds[0][0]
	topBound = givenBounds[0][1]
	rightBound = givenBounds[1][0]
	bottomBound = givenBounds[1][1]

	pointA = (0, 0)#lineBounds[0]
	pointB = (0, 0)#lineBounds[1]

	yA = slope * (leftBound - mPtX) + mPtY
	
	if yA > topBound:
		xA = mPtX + (topBound - mPtY)/slope
		pointA = (xA, topBound)
	elif yA < bottomBound:
		xA = mPtX + (bottomBound - mPtY)/slope
		pointA = (xA, bottomBound)
	else:
		pointA = (leftBound, yA)

	yB = slope * (rightBound - mPtX) + mPtY
	
	if yB > topBound:
		xB = mPtX + (topBound - mPtY)/slope
		pointB = (xB, topBound)
	elif yB < bottomBound:
		xB = mPtX + (bottomBound - mPtY)/slope
		pointB = (xB, bottomBound)
	else:
		pointB = (rightBound, yB)

	return pointA, pointB

plt.figure(figsize=(7, 7))
plt.ylim(0, 200)
plt.xlim(0, 200)

plt.title("pixel_plot")

#points = [[50, 50], [25, 25], [75, 75]]

n = len(points)
	
for i in range(n):
	for j in range(0, n - i - 1):
		if points[j][1] > points[j + 1][1]:
			points[j], points[j + 1] = points[j + 1], points[j]

for i in range(n):
	cell.update({ f"{str(points[i]).replace(', ', '_')}" : {"point":points[i], "otherPoint":{ "(None_None)" : {"point":[None, None], "slope":None, "midpoint":[None, None], "boundA":[0, 200], "boundB":[200, 0]} } } })

# Go through the points and find all the edges with the nearest point (will need to change this later as most cells have edges with more than just their nearest neighbor)
length = points.__len__()
for i in range(0, length):
	pt = points[i]
	points2 = points.copy()
	points2.remove(pt)

	#print(pt)

	n = len(points2)
	
	for i in range(n):
		for j in range(0, n - i - 1):
			point1 = points2[j]
			point2 = points2[j + 1]

			distance1 = distance(pt[0], pt[1], point1[0], point1[1])
			distance2 = distance(pt[0], pt[1], point2[0], point2[1])

			if distance1 > distance2:
				points2[j], points2[j + 1] = points2[j + 1], points2[j]


	def solver(a, b, c, d):
		#if c < a and d < b:
		#	(a, b), (c, d) = (c, d), (a, b)

		m = (b - d) / (a - c)

		mPtX = (a + c) / 2
		mPtY = (b + d) / 2
		
		if f"({a}_{b})" != f"({c}_{d})":

			boundA, boundB = setDefaultBounds(-1/m, mPtX, mPtY, defaultBounds)

			if "(None_None)" == list(cell[f"({a}_{b})"]["otherPoint"].keys())[0]:
				cell.update({ f"({a}_{b})" : {"point":[a, b], "otherPoint":{ f"({c}_{d})" : {"point":[c, d], "slope":-1/m, "midpoint":[mPtX, mPtY], "boundA":boundA, "boundB":boundB} } } })
				#print(f"({a}_{b}) contains a (None_None)")
			elif not f"({a}_{b})" in cell:
				cell.update({ f"({a}_{b})" : {"point":[a, b], "otherPoint":{ f"({c}_{d})" : {"point":[c, d], "slope":-1/m, "midpoint":[mPtX, mPtY], "boundA":boundA, "boundB":boundB} } } })
				#print(f"cell does not contain ({a}_{b})")
			elif f"({a}_{b})" in cell:
				#print(f"cell contains ({a}_{b})")
				if not f"({c}_{d})" in cell[f"({a}_{b})"]["otherPoint"]:
					#print(f"({a}_{b}) does not contain ({c}_{d})")
					cell[f"({a}_{b})"]["otherPoint"].update({ f"({c}_{d})" : {"point":[c, d], "slope":-1/m, "midpoint":[mPtX, mPtY], "boundA":boundA, "boundB":boundB} } )
			#print(cell[f"({a}_{b})"]["otherPoint"])
			#print()

	#n2 = points2.__len__()
	for j in range(0, n):
		solver(pt[0], pt[1], points2[j][0], points2[j][1])

#print(cell)

# Go through the points and find the intersection points in order to form edges
#-------------------------------------------------------------------------------------------------Current issues: 
#1) a perpendicular line between two of the points is now showing up
#2) no intersection points are being found where there should be at least 1 (?)
#3) no triple intersection points are being found whne there should be 1

for currentPoint in points:

	cell2 = cell.copy()
	arrayPoint = str(currentPoint).replace(", ", "_")

	#kys = cell2.keys()
	
	def sort(target, array):
		n = len(array)

		keys = list(array.keys())

		for i in range(n):
			for j in range(0, n - i - 1):
				point1 = array[keys[j]]["midpoint"]
				point2 = array[keys[j + 1]]["midpoint"]

				distance1 = distance(target[0], target[1], point1[0], point1[1])
				distance2 = distance(target[0], target[1], point2[0], point2[1])

				if distance1 > distance2:
					array[keys[j]], array[keys[j + 1]] = array[keys[j + 1]], array[keys[j]]

	#The easiest way to get the verticies of the edges may be to just find all of the interesection points of 3 lines and keep track of the points that made them,
	#	then connect each of those verticies to 3 other verticies (stopping at this step would result in no edges being connected to the boundry, which is an issue)
	#	The above issue could be solved by including finding intersections with the boundaries after finding all the other intersections and only requiring 2 lines
	#		(the line and the boundary) to interesect in this case

	#for key in kys:

		#print(list(map(int, key.replace("_", ", ").removesuffix(")").removeprefix("(").split(", "))))
	#	sort(list(map(int, key.replace("_", ", ").removesuffix(")").removeprefix("(").split(", "))), cell2[key]["otherPoint"])
		#print(cell2)

	#print(cell2[arrayPoint])

	sort(cell2[arrayPoint]["point"], cell2[arrayPoint]["otherPoint"])

	kys = list(cell2[arrayPoint]["otherPoint"].keys())

	for key1 in kys:
		for key2 in kys:
			if key1 != key2:
				point1 = cell2[arrayPoint]["otherPoint"][key1]
				point2 = cell2[arrayPoint]["otherPoint"][key2]
				intX, intY = intersectSolver(point1, point2)
				if intX != None:
					print(f"point1: {point1['point']} point2: {point2['point']} intersect: ({intX, intY})")
					plt.plot(intX, intY, "bo")

	#n = kys.__len__()
	#print("a")
	for key1 in kys:
		point1 = cell2[arrayPoint]["otherPoint"][key1]
		#print(" b")
		for key2 in kys:
			#print("  c")
			if key2 != key1:
				#print("   d")
				point2 = cell2[arrayPoint]["otherPoint"][key2]

				intX, intY = intersectSolver(point1, point2)

				if intX != None:
					#print("     e")
					for key3 in kys:
						#print("      f")
						if key3 != key1 and key3 != key2:
							#print("       g")
							point3 = cell2[arrayPoint]["otherPoint"][key3]
							
							y = equationToPoint(point3, intX)

							if y == intY:
								#print("        h")
								if intX > point1["midpoint"][0]:
									point1["boundB"] = [intX, intY]
								#elif intX < point1["midpoint"][0]:
								else:
									point1["boundA"] = [intX, intY]

								if intX > point2["midpoint"][0]:
									point2["boundB"] = [intX, intY]
								#elif intX < point2["midpoint"][0]:
								else:
									point2["boundA"] = [intX, intY]

								if intX > point3["midpoint"][0]:
									point3["boundB"] = [intX, intY]
								#elif intX < point3["midpoint"][0]:
								else:
									point3["boundA"] = [intX, intY]

								intersection3Points.update({
"intPosition":[intX, intY], 
"line1":{"point":point1["point"], "slope":point1["slope"], "midpoint":point1["midpoint"], "boundA":point1["boundA"], "boundB":point1["boundB"]},
"line2":{"point":point2["point"], "slope":point2["slope"], "midpoint":point2["midpoint"], "boundA":point2["boundA"], "boundB":point2["boundB"]},
"line3":{"point":point3["point"], "slope":point3["slope"], "midpoint":point3["midpoint"], "boundA":point3["boundA"], "boundB":point3["boundB"]}
})

print(intersection3Points)
print(cell["(98_70)"]["otherPoint"])

print(cell.__len__())
for site in cell:
	plt.plot(cell[site]["point"][0], cell[site]["point"][1], "ro")

	for line in cell[site]["otherPoint"]:
		
		plt.plot(cell[site]["otherPoint"][line]["midpoint"][0], cell[site]["otherPoint"][line]["midpoint"][1], "yo")

		plt.plot([cell[site]["otherPoint"][line]["boundA"][0], cell[site]["otherPoint"][line]["boundB"][0]], [cell[site]["otherPoint"][line]["boundA"][1], cell[site]["otherPoint"][line]["boundB"][1]], "-go")

#for pt in points:
#	plt.plot(pt[0], pt[1], "ro")

plt.show()






