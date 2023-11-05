
from email.policy import default
import random
import matplotlib.pyplot as plt

defaultBounds = [[0, 200], [200, 0]]
def main(plt):
	nPoints = 4#random.randint(3, 5)
	points = []
	#corners = [ [defaultBounds[0][0], defaultBounds[1][1]], [defaultBounds[0][0], defaultBounds[0][1]], [defaultBounds[1][0], defaultBounds[1][1]], [defaultBounds[0][1], defaultBounds[1][0]] ]
	cell = {}
	intersection3Points = {}
	edges = {}
	possibleEdges = {}

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


	def equationToPoint(equation, x):
		return equation["slope"] * (x - equation["midpoint"][0]) + equation["midpoint"][1]
	
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

# 	def getSlope(a, b, c, d):
# 		m = 0
# 		if (a - c) == 0 and (b - d) < 0:
# 			m = -1000
# 		elif (a - c) == 0 and (b - d) > 0:
# 			m = 1000
# 		else:
# 			m = (b - d) / (a - c)
# 		return m

	for i in range(0, nPoints):
		n1 = int(random.random() * 200)
		n2 = int(random.random() * 200)
		points.append([n1, n2])
	#points = [(100, 10), (156, 109), (118, 144), (197, 160)]
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
						testY = equationToPoint(line3, intX)
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
								intersection3Points.update({f"[{intX}_{intY}]" : {"intPoint":[intX, intY], "points":[currentPoint, line1["point"], line2["point"]], "line1":line1, "line2":line2, "line3":line3}})

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
				site1 = intersection3Points[inter]["points"][0]
				site2 = intersection3Points[inter]["points"][1]
				site3 = intersection3Points[inter]["points"][2]
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
		minDist = distance(intPoint[0], intPoint[1], intersection3Points[inter]["points"][0][0], intersection3Points[inter]["points"][0][1]) - 0.1
		for site in points:
			dist = distance(intPoint[0], intPoint[1], site[0], site[1])
			if dist < minDist:
				del intersection3Points[inter]
				break

	for inter in intersection3Points:
		intPt = intersection3Points[inter]["intPoint"]
		line1 = intersection3Points[inter]["line1"]
		line2 = intersection3Points[inter]["line2"]
		line3 = intersection3Points[inter]["line3"]

		dist1 = distance(intPt[0], intPt[1], line1["midpoint"][0], line1["midpoint"][1])
		dist2 = distance(intPt[0], intPt[1], line2["midpoint"][0], line2["midpoint"][1])
		dist3 = distance(intPt[0], intPt[1], line3["midpoint"][0], line3["midpoint"][1])

# 		if dist1 < dist2 and dist1 < dist3:
# 			if line1[0] < intPt[0]:
# 				line1["boundB"] = intPt
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

		

# 		if dist1 < dist2 and dist1 < dist3:
# 			if line1["midpoint"][0] < intPt[0]:
# 				line1["boundB"] = intPt
# 				#cell[arrayPoint]["otherPoint"][key1]["boundA"] = [intX, intY]
# 				#cell[key1]["otherPoint"][arrayPoint]["boundA"] = [intX, intY]
# 			else:
# 				line1["boundA"] = intPt
# 				#cell[arrayPoint]["otherPoint"][key1]["boundB"] = [intX, intY]
# 				#cell[key1]["otherPoint"][arrayPoint]["boundB"] = [intX, intY]
# 		else:
# 			if line1["midpoint"][0] < intPt[0]:
# 				line1["boundB"] = intPt
# 				#cell[arrayPoint]["otherPoint"][key1]["boundB"] = [intX, intY]
# 				#cell[key1]["otherPoint"][arrayPoint]["boundB"] = [intX, intY]
# 			else:
# 				line1["boundA"] = intPt
# 				#cell[arrayPoint]["otherPoint"][key1]["boundA"] = [intX, intY]
# 				#cell[key1]["otherPoint"][arrayPoint]["boundA"] = [intX, intY]
# 
# 		if dist2 < dist1 and dist2 < dist3:
# 			if intPt[0] > line2["midpoint"][0]:
# 				line2["boundA"] = intPt
# 				#cell[arrayPoint]["otherPoint"][key2]["boundA"] = [intX, intY]
# 				#cell[key2]["otherPoint"][arrayPoint]["boundA"] = [intX, intY]
# 			else:
# 				line2["boundB"] = intPt
# 				#cell[arrayPoint]["otherPoint"][key2]["boundB"] = [intX, intY]
# 				#cell[key2]["otherPoint"][arrayPoint]["boundB"] = [intX, intY]
# 		else:
# 			if intPt[0] > line2["midpoint"][0]:
# 				line2["boundB"] = intPt
# 				#cell[arrayPoint]["otherPoint"][key2]["boundB"] = [intX, intY]
# 				#cell[key2]["otherPoint"][arrayPoint]["boundB"] = [intX, intY]
# 			else:
# 				line2["boundA"] = intPt
# 				#cell[arrayPoint]["otherPoint"][key2]["boundA"] = [intX, intY]
# 				#cell[key2]["otherPoint"][arrayPoint]["boundA"] = [intX, intY]
# 
# 		if dist3 < dist1 and dist3 < dist2:
# 			if intPt[0] > line3["midpoint"][0]:
# 				line3["boundA"] = intPt
# 				#cell[key1]["otherPoint"][key2]["boundA"] = [intX, intY]
# 				#cell[key2]["otherPoint"][key1]["boundA"] = [intX, intY]
# 			else:
# 				line3["boundB"] = intPt
# 				#cell[key1]["otherPoint"][key2]["boundB"] = [intX, intY]
# 				#cell[key2]["otherPoint"][key1]["boundB"] = [intX, intY]
# 		else:
# 			if intPt[0] > line3["midpoint"][0]:
# 				line3["boundB"] = intPt
# 				#cell[key1]["otherPoint"][key2]["boundB"] = [intX, intY]
# 				#cell[key2]["otherPoint"][key1]["boundB"] = [intX, intY]
# 			else:
# 				line3["boundA"] = intPt
# 				#cell[key1]["otherPoint"][key2]["boundA"] = [intX, intY]
# 				#cell[key2]["otherPoint"][key1]["boundA"] = [intX, intY]
				

	def updateEdges(array, int1, int2, line, edges):
		site1 = array[int1][line]["point"]
		site2 = array[int2][line]["point"]

		#intPt1 = array[key1]["intPoint"]
		#intPt2 = array[key2]["intPoint"]

		edgeBoundA = array[int1]["intPoint"]
		edgeBoundB = array[int2]["intPoint"]

		if edgeBoundA[0] > edgeBoundB[0]:
			edgeBoundA, edgeBoundB = edgeBoundB, edgeBoundA
		

		if not int1 in edges:
			edges.update({int1 : {"point":site1, "edge": [{"boundA":edgeBoundA, "boundB":edgeBoundB}] }})
		else:
			edges[int1]["edge"].append({"boundA":edgeBoundA, "boundB":edgeBoundB})

		if not int2 in edges:
			edges.update({int2 : {"point":site2, "edge": [{"boundA":edgeBoundA, "boundB":edgeBoundB}] }})
		else:
			edges[int2]["edge"].append({"boundA":edgeBoundA, "boundB":edgeBoundB})
	
		print(site1, site2)

		print(array[int1][line])
		print(array[int2][line])
		
		possibleEdges1 = array[int1].copy()
		del possibleEdges1[line]
		del possibleEdges1["points"][possibleEdges1["points"].index(site1)]
		del possibleEdges1["intPoint"]
		print(possibleEdges1)
		
		possibleKeys1 = list(possibleEdges1.keys())

		for key in possibleKeys1:
			if key != 'points':
				if (possibleEdges1[key]["boundA"][0] == defaultBounds[0][0] or possibleEdges1[key]["boundA"][1] == defaultBounds[0][1] or possibleEdges1[key]["boundA"][1] == defaultBounds[1][1]) or (possibleEdges1[key]["boundB"][0] == defaultBounds[1][0] or possibleEdges1[key]["boundB"][1] == defaultBounds[0][1] or possibleEdges1[key]["boundB"][1] == defaultBounds[1][1]):
					edges[int1]["edge"].append([{"boundA":possibleEdges1[key]["boundA"], "boundB":possibleEdges1[key]["boundB"]}])

# 		possEdgesKeys = list(possibleEdges.keys())
# 		L1Midpoint = str(array[int1][line]["midpoint"]).replace(", ", "_")
# 
# 		temp =  array[int1].copy()
# 		del temp[line]
# 		del temp["intPoint"]
# 		del temp["points"][temp["points"].index(site1)]
# 		print(temp)
# 
# 		if possEdgesKeys.__len__() != 0:
# 			if L1Midpoint in possEdgesKeys:
# 				del possibleEdges[L1Midpoint]
# 			else:
# 				possibleEdges.update({L1Midpoint : {"sites":{[site1, site2]}, "line":line} })
# 		else:
# 			possibleEdges.update({L1Midpoint : {"sites":[site1, site2], "line":line} })

		print()
		# print(array[key1][line]["boundA"], array[key1][line]["boundB"])
		#print(array[key2][line]["boundA"], array[key2][line]["boundB"])

		# array[key1][line]["boundA"] = edgeBoundA
		# array[key1][line]["boundB"] = edgeBoundB
		#array[key2][line]["boundA"] = edgeBoundA
		#array[key2][line]["boundB"] = edgeBoundB

		# print(array[key1][line]["boundA"], array[key1][line]["boundB"])
		#print(array[key2][line]["boundA"], array[key2][line]["boundB"])
		# print()

	print("making edges")
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

# 				if int1Line1 == int2Line1 or int1Line1 == int2Line2 or int1Line1 == int2Line3:
# 					updateEdges(intersection3Points, key1, key2, "line1", edges)
# 				elif int1Line2 == int2Line1 or int1Line2 == int2Line2 or int1Line2 == int2Line3:
# 					updateEdges(intersection3Points, key1, key2, "line2", edges)
# 				elif int1Line3 == int2Line1 or int1Line3 == int2Line2 or int1Line3 == int2Line3:
# 					updateEdges(intersection3Points, key1, key2, "line3", edges)

				if (int1Line1["slope"] == int2Line1["slope"] and int1Line1["midpoint"] == int2Line1["midpoint"]) or (int1Line1["slope"] == int2Line2["slope"] and int1Line1["midpoint"] == int2Line2["midpoint"]) or (int1Line1["slope"] == int2Line3["slope"] and int1Line1["midpoint"] == int2Line3["midpoint"]):
					updateEdges(intersection3Points, key1, key2, "line1", edges)
				elif (int1Line2["slope"] == int2Line1["slope"] and int1Line2["midpoint"] == int2Line1["midpoint"]) or (int1Line2["slope"] == int2Line2["slope"] and int1Line2["midpoint"] == int2Line2["midpoint"]) or (int1Line2["slope"] == int2Line3["slope"] and int1Line2["midpoint"] == int2Line3["midpoint"]):
					updateEdges(intersection3Points, key1, key2, "line2", edges)
				elif (int1Line3["slope"] == int2Line1["slope"] and int1Line3["midpoint"] == int2Line1["midpoint"]) or (int1Line3["slope"] == int2Line2["slope"] and int1Line3["midpoint"] == int2Line2["midpoint"]) or (int1Line3["slope"] == int2Line3["slope"] and int1Line3["midpoint"] == int2Line3["midpoint"]):
					updateEdges(intersection3Points, key1, key2, "line3", edges)


	plt.title("pixel_plot")

	for pt in points:
		plt.plot(pt[0], pt[1], "ro")

	for site in cell:
		plt.plot(cell[site]["point"][0], cell[site]["point"][1], "ro")
		for line in cell[site]["otherPoint"]:
			plt.plot(cell[site]["otherPoint"][line]["midpoint"][0], cell[site]["otherPoint"][line]["midpoint"][1], "yo")

			#plt.plot([cell[site]["otherPoint"][line]["boundA"][0], cell[site]["otherPoint"][line]["boundB"][0]], [cell[site]["otherPoint"][line]["boundA"][1], cell[site]["otherPoint"][line]["boundB"][1]], color=(random.random(), random.random(), random.random()))

	for point in intersection3Points:
		plt.plot(intersection3Points[point]["intPoint"][0], intersection3Points[point]["intPoint"][1], "go")
		plt.plot([intersection3Points[point]["line1"]["boundA"][0], intersection3Points[point]["line1"]["boundB"][0]], [intersection3Points[point]["line1"]["boundA"][1], intersection3Points[point]["line1"]["boundB"][1]], color=(random.random(), random.random(), random.random()))
		plt.plot([intersection3Points[point]["line2"]["boundA"][0], intersection3Points[point]["line2"]["boundB"][0]], [intersection3Points[point]["line2"]["boundA"][1], intersection3Points[point]["line2"]["boundB"][1]], color=(random.random(), random.random(), random.random()))
		plt.plot([intersection3Points[point]["line3"]["boundA"][0], intersection3Points[point]["line3"]["boundB"][0]], [intersection3Points[point]["line3"]["boundA"][1], intersection3Points[point]["line3"]["boundB"][1]], color=(random.random(), random.random(), random.random()))

	for site in edges:
		for edgeN in edges[site]["edge"]:
			plt.plot([edgeN["boundA"][0], edgeN["boundB"][0]], [edgeN["boundA"][1], edgeN["boundB"][1]], "-bo")

	for boundEdgeMid in possibleEdges:
		plt.plot([possibleEdges[boundEdgeMid]["line"]["boundA"][0], possibleEdges[boundEdgeMid]["line"]["boundB"][0]], [possibleEdges[boundEdgeMid]["line"]["boundA"][1], possibleEdges[boundEdgeMid]["line"]["boundB"][1]], "-go")

	plt.show()




plt.figure(figsize=(7, 7))
for i in range(0, 20):
	
	plt.ylim(defaultBounds[1][1], defaultBounds[1][0])
	plt.xlim(defaultBounds[0][0], defaultBounds[0][1])
	main(plt)
	#sleep(1)
	plt.clf()

