#https://stackoverflow.com/questions/28504737/how-to-plot-a-single-point-in-matplotlib
#https://www.geeksforgeeks.org/create-2d-pixel-plot-in-python/
#https://stackoverflow.com/questions/66238749/how-to-find-the-closest-coordinate-from-a-list-of-points
#https://www.geeksforgeeks.org/sorting-algorithms-in-python/

import numpy as np
import matplotlib.pyplot as plt
#import math

points = [(50, 50), (25, 25), (75, 75)]
data = []
#cell = []
cell = {}

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

		#x = ( (slope1 * midPt1[0]) - (slope2 * midPt2[0]) ) + ( midPt1[1] - midPt2[1] )
		x = (midPt1[0] * slope1) - (midPt2[0] * slope2) - midPt1[1] + midPt2[1]
		y = slope1 * (x - midPt1[0]) + midPt1[1]
	
		print(f"intersect of y = {slope1}(x - {midPt1[0]}) + {midPt1[1]} and y = {slope2}(x - {midPt2[0]}) + {midPt2[1]} is ({x}, {y})")
		
		if (x > line1["boundA"][0] and x < line1["boundB"][0] and y < line1["boundA"][1] and y > line1["boundB"][1]) and (x > line2["boundA"][0] and x < line2["boundB"][0] and y < line2["boundA"][1] and y > line2["boundB"][1]):
			return x, y
		else:
			print(f'intersection is out of bounds ({line1["boundA"][0]}, {line1["boundA"][1]}) ({line1["boundB"][0]}, {line1["boundB"][1]}) or ({line2["boundA"][0]}, {line2["boundA"][1]}) ({line2["boundB"][0]}, {line2["boundB"][1]})')
			return (None, None)
	else:
		print(f"there is no interesection of y = {slope1}(x - {midPt1[0]}) + {midPt1[1]} and y = {slope2}(x - {midPt2[0]}) + {midPt2[1]} or they are the same equation")
		return (None, None)


def equationToPoint(equation, x):
	return equation["slope"] * (x - equation["midpoint"][0]) + equation["midpoint"][1]


# Driver code
 
# Example to test the above code
#arr = [ 2, 1, 10, 23 ]
 
#bubbleSort(arr)
 
#print("Sorted array is:")
#for i in range(len(arr)):
#    print("%d" % arr[i])

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

#for i in range(n):
#	cell.append( { f"{str(points[i]).replace(', ', '_')}" : {"otherPoint":[], "slope":None, "midpoint":[None, None], "boundA":[0, 200], "boundB":[200, 0]} } )

for i in range(n):
	#cell.update({ f"{str(points[i]).replace(', ', '_')}" : {"otherPoint":[], "slope":None, "midpoint":[None, None], "boundA":[0, 200], "boundB":[200, 0]} })
	cell.update({ f"{str(points[i]).replace(', ', '_')}" : {"otherPoint":[{ "(None_None)" : {"slope":None, "midpoint":[None, None], "boundA":[0, 200], "boundB":[200, 0]} }] } })

print(cell)

# Go through the points and find all the edges with the nearest point (will need to change this later as most cells have edges with more than just their nearest neighbor)
for pt in points:

	points2 = points.copy()
	points2.remove(pt)

	#xy = np.array(points2).T

	#d = ( (xy[0] - pt[0]) ** 2 + (xy[1] - pt[1]) ** 2) ** 0.5

	#closest_idx = np.argmin(d)
	#closest = points2[closest_idx]

	#print(pt, closest)

	#a = pt[0]
	#b = pt[1]
	#c = closest[0]
	#d = closest[1]

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
		if c < a and d < b:
			#e = a
			#f = b

			#a = c
			#b = d

			#c = e
			#d = f

			(a, b), (c, d) = (c, d), (a, b)

		m = (b - d) / (a - c)
		#y = (-1 / m) * (x - a) + b

		mPtX = (a + c) / 2
		mPtY = (b + d) / 2

		#plt.plot(mPtX, mPtY, "yo")

		#y = (-1 / m) * (x - mPtX) + mPtY

		#try:
		#	data.index({"pointA":[a, b], "pointB":[c, d], "slope":-1/m, "midpoint":[mPtX, mPtY], "boundA":[0, (-1/m) * (-1 * mPtX) + mPtY], "boundB":[mPtX - (mPtY/ (-1/m)), 0]})
			
			#return None
		#except Exception:
		#	data.append({"pointA":[a, b], "pointB":[c, d], "slope":-1/m, "midpoint":[mPtX, mPtY], "boundA":[0, (-1/m) * (-1 * mPtX) + mPtY], "boundB":[mPtX - (mPtY/ (-1/m)), 0]})
		#	print(f"({mPtX - (mPtY/ (-1/m) )}, 0), ({mPtX}, {mPtY})")
		
			#print((a, b), (c, d), (x, y), (-1 / m), (mPtX, mPtY))
			#return y

		#return y
		#return ( -(d ** 2) - (c ** 2) + (2 * c * x) + (b ** 2) + (a ** 2) - (2 * a * x) ) / ( (-2 * d) + (2 * b) )

		#try:
			#loc = cell.index(f"({a}_{b})")
			#cell[loc]["otherPoint"].append([c, d])
			#cell[loc]["slope"] = -1/m
			#cell[loc]["midpoint"] = [mPtX, mPtY]
			#cell[loc]["boundA"] = [0, (-1/m) * (-1 * mPtX) + mPtY]
			#cell[loc]["boundB"] = [mPtX - (mPtY/ (-1/m)), 0]

		#except Exception as e:
			#cell.append({f"({a}_{b})":{"otherPoint":[[c, d]], "slope":None, "midpoint":[None, None], "boundA":[0, 200], "boundB":[200, 0]} })
			#print(e)
		#print("a")
		#print(cell[f"({a}_{b})"])
		#print(list(cell[f"({a}_{b})"]["otherPoint"][0].keys())[0])
		#if the entry already exists, don't change it (do nothing) (?)
		if "(None_None)" == list(cell[f"({a}_{b})"]["otherPoint"][0].keys())[0]:
			print("b")
			cell.update({ f"({a}_{b})" : {"otherPoint":[{ f"({c}_{d})" : {"slope":-1/m, "midpoint":[mPtX, mPtY], "boundA":[0, (-1/m) * (-1 * mPtX) + mPtY], "boundB":[mPtX - (mPtY/ (-1/m)), 0]} }] } })
			#del cell[f"({a}_{b})"]["otherPoint"][0]
		elif not f"({a}_{b})" in cell:
			#cell[f"({a}_{b})"] = {}
			print("c")
			cell.update({ f"({a}_{b})" : {"otherPoint":[{ f"({c}_{d})" : {"slope":-1/m, "midpoint":[mPtX, mPtY], "boundA":[0, (-1/m) * (-1 * mPtX) + mPtY], "boundB":[mPtX - (mPtY/ (-1/m)), 0]} }] } })
		elif f"({a}_{b})" in cell:
			print("d")
			try:
				cell[f"({a}_{b})"]["otherPoint"].index({ f"({c}_{d})" : {"slope":-1/m, "midpoint":[mPtX, mPtY], "boundA":[0, (-1/m) * (-1 * mPtX) + mPtY], "boundB":[mPtX - (mPtY/ (-1/m)), 0]} })
			except Exception:
				print("e")
				cell[f"({a}_{b})"]["otherPoint"].append({ f"({c}_{d})" : {"slope":-1/m, "midpoint":[mPtX, mPtY], "boundA":[0, (-1/m) * (-1 * mPtX) + mPtY], "boundB":[mPtX - (mPtY/ (-1/m)), 0]} } )
		
		#if f"({a}_{b})" in cell:
			#if the entry already already exists
			#cell[f"({a}_{b})"][f"({c}_{d})"]
		#elif "(None_None)" in cell[f"({a}_{b})"]:
			#if nothing has been entered into the location

		#else:
			#if the entry does not exist but stuff as already been entered


	#solver(a, b, c, d)

	for otherPoint in points2:
		solver(pt[0], pt[1], otherPoint[0], otherPoint[1])

	#solver(pt[0], pt[1], points2[0][0], points2[0][1])

#print(data.__len__())

print(cell)

# Go through the points and find the intersection points in order to form edges
for currentPoint in points:
	#points2 = points.copy()
	#data2 = data.copy()
	
	#distanceTargetSort(currentPoint, data2)

	#n = data2.__len__()
	#print(n)

#	for i in range(0, n - 1):
#		#print(i)
#		x, y = intersectSolver(data2[i], data2[i + 1])
#
#		if x != None:
#			if x > data2[i]["midpoint"][0] and x < data2[i + 1]["midpoint"][0]: # x is between the midpoints of the two points, mid1 < x < mid2, greater than the first and less than the second
#				data2[i]["boundB"][0] = x
#				data2[i]["boundB"][1] = y
#							
#				data2[i]["boundA"][0] = x
#				data2[i]["boundA"][1] = y
#			elif x < data2[i]["midpoint"][0] and x > data2[i + 1]["midpoint"][0]: # mid2 < x < mid1
#				data2[i]["boundA"][0] = x
#				data2[i]["boundA"][1] = y
#							
#				data2[i]["boundB"][0] = x
#				data2[i]["boundB"][1] = y
#			elif x < data2[i]["midpoint"][0] and x < data2[i + 1]["midpoint"][0]: # x < mid1 & mid2
#				data2[i]["boundA"][0] = x
#				data2[i]["boundA"][1] = y
#							
#				data2[i]["boundA"][0] = x
#				data2[i]["boundA"][1] = y
#			elif x > data2[i]["midpoint"][0] and x > data2[i + 1]["midpoint"][0]: # x > mid1 & mid2
#				data2[i]["boundB"][0] = x
#				data2[i]["boundB"][1] = y
#							
#				data2[i]["boundB"][0] = x
#				data2[i]["boundB"][1] = y

	cell2 = cell.copy()
	
	kys = cell2.keys()
	
	def sort(target, array):
		n = len(array)
	
		for i in range(n):
			for j in range(0, n - i - 1):
				point1 = array[j]["midpoint"]
				point2 = array[j + 1]["midpoint"]

				distance1 = distance(target[0], target[1], point1[0], point1[1])
				distance2 = distance(target[0], target[1], point2[0], point2[1])

				if distance1 > distance2:
					array[j], array[j + 1] = array[j + 1], array[j]

	for key in kys:
		#need to sort the set of otherPoints based on the distance to the point, but first need to decide if I want otherPoint to be a dictionary or a list because a list of dictionary items is kind of the worst of both worlds
		#update: a dictionary would probably be better since a dictionary can be iterated though as easily as a list using the .keys() and can check if an item exists without causing an error
		cell2[key]

# Plot the data
for info in data:
	#midPt = info["midpoint"]
	
	#y1 = equationToPoint(info, info["boundA"][0])
	#y2 = equationToPoint(info, info["boundB"][0])

	#plt.plot([info["boundA"][0], info["boundB"][0]], [y1, y2], "-go")
	#print(info["boundA"][0])
	#print(f'{info["boundA"][0], info["boundA"][1]} {info["boundB"][0], info["boundB"][1]}')
	plt.plot([info["boundA"][0], info["boundB"][0]], [info["boundA"][1], info["boundB"][1]], "-go")

	plt.plot(info["midpoint"][0], info["midpoint"][1], "yo")

for pt in points:
	plt.plot(pt[0], pt[1], "ro")

plt.show()




