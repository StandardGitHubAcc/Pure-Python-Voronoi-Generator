#https://stackoverflow.com/questions/28504737/how-to-plot-a-single-point-in-matplotlib
#https://www.geeksforgeeks.org/create-2d-pixel-plot-in-python/
#https://stackoverflow.com/questions/66238749/how-to-find-the-closest-coordinate-from-a-list-of-points
#https://www.geeksforgeeks.org/sorting-algorithms-in-python/

#import numpy as np
import random
import matplotlib.pyplot as plt
#import math

defaultBounds = [[0, 200], [200, 0]]

points = [(50, 50), (25, 25), (75, 75), (98, 70)]
#		bottomleft, topleft, bottomright, topright
corners = [[0, 0], [0, 200], [200, 0], [200, 200]] #[ [defaultBounds[0][0], defaultBounds[1][1]], [defaultBounds[0][0], defaultBounds[0][1]], [defaultBounds[1][0], defaultBounds[1][1]], [defaultBounds[0][1], defaultBounds[1][0]] ]
#points = [(50, 50), (25, 25), (75, 75)]
#data = []
#cell = []
cell = {}
intersection3Points = {}
finalCell = {}

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
			return None, None
	else:
		#print(f"there is no interesection of y = {slope1}(x - {midPt1[0]}) + {midPt1[1]} and y = {slope2}(x - {midPt2[0]}) + {midPt2[1]} or they are the same equation")
		return None, None


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

def boundryCheck(line, givenBounds):
	#leftY = float("%.8f" % equationToPoint(line, givenBounds[0][0]))
	#topY = float("%.8f" % equationToPoint(line, givenBounds[0][1]))
	#rightY = float("%.8f" % equationToPoint(line, givenBounds[1][0]))
	#bottomY = float("%.8f" % equationToPoint(line, givenBounds[1][1]))

	boundA = line["boundA"]
	boundB = line["boundB"]

	#locationA = ""
	#locationB = ""

	

	if boundA[0] == givenBounds[0][0] or boundA[1] == givenBounds[0][1] or boundA == givenBounds[1][1]:
		return True
	elif boundB[0] == givenBounds[1][0] or boundB[1] == givenBounds[0][1] or boundB == givenBounds[1][1]:
		return True
#points = [[50, 50], [25, 25], [75, 75]]

n = len(points)
	
for i in range(n):
	for j in range(0, n - i - 1):
		if points[j][1] > points[j + 1][1]:
			points[j], points[j + 1] = points[j + 1], points[j]

for i in range(n):
	cell.update({ f"{str(points[i]).replace(', ', '_')}" : {"point":points[i], "otherPoint":{ "(None_None)" : {"point":[None, None], "slope":None, "midpoint":[None, None], "boundA":[0, 200], "boundB":[200, 0]} } } })

# Go through the points and find all of the perpendicular lines, as well as setting the boundary for each line
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

	for j in range(0, n):
		solver(pt[0], pt[1], points2[j][0], points2[j][1])

#print(cell.__len__())
# Remove the midpoints that are too close to a site to possibly be valid
for site in cell:
	kys = list(cell[site]["otherPoint"].keys())
	#print(cell[site]["otherPoint"].__len__())
	for key in kys:
		#print(site, key, cell[site]["otherPoint"][key]["midpoint"])
		#dist = distance(cell[site]["point"][0], cell[site]["point"][1], cell[site]["otherPoint"][key]["midpoint"][0], cell[site]["otherPoint"][key]["midpoint"][1])
		for point in points:
			try:
				#print(point, key, cell[site]["otherPoint"][key]["midpoint"])
				dist = distance(point[0], point[0], cell[site]["otherPoint"][key]["midpoint"][0], cell[site]["otherPoint"][key]["midpoint"][1])
				#print(dist)
				if dist < 0.1:
					del cell[site]["otherPoint"][key]
				
					#print("deleted")
			except Exception:
				pass

# Go through the points and find the tripple intersection points
for currentPoint in points:

	cell2 = cell.copy()
	arrayPoint = str(currentPoint).replace(", ", "_")

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

	sort(cell2[arrayPoint]["point"], cell2[arrayPoint]["otherPoint"])
	#print(cell2[arrayPoint]["otherPoint"].__len__())
	kys = list(cell2[arrayPoint]["otherPoint"].keys())

	for key1 in kys:
		for key2 in kys:
			if key1 != key2:
				line1 = cell2[arrayPoint]["otherPoint"][key1]
				line2 = cell2[arrayPoint]["otherPoint"][key2]
				intX, intY = intersectSolver(line1, line2)
				if intX != None:
					#intY = "%.8f" % intY
					#if not f"({intX}_{intY})" in intersection3Points:
					#print(f"site: {currentPoint} point1: {line1['point']} point2: {line2['point']} intersect: {intX, intY}")
					#plt.plot(intX, intY, "bo")

					line3 = cell2[key1]["otherPoint"][key2]
					#print(line3["point"])
					yTest = equationToPoint(line3, intX)
					yTest = float("%.8f" % yTest)
					intY = float("%.8f" % intY)
					intX = float("%.8f" % intX)
					#print(intY)
					#print(yTest)
					
					if yTest == intY:
						#print("success")

						distCurrentToL1 = distance(currentPoint[0], currentPoint[1], line1["point"][0], line1["point"][1])
						distCurrentToL2 = distance(currentPoint[0], currentPoint[1], line2["point"][0], line2["point"][1])
						distL1ToL2 = distance(line1["point"][0], line1["point"][1], line2["point"][0], line2["point"][1])

						#distances = {arrayPoint : {key1: distance(currentPoint[0], currentPoint[1], line1["point"][0], line1["point"][1]), key2 : distance(line1["point"][0], line1["point"][1], line2["point"][0], line2["point"][1])}}

						if distCurrentToL1 > distCurrentToL2 and distCurrentToL1 > distL1ToL2:
							if intX > line1["midpoint"][0]:
								line1["boundA"] = [intX, intY]
								cell[arrayPoint]["otherPoint"][key1]["boundA"] = [intX, intY]
								cell[key1]["otherPoint"][arrayPoint]["boundA"] = [intX, intY]
							else:
								line1["boundB"] = [intX, intY]
								cell[arrayPoint]["otherPoint"][key1]["boundB"] = [intX, intY]
								cell[key1]["otherPoint"][arrayPoint]["boundB"] = [intX, intY]
						else:
							if intX > line1["midpoint"][0]:
								line1["boundB"] = [intX, intY]
								cell[arrayPoint]["otherPoint"][key1]["boundB"] = [intX, intY]
								cell[key1]["otherPoint"][arrayPoint]["boundB"] = [intX, intY]
							else:
								line1["boundA"] = [intX, intY]
								cell[arrayPoint]["otherPoint"][key1]["boundA"] = [intX, intY]
								cell[key1]["otherPoint"][arrayPoint]["boundA"] = [intX, intY]

						if distCurrentToL2 > distCurrentToL1 and distCurrentToL2 > distL1ToL2:
							if intX > line2["midpoint"][0]:
								line2["boundA"] = [intX, intY]
								cell[arrayPoint]["otherPoint"][key2]["boundA"] = [intX, intY]
								cell[key2]["otherPoint"][arrayPoint]["boundA"] = [intX, intY]
							else:
								line2["boundB"] = [intX, intY]
								cell[arrayPoint]["otherPoint"][key2]["boundB"] = [intX, intY]
								cell[key2]["otherPoint"][arrayPoint]["boundB"] = [intX, intY]
						else:
							if intX > line2["midpoint"][0]:
								line2["boundB"] = [intX, intY]
								cell[arrayPoint]["otherPoint"][key2]["boundB"] = [intX, intY]
								cell[key2]["otherPoint"][arrayPoint]["boundB"] = [intX, intY]
							else:
								line2["boundA"] = [intX, intY]
								cell[arrayPoint]["otherPoint"][key2]["boundA"] = [intX, intY]
								cell[key2]["otherPoint"][arrayPoint]["boundA"] = [intX, intY]

						if distL1ToL2 > distCurrentToL1 and distL1ToL2 > distCurrentToL2:
							if intX > line3["midpoint"][0]:
								line3["boundA"] = [intX, intY]
								cell[key1]["otherPoint"][key2]["boundA"] = [intX, intY]
								cell[key2]["otherPoint"][key1]["boundA"] = [intX, intY]
							else:
								line3["boundB"] = [intX, intY]
								cell[key1]["otherPoint"][key2]["boundB"] = [intX, intY]
								cell[key2]["otherPoint"][key1]["boundB"] = [intX, intY]
						else:
							if intX > line3["midpoint"][0]:
								line3["boundB"] = [intX, intY]
								cell[key1]["otherPoint"][key2]["boundB"] = [intX, intY]
								cell[key2]["otherPoint"][key1]["boundB"] = [intX, intY]
							else:
								line3["boundA"] = [intX, intY]
								cell[key1]["otherPoint"][key2]["boundA"] = [intX, intY]
								cell[key2]["otherPoint"][key1]["boundA"] = [intX, intY]

						#print(distance(intX, intY, currentPoint[0], currentPoint[1]))
						#print(distance(intX, intY, line1["point"][0], line1["point"][1]))
						#print(distance(intX, intY, line2["point"][0], line2["point"][1]))
						#print(key1)
						#print()

						intersection3Points.update({ f"({intX}_{intY})" : {
"intPosition":[intX, intY], 
"line1":{"points":[currentPoint, line1["point"]], "slope":line1["slope"], "midpoint":line1["midpoint"], "boundA":line1["boundA"], "boundB":line1["boundB"]},
"line2":{"points":[currentPoint, line2["point"]], "slope":line2["slope"], "midpoint":line2["midpoint"], "boundA":line2["boundA"], "boundB":line2["boundB"]},
"line3":{"points":[line1["point"], line2["point"]], "slope":line3["slope"], "midpoint":line3["midpoint"], "boundA":line3["boundA"], "boundB":line3["boundB"]}
						}})


#print(cell.__len__())

for site in cell:
	cellKeys = list(cell[site]["otherPoint"].keys())
	for key in cellKeys:
		for entry in intersection3Points:
			intX1, intY1 = intersectSolver(cell[site]["otherPoint"][key], intersection3Points[entry]["line1"])
			intX2, intY2 = intersectSolver(cell[site]["otherPoint"][key], intersection3Points[entry]["line2"])
			intX3, intY3 = intersectSolver(cell[site]["otherPoint"][key], intersection3Points[entry]["line3"])
			#print(site, cell[site]["otherPoint"][key]["midpoint"][0])

			if intX1 != None or intX2 != None or intX3 != None:
				del cell[site]["otherPoint"][key]
				#print("deleting")

# Need to 
# 1. determine if the boundry of a line is on the overall boundry
# 2. find other points that have hit the overall boundry
# 3. determine if those points should be connected
# 4. determine if the site is the closest one to one of the corners
# 5. if it is, include the corner point along with the other two points

# For each of the sites related to a 3-intersect, if the lines with the other two points both hit an overall boundry, those two points should be connected

# a site may only be completely surrounded if it is paired with at least 3 other sites
#	if a site is paired with 1 other site, that site must be in the corner
#	just because a site is paired with 3 other sites does not mean that it will be completely surrounded

for site in cell:
	leftX = defaultBounds[0][0]
	rightX = defaultBounds[1][0]
	bottomY = defaultBounds[0][1]
	topY = defaultBounds[1][1]

	def basicDistanceTargetSort(target, array): #there is another place where this is done, so I should make this a global function and just reference it when I need to do this
		n = len(array)
	
		for i in range(n):
			for j in range(0, n - i - 1):
				point1 = array[j]
				point2 = array[j + 1]

				distance1 = distance(target[0], target[1], point1[0], point1[1])
				distance2 = distance(target[0], target[1], point2[0], point2[1])

				if distance1 > distance2:
					array[j], array[j + 1] = array[j + 1], array[j]

	def keyToPoints(key):
		return list(map(float, key.replace("_", ", ").removesuffix(")").removeprefix("(").split(", ")))

	match cell[site]["otherPoint"].__len__():
		case 0:
			#finalCell.update({ site: {"pointForm":keyToPoints(site), "vertices":[corners[0], corners[1], corners[2], corners[3] ]} })
			finalCell.update({ site: {"pointForm":keyToPoints(site), "vertices":[[corners[1], corners[2]], [corners[2], corners[4]], [corners[4], corners[3]], [corners[3], corners[0]], [corners[0], corners[1]] ]} })
		case 1: #will probably need to redo the organization of the vertices within finalCell to avoid any mistakes
			#figure out which corner it is closests to and where the boundrys of the lines are
			ky = list(cell[site]["otherPoint"].keys())[0]
			boundAX = cell[site]["otherPoint"][ky]["boundA"][0]
			boundAY = cell[site]["otherPoint"][ky]["boundA"][1]
			boundBX = cell[site]["otherPoint"][ky]["boundB"][0]
			boundBY = cell[site]["otherPoint"][ky]["boundB"][1]
			if ( boundAX == leftX and (boundBY == topY or boundBY == bottomY) ) or ( boundBX == rightX and (boundAY == topY or boundAY == bottomY) ): #if the site is in a corner
				#print("corner")
				corner = corners.copy()
				basicDistanceTargetSort(keyToPoints(site), corner)
				#finalCell.update( { site: {"pointForm":keyToPoints(site), "vertices":[cell[site]["otherPoint"][ky]["boundA"], corner[0], cell[site]["otherPoint"][ky]["boundB"] ]} })
				finalCell.update( { site: {"pointForm":keyToPoints(site), "vertices":[[cell[site]["otherPoint"][ky]["boundA"], corner[0]], [corner[0], cell[site]["otherPoint"][ky]["boundB"]], [cell[site]["otherPoint"][ky]["boundB"], cell[site]["otherPoint"][ky]["boundA"]] ]} })
			else: #if the site is not in a corner  #would be the same as elif ( boundAX == leftX and boundBX == rightX ) or ( boundAY == bottomY and boundBY == topY ) or (boundAY == topY and boundBY == bottomY):

				if boundAX == leftX and boundBX == rightX: #if the cell stretches horizontally across the area
					if cell[site]["otherPoint"][ky]["point"][1] > cell[site]["point"][1]: #if the site is below its pair
						#finalCell.update({ site: {"pointForm":keyToPoints(site), "vertices":[cell[site]["otherPoint"][ky]["boundA"], corners[0], corners[2], cell[site]["otherPoint"][ky]["boundB"] ]} })
						finalCell.update({ site: {"pointForm":keyToPoints(site), "vertices":[[cell[site]["otherPoint"][ky]["boundA"], corners[0]], [corners[0], corners[2]], [corners[2], cell[site]["otherPoint"][ky]["boundB"]], [cell[site]["otherPoint"][ky]["boundB"], cell[site]["otherPoint"][ky]["boundA"]] ]} })
					else: #if the site is above its pair
						#finalCell.update({ site: {"pointForm":keyToPoints(site), "vertices":[cell[site]["otherPoint"][ky]["boundA"], corners[1], corners[3], cell[site]["otherPoint"][ky]["boundB"] ]} })
						finalCell.update({ site: {"pointForm":keyToPoints(site), "vertices":[[cell[site]["otherPoint"][ky]["boundA"], corners[1]], [corners[1], corners[3]], [corners[3], cell[site]["otherPoint"][ky]["boundB"]], [cell[site]["otherPoint"][ky]["boundB"], cell[site]["otherPoint"][ky]["boundA"]] ]} })

				else: #if the cell stretches vertically across the area  #elif (boundAX == bottomY and boundBX == topY) or (boundAX == topY and boundBX == bottomY):
					if cell[site]["otherPoint"][ky]["point"][0] > cell[site]["point"][0]: #if the site is to the left of the pair
						#finalCell.update({ site: {"pointForm":keyToPoints(site), "vertices":[cell[site]["otherPoint"][ky]["boundA"], corners[0], corners[1], cell[site]["otherPoint"][ky]["boundB"] ]} })
						if cell[site]["otherPoint"][ky]["slope"] < 0:
							finalCell.update({ site: {"pointForm":keyToPoints(site), "vertices":[[cell[site]["otherPoint"][ky]["boundA"], corners[1]], [corners[1], corners[0]], [corners[0], cell[site]["otherPoint"][ky]["boundB"]], [cell[site]["otherPoint"][ky]["boundB"], cell[site]["otherPoint"][ky]["boundA"]] ]} })
						else:
							finalCell.update({ site: {"pointForm":keyToPoints(site), "vertices":[[cell[site]["otherPoint"][ky]["boundA"], corners[0]], [corners[0], corners[1]], [corners[1], cell[site]["otherPoint"][ky]["boundB"]], [cell[site]["otherPoint"][ky]["boundB"], cell[site]["otherPoint"][ky]["boundA"]] ]} })
					else: #if the site is to the right of the pair
						#finalCell.update({ site: {"pointForm":keyToPoints(site), "vertices":[cell[site]["otherPoint"][ky]["boundA"], corners[2], corners[3], cell[site]["otherPoint"][ky]["boundB"] ]} })
						if cell[site]["otherPoint"][ky]["slope"] < 0:
							finalCell.update({ site: {"pointForm":keyToPoints(site), "vertices":[[cell[site]["otherPoint"][ky]["boundA"], corners[4]], [corners[4], corners[3]], [corners[3], cell[site]["otherPoint"][ky]["boundB"]], [cell[site]["otherPoint"][ky]["boundB"], cell[site]["otherPoint"][ky]["boundA"]] ]} })
						else:
							finalCell.update({ site: {"pointForm":keyToPoints(site), "vertices":[[cell[site]["otherPoint"][ky]["boundA"], corners[3]], [corners[3], corners[4]], [corners[4], cell[site]["otherPoint"][ky]["boundB"]], [cell[site]["otherPoint"][ky]["boundB"], cell[site]["otherPoint"][ky]["boundA"]] ]} })
		case 2:
			boundryPairs = [] 

			kys = list(cell[site]["otherPoint"].keys())

			line1 = cell[site]["otherPoint"][kys[0]]
			line2 = cell[site]["otherPoint"][kys[1]]

			L1boundAX = cell[site]["otherPoint"][line1]["boundA"][0]
			L1boundAY = cell[site]["otherPoint"][line1]["boundA"][1]
			L1boundBX = cell[site]["otherPoint"][line1]["boundB"][0]
			L1boundBY = cell[site]["otherPoint"][line1]["boundB"][1]

			L2boundAX = cell[site]["otherPoint"][line2]["boundA"][0]
			L2boundAY = cell[site]["otherPoint"][line2]["boundA"][1]
			L2boundBX = cell[site]["otherPoint"][line2]["boundB"][0]
			L2boundBY = cell[site]["otherPoint"][line2]["boundB"][1]

			L1BoundPt = (0, 0)
			L2BoundPt = (0, 0)

			avX = (line1["point"][0] + line2["point"][0])/(2)
			avY = (line1["point"][1] + line2["point"][1])/(2)
			#P1Type = "None"
			#P2Type = "None"

			if L1boundAX == leftX or L1boundAY == topY or L1boundAY == bottomY:
				L1BoundPt = (L1boundAX, L1boundAY)
				#P1Type = "A"
			elif L1boundBX == rightX or L1boundBY == topY or L1boundBY == bottomY:
				L1BoundPt = (L1boundBX, L1boundBY)
				#P1Type = "B"

			if L2boundAX == leftX or L2boundAY == topY or L2boundAY == bottomY:
				L2BoundPt = (L2boundAX, L2boundAY)
				#P2Type = "A"
			elif L2boundBX == rightX or L2boundBY == topY or L2boundBY == bottomY:
				L2BoundPt = (L2boundBX, L2boundBY)
				#P2Type = "B"

			if L1BoundPt[0] == L2BoundPt[0] and L1BoundPt[1] != L2BoundPt[1]:
				boundryPairs.append([L1BoundPt, L2BoundPt])
			else:
				if (L1BoundPt[0] == leftX and L2BoundPt[1] == topY) or (L2BoundPt[0] == leftX and L1BoundPt[1] == topY): #top left
					boundryPairs.append([ [L1BoundPt, corners[1]], [corners[1], L2BoundPt] ])
				elif (L1BoundPt[0] == leftX and L2BoundPt[1] == bottomY) or (L2BoundPt[0] == leftX and L1BoundPt[1] == bottomY): #bottom left
					boundryPairs.append([ [L1BoundPt, corners[0]], [corners[0], L2BoundPt] ])
				elif (L1BoundPt[0] == rightX and L2BoundPt[1] == topY) or (L2BoundPt[0] == rightX and L1BoundPt[1] == topY): #top right
					boundryPairs.append([ [L1BoundPt, corners[3]], [corners[3], L2BoundPt] ])
				elif (L1BoundPt[0] == rightX and L2BoundPt[1] == bottomY) or (L2BoundPt[0] == rightX and L1BoundPt[1] == bottomY): #bottom right
					boundryPairs.append([ [L1BoundPt, corners[2]], [corners[2], L2BoundPt] ])
				elif (L1BoundPt[0] == leftX and L2BoundPt[0] == rightX) or (L2BoundPt[0] == leftX and L1BoundPt[0] == rightX): # stretch left right
					if cell[site]["point"][1] < avY: # the site is on the bottom
						if L1BoundPt[0] < L2BoundPt[0]:
							boundryPairs.append([ [L1BoundPt, corners[0]], [corners[0], corners[2]], [corners[2], L2BoundPt] ])
						else:
							boundryPairs.append([ [L2BoundPt, corners[0]], [corners[0], corners[2]], [corners[2], L1BoundPt] ])
					else: # the site is on the top
						if L1BoundPt[0] < L2BoundPt[0]:
							boundryPairs.append([ [L2BoundPt, corners[1]], [corners[1], corners[3]], [corners[3], L1BoundPt] ])
						else:
							boundryPairs.append([ [L2BoundPt, corners[1]], [corners[1], corners[3]], [corners[3], L1BoundPt] ])
				elif (L1BoundPt[1] == topY and L2BoundPt[1] == bottomY) or (L2BoundPt[1] == topY and L1BoundPt[1] == bottomY): # stretch top bottom
					if cell[site]["point"][0] < avX: # the site is on the left side
						
						if L1BoundPt[0] < L2BoundPt[0]:
							d1 = distance(L1BoundPt[0], L1BoundPt[1], corners[0][0], corners[0][1])
							d2 = distance(L1BoundPt[0], L1BoundPt[1], corners[1][0], corners[1][1])
							boundryPairs.append([ [L1BoundPt, corners[0]], [corners[0], corners[2]], [corners[2], L2BoundPt] ])
						else:
							boundryPairs.append([ [L2BoundPt, corners[0]], [corners[0], corners[2]], [corners[2], L1BoundPt] ])
					else: # the site is on the right side

			for line in cell[site]["otherPoint"]: #this works for cases such as site (50, 50) since it has a pair of points on the boundry on two different boundries, 
												  #	but does not work for cases such as site (75, 75) and (98, 70) where there is one point on one boundry and another point another another boundry
												  # cases such as (75, 75) and (98, 70) can be like corner points, but I am not sure how to tell if this is the case
				boundAX = cell[site]["otherPoint"][line]["boundA"][0]
				boundAY = cell[site]["otherPoint"][line]["boundA"][1]
				boundBX = cell[site]["otherPoint"][line]["boundB"][0]
				boundBY = cell[site]["otherPoint"][line]["boundB"][1]

				if boundAX == leftX or boundAY == topY or boundAY == bottomY:
					for line2 in cell[site]["otherPoint"]:
						if line2 != line1:
							boundAX2 = cell[site]["otherPoint"][line2]["boundA"][0]
							boundAY2 = cell[site]["otherPoint"][line2]["boundA"][1]
							boundBX2 = cell[site]["otherPoint"][line2]["boundB"][0]
							boundBY2 = cell[site]["otherPoint"][line2]["boundB"][1]	
							if (boundAX == boundAX2 and boundAY != boundAY2) or (boundAY == boundAY2 and boundAX != boundAX2):
								if not [cell[site]["otherPoint"][line]["boundA"], cell[site]["otherPoint"][line2]["boundA"]] in boundryPairs and not [cell[site]["otherPoint"][line2]["boundA"], cell[site]["otherPoint"][line]["boundA"]] in boundryPairs:
									boundryPairs.append([cell[site]["otherPoint"][line]["boundA"], cell[site]["otherPoint"][line2]["boundA"]])
							else:
#								if boundAX == leftX and boundBY2 == topY:
#									pass
#								elif boundAX == leftX and boundBY2 == bottomY:
#									pass
#								elif boundAY == topY and boundBX2 == rightX:
#									pass
#								elif boundAY == bottomY and boundBX2 == rightX:
#									pass
#								elif boundAY == topY and boundB
								pass				
				if boundBX == rightX or boundBY == topY or boundBY == bottomY:
					for line2 in cell[site]["otherPoint"]:
						if line2 != line1:
							#boundAX2 = cell[site]["otherPoint"][line2]["boundA"][0]
							#boundAY2 = cell[site]["otherPoint"][line2]["boundA"][1]
							boundBX2 = cell[site]["otherPoint"][line2]["boundB"][0]
							boundBY2 = cell[site]["otherPoint"][line2]["boundB"][1]	
							if (boundBX == boundBX2 and boundBY != boundBY2) or (boundBY == boundBY2 and boundBX != boundBX2):
								if not [cell[site]["otherPoint"][line]["boundB"], cell[site]["otherPoint"][line2]["boundB"]] in boundryPairs and not [cell[site]["otherPoint"][line2]["boundB"], cell[site]["otherPoint"][line]["boundB"]] in boundryPairs:
									boundryPairs.append([cell[site]["otherPoint"][line]["boundB"], cell[site]["otherPoint"][line2]["boundB"]])

				print()
				print(site, boundryPairs)
		
		case _: #default
			boundryPairs = [] 

			for line in cell[site]["otherPoint"]: #this works for cases such as site (50, 50) since it has a pair of points on the boundry on two different boundries, 
												  #	but does not work for cases such as site (75, 75) and (98, 70) where there is one point on one boundry and another point another another boundry
												  # cases such as (75, 75) and (98, 70) can be like corner points, but I am not sure how to tell if this is the case
				boundAX = cell[site]["otherPoint"][line]["boundA"][0]
				boundAY = cell[site]["otherPoint"][line]["boundA"][1]
				boundBX = cell[site]["otherPoint"][line]["boundB"][0]
				boundBY = cell[site]["otherPoint"][line]["boundB"][1]

				if boundAX == leftX or boundAY == topY or boundAY == bottomY:
					for line2 in cell[site]["otherPoint"]:
						if line2 != line1:
							boundAX2 = cell[site]["otherPoint"][line2]["boundA"][0]
							boundAY2 = cell[site]["otherPoint"][line2]["boundA"][1]
							#boundBX2 = cell[site]["otherPoint"][line2]["boundB"][0]
							#boundBY2 = cell[site]["otherPoint"][line2]["boundB"][1]	
							if (boundAX == boundAX2 and boundAY != boundAY2) or (boundAY == boundAY2 and boundAX != boundAX2):
								if not [cell[site]["otherPoint"][line]["boundA"], cell[site]["otherPoint"][line2]["boundA"]] in boundryPairs and not [cell[site]["otherPoint"][line2]["boundA"], cell[site]["otherPoint"][line]["boundA"]] in boundryPairs:
									boundryPairs.append([cell[site]["otherPoint"][line]["boundA"], cell[site]["otherPoint"][line2]["boundA"]])
				
				if boundBX == rightX or boundBY == topY or boundBY == bottomY:
					for line2 in cell[site]["otherPoint"]:
						if line2 != line1:
							#boundAX2 = cell[site]["otherPoint"][line2]["boundA"][0]
							#boundAY2 = cell[site]["otherPoint"][line2]["boundA"][1]
							boundBX2 = cell[site]["otherPoint"][line2]["boundB"][0]
							boundBY2 = cell[site]["otherPoint"][line2]["boundB"][1]	
							if (boundBX == boundBX2 and boundBY != boundBY2) or (boundBY == boundBY2 and boundBX != boundBX2):
								if not [cell[site]["otherPoint"][line]["boundB"], cell[site]["otherPoint"][line2]["boundB"]] in boundryPairs and not [cell[site]["otherPoint"][line2]["boundB"], cell[site]["otherPoint"][line]["boundB"]] in boundryPairs:
									boundryPairs.append([cell[site]["otherPoint"][line]["boundB"], cell[site]["otherPoint"][line2]["boundB"]])

				print()
				print(site, boundryPairs)
				
			


	

plt.figure(figsize=(7, 7))
plt.ylim(defaultBounds[1][1], defaultBounds[1][0])
plt.xlim(defaultBounds[0][0], defaultBounds[0][1])

plt.title("pixel_plot")

for site in cell: #If I want to make it so that it displays all of the perp lines, go to the area for finding the intersection of 3 lines and comment out all of the references to cell
	plt.plot(cell[site]["point"][0], cell[site]["point"][1], "ro")
	#print(cell[site]["otherPoint"].__len__())
	for line in cell[site]["otherPoint"]:
		#print(cell[site]["point"], line, cell[site]["otherPoint"][line]["boundA"], cell[site]["otherPoint"][line]["boundB"])
		#print(f'site: {cell[site]["point"]} line: {line} midpoint: {cell[site]["otherPoint"][line]["midpoint"]} boundA: {cell[site]["otherPoint"][line]["boundA"]} boundB: {cell[site]["otherPoint"][line]["boundB"]}')
		plt.plot(cell[site]["otherPoint"][line]["midpoint"][0], cell[site]["otherPoint"][line]["midpoint"][1], "yo")

		plt.plot([cell[site]["otherPoint"][line]["boundA"][0], cell[site]["otherPoint"][line]["boundB"][0]], [cell[site]["otherPoint"][line]["boundA"][1], cell[site]["otherPoint"][line]["boundB"][1]], "-go")
		#plt.plot([cell[site]["otherPoint"][line]["boundA"][0], cell[site]["otherPoint"][line]["boundB"][0]], [cell[site]["otherPoint"][line]["boundA"][1], cell[site]["otherPoint"][line]["boundB"][1]], color="red")

#intersect3Keys = intersection3Points.keys()

#for key in intersect3Keys:
	#plt.plot(intersection3Points[key]["intPosition"][0], intersection3Points[key]["intPosition"][1], "bo")
	#print(f'intersection point {intersection3Points[key]["intPosition"]} between {intersection3Points[key]["line1"]["points"][0]} {intersection3Points[key]["line2"]["points"][1]} {intersection3Points[key]["line3"]["points"][0]}')
	#print(f'point: {intersection3Points[key]["line1"]["points"][0]} {intersection3Points[key]["line1"]["points"][1]} boundA: {intersection3Points[key]["line1"]["boundA"]} boundB: {intersection3Points[key]["line1"]["boundB"]}')
	#print(f'point: {intersection3Points[key]["line2"]["points"][0]} {intersection3Points[key]["line2"]["points"][1]} boundA: {intersection3Points[key]["line2"]["boundA"]} boundB: {intersection3Points[key]["line2"]["boundB"]}')
	#print(f'point: {intersection3Points[key]["line3"]["points"][0]} {intersection3Points[key]["line3"]["points"][1]} boundA: {intersection3Points[key]["line3"]["boundA"]} boundB: {intersection3Points[key]["line3"]["boundB"]}')
	#plt.plot([intersection3Points[key]["line1"]["boundA"][0], intersection3Points[key]["line1"]["boundB"][0]], [intersection3Points[key]["line1"]["boundA"][1], intersection3Points[key]["line1"]["boundB"][1]], "-bo")
	#plt.plot([intersection3Points[key]["line2"]["boundA"][0], intersection3Points[key]["line2"]["boundB"][0]], [intersection3Points[key]["line2"]["boundA"][1], intersection3Points[key]["line2"]["boundB"][1]], "-bo")
	#plt.plot([intersection3Points[key]["line3"]["boundA"][0], intersection3Points[key]["line3"]["boundB"][0]], [intersection3Points[key]["line3"]["boundA"][1], intersection3Points[key]["line3"]["boundB"][1]], "-bo")
	#pass

for entry in finalCell:
	#fullCell = finalCell[entry]
	clr1 = random.random()
	clr2 = random.random()
	clr3 = random.random()

	for edge in finalCell[entry]["vertices"]:
		#print(edge)
		#vert = finalCell[entry]["vertices"]
		plt.plot([edge[0][0], edge[1][0]], [edge[0][1], edge[1][1]], color=(clr1, clr2, clr3))
	#print(fullCell["vertices"][0][0][0], fullCell["vertices"][0][1][0], fullCell["vertices"][0][0][1], fullCell["vertices"][0][1][1])
	#plt.plot([ fullCell["vertices"][0][0][0], fullCell["vertices"][0][1][0], fullCell["vertices"][1][1][0], fullCell["vertices"][2][1][0] ], [ fullCell["vertices"][0][0][1], fullCell["vertices"][0][1][1], fullCell["vertices"][1][1][1], fullCell["vertices"][2][1][1] ], color=(clr1, clr2, clr3))
	#plt.plot([0, 0], [75, 0], "-bo")
	
plt.show()