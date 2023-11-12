
from email.policy import default
import random
import matplotlib.pyplot as plt
#import mplcursors
#				#top left	#bottom right
defaultBounds = [[0, 200], [200, 0]]
def main(plt):
	nPoints = 3#random.randint(3, 5)
	points = []
	#			#bottom left								#top left									#top right									#bottom right
	corners = [ [defaultBounds[0][0], defaultBounds[1][1]], [defaultBounds[0][0], defaultBounds[0][1]], [defaultBounds[1][0], defaultBounds[1][1]], [defaultBounds[0][1], defaultBounds[1][0]] ]
	cell = {}
	intersection3Points = {}
	edges = {}
	#possibleEdges = {}

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
		
			#print(x, y)
			#print(x > line1["boundA"][0], x > line2["boundA"][0], x < line1["boundB"][0], x < line2["boundB"][0])
			#if slope1 < 0:
			#	print(y < line1["boundA"][1], y > line1["boundB"][1])
			#else:
			#	print(y > line1["boundA"][1], y < line1["boundB"][1])

			#if slope2 < 0:
			#	print(y < line2["boundA"][1], y > line2["boundB"][1])
			#else:
			#	print(y > line2["boundA"][1], y < line2["boundB"][1])

			#print(f'line1: {line1["boundA"]} {line1["boundB"]} line2: {line2["boundA"]} {line2["boundB"]}')

			if x > line1["boundA"][0] and x > line2["boundA"][0] and x < line1["boundB"][0] and x < line2["boundB"][0]:
				check1 = False
				check2 = False

				if (slope1 < 0 and y < line1["boundA"][1] and y > line1["boundB"][1]) or (slope1 > 0 and y > line1["boundA"][1] and y < line1["boundB"][1]):
					check1 = True

				if (slope2 < 0 and y < line2["boundA"][1] and y > line2["boundB"][1]) or (slope2 > 0 and y > line2["boundA"][1] and y < line2["boundB"][1]):
					check2 = True

				if check1 == True and check2 == True:
					return x, y
				else:
					return None, None
			else:
				#print(f'intersection {x, y} is out of bounds {line1["boundA"]} {line1["boundB"]} or {line2["boundA"]} {line2["boundB"]}')
				return None, None
		else:
			#print(f"there is no interesection of y = {slope1}(x - {midPt1[0]}) + {midPt1[1]} and y = {slope2}(x - {midPt2[0]}) + {midPt2[1]} or they are the same equation")
			return None, None


	def equationToYPoint(equation, x):
		return equation["slope"] * (x - equation["midpoint"][0]) + equation["midpoint"][1]

	def equationToXPoint(equation, y):
		return ((y - equation["midpoint"][1])/equation["slope"]) + equation["midpoint"][0]
	
	def setDefaultBounds(slope, mPtX, mPtY, givenBounds):#, lineBounds):
		leftBound = givenBounds[0][0]
		topBound = givenBounds[0][1]
		rightBound = givenBounds[1][0]
		bottomBound = givenBounds[1][1]

		pointA = [0, 0]#lineBounds[0]
		pointB = [0, 0]#lineBounds[1]

		yA = slope * (leftBound - mPtX) + mPtY
	
		if yA > topBound:
			xA = mPtX + (topBound - mPtY)/slope
			pointA = [xA, topBound]
		elif yA < bottomBound:
			xA = mPtX + (bottomBound - mPtY)/slope
			pointA = [xA, bottomBound]
		else:
			pointA = [leftBound, yA]

		yB = slope * (rightBound - mPtX) + mPtY
	
		if yB > topBound:
			xB = mPtX + (topBound - mPtY)/slope
			pointB = [xB, topBound]
		elif yB < bottomBound:
			xB = mPtX + (bottomBound - mPtY)/slope
			pointB = [xB, bottomBound]
		else:
			pointB = [rightBound, yB]

		return pointA, pointB

	def pointDistanceTargetSort(target, array): 
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
		return list(map(float, key.replace("_", ", ").removesuffix("]").removeprefix("[").split(", ")))

	def pointToKey(point):
		return str(point).replace(', ', '_')

# 	def getSlope(a, b, c, d):
# 		m = 0
# 		if (a - c) == 0 and (b - d) < 0:
# 			m = -1000
# 		elif (a - c) == 0 and (b - d) > 0:
# 			m = 1000
# 		else:
# 			m = (b - d) / (a - c)
# 		return m

	def findMinX(array):
		n = len(array)
	
		for i in range(n):
			for j in range(0, n - i - 1):
				if array[j][0] > array[j + 1][0]:
					array[j], array[j + 1] = array[j + 1], array[j]
		return array[0]

	def findMaxX(array):
		n = len(array)
	
		for i in range(n):
			for j in range(0, n - i - 1):
				if array[j][0] < array[j + 1][0]:
					array[j], array[j + 1] = array[j + 1], array[j]
		return array[0]

	def findMinY(array):
		n = len(array)
	
		for i in range(n):
			for j in range(0, n - i - 1):
				if array[j][1] > array[j + 1][1]:
					array[j], array[j + 1] = array[j + 1], array[j]
		return array[0]

	def findMaxY(array):
		n = len(array)
	
		for i in range(n):
			for j in range(0, n - i - 1):
				if array[j][1] < array[j + 1][1]:
					array[j], array[j + 1] = array[j + 1], array[j]
		return array[0]

	for i in range(0, nPoints):
		n1 = int(random.random() * 200)
		n2 = int(random.random() * 200)
		points.append([n1, n2])
	#points = [[73, 147], [140, 180], [6, 187]]
	n = len(points)
	
	for i in range(n):
		for j in range(0, n - i - 1):
			if points[j][1] > points[j + 1][1]:
				points[j], points[j + 1] = points[j + 1], points[j]

	for i in range(n):
		cell.update({ f"{str(points[i]).replace(', ', '_')}" : {"point":points[i], "otherPoint":{ "[None_None]" : {"point":[None, None], "slope":None, "midpoint":[None, None], "boundA":[0, 200], "boundB":[200, 0]} } } })

	

	#[(88, 56), (178, 131), (28, 147), (89, 181)] #problem
	#[(187, 34), (112, 75), (91, 144)] #problem?
	#[(52, 31), (2, 72), (125, 92)] #not problem
	#[(27, 102), (85, 131), (40, 155), (141, 157)] #problem
	#[(195, 68), (149, 99), (65, 114), (113, 133), (168, 192)] #problem?
	#[(112, 39), (54, 63), (79, 142), (63, 148)] #problem?
	#[(68, 7), (52, 39), (17, 53), (180, 139)] #not problem?
	#[(62, 22), (34, 46), (184, 66), (197, 99)] #problem!
	#[(22, 53), (111, 56), (5, 70), (87, 89), (43, 124)] #problem
	#[(21, 81), (133, 99), (57, 111), (113, 173)] #very good example of a problem
	#[(13, 109), (2, 145), (174, 174), (157, 191)] #problem
	#[(134, 8), (160, 37), (27, 49), (183, 84), (25, 109)] #problem

	#[(82, 15), (108, 74), (55, 161)] #didn't detect a 3-intersect
	#[(127, 14), (104, 85), (153, 90), (134, 113)] #very incorrect
	#[(97, 49), (67, 91), (155, 152), (99, 179)] #very incorrect
	#[(56, 25), (46, 159), (171, 161), (14, 165)]
	#[(197, 3), (132, 19), (89, 179)] #didn't detect a 3-intersect
	#[(108, 17), (2, 41), (193, 53)] #working correctly
	#[(191, 97), (180, 162), (144, 196)] #didn't detect a 3-intersect
	#[(143, 14), (163, 78), (161, 98), (0, 171)] #has maybe two 3-intersects close together
	#[(99, 42), (154, 80), (5, 140), (155, 170), (101, 171)]
	#[(21, 14), (166, 67), (173, 108), (8, 112), (55, 113)]
	#[(167, 12), (65, 24), (11, 81), (51, 187)]

	#[(67, 55), (31, 64), (151, 76), (111, 188)] #an example of the removal of an intersection working

	#[(183, 55), (150, 64), (118, 104), (106, 119)] #problem

	#[[174, 14], [159, 100], [127, 103], [176, 105]] #edge formation not working?

	print(points)

	# easy to see arrangements
	#[(3, 56), (77, 74), (93, 187)]
	#[(37, 38), (131, 51), (121, 108), (33, 111)]
	#[(19, 43), (110, 55), (14, 131), (150, 192)]
	#[(111, 29), (15, 70), (27, 74), (51, 168)]
	#[(166, 99), (67, 174), (196, 186), (127, 188)]
	#[(68, 24), (106, 67), (146, 71), (41, 162)]
	#[[95, 50], [43, 107], [187, 143], [43, 196]]
	#[[55, 18], [193, 105], [96, 156], [9, 159]]
	#[[58, 75], [188, 87], [131, 107], [168, 143]]
	#[[2, 41], [136, 101], [164, 150], [29, 189]]

	#neat arrangements
	#[(102, 110), (48, 145), (6, 198)]
	#[(168, 15), (51, 117), (19, 147)]
	#[(38, 69), (127, 168), (39, 171)]
	#[(14, 31), (16, 35), (76, 37), (79, 114), (63, 120)]
	#[(196, 5), (198, 15), (6, 72)]
	#[(7, 14), (17, 62), (186, 82), (197, 115), (178, 139)]
	#[(39, 115), (23, 125), (40, 126)]
	#[(12, 40), (163, 79), (33, 136)]
	#[(88, 75), (4, 103), (191, 156), (118, 169)]
	#[(41, 69), (89, 73), (121, 76), (74, 78), (52, 111)]
	#[(132, 1), (130, 74), (126, 130), (2, 135), (47, 139)]
	#[(27, 97), (6, 123), (67, 158), (115, 197)]

	#working
	#[(181, 97), (168, 102), (178, 111), (70, 148)]
	#[(172, 24), (54, 66), (10, 94), (95, 107)]

	# the cases were lines that appear to intersect but are not registered is when one of the lines is actually 2 lines less than 0.3 appart, but they intersect at two diff spots
	#[(86, 29), (134, 29), (30, 101)] 
	#[(193, 9), (162, 18), (141, 54), (56, 54), (137, 70)]

	#[(190, 29), (59, 57), (64, 131), (6, 134), (13, 187)] # a test of the triangle check

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
			m = 0

			if (b - d) == 0 and (a - c) < 0:
				m = 1000
			elif (b - d) == 0 and (a - c) > 0:
				m = -1000
			else:
				m = -1 * (a - c) / (b - d)
		
# 			m2 = getSlope(a, b, c, d) * -1
# 			print(m == m2, m, m2)

			mPtX = (a + c) / 2
			mPtY = (b + d) / 2
		
			if f"[{a}_{b}]" != f"[{c}_{d}]":

				boundA, boundB = setDefaultBounds(m, mPtX, mPtY, defaultBounds)
			
				if not f"[{a}_{b}]" in cell:
					cell.update({ f"[{a}_{b}]" : {"point":[a, b], "otherPoint":{ f"[{c}_{d}]" : {"point":[c, d], "slope":m, "midpoint":[mPtX, mPtY], "boundA":boundA, "boundB":boundB} } } })
					#print(f"cell does not contain ({a}_{b})")
				elif f"[{a}_{b}]" in cell:
					#print(f"cell contains ({a}_{b})")
					if "[None_None]" == list(cell[f"[{a}_{b}]"]["otherPoint"].keys())[0]:
						cell.update({ f"[{a}_{b}]" : {"point":[a, b], "otherPoint":{ f"[{c}_{d}]" : {"point":[c, d], "slope":m, "midpoint":[mPtX, mPtY], "boundA":boundA, "boundB":boundB} } } })
					elif not f"[{c}_{d}]" in cell[f"[{a}_{b}]"]["otherPoint"]:
						#print(f"({a}_{b}) does not contain ({c}_{d})")
						cell[f"[{a}_{b}]"]["otherPoint"].update({ f"[{c}_{d}]" : {"point":[c, d], "slope":m, "midpoint":[mPtX, mPtY], "boundA":boundA, "boundB":boundB} } )

		for j in range(0, n):
			solver(pt[0], pt[1], points2[j][0], points2[j][1])

	#removes intersects that are too close to a site and merges lines that are too close
	for site in cell:
		kys = list(cell[site]["otherPoint"].keys())

		for key in kys:
			for point in points:
				if key in cell[site]["otherPoint"]:
					dist = distance(point[0], point[0], cell[site]["otherPoint"][key]["midpoint"][0], cell[site]["otherPoint"][key]["midpoint"][1])
					if dist < 0.1:
						del cell[site]["otherPoint"][key]
						print("deleting")
					
		for key1 in kys:
			for key2 in kys:
				if key1 != key2:
					if (cell[site]["otherPoint"][key1]["boundA"][0] - cell[site]["otherPoint"][key2]["boundA"][0] < 0.3 and cell[site]["otherPoint"][key1]["boundA"][0] - cell[site]["otherPoint"][key2]["boundA"][0] > -0.3) and (cell[site]["otherPoint"][key1]["boundB"][0] - cell[site]["otherPoint"][key2]["boundB"][0] < 0.3 and cell[site]["otherPoint"][key1]["boundB"][0] - cell[site]["otherPoint"][key2]["boundB"][0] > -0.3):
						cell[site]["otherPoint"][key1]["boundA"][0] = (cell[site]["otherPoint"][key1]["boundA"][0] + cell[site]["otherPoint"][key2]["boundA"][0])/2
						cell[site]["otherPoint"][key1]["boundB"][0] = (cell[site]["otherPoint"][key1]["boundB"][0] + cell[site]["otherPoint"][key2]["boundB"][0])/2
						cell[site]["otherPoint"][key2]["boundA"][0] = (cell[site]["otherPoint"][key1]["boundA"][0] + cell[site]["otherPoint"][key2]["boundA"][0])/2
						cell[site]["otherPoint"][key2]["boundB"][0] = (cell[site]["otherPoint"][key1]["boundB"][0] + cell[site]["otherPoint"][key2]["boundB"][0])/2

	for currentPoint in points:
		cell2 = cell.copy()
		arrayPoint = str(currentPoint).replace(", ", "_")
		array = cell2[arrayPoint]["otherPoint"]

		n = len(array)

		keys = list(array.keys())

		for i in range(n):
			for j in range(0, n - i - 1):
				point1 = array[keys[j]]["midpoint"]
				point2 = array[keys[j + 1]]["midpoint"]

				distance1 = distance(currentPoint[0], currentPoint[1], point1[0], point1[1])
				distance2 = distance(currentPoint[0], currentPoint[1], point2[0], point2[1])

				if distance1 > distance2:
					array[keys[j]], array[keys[j + 1]] = array[keys[j + 1]], array[keys[j]]

		keys = list(array.keys())
		for key1 in keys:
			for key2 in keys:
				if key1 != key2:
					line1 = array[key1]
					line2 = array[key2]
					#print()
					intX, intY = intersectSolver(line1, line2)
					#print(intX, intY, f"({intX}_{intY})" in intersection3Points)
					if intX != None and not f"[{intX}_{intY}]" in intersection3Points:
						line3 = cell2[key1]["otherPoint"][key2]
						testY = equationToYPoint(line3, intX)
						testY = float("%.8f" % testY)
						intY = float("%.8f" % intY)
						intX = float("%.8f" % intX)
						#print(testY, intY, testY == intY)
						if testY == intY:
							d1 = distance(intX, intY, currentPoint[0], currentPoint[1])
							d2 = distance(intX, intY, line1["point"][0], line1["point"][1])
							d3 = distance(intX, intY, line2["point"][0], line2["point"][1])

							d1 = float("%.5f" % d1)
							d2 = float("%.5f" % d2)
							d3 = float("%.5f" % d3)

							if d1 == d2 == d3:
								intersection3Points.update({f"[{intX}_{intY}]" : {"intPoint":[intX, intY], "sites":[currentPoint, line1["point"], line2["point"]],
 "line1":{"sites":[currentPoint, line1["point"]], "slope":line1["slope"], "midpoint":line1["midpoint"], "boundA":line1["boundA"], "boundB":line1["boundB"]},
 "line2":{"sites":[currentPoint, line2["point"]], "slope":line2["slope"], "midpoint":line2["midpoint"], "boundA":line2["boundA"], "boundB":line2["boundB"]},
 "line3":{"sites":[line1["point"], line2["point"]], "slope":line3["slope"], "midpoint":line3["midpoint"], "boundA":line3["boundA"], "boundB":line3["boundB"]}
}})

		def createLine(a, b, c, d):
			if a > c:
				a, b, c, d = c, d, a, b
			m = 0

			if (a - c) == 0 and (b - d) < 0:
				m = -1000
			elif (a - c) == 0 and (b - d) > 0:
				m = 1000
			else:
				m = (b - d) / (a - c)

			mPtX = (a + c) / 2
			mPtY = (b + d) / 2

			return {"slope":m, "midpoint":[mPtX, mPtY], "boundA":[a, b], "boundB":[c, d]}

		closest =array[keys[0]]["midpoint"]
		minDist = distance(currentPoint[0], currentPoint[1], closest[0], closest[1])
		intersects = list(intersection3Points.keys())
		for inter in intersects:
			testDist = distance(intersection3Points[inter]["intPoint"][0], intersection3Points[inter]["intPoint"][1], currentPoint[0], currentPoint[1])
			if testDist < minDist:
				try:
					del intersection3Points[inter]
					print("removing an intersection")
				except Exception:
					pass
			else:
				site1 = intersection3Points[inter]["sites"][0]
				site2 = intersection3Points[inter]["sites"][1]
				site3 = intersection3Points[inter]["sites"][2]
				#intPt = intersection3Points[inter]["intPoint"]

				S1ToS2 = createLine(site1[0], site1[1], site2[0], site2[1])
				S1ToS3 = createLine(site1[0], site1[1], site3[0], site3[1])
				S2ToS3 = createLine(site2[0], site2[1], site3[0], site3[1])

				#plt.plot([site1[0], site2[0], site3[0]], [site1[1], site2[1], site3[1]], "-yo")

				for pt in points:
					#if pt != site1 and pt != site2 and pt != site3:
					if pt[0] != site1[0] and pt[1] != site1[1] and pt[0] != site2[0] and pt[1] != site2[1] and pt[0] != site3[0] and pt[1] != site3[1]:
						#print(f"slope:{(pt[1] - defaultBounds[0][1])/(pt[0] - defaultBounds[0][0])}")
						#print(f"midpoint:{(pt[0] + defaultBounds[0][0])/2, (pt[1] + defaultBounds[0][1])/2}")
						#print(f'boundA:{defaultBounds[0][0], defaultBounds[0][1]}')
						#print(f'boundB:{pt}')
						test = {"slope":(pt[1] - defaultBounds[0][1])/(pt[0] - defaultBounds[0][0]), "midpoint":[(pt[0] + defaultBounds[0][0])/2, (pt[1] + defaultBounds[0][1])/2], "boundA":[defaultBounds[0][0], defaultBounds[0][1]], "boundB":pt}
						#plt.plot([defaultBounds[0][0], pt[0]], [defaultBounds[0][1], pt[1]], "-go")
						int1X, int1Y = intersectSolver(S1ToS2, test)
						int2X, int2Y = intersectSolver(S1ToS3, test)
						int3X, int3Y = intersectSolver(S2ToS3, test)
						
						nIntersects = 0
						if int1X != None:
							nIntersects += 1
						if int2X != None:
							nIntersects += 1
						if int3X != None:
							nIntersects += 1
						
						if nIntersects == 1:
							#print(f"point being removed: {intersection3Points[inter]['intPoint']}")
							del intersection3Points[inter]
	
	# Gets rid of intersection points that are not in the correct location but otherwise would be valid
	intersects = list(intersection3Points.keys())
	for inter in intersects:
		intPoint = intersection3Points[inter]["intPoint"]
		minDist = distance(intPoint[0], intPoint[1], intersection3Points[inter]["sites"][0][0], intersection3Points[inter]["sites"][0][1]) - 0.1
		for site in points:
			dist = distance(intPoint[0], intPoint[1], site[0], site[1])
			if dist < minDist:
				del intersection3Points[inter]
				break
	# Need to also change cell list somehow
	for inter in intersection3Points:
		intPt = intersection3Points[inter]["intPoint"]
		line1 = intersection3Points[inter]["line1"]
		line2 = intersection3Points[inter]["line2"]
		line3 = intersection3Points[inter]["line3"]

		dist1 = distance(intPt[0], intPt[1], line1["midpoint"][0], line1["midpoint"][1])
		dist2 = distance(intPt[0], intPt[1], line2["midpoint"][0], line2["midpoint"][1])
		dist3 = distance(intPt[0], intPt[1], line3["midpoint"][0], line3["midpoint"][1])

		allLeft = line1["midpoint"][0] < intPt[0] and line2["midpoint"][0] < intPt[0] and line3["midpoint"][0] < intPt[0]
		allRight = line1["midpoint"][0] > intPt[0] and line2["midpoint"][0] > intPt[0] and line3["midpoint"][0] > intPt[0]
		allBottom = line1["midpoint"][1] < intPt[1] and line2["midpoint"][1] < intPt[1] and line3["midpoint"][1] < intPt[1]
		allTop = line1["midpoint"][1] > intPt[1] and line2["midpoint"][1] > intPt[1] and line3["midpoint"][1] > intPt[1]

		if allLeft or allRight or allBottom or allTop:
			if dist1 < dist2 and dist1 < dist3:
				if line1["midpoint"][0] < intPt[0]:
					line1["boundA"] = intPt
				else:
					line1["boundB"] = intPt
			else:
				if line1["midpoint"][0] < intPt[0]:
					line1["boundB"] = intPt
				else:
					line1["boundA"] = intPt

			if dist2 < dist1 and dist2 < dist3:
				if line2["midpoint"][0] < intPt[0]:
					line2["boundA"] = intPt
				else:
					line2["boundB"] = intPt
			else:
				if line2["midpoint"][0] < intPt[0]:
					line2["boundB"] = intPt
				else:
					line2["boundA"] = intPt

			if dist3 < dist1 and dist3 < dist2:
				if line3["midpoint"][0] < intPt[0]:
					line3["boundA"] = intPt
				else:
					line3["boundB"] = intPt
			else:
				if line3["midpoint"][0] < intPt[0]:
					line3["boundB"] = intPt
				else:
					line3["boundA"] = intPt

		else:
			if line1["midpoint"][0] < intPt[0]:
				line1["boundB"] = intPt
			else:
				line1["boundA"] = intPt

			if line2["midpoint"][0] < intPt[0]:
				line2["boundB"] = intPt
			else:
				line2["boundA"] = intPt

			if line3["midpoint"][0] < intPt[0]:
				line3["boundB"] = intPt
			else:
				line3["boundA"] = intPt

	# Fixes times when the line that goes through two intersection points does not get its boundry changed correctly
	for inter1 in intersection3Points:
		for inter2 in intersection3Points:
			if inter1 != inter2:
				p1L1 = intersection3Points[inter1]["line1"]
				p1L2 = intersection3Points[inter1]["line2"]
				p1L3 = intersection3Points[inter1]["line3"]

				p2L1 = intersection3Points[inter2]["line1"]
				p2L2 = intersection3Points[inter2]["line2"]
				p2L3 = intersection3Points[inter2]["line3"]

				if p1L1["slope"] == p2L1["slope"] or p1L1["slope"] == p2L2["slope"] or p1L1["slope"] == p2L3["slope"]:
					if p1L1["slope"] == p2L1["slope"]:
						if intersection3Points[inter1]["intPoint"][0] < intersection3Points[inter2]["intPoint"][0]:
							p1L1["boundA"] = intersection3Points[inter1]["intPoint"]
							#p1L1["boundB"] = intersection3Points[inter2]["intPoint"]
							p2L1["boundA"] = intersection3Points[inter1]["intPoint"]
							#p2L1["boundB"] = intersection3Points[inter2]["intPoint"]
						else:
							p1L1["boundB"] = intersection3Points[inter1]["intPoint"]
							#p1L1["boundA"] = intersection3Points[inter2]["intPoint"]
							p2L1["boundB"] = intersection3Points[inter1]["intPoint"]
							#p2L1["boundA"] = intersection3Points[inter2]["intPoint"]
					elif p1L1["slope"] == p2L2["slope"]:
						if intersection3Points[inter1]["intPoint"][0] < intersection3Points[inter2]["intPoint"][0]:
							p1L1["boundA"] = intersection3Points[inter1]["intPoint"]
							#p1L1["boundB"] = intersection3Points[inter2]["intPoint"]
							p2L2["boundA"] = intersection3Points[inter1]["intPoint"]
							#p2L2["boundB"] = intersection3Points[inter2]["intPoint"]
						else:
							p1L1["boundB"] = intersection3Points[inter1]["intPoint"]
							#p1L1["boundA"] = intersection3Points[inter2]["intPoint"]
							p2L2["boundB"] = intersection3Points[inter1]["intPoint"]
							#p2L2["boundA"] = intersection3Points[inter2]["intPoint"]
					else:
						if intersection3Points[inter1]["intPoint"][0] < intersection3Points[inter2]["intPoint"][0]:
							p1L1["boundA"] = intersection3Points[inter1]["intPoint"]
							#p1L1["boundB"] = intersection3Points[inter2]["intPoint"]
							p2L3["boundA"] = intersection3Points[inter1]["intPoint"]
							#p2L3["boundB"] = intersection3Points[inter2]["intPoint"]
						else:
							p1L1["boundB"] = intersection3Points[inter1]["intPoint"]
							#p1L1["boundA"] = intersection3Points[inter2]["intPoint"]
							p2L3["boundB"] = intersection3Points[inter1]["intPoint"]
							#p2L3["boundA"] = intersection3Points[inter2]["intPoint"]
				elif p1L2["slope"] == p2L1["slope"] or p1L2["slope"] == p2L2["slope"] or p1L2["slope"] == p2L3["slope"]:
					if p1L2["slope"] == p2L1["slope"]:
						if intersection3Points[inter1]["intPoint"][0] < intersection3Points[inter2]["intPoint"][0]:
							p1L2["boundA"] = intersection3Points[inter1]["intPoint"]
							#p1L2["boundB"] = intersection3Points[inter2]["intPoint"]
							p2L1["boundA"] = intersection3Points[inter1]["intPoint"]
							#p2L1["boundB"] = intersection3Points[inter2]["intPoint"]
						else:
							p1L2["boundB"] = intersection3Points[inter1]["intPoint"]
							#p1L2["boundA"] = intersection3Points[inter2]["intPoint"]
							p2L1["boundB"] = intersection3Points[inter1]["intPoint"]
							#p2L1["boundA"] = intersection3Points[inter2]["intPoint"]
					elif p1L2["slope"] == p2L2["slope"]:
						if intersection3Points[inter1]["intPoint"][0] < intersection3Points[inter2]["intPoint"][0]:
							p1L2["boundA"] = intersection3Points[inter1]["intPoint"]
							#p1L2["boundB"] = intersection3Points[inter2]["intPoint"]
							p2L2["boundA"] = intersection3Points[inter1]["intPoint"]
							#p2L2["boundB"] = intersection3Points[inter2]["intPoint"]
						else:
							p1L2["boundB"] = intersection3Points[inter1]["intPoint"]
							#p1L2["boundA"] = intersection3Points[inter2]["intPoint"]
							p2L2["boundB"] = intersection3Points[inter1]["intPoint"]
							#p2L2["boundA"] = intersection3Points[inter2]["intPoint"]
					else:
						if intersection3Points[inter1]["intPoint"][0] < intersection3Points[inter2]["intPoint"][0]:
							p1L2["boundA"] = intersection3Points[inter1]["intPoint"]
							#p1L2["boundB"] = intersection3Points[inter2]["intPoint"]
							p2L3["boundA"] = intersection3Points[inter1]["intPoint"]
							#p2L3["boundB"] = intersection3Points[inter2]["intPoint"]
						else:
							p1L2["boundB"] = intersection3Points[inter1]["intPoint"]
							#p1L2["boundA"] = intersection3Points[inter2]["intPoint"]
							p2L3["boundB"] = intersection3Points[inter1]["intPoint"]
							#p2L3["boundA"] = intersection3Points[inter2]["intPoint"]
				elif p1L3["slope"] == p2L1["slope"] or p1L3["slope"] == p2L2["slope"] or p1L3["slope"] == p2L3["slope"]:
					if p1L3["slope"] == p2L1["slope"]:
						if intersection3Points[inter1]["intPoint"][0] < intersection3Points[inter2]["intPoint"][0]:
							p1L3["boundA"] = intersection3Points[inter1]["intPoint"]
							#p1L3["boundB"] = intersection3Points[inter2]["intPoint"]
							p2L1["boundA"] = intersection3Points[inter1]["intPoint"]
							#p2L1["boundB"] = intersection3Points[inter2]["intPoint"]
						else:
							p1L3["boundB"] = intersection3Points[inter1]["intPoint"]
							#p1L3["boundA"] = intersection3Points[inter2]["intPoint"]
							p2L1["boundB"] = intersection3Points[inter1]["intPoint"]
							#p2L1["boundA"] = intersection3Points[inter2]["intPoint"]
					elif p1L3["slope"] == p2L2["slope"]:
						if intersection3Points[inter1]["intPoint"][0] < intersection3Points[inter2]["intPoint"][0]:
							p1L3["boundA"] = intersection3Points[inter1]["intPoint"]
							#p1L3["boundB"] = intersection3Points[inter2]["intPoint"]
							p2L2["boundA"] = intersection3Points[inter1]["intPoint"]
							#p2L2["boundB"] = intersection3Points[inter2]["intPoint"]
						else:
							p1L3["boundB"] = intersection3Points[inter1]["intPoint"]
							#p1L3["boundA"] = intersection3Points[inter2]["intPoint"]
							p2L2["boundB"] = intersection3Points[inter1]["intPoint"]
							#p2L2["boundA"] = intersection3Points[inter2]["intPoint"]
					else:
						if p1L3["slope"] == p2L1["slope"]:
							if intersection3Points[inter1]["intPoint"][0] < intersection3Points[inter2]["intPoint"][0]:
								p1L3["boundA"] = intersection3Points[inter1]["intPoint"]
								#p1L3["boundB"] = intersection3Points[inter2]["intPoint"]
								p2L1["boundA"] = intersection3Points[inter1]["intPoint"]
								#p2L1["boundB"] = intersection3Points[inter2]["intPoint"]
							else:
								p1L3["boundB"] = intersection3Points[inter1]["intPoint"]
								#p1L3["boundA"] = intersection3Points[inter2]["intPoint"]
								p2L1["boundB"] = intersection3Points[inter1]["intPoint"]
								#p2L1["boundA"] = intersection3Points[inter2]["intPoint"]
						elif p1L3["slope"] == p2L2["slope"]:
							if intersection3Points[inter1]["intPoint"][0] < intersection3Points[inter2]["intPoint"][0]:
								p1L3["boundA"] = intersection3Points[inter1]["intPoint"]
								#p1L3["boundB"] = intersection3Points[inter2]["intPoint"]
								p2L2["boundA"] = intersection3Points[inter1]["intPoint"]
								#p2L2["boundB"] = intersection3Points[inter2]["intPoint"]
							else:
								p1L3["boundB"] = intersection3Points[inter1]["intPoint"]
								#p1L3["boundA"] = intersection3Points[inter2]["intPoint"]
								p2L2["boundB"] = intersection3Points[inter1]["intPoint"]
								#p2L2["boundA"] = intersection3Points[inter2]["intPoint"]
						else:
							if intersection3Points[inter1]["intPoint"][0] < intersection3Points[inter2]["intPoint"][0]:
								p1L3["boundA"] = intersection3Points[inter1]["intPoint"]
								#p1L3["boundB"] = intersection3Points[inter2]["intPoint"]
								p2L3["boundA"] = intersection3Points[inter1]["intPoint"]
								#p2L3["boundB"] = intersection3Points[inter2]["intPoint"]
							else:
								p1L3["boundB"] = intersection3Points[inter1]["intPoint"]
								#p1L3["boundA"] = intersection3Points[inter2]["intPoint"]
								p2L3["boundB"] = intersection3Points[inter1]["intPoint"]
								#p2L3["boundA"] = intersection3Points[inter2]["intPoint"]
	# changes the boundries of the lines in the "cell" list
	if intersection3Points.__len__() > 0:
		for inter in intersection3Points:
			for site1 in intersection3Points[inter]["sites"]:
				for site2 in intersection3Points[inter]["sites"]:
					if pointToKey(site1) != pointToKey(site2):
						keySite1 = pointToKey(site1)
						keySite2 = pointToKey(site2)
						if cell[keySite1]["otherPoint"][keySite2]["slope"] == intersection3Points[inter]["line1"]["slope"]:
							cell[keySite1]["otherPoint"][keySite2]["boundA"] = intersection3Points[inter]["line1"]["boundA"]
							cell[keySite1]["otherPoint"][keySite2]["boundB"] = intersection3Points[inter]["line1"]["boundB"]
						elif cell[keySite1]["otherPoint"][keySite2]["slope"] == intersection3Points[inter]["line2"]["slope"]:
							cell[keySite1]["otherPoint"][keySite2]["boundA"] = intersection3Points[inter]["line2"]["boundA"]
							cell[keySite1]["otherPoint"][keySite2]["boundB"] = intersection3Points[inter]["line2"]["boundB"]
						else:
							cell[keySite1]["otherPoint"][keySite2]["boundA"] = intersection3Points[inter]["line3"]["boundA"]
							cell[keySite1]["otherPoint"][keySite2]["boundB"] = intersection3Points[inter]["line3"]["boundB"]
						

	def updateEdges(array, int1, int2, line1, line2, edges):
		site1 = array[int1][line1]["sites"][0]
		site2 = array[int1][line1]["sites"][1]

		edgeBoundA = array[int1]["intPoint"]
		edgeBoundB = array[int2]["intPoint"]

		if edgeBoundA[0] > edgeBoundB[0]:
			edgeBoundA, edgeBoundB = edgeBoundB, edgeBoundA
			array[int1][line1]["boundB"] = edgeBoundB
			array[int2][line2]["boundA"] = edgeBoundA
			print("change")
		else:
			array[int1][line1]["boundA"] = edgeBoundA
			array[int2][line2]["boundB"] = edgeBoundB
		print(edgeBoundA, edgeBoundB)

		if not f"[{site1[0]}_{site1[1]}]" in edges:
			edges.update({f"[{site1[0]}_{site1[1]}]" : {"sitePoint":site1, "edges":[{"boundA":edgeBoundA, "boundB":edgeBoundB}]}})
		else:
			edges[f"[{site1[0]}_{site1[1]}]"]["edges"].append({"boundA":edgeBoundA, "boundB":edgeBoundB})
	
		if not f"[{site2[0]}_{site2[1]}]" in edges:
			edges.update({f"[{site2[0]}_{site2[1]}]" : {"sitePoint":site2, "edges":[{"boundA":edgeBoundA, "boundB":edgeBoundB}]}})
		else:
			edges[f"[{site2[0]}_{site2[1]}]"]["edges"].append({"boundA":edgeBoundA, "boundB":edgeBoundB})

		print(array[int1][line1])
		print(array[int2][line2])

		possibleEdges = array[int1].copy()
		del possibleEdges[line1]
		del possibleEdges["sites"]
		del possibleEdges["intPoint"]
		print(f"possibleEdges- {possibleEdges}")

		possibleKeys = list(possibleEdges.keys())
		for key in possibleKeys:
			if (possibleEdges[key]["boundA"][0] == defaultBounds[0][0] or possibleEdges[key]["boundA"][1] == defaultBounds[0][1] or possibleEdges[key]["boundA"][1] == defaultBounds[1][1]) or (possibleEdges[key]["boundB"][0] == defaultBounds[1][0] or possibleEdges[key]["boundB"][1] == defaultBounds[0][1] or possibleEdges[key]["boundB"][1] == defaultBounds[1][1]):
				edges[f"[{site1[0]}_{site1[1]}]"]["edges"].append({"boundA":possibleEdges[key]["boundA"], "boundB":possibleEdges[key]["boundB"]})
		print()

	# Makes edges that are guaranteed correct
	intKeys = list(intersection3Points.keys())
	for key1 in intKeys:
		for key2 in intKeys:
			if key1 != key2:
				int1Line1 = intersection3Points[key1]["line1"]
				int1Line2 = intersection3Points[key1]["line2"]
				int1Line3 = intersection3Points[key1]["line3"]

				int2Line1 = intersection3Points[key2]["line1"]
				int2Line2 = intersection3Points[key2]["line2"]
				int2Line3 = intersection3Points[key2]["line3"]

				#print(int1Line1["sites"][0] in int2Line1["sites"] and int1Line1["sites"][1] in int2Line1["sites"])
				#print(int1Line1["sites"][0] in int2Line2["sites"] and int1Line1["sites"][1] in int2Line2["sites"])
				#print(int1Line1["sites"][0] in int2Line3["sites"] and int1Line1["sites"][1] in int2Line3["sites"])

				print(int1Line1["midpoint"] == int2Line1["midpoint"], int1Line1["midpoint"], int2Line1["midpoint"])
				print(int1Line1["midpoint"] == int2Line2["midpoint"], int1Line1["midpoint"], int2Line2["midpoint"])
				print(int1Line1["midpoint"] == int2Line3["midpoint"], int1Line1["midpoint"], int2Line3["midpoint"])

				print()

				if int1Line1["midpoint"] == int2Line1["midpoint"] or int1Line1["midpoint"] == int2Line2["midpoint"] or int1Line1["midpoint"] == int2Line3["midpoint"]:
					if (int1Line1["boundA"][0] == defaultBounds[0][0] or int1Line1["boundA"][1] == defaultBounds[0][1] or int1Line1["boundA"][1] == defaultBounds[1][1]) and (int1Line1["boundB"][0] == defaultBounds[1][0] or int1Line1["boundB"][1] == defaultBounds[0][1] or int1Line1["boundB"][1] == defaultBounds[1][1]):
						pass
					if int1Line1["midpoint"] == int2Line1["midpoint"]:
						updateEdges(intersection3Points, key1, key2, "line1", "line1", edges)
					elif int1Line1["midpoint"] == int2Line2["midpoint"]:
						updateEdges(intersection3Points, key1, key2, "line1", "line2", edges)
					else:
						updateEdges(intersection3Points, key1, key2, "line1", "line3", edges)
				elif int1Line2["midpoint"] == int2Line1["midpoint"] or int1Line2["midpoint"] == int2Line2["midpoint"] or int1Line2["midpoint"] == int2Line3["midpoint"]:
					if int1Line2["midpoint"] == int2Line1["midpoint"]:
						updateEdges(intersection3Points, key1, key2, "line2", "line1", edges)
					elif int1Line2["midpoint"] == int2Line2["midpoint"]:
						updateEdges(intersection3Points, key1, key2, "line2", "line2", edges)
					else:
						updateEdges(intersection3Points, key1, key2, "line2", "line3", edges)
				elif int1Line3["midpoint"] == int2Line1["midpoint"] or int1Line3["midpoint"] == int2Line2["midpoint"] or int1Line3["midpoint"] == int2Line3["midpoint"]:
					if int1Line3["midpoint"] == int2Line1["midpoint"]:
						updateEdges(intersection3Points, key1, key2, "line3", "line1", edges)
					elif int1Line3["midpoint"] == int2Line2["midpoint"]:
						updateEdges(intersection3Points, key1, key2, "line3", "line2", edges)
					else:
						updateEdges(intersection3Points, key1, key2, "line3", "line3", edges)

	siteKeys = cell.keys()
	
	for site in siteKeys:
		if cell[site]["otherPoint"].__len__() > 1:
			points2 = points.copy()
			#pointDistanceTargetSort(keyToPoints(site), points2)
			#del points2[0]
			
			#shouldRemove = True
			#for inter in intersection3Points:
			#	test = [pointToKey(intersection3Points[inter]["sites"][0]), pointToKey(intersection3Points[inter]["sites"][1]), pointToKey(intersection3Points[inter]["sites"][2])]
			#	if not (site in test and pointToKey(points[0]) in test and pointToKey(points[1]) in test):
			#		shouldRemove =
			

			minX = findMinX(points2)
			maxX = findMaxX(points2)

			if intersection3Points.__len__() == 0 and (keyToPoints(site)[0] == minX[0] or keyToPoints(site)[0] == maxX[0]):
				del cell[site]["otherPoint"][list(cell[site]["otherPoint"].keys())[1]]
					

	edgeSiteKeys = list(edges.keys())
	leftX = defaultBounds[0][0]
	rightX = defaultBounds[1][0]
	bottomY = defaultBounds[1][1]
	topY = defaultBounds[0][1]
	#print("a")
	#print(edgeSiteKeys)

	for site in cell:
		#print(site)
		match cell[site]["otherPoint"].__len__():
			case 0:
				print("case 0")
				edges.update({site: {"sitePoint":keyToPoints(site), "edges":[
{"boundA":corners[0], "boundB":corners[1]},
{"boundA":corners[1], "boundB":corners[2]},
{"boundA":corners[2], "boundB":corners[3]},
{"boundA":corners[0], "boundB":corners[3]}
]}})
			case 1:
				print("case 1")
				#edgeLine = createLine(edges[site][0][0], edges[site][0][1], edges[site][1][0], edges[site][1][1])
				sitePoint = keyToPoints(site)
				ky = list(cell[site]["otherPoint"].keys())[0]
				boundAX = cell[site]["otherPoint"][ky]["boundA"][0]
				boundAY = cell[site]["otherPoint"][ky]["boundA"][1]
				boundBX = cell[site]["otherPoint"][ky]["boundB"][0]
				boundBY = cell[site]["otherPoint"][ky]["boundB"][1]
				
				#yAtX = equationToPoint(edgeLine, sitePoint[0])
				if ( boundAX == leftX and (boundBY == topY or boundBY == bottomY) ) or ( boundBX == rightX and (boundAY == topY or boundAY == bottomY) ): #if the site is in a corner
					corner = corners.copy()
					pointDistanceTargetSort(sitePoint, corner)
					edges.update({site: {"sitePoint":sitePoint, "edges":[
{"boundA":cell[site]["otherPoint"][ky]["boundA"], "boundB":corner[0]},
{"boundA":corner[0], "boundB":cell[site]["otherPoint"][ky]["boundB"]},
{"boundA":cell[site]["otherPoint"][ky]["boundB"], "boundB":cell[site]["otherPoint"][ky]["boundA"]}
]}})
				else: #if the site is not in a corner  #would be the same as elif ( boundAX == leftX and boundBX == rightX ) or ( boundAY == bottomY and boundBY == topY ) or (boundAY == topY and boundBY == bottomY):
					#edgeLine = createLine(boundAX, boundAY, boundBX, boundBY)
					#yAtX = equationToYPoint(edgeLine, sitePoint[0])

					if boundAX == leftX and boundBX == rightX: #if the cell stretches horizontally across the area
						if cell[site]["otherPoint"][ky]["point"][1] > cell[site]["point"][1]: #if the site is below its pair/line
							edges.update({site: {"sitePoint":sitePoint, "edges":[
{"boundA":cell[site]["otherPoint"][ky]["boundA"], "boundB":corners[0]},
{"boundA":corners[0], "boundB":corners[2]},
{"boundA":corners[2], "boundB":cell[site]["otherPoint"][ky]["boundB"]},
{"boundA":cell[site]["otherPoint"][ky]["boundB"], "boundB":cell[site]["otherPoint"][ky]["boundA"]}
]}})
						else: #if the site is above its pair/line
							edges.update({site: {"sitePoint":sitePoint, "edges":[
{"boundA":cell[site]["otherPoint"][ky]["boundA"], "boundB":corners[1]},
{"boundA":corners[1], "boundB":corners[3]},
{"boundA":corners[3], "boundB":cell[site]["otherPoint"][ky]["boundB"]},
{"boundA":cell[site]["otherPoint"][ky]["boundB"], "boundB":cell[site]["otherPoint"][ky]["boundA"]}
]}})
					else: #if the cell stretches vertically across the area  #elif (boundAX == bottomY and boundBX == topY) or (boundAX == topY and boundBX == bottomY):
						#midX = (edges[site][0][0] + edges[site][1][0])/2
						if cell[site]["otherPoint"][ky]["point"][0] > cell[site]["point"][0]: #if the site is to the left of the pair/line
							if cell[site]["otherPoint"][ky]["slope"] < 0:
								edges.update({site: {"sitePoint":sitePoint, "edges":[
{"boundA":cell[site]["otherPoint"][ky]["boundA"], "boundB":corners[1]},
{"boundA":corners[1], "boundB":corners[0]},
{"boundA":corners[0], "boundB":cell[site]["otherPoint"][ky]["boundB"]},
{"boundA":cell[site]["otherPoint"][ky]["boundB"], "boundB":cell[site]["otherPoint"][ky]["boundA"]},
]}})
							else:
								edges.update({site: {"sitePoint":sitePoint, "edges":[
{"boundA":cell[site]["otherPoint"][ky]["boundA"], "boundB":corners[0]},
{"boundA":corners[0], "boundB":corners[1]},
{"boundA":corners[1], "boundB":cell[site]["otherPoint"][ky]["boundB"]},
{"boundA":cell[site]["otherPoint"][ky]["boundB"], "boundB":cell[site]["otherPoint"][ky]["boundA"]},
]}})
						else: #if the site is to the right of the pair/line
							if cell[site]["otherPoint"][ky]["slope"] < 0:
								edges.update({site: {"sitePoint":sitePoint, "edges":[
{"boundA":cell[site]["otherPoint"][ky]["boundA"], "boundB":corners[3]},
{"boundA":corners[3], "boundB":corners[2]},
{"boundA":corners[2], "boundB":cell[site]["otherPoint"][ky]["boundB"]},
{"boundA":cell[site]["otherPoint"][ky]["boundB"], "boundB":cell[site]["otherPoint"][ky]["boundA"]},
]}})
							else:
								edges.update({site: {"sitePoint":sitePoint, "edges":[
{"boundA":cell[site]["otherPoint"][ky]["boundA"], "boundB":corners[2]},
{"boundA":corners[2], "boundB":corners[3]},
{"boundA":corners[3], "boundB":cell[site]["otherPoint"][ky]["boundB"]},
{"boundA":cell[site]["otherPoint"][ky]["boundB"], "boundB":cell[site]["otherPoint"][ky]["boundA"]},
]}})

			case 2:
				print("case 2")
				print(f"site: {site}")
				boundryPairs = []
				possiblePairs = []

				boundLPts = []
				boundRPts = []
				boundTPts = []
				boundBPts = []

				kys = list(cell[site]["otherPoint"].keys())

				for otherSiteKey in kys:
					print(f"otherSiteKey: {otherSiteKey}")
					otherSite = cell[site]["otherPoint"][otherSiteKey]

					if otherSite["boundA"][0] == corners[0][0]:
						boundLPts.append(otherSite["boundA"])
					elif otherSite["boundA"][1] == corners[1][1]:
						boundTPts.append(otherSite["boundA"])
					elif otherSite["boundA"][1] == corners[0][0]:
						boundBPts.append(otherSite["boundA"])

					if otherSite["boundB"][0] == corners[3][0]:
						boundRPts.append(otherSite["boundB"])
					elif otherSite["boundB"][1] == corners[1][1]:
						boundTPts.append(otherSite["boundB"])
					elif otherSite["boundB"][1] == corners[0][0]:
						boundBPts.append(otherSite["boundB"])
					
					#possiblePairs.append([otherSite["boundA"], otherSite["boundB"]])
					if not otherSiteKey in edges:
						boundryPairs.append([otherSite["boundA"], otherSite["boundB"]])

				if boundLPts.__len__() > 1:
					boundryPairs.append([boundLPts[0], boundLPts[1]])
				elif boundLPts.__len__() == 1 and boundTPts.__len__() == 1:
					print("corner")
					boundryPairs.extend([[boundLPts[0], corners[1]], [corners[1], boundTPts[0]]])
					#boundryPairs.append([boundLPts[0], boundRPts[0]])

				if boundRPts.__len__() > 1:
					boundryPairs.append([boundRPts[0], boundRPts[1]])
				elif boundRPts.__len__() == 1 and boundBPts.__len__():
					print("corner")
					boundryPairs.extend([[boundRPts[0], corners[3]], [corners[3], boundBPts[0]]])
					#boundryPairs.append([boundRPts[0], boundBPts[0]])

				if boundTPts.__len__() > 1:
					boundryPairs.append([boundTPts[0], boundTPts[1]])
				elif boundTPts.__len__() == 1 and boundRPts.__len__() == 1:
					print("corner")
					boundryPairs.extend([[boundTPts[0], corners[2]], [corners[2], boundRPts[0]]])
					#boundryPairs.append([boundTPts[0], boundRPts[0]])

				if boundBPts.__len__() > 1:
					boundryPairs.append([boundBPts[0], boundBPts[1]])
				elif boundBPts.__len__() == 1 and boundLPts.__len__() == 1:
					print("corner")
					boundryPairs.extend([[boundBPts[0], corners[0]], [corners[0], boundLPts[0]]])
					#boundryPairs.append([boundBPts[0], boundLPts[0]])

				
				#if boundBPts.__len__() > 1 and boundLPts.__len__() > 1:
				#	possiblePairs.append([findMinY(boundLPts), findMinX(boundBPts)])
				#if boundLPts.__len__() > 1 and boundTPts.__len__() > 1:
				#	possiblePairs.append([findMaxY(boundLPts), findMinX(boundTPts)])
				#if boundTPts.__len__() > 1 and boundRPts.__len__() > 1:
				#	possiblePairs.append([findMaxX(boundTPts), findMaxY(boundRPts)])
				#if boundBPts.__len__() > 1 and boundRPts.__len__() > 1:
				#	possiblePairs.append([findMaxX(boundBPts), findMinY(boundRPts)])


				if boundLPts.__len__() == 1 and boundRPts.__len__() == 1:
					midY = (boundLPts[0][1] + boundRPts[0][1])/2
					if midY > cell[site]["point"][1]:
						boundryPairs.extend([[boundLPts[0], corners[0]], [corners[0], corners[3]], [corners[3], boundRPts[0]]])
						#possiblePairs.append([boundLPts[0], boundRPts[0]])
					else:
						boundryPairs.extend([[boundLPts[0], corners[1]], [corners[1], corners[2]], [corners[2], boundRPts[0]]])
						#possiblePairs.append([boundLPts[0], boundRPts[0]])
				elif boundTPts.__len__() == 1 and boundBPts.__len__() == 1:
					midX = (boundTPts[0][0] + boundBPts[0][0])/2
					if midX > cell[site]["point"][0]:
						boundryPairs.extend([[boundTPts[0], corners[2]], [corners[2], corners[3]], [corners[3], boundBPts[0]]])
						#possiblePairs.append([boundTPts[0], boundBPts[0]])
					else:
						boundryPairs.extend([[boundTPts[0], corners[1]], [corners[1], corners[0]], [corners[0], boundBPts[0]]])
						#possiblePairs.append([boundTPts[0], boundBPts[0]])

				print(f"boundryPairs: {boundryPairs}")
				print(f"boundLPts: {boundLPts}")
				print(f"boundRPts: {boundRPts}")
				print(f"boundTPts: {boundTPts}")
				print(f"boundBPts: {boundBPts}")
				print(f"possiblePairs: {possiblePairs}")
				#possiblePairKeys = list(map(str, possiblePairs))
				#print(possiblePairKeys)
				if site in edges:
					for pairs in boundryPairs:
						edges[site]["edges"].append({"boundA":pairs[0], "boundB":pairs[1]})

					#edges[site]["edges"].extend(boundryPairs)

					#edgeKeys = list(edges[site]["edges"].keys())

					#possiblePairKeys = list(map(str, possiblePairs))
					#print(possiblePairKeys)
					#for pos in possiblePairs
					#for edge in edgeKeys:
					#	testEdge = [pointToKey(edges[site]["edges"][edge]["boundA"]), pointToKey(edges[site]["edges"][edge]["boundB"])]
						
				else:
					edges.update({site : {"sitePoint":keyToPoints(site), "edges":[]}})
					for pairs in boundryPairs:
						edges[site]["edges"].append({"boundA":pairs[0], "boundB":pairs[1]})

					#if intersection3Points.__len__() == 0:
					#	for possible in possiblePairs:
					#		edges[site]["edges"].append({"boundA":possible[0], "boundB":possible[1]})
					#edges[site]["edges"].append({"boundA":pairs[0], "boundB":pairs[1]})
					#pass
					#print(edges[site]["edges"])
				
				print()
			case _:
				print("case _")



# 	nEdges = edgeSiteKeys.__len__()
# 
# 	match nEdges:
# 		case 0:
# 			edges.update({str(points[0]).replace(", ", "_"): {"sitePoint":points[0], "edges":[
# {"boundA":corners[0], "boundB":corners[1]},
# {"boundA":corners[1], "boundB":corners[2]},
# {"boundA":corners[2], "boundB":corners[3]},
# {"boundA":corners[0], "boundB":corners[3]}
# ]}})
# 		case 1:
# 			
# 		case 2:
# 
# 		case _:



# 	for site in edgeSiteKeys:
# 		print(site)
# 		match edges[edgeSiteKeys].__len__():
# 			case 0:
# 				print("case 0")
# 				edges.update({site: {"sitePoint":keyToPoints(site), "edges":[
# {"boundA":corners[0], "boundB":corners[1]},
# {"boundA":corners[1], "boundB":corners[2]},
# {"boundA":corners[2], "boundB":corners[3]},
# {"boundA":corners[0], "boundB":corners[3]}
# ]}})
# 			case 1:
# 				print("case 1")
# 				#edgeLine = createLine(edges[site][0][0], edges[site][0][1], edges[site][1][0], edges[site][1][1])
# 				sitePoint = keyToPoints(site)
# 				boundAX = edges[site][0][0]
# 				boundAY = edges[site][0][1]
# 				boundBX = edges[site][1][0]
# 				boundBY = edges[site][1][1]
# 				
# 				#yAtX = equationToPoint(edgeLine, sitePoint[0])
# 				if ( boundAX == leftX and (boundBY == topY or boundBY == bottomY) ) or ( boundBX == rightX and (boundAY == topY or boundAY == bottomY) ): #if the site is in a corner
# 					corner = corners.copy()
# 					pointDistanceTargetSort(sitePoint, corner)
# 					edges.update({site: {"sitePoint":sitePoint, "edges":[
# {"boundA":edges[site][0], "boundB":corner[0]},
# {"boundA":corner[0], "boundB":edges[site][1]},
# {"boundA":edges[site][1], "boundB":edges[site][0]}
# ]}})
# 				else: #if the site is not in a corner  #would be the same as elif ( boundAX == leftX and boundBX == rightX ) or ( boundAY == bottomY and boundBY == topY ) or (boundAY == topY and boundBY == bottomY):
# 					edgeLine = createLine(boundAX, boundAY, boundBX, boundBY)
# 					yAtX = equationToYPoint(edgeLine, sitePoint[0])
# 
# 					if boundAX == leftX and boundBX == rightX: #if the cell stretches horizontally across the area
# 						if sitePoint[1] < yAtX: #if the site is below its pair/line
# 							edges.update({site: {"sitePoint":sitePoint, "edges":[
# {"boundA":edges[site][0], "boundB":corners[0]},
# {"boundA":corners[0], "boundB":corners[2]},
# {"boundA":corners[2], "boundB":edges[site][1]},
# {"boundA":edges[site][1], "boundB":edges[site][0]}
# ]}})
# 						else: #if the site is above its pair/line
# 							edges.update({site: {"sitePoint":sitePoint, "edges":[
# {"boundA":edges[site][0], "boundB":corners[1]},
# {"boundA":corners[1], "boundB":corners[3]},
# {"boundA":corners[3], "boundB":edges[site][1]},
# {"boundA":edges[site][1], "boundB":edges[site][0]}
# ]}})
# 					else: #if the cell stretches vertically across the area  #elif (boundAX == bottomY and boundBX == topY) or (boundAX == topY and boundBX == bottomY):
# 						midX = (edges[site][0][0] + edges[site][1][0])/2
# 						if sitePoint[0] < midX: #if the site is to the left of the pair/line
# 							if edgeLine["slope"] < 0:
# 								edges.update({site: {"sitePoint":sitePoint, "edges":[
# {"boundA":edges[site][0], "boundB":corners[1]},
# {"boundA":corners[1], "boundB":corners[0]},
# {"boundA":corners[0], "boundB":edges[site][1]},
# {"boundA":edges[site][1], "boundB":edges[site][0]},
# ]}})
# 							else:
# 								edges.update({site: {"sitePoint":sitePoint, "edges":[
# {"boundA":edges[site][0], "boundB":corners[0]},
# {"boundA":corners[0], "boundB":corners[1]},
# {"boundA":corners[1], "boundB":edges[site][1]},
# {"boundA":edges[site][1], "boundB":edges[site][0]},
# ]}})
# 						else: #if the site is to the right of the pair/line
# 							if edgeLine["slope"] < 0:
# 								edges.update({site: {"sitePoint":sitePoint, "edges":[
# {"boundA":edges[site][0], "boundB":corners[3]},
# {"boundA":corners[3], "boundB":corners[2]},
# {"boundA":corners[2], "boundB":edges[site][1]},
# {"boundA":edges[site][1], "boundB":edges[site][0]},
# ]}})
# 							else:
# 								edges.update({site: {"sitePoint":sitePoint, "edges":[
# {"boundA":edges[site][0], "boundB":corners[2]},
# {"boundA":corners[2], "boundB":corners[3]},
# {"boundA":corners[3], "boundB":edges[site][1]},
# {"boundA":edges[site][1], "boundB":edges[site][0]},
# ]}})
# 
# 			case 2:
# 				print("case 2")
# 			case _:
# 				print("case _")

	plt.title("pixel_plot")

	for pt in points:
		plt.plot(pt[0], pt[1], "ro")

	for site in cell:
		plt.plot(cell[site]["point"][0], cell[site]["point"][1], "ro")
		for line in cell[site]["otherPoint"]:
			plt.plot(cell[site]["otherPoint"][line]["midpoint"][0], cell[site]["otherPoint"][line]["midpoint"][1], "yo")

			plt.plot([cell[site]["otherPoint"][line]["boundA"][0], cell[site]["otherPoint"][line]["boundB"][0]], [cell[site]["otherPoint"][line]["boundA"][1], cell[site]["otherPoint"][line]["boundB"][1]], color=(random.random(), random.random(), random.random()))

	for point in intersection3Points:
		plt.plot(intersection3Points[point]["intPoint"][0], intersection3Points[point]["intPoint"][1], "go")
		plt.plot([intersection3Points[point]["line1"]["boundA"][0], intersection3Points[point]["line1"]["boundB"][0]], [intersection3Points[point]["line1"]["boundA"][1], intersection3Points[point]["line1"]["boundB"][1]], color=(random.random(), random.random(), random.random()))
		plt.plot([intersection3Points[point]["line2"]["boundA"][0], intersection3Points[point]["line2"]["boundB"][0]], [intersection3Points[point]["line2"]["boundA"][1], intersection3Points[point]["line2"]["boundB"][1]], color=(random.random(), random.random(), random.random()))
		plt.plot([intersection3Points[point]["line3"]["boundA"][0], intersection3Points[point]["line3"]["boundB"][0]], [intersection3Points[point]["line3"]["boundA"][1], intersection3Points[point]["line3"]["boundB"][1]], color=(random.random(), random.random(), random.random()))

	for site in edges:
		for edgeN in edges[site]["edges"]:
			print(site, edgeN)
			plt.plot([edgeN["boundA"][0], edgeN["boundB"][0]], [edgeN["boundA"][1], edgeN["boundB"][1]], "-bo")
			

# 	for boundEdgeMid in possibleEdges:
# 		plt.plot([possibleEdges[boundEdgeMid]["line"]["boundA"][0], possibleEdges[boundEdgeMid]["line"]["boundB"][0]], [possibleEdges[boundEdgeMid]["line"]["boundA"][1], possibleEdges[boundEdgeMid]["line"]["boundB"][1]], "-go")

#	def showAnnotation(sel):
		#sel.annotation.set_text(f"")
#		print(sel.index)
		

#	cursor1 = mplcursors.cursor(hover=True)
#	cursor1.connect('add', showAnnotation)

	plt.show()




plt.figure(figsize=(7, 7))
for i in range(0, 20):
	
	plt.ylim(defaultBounds[1][1], defaultBounds[1][0])
	plt.xlim(defaultBounds[0][0], defaultBounds[0][1])
	main(plt)
	#sleep(1)
	plt.clf()

