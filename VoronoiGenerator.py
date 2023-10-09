#https://stackoverflow.com/questions/28504737/how-to-plot-a-single-point-in-matplotlib
#https://www.geeksforgeeks.org/create-2d-pixel-plot-in-python/
#https://stackoverflow.com/questions/66238749/how-to-find-the-closest-coordinate-from-a-list-of-points
#https://www.geeksforgeeks.org/sorting-algorithms-in-python/

import numpy as np
import matplotlib.pyplot as plt
import math

def distance(x1, y1, x2, y2):
	return (((x1 - x2) ** 2) + ((y1 - y2) ** 2)) ** 0.5

def bubbleSort(arr):
     
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

def customSort(target, array):
	n = len(array)
	
	for i in range(n):
		for j in range(0, n - i - 1):
			#pointA1 = array[j]["pointA"]
			#pointB1 = array[j]["pointB"]
			#pointA2 = array[j + 1]["pointA"]
			#pointB2 = array[j + 1]["pointB"]

			#distance1 = distance(target[0], target[1], pointB1[0], pointB1[1])
			#distance2 = distance(target[0], target[1], pointB2[0], pointB2[1])

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

	#x = ( (slope1 * midPt1[0]) - (slope2 * midPt2[0]) ) + ( midPt1[1] - midPt2[1] )
	x = (midPt1[0] * slope1) - (midPt2[0] * slope2) - midPt1[1] + midPt2[1]
	y = slope1 * (x - midPt1[0]) + midPt1[1]
	
	print(f"intersect of y = {slope1}(x - {midPt1[0]}) + {midPt1[1]} and y = {slope2}(x - {midPt2[0]}) + {midPt2[1]} is ({x}, {y})")
	return (x, y)
          
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

# 
plt.title("pixel_plot")

#points = [[50, 50], [25, 25], [75, 75]]
points = [(50, 50), (25, 25), (75, 75)]

for pt in points:
	plt.plot(pt[0], pt[1], "ro")

data = []

for pt in points:

	points2 = points.copy()
	points2.remove(pt)

	xy = np.array(points2).T

	d = ( (xy[0] - pt[0]) ** 2 + (xy[1] - pt[1]) ** 2) ** 0.5

	closest_idx = np.argmin(d)
	closest = points2[closest_idx]

	#print(pt, closest)

	a = pt[0]
	b = pt[1]
	c = closest[0]
	d = closest[1]

	def solver(a, b, c, d, x):
		if c < a and d < b:
			e = a
			f = b

			a = c
			b = d

			c = e
			d = f

		m = (b - d) / (a - c)
		#y = (-1 / m) * (x - a) + b

		mPtX = (a + c) / 2
		mPtY = (b + d) / 2

		plt.plot(mPtX, mPtY, "yo")

		y = (-1 / m) * (x - mPtX) + mPtY

		
		try:
			data.index({"pointA":[a, b], "pointB":[c, d], "slope":-1/m, "midpoint":[mPtX, mPtY]})
			#return None
		except Exception:
			data.append({"pointA":[a, b], "pointB":[c, d], "slope":-1/m, "midpoint":[mPtX, mPtY]})
			print((a, b), (c, d), (x, y), (-1 / m), (mPtX, mPtY))
			#return y

		return y
		#return ( -(d ** 2) - (c ** 2) + (2 * c * x) + (b ** 2) + (a ** 2) - (2 * a * x) ) / ( (-2 * d) + (2 * b) )

	x1 = a + 20
	x2 = a - 20

	y1 = solver(a, b, c, d, x1) #This set with y1 and y2 is only necesssary to graph the lines but is not the same as what is in data
	y2 = solver(a, b, c, d, x2)	#If the solver is set up to return None and y and depending on if the line already exists, it will always return 1 None and 1 y if it is run twice on the same line, so it will not give 2 points to graph

	if y1 != None and y2 != None:
		plt.plot([x1, x2], [y1, y2], "-go")

cell = []

for currentPoint in points:
	#points2 = points.copy()
	data2 = data.copy()
	
	customSort(currentPoint, data2)

	n = data2.__len__()

	for i in range(0, n - 1):

		(x, y) = intersectSolver(data2[i], data2[i + 1])

		

plt.show()
