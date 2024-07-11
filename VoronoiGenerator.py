import matplotlib.pyplot as plt
import random
import math
from math import *

#                 width     height
#defaultBounds = [[0, 200], [200, 0]]
defaultBounds = [[0, 100], [300, 0]]

#		bottomleft, topleft, bottomright, topright
#corners = [[0, 0], [0, 200], [200, 0], [200, 200]]
corners = [ [defaultBounds[0][0], defaultBounds[1][1]], [defaultBounds[0][0], defaultBounds[1][0]], [defaultBounds[0][1], defaultBounds[1][1]], [defaultBounds[0][1], defaultBounds[1][0]] ]


points = []
for i in range(1, 30):
	  points.append([random.randint(0, defaultBounds[0][1]), random.randint(0, defaultBounds[1][0])])  

#points = [[50, 50], [25, 25], [75, 75], [98, 70]]
#points = [[50, 50], [25, 20], [75, 75], [98, 70]]
#points = [[30, 40], [25, 60], [80, 97]]
#points = [[50, 50], [75, 75]]  
#points = [[50, 50]]

#points = [[30, 30], [40, 40], [10, 50]]
#points = [[90,81],[48,121],[163,120],[83,23]]

	  

#points = [[59, 55], [30, 88], [1, 93]] #[[186, 15], [162, 127], [25, 144]] this is pretty much just a bigger version of the first set
#points = [[186, 15], [162, 127], [25, 144]]
#points = [[19, 27], [131, 44], [38, 130]]
#points = [[57, 67], [21, 80], [79, 198]]
#points = [[17, 45], [62, 54], [152, 194]]

#points = [[71, 79], [167, 127], [178, 141]]#[[57, 67], [21, 80], [79, 198]]#[[17, 45], [62, 54], [152, 194]]#[[159, 66], [100, 166], [73, 197]]#[[71, 79], [167, 127], [178, 141]]
#points = [[159, 66], [100, 166], [73, 197]]

#points = [[106, 6], [88, 11], [9, 18], [2, 105], [20, 105], [115, 140], [52, 168]] #causes division by zero in getTimeAtX
#points = [[13, 23], [181, 40], [129, 55], [93, 100], [59, 127], [12, 160], [156, 163]] #---edge finding issue
#points = [[76, 30], [196, 40], [165, 47], [104, 66], [128, 120], [88, 159], [166, 180]] #easy to see graph. In a previous, more broken version of the program, another line and intersection point near the one on the far right existed, which is necessary to correctly complete the graph
# ^there is an issue with the plot for the line above

#points = [[194, 2], [94, 30], [11, 91], [88, 92], [57, 143], [43, 190], [6, 198]]
#points = [[12, 1], [97, 12], [168, 24], [98, 58], [182, 111], [102, 111], [72, 122]]

#points = [[159, 12], [197, 12], [123, 38], [145, 92], [56, 123], [85, 160], [44, 166]] #causes a division by zero in yAtX

#[[95, 52], [68, 62], [137, 79], [127, 132], [42, 155], [90, 182], [179, 183]] #might be messed up?

#points = [[25, 17], [109, 37], [68, 45], [35, 85], [2, 124], [138, 138], [190, 145]]
#[[159, 3], [193, 10], [140, 34], [151, 84], [93, 107], [64, 155], [57, 195]]
#points = [[147, 1], [35, 16], [52, 25], [79, 70], [152, 91], [151, 97], [60, 139]] # all vertices are connected to exactly 2 other vertices
#points = [[41, 27], [40, 27], [52, 44], [116, 60], [28, 67], [182, 118], [64, 129]] #breaks neighboring cells

#[[140, 7], [29, 12], [13, 12], [120, 24], [13, 32], [68, 62], [141, 86]] 
#points = [[165, 25], [18, 33], [176, 41], [85, 102], [113, 128], [72, 153], [49, 162]] #looks like something is broken since a vertice with a higher y value than its connections does not have the highest time out of the 3

#points = [[144, 2], [143, 11], [71, 34], [68, 133], [104, 139], [108, 182], [135, 187]] #breaks finding second line
#points = [[21, 25], [45, 31], [162, 44], [132, 75], [109, 97], [7, 157], [31, 185]]
#[[27, 59], [150, 90], [79, 90], [101, 124], [94, 136], [178, 186], [157, 200]]      

#points = [[175, 23], [78, 24], [160, 108], [161, 141], [157, 159], [59, 188], [66, 188]]
#points = [[63, 50], [35, 72], [31, 79], [107, 125], [22, 153], [187, 172], [5, 175]]

#points = [[153, 24], [74, 52], [197, 54], [169, 69], [88, 143], [57, 169], [18, 188]]

#points = [[5, 19], [5, 43], [140, 56], [93, 87], [37, 117], [117, 179], [188, 199]] # causes division by 0 in nearestBoundry

#[[90, 22], [164, 23], [9, 118], [91, 120], [200, 179], [29, 195], [138, 199]] # neat

#points = [[146, 15], [189, 55], [44, 75], [90, 95], [52, 138], [111, 157], [117, 181]]

#points = [[159, 14], [49, 18], [63, 32], [87, 48], [191, 60], [131, 99], [150, 183]] # breaks stuff, not sure what exactly
#points = [[59, 65], [194, 108], [134, 152], [147, 155], [75, 166], [64, 172], [180, 195]] # breaks stuff, not sure what exactly

#points = [[25, 25], [175, 175], [25, 175], [175, 25], [100, 100]]
#points = [[50, 50], [75, 75], [195, 195]]	  

#points = [[43, 20], [10, 32], [91, 55], [136, 72], [123, 79], [52, 99], [0, 174]]
#points = [[200, 41], [81, 57], [167, 95], [142, 136], [109, 163], [42, 174], [188, 191]]

#points = [[20, 25], [55, 100], [70, 160], [95, 190]]
#points = [[20, 25], [55, 100], [95, 190]]
#points = [[20, 25], [40, 100], [70, 160], [95, 190]]

#points = [[73, 8], [62, 92], [37, 95], [80, 139], [154, 147], [84, 177], [85, 177]] # broke finding boundry edges with outside angles

#points = [[75, 14], [85, 22], [86, 26], [94, 32], [92, 45], [32, 71], [0, 127], [50, 132], [10, 134], [28, 134], [21, 134], [95, 147], [38, 152], [63, 162], [70, 168], [7, 175], [4, 176], [65, 179], [12, 187], [87, 190], [23, 197], [7, 206], [91, 209], [100, 234], [73, 236], [33, 267], [10, 273], [20, 278], [96, 298]]
points = [[86, 16], [33, 30], [49, 32], [27, 36], [98, 40], [23, 47], [11, 49], [69, 59], [67, 66], [81, 75], [75, 78], [6, 81], [1, 108], [4, 133], [100, 151], [30, 165], [86, 189], [30, 226], [54, 244], [15, 253], [41, 255], [52, 267], [11, 269], [27, 271], [13, 272], [49, 293], [84, 294], [2, 298], [46, 300]]
# ^ I think caused by the fact that when the x-values are the same, it just picks a slope without much good reasoning behind it, here causing the slope to be on the wrong side of the intersection

#with box that is 100 wide and 300 tall
#points = [[45, 70], [61, 100], [13, 162], [84, 208], [99, 233], [73, 270], [6, 281]]
#points = [[15, 38], [22, 55], [25, 158], [75, 197], [0, 225], [68, 248], [83, 249]]

plt.figure(figsize=(7, 7))
plt.ylim(defaultBounds[1][1], defaultBounds[1][0])
plt.xlim(defaultBounds[0][0], defaultBounds[0][1])
plt.title("pixel_plot")



cell = {}
vertices = {}
removeVerts = []
finalCell = {}
boundryEdges = []

def distance(x1, y1, x2, y2):
	return (((x1 - x2) ** 2) + ((y1 - y2) ** 2)) ** 0.5

def distancePt(pt1, pt2):
	return (((pt1[0] - pt2[0]) ** 2) + ((pt1[1] - pt2[1]) ** 2)) ** 0.5   

def distanceTargetSort(target, array):
	n = len(array)
 
	for i in range(n):
		for j in range(0, n - i - 1):
			 
			# Range of the array is from 0 to n-i-1
			# Swap the elements if the element found 
			#is greater than the adjacent element
			dist1 = distance(target[0], target[1], array[j][0], array[j][1])
			dist2 = distance(target[0], target[1], array[j+1][0], array[j+1][1])
			
			if dist1 > dist2:
				array[j], array[j + 1] = array[j + 1], array[j]

def sortByY(array):
	n = len(array)
 
	for i in range(n):
		for j in range(0, n - i - 1):
			 
			# Range of the array is from 0 to n-i-1
			# Swap the elements if the element found 
			#is greater than the adjacent element
			
			if array[j][1] > array[j + 1][1]:
				array[j], array[j + 1] = array[j + 1], array[j]

def sortByX(array):
	n = len(array)
 
	for i in range(n):
		for j in range(0, n - i - 1):
			
			if array[j][0] > array[j + 1][0]:
				array[j], array[j + 1] = array[j + 1], array[j]

def find3IntersectX(pt1, pt2, pt3): # finds x-value of intersection of 3 parabolas	
	a, b, c, d, e, f = pt1[0], pt1[1], pt2[0], pt2[1], pt3[0], pt3[1]
	if (2 * ( ((a-e)*(b-d)) - ((a-c)*(b-f))) ) != 0:
		x = ( ( ((a**2) - (e**2))*(b-d) ) - ( ((a**2) - (c**2)) * (b-f) ) - ( (d-f)*(b-f)*(b-d) )) / (2 * ( ((a-e)*(b-d)) - ((a-c)*(b-f))) )
		return float("%.10f" % x)#x
	else: # I need to have it return the midpoint between the site and nearest site if there is division by zero, because that means that the two lines are parallel and the farther site will not be valid
		# Seems to not break anything despite the fact that the division by 0 is not handled properly
		# division by zero happens with the points: 
		# [50, 50] [25, 25] [75, 75]
		# [7, 34] [87, 254] [91, 265]

		#print(( ( ((a**2) - (e**2))*(b-d) ) - ( ((a**2) - (c**2)) * (b-f) ) - ( (d-f)*(b-f)*(b-d) )), (2 * ( ((a-e)*(b-d)) - ((a-c)*(b-f))) ))
		#print(f"({a}, {b}) ({c}, {d}) ({e}, {f})")
		#print(a-e, b-d, a-c, b-f)
		#print("b",(a - c)/2)                      
		#return (a - c)/2   #returning (a-c)/2 or 0 doesn't seem to make a difference
		#return 0
		print(f"zero division error in find3IntersectX with {pt1} {pt2} {pt3}")
		return defaultBounds[0][0] - 5
		#return midPoint(pt1, pt2)

def otherXOnBisectorAtT(pt1, pt2, pt3, t): # pt1 and pt2 form the bisector and pt3 makes the parabola that it intersects with
	try:
		a, b, c, d, e, f = pt1[0], pt1[1], pt2[0], pt2[1], pt3[0], pt3[1]
		
		m = d-b
		n = 2 * ( ( (a-c) * (t-f) ) + (e * (b-d)) )
		o = -1 * ( ( (b-d) * ( (e**2) + (f**2) - (t**2) ) ) - ( (t-f) * ( (d**2) - (b**2) - (a**2) + (c**2) ) ) )

		x = ( (-1 * n) - ( ( (n**2) - (4 * m * o) )**0.5 ) ) / (2 * m)#( (-1 * n) + ( ( (n**2) - (4 * m * o) )**0.5 ) ) / (2 * m) 
		return float("%.10f" % x)
	except ZeroDivisionError:
		print(f"zero division error in otherXOnBisectorAtT with {pt1} {pt2} {pt3} t={t}")        
		return defaultBounds[1][1] -5  

def getXAtTime(pt1, pt2, t): # finds x-value of intersection of two parabolas at given time, imaginary if it doesn't exist
	# The base equation is sensitive to order but this function should be resistant to order
	# pt1, pt2 using the x1 equation is the same as pt2, pt1 using the x2 equation
	try:
		a, b, c, d = pt1[0], pt1[1], pt2[0], pt2[1]

		# Math is the same as otherXOnBisectorAtT except e is replaced with a and f is replaced with b
		m = d-b
		n = 2 * ( ( (a-c) * (t-b) ) + (a * (b-d)) )        
		o = -1 * ( ( (b-d) * ( (a**2) + (b**2) - (t**2) ) ) - ( (t-b) * ( (d**2) - (b**2) - (a**2) + (c**2) ) ) )
		
		mid = midPoint(pt1, pt2)
		x1 = ( (-1 * n) + ( ( (n**2) - (4 * m * o) )**0.5 ) ) / (2 * m)
		x2 = ( (-1 * n) - ( ( (n**2) - (4 * m * o) )**0.5 ) ) / (2 * m)
		dist1 = abs(mid[0] - x1)
		dist2 = abs(mid[0] - x2)
		
		if x1.imag != 0.0 or x2.imag != 0.0:
			return None
		if dist1 < dist2:
			return float("%.10f" % x1)
		else:
			return float("%.10f" % x2)

	except ZeroDivisionError:
		print(f"zero division error in find2IntersectAtTime with {pt1} {pt2} {pt3} t={t}")
		return defaultBounds[1][1] -5

def getXAtTimeRef(pt1, pt2, t, refX):
	try:
		a, b, c, d = pt1[0], pt1[1], pt2[0], pt2[1]
		m = d-b
		n = 2 * ( ( (a-c) * (t-b) ) + (a * (b-d)) )
		o = -1 * ( ( (b-d) * ( (a**2) + (b**2) - (t**2) ) ) - ( (t-b) * ( (d**2) - (b**2) - (a**2) + (c**2) ) ) )
		
		x1 = ( (-1 * n) + ( ( (n**2) - (4 * m * o) )**0.5 ) ) / (2 * m)
		x2 = ( (-1 * n) - ( ( (n**2) - (4 * m * o) )**0.5 ) ) / (2 * m)

		if x1.imag != 0.0 or x2.imag != 0.0:
			return None

		dist1 = abs(refX - x1)
		dist2 = abs(refX - x2)
		
		if dist1 < dist2:
			return float("%.10f" % x1)
		else:
			return float("%.10f" % x2)

	except ZeroDivisionError:
		print(f"zero division error in find2IntersectAtTime with {pt1} {pt2} {pt3} t={t}")
		return defaultBounds[1][1] -5

def getTimeAtX(pt1, pt2, pt3, x): # finds time when parabola pt1 has given x value, (pt1, pt2, pt3) = (pt1, pt3, pt2)
	try:
		a, b, c, d, e, f = pt1[0], pt1[1], pt2[0], pt2[1], pt3[0], pt3[1]
		j = b-d
		k = -( (a**2) + (b**2) - (c**2) - (d**2) + (2 * x * (c-a)))#-1 * ( (a**2) + (-2 * x * a) + (b**2) - (d**2) + (b * d) - (c**2) + (2 * x * c) - (d * b) )#-( (a**2) + (b**2) ) + (c**2) + (d**2) + (2 * x * (a-c)) #this last one is incorrect
		L = f * ( (a**2) + (b**2) - (c**2) - (d**2) - (2 * x * (a - c) ) ) - ( ( (x**2) + (e**2) + (f**2) - (2 * x * e) ) * j )#f * ( (a**2) + (b**2) - (c**2) - (d**2) - (2 * x * (a - c) ) ) - ( ( (x**2) + (e**2) + (f**2) - (2 * x * e) ) * (b - d) ) #f*( (a**2) - (c**2) + (b**2) - (d**2) - (2 * x * (a-c)) ) - (( ((x-e)**2) + (f**2) )*(b-d))
		t = ((-1 * k) - ( (k**2) - (4 * j * L))**0.5) / (2 * j) # division by 0 if j = 0, j = 0 if b-d = 0, so if the first 2 points have the same y value
		return float("%.10f" % t)
	except ZeroDivisionError:
		print(f"zero division error in getTimeAtX with {pt1} {pt2} {pt3} x={x} j={j} k={k} L={L}")        
		return pt1[1]

def getYAtTimeAndX(pt1, t, x): # just the y-value of the parabola at the given t and x, which may different than yAtX since that is locked to the bisector
	try:
		a, b = pt1[0], pt1[1]
		y = (((x-a)**2) / (2 * (b-t))) + (0.5 * (b+t)) # divides by 0 if b+t = 0 and b-t = 0, which is not possible
		return float("%.10f" % y)
	except ZeroDivisionError:
		print(f"zero division error in getYAtTimeAndX with {pt1} t={t} x={x}")
		return defaultBounds[1][1] -5

def yAtX(pt1, pt2, x): # gives y value of bisector between two parabolas at given x value
	try:
		a, b, c, d = pt1[0], pt1[1], pt2[0], pt2[1]
		y = ((c-a) / (b-d)) * (x - ( (a+c)/2) ) + ((b+d)/2) # divides by 0 if b-d = 0 (points have same y value), so the valid y value would also be the same
		return float("%.10f" % y)
	except ZeroDivisionError:
		print(f"zero division error in yAtX with {pt1} {pt2} x={x}")
		return pt1[1]
	
def xAtY(pt1, pt2, y): # gives x value of bisector between two parabolas at given y value
	try:
		a, b, c, d = pt1[0], pt1[1], pt2[0], pt2[1]
		x = ( (2 * y * (d-b)) - ((d**2) - (b**2)) + ((a**2) - (c**2)) ) / (2 * (a-c)) # divides by 0 if a-c = 0 (points have the same x value), so the correct x value would be the same as well
		return float("%.10f" % x)
	except ZeroDivisionError:
		print(f"zero division error in xAtY with {pt1} {pt2} y={y}")
		return pt1[0]

def tAtXandY(pt1, x, y):
	a, b = pt1[0], pt1[1]
	#t = ((2 * y) + (( (4 * (y**2)) + 4*( ((x-a)**2) - (2 * y * b) + (b**2 ) ) ) ** 0.5)) / 2
	k = -2 * y
	l = -1 * ( ( (x-a) ** 2 ) - (2 * y * b) + (b ** 2) )
	t = ( (-1 * k) + ( ( (k ** 2) - (4 * l) ) ** 0.5 ) ) / 2

	return float("%.10f" % t)


def pointSlope(pt, slope, x):
	return float("%.10f" % ((slope * (x - pt[0])) + pt[1]) )

def pointSlopeX(pt, slope, y):
	return float("%.10f" % ( (y - pt[1] + (slope * pt[0])) / slope) )

def nearestBoundry(startPt, throughPt):
	m = slope(startPt, throughPt)

	topX = pointSlopeX(startPt, m, defaultBounds[1][0]) # The x-coordinate of the line when its y equals the top y
	bottomX = pointSlopeX(startPt, m, defaultBounds[1][1])
	leftY = pointSlope(startPt, m, defaultBounds[0][0]) # The y-coordinate of the line when its x equals the left x
	rightY = pointSlope(startPt, m, defaultBounds[0][1])
	choice = []

	if throughPt[1] > startPt[1] and throughPt[0] > startPt[0]: # Towards top right
		choice = [[topX, defaultBounds[1][0]], [defaultBounds[0][1], rightY]] #top and right

	elif throughPt[1] < startPt[1] and throughPt[0] > startPt[0]: # Towards bottom right
		choice = [[bottomX, defaultBounds[1][1]], [defaultBounds[0][1], rightY]] #bottom and right
		
	elif throughPt[1] > startPt[1] and throughPt[0] < startPt[0]: # Towards top left
		choice = [[topX, defaultBounds[1][0]], [defaultBounds[0][0], leftY]] #top and left

	elif throughPt[1] < startPt[1] and throughPt[0] < startPt[0]: # Towards bottom left
		choice = [[bottomX, defaultBounds[1][1]], [defaultBounds[0][0], leftY]] #bottom and left

	else: # throughPt and startPt have the same y
		choice = [[defaultBounds[0][0], throughPt[1]], [defaultBounds[0][1], throughPt[1]]]
	
	distanceTargetSort(startPt, choice)
	
	return choice[0]

def nearestOutsideBoundry(startPt, throughPt):
	m = slope(startPt, throughPt)
		
	topX = pointSlopeX(startPt, m, defaultBounds[1][0]) # The x-coordinate of the line when its y equals the top y
	bottomX = pointSlopeX(startPt, m, defaultBounds[1][1])
	leftY = pointSlope(startPt, m, defaultBounds[0][0]) # The y-coordinate of the line when its x equals the left x
	rightY = pointSlope(startPt, m, defaultBounds[0][1])
	#				top								bottom								left						right
	choice = [[topX, defaultBounds[1][0]], [bottomX, defaultBounds[1][1]], [defaultBounds[0][0], leftY], [defaultBounds[0][1], rightY]]

	distanceTargetSort(startPt, choice)

	if choice[0][1] >= defaultBounds[1][1] and choice[0][1] <= defaultBounds[1][0] and choice[0][0] >= defaultBounds[0][0] and choice[0][0] <= defaultBounds[0][1]:
		return choice[0]
	elif choice[1][1] >= defaultBounds[1][1] and choice[1][1] <= defaultBounds[1][0] and choice[1][0] >= defaultBounds[0][0] and choice[1][0] <= defaultBounds[0][1]:                 
		return choice[1]
	else:
		return None

# I think this is probably over-engineered
def slope(pt1, pt2):
	try:
		if (pt1[1] - pt2[1]) / (pt1[0] - pt2[0]) == 0: # Just having 'pt1[0] - pt2[0] == 0' doesn't work as it allows for a slope of 0
			if pt1[1] - pt2[1] < 0: # Parts of my code can not handle a slope of 0, so this is here to make it almost 0
				return -0.0000001 # This is kinda arbitrary
			else:
				return 0.0000001
		else:
			return (pt1[1] - pt2[1]) / (pt1[0] - pt2[0])
	except ZeroDivisionError: 
		print(f"zero division error in slope with {pt1} {pt2}")
		if pt1[1] - pt2[1] < 0: # This is diffrent from the above since here the two points have the same x-value, so one is right above the other and the slope needs to be extremely big
			return -100000
		else:
			return 100000

def midPoint(pt1, pt2):
	return [ (pt1[0] + pt2[0]) / 2,  (pt1[1] + pt2[1]) / 2]    

def withinBounds(vert, bounds):
	return vert[0] >= bounds[0][0] and vert[0] <= bounds[0][1] and vert[1] >= bounds[1][1] and vert[1] <= bounds[1][0]

def formatVertex(vertices):
	for i in range(0, vertices.__len__()):

		for j in range(0, vertices[i].__len__()):
			if type(vertices[i][j]) == list:
				vertices[i][j][0] = float("%.10f" % vertices[i][j][0])
				vertices[i][j][1] = float("%.10f" % vertices[i][j][1])
			else:
				vertices[i][j] = float("%.10f" % vertices[i][j])


sortByY(points)
print(points)

# These two loops try to ensure that there are no points with the same y-value,
# could probably just do the random.random() to avoid having two loops, if that was necessary
for i in range(0, points.__len__() -1):
	if points[i][1] == points[i + 1][1]:
		points[i + 1][1] += 1
sortByY(points)
for i in range(0, points.__len__() -1):
	if points[i][1] == points[i + 1][1]:
		points[i + 1][1] += random.random()


tmp = []
for point in points:   
	finalCell.update({f"{str(point).replace(', ', '_')}" : {"site":point, "vertices":[]}})
	tmp.extend(point)

print(tmp) # this tmp is never used after this, it just used to print the points in a different format here

# Finds intersection points of sites, including some that are invalid
for site1 in points:
	for site2 in points:
		if site1 != site2:
			for site3 in points:
				if site3 != site2 and site3 != site1:
					sites = [site1, site2, site3]
					sortByY(sites)

					x = find3IntersectX(sites[0], sites[1], sites[2])
					t = getTimeAtX(sites[0], sites[1], sites[2], x)
					y = getYAtTimeAndX(sites[0], t, x)
					
					# bufferBounds just increases the bounds of the selected area by a certain amount so that intersection points can happen within it and are not outright rejected
					#	but need to be accounted for seperately and fixed
					# The size of bufferWidth and bufferHeight are kind of arbitrary, I just went with 1/4 of the their respective dimension
					bufferWidth = (defaultBounds[0][0] + defaultBounds[0][1])/4 # the midpoint divided by 2
					bufferHeight = (defaultBounds[1][1] + defaultBounds[1][0])/4
					bufferBounds = [[defaultBounds[0][0] - bufferWidth, defaultBounds[0][1] + bufferHeight], [defaultBounds[1][0] + bufferHeight, defaultBounds[1][1] - bufferHeight]]
					
					if t > site1[1] and t > site2[1] and t > site3[1] and withinBounds([x, y], bufferBounds):
							
						if f"{str(site1).replace(', ', '_')}" in cell:
							cell[f"{str(site1).replace(', ', '_')}"].append({"point1":site1, "point2":site2, "point3":site3, "time":float("%.10f" % t), "at":[float("%.10f" % x), float("%.10f" % y)]})
						else:
							cell.update({f"{str(site1).replace(', ', '_')}" : [{"point1":site1, "point2":site2, "point3":site3, "time":float("%.10f" % t), "at":[float("%.10f" % x), float("%.10f" % y)]}]})
	
# Finds invalid intersects and marks them for removal
for site1 in cell: 
	for entry in cell[site1]:
		for others in points:
			if entry["point1"] != others and entry["point2"] != others and entry["point3"] != others and others[1] < entry["time"]:
												
				otherPointY = getYAtTimeAndX(others, entry["time"], entry["at"][0])

				if otherPointY > entry["at"][1]:
					removeVerts.append([site1, entry])

if removeVerts.__len__() > 0:
	for site, vert in removeVerts:       
		try:               
			del cell[site][cell[site].index(vert)]
		except Exception:
			pass

# There are 3 cases that have to be dealth with seperately: 1 site, 3 sites, and 2 or 3+ sites 
# (technically 2 sites have to be dealt with seperately but are the same as having a cell in a corner so can be dealt with later)
if points.__len__() == 3:
	kys = list(cell.keys())

	if kys.__len__() != 0:
		current = cell[kys[0]][0]
		vert = f"{str(current['at']).replace(', ', '_')}"
		bound = nearestBoundry(current["at"], midPoint(current["point1"], current["point2"]))
	
		vertices[vert] = {"sites":[current["point1"], current["point2"], current["point3"]], "with":[[current["point1"], current["point2"]]], "at":[bound]}
		finalCell[kys[0]]["vertices"].append([current["at"], bound])
		finalCell[kys[1]]["vertices"].append([current["at"], bound])

 # Trying to handle 1 site here will cause the boundry edge finding section to duplicate two sides, 
#	and not handling this here breaks nothing, so it is handled after everything else	
elif points.__len__() == 1:
	pass
else:    
	usedPoints = []
	for entry in cell: # entry is a site
		for vert in cell[entry]: # cell[entry] is a list of vertices (dictionaries) associated with the site
			if vert["point1"] not in usedPoints:
				usedPoints.append(vert["point1"])
			if vert["point2"] not in usedPoints:
				usedPoints.append(vert["point2"])
			if vert["point3"] not in usedPoints:
				usedPoints.append(vert["point3"])

	for i in range(points.__len__()):   
		point = points[i]    
		if point not in usedPoints:
			boundVerts = []
			relative = points.copy()
			distanceTargetSort(point, relative)
		
			site2 = relative[1] # relative[1] is the closest site to point (relative[0] is point since I didn't remove it from the list)
		
			boundLy = yAtX(point, site2, defaultBounds[0][0]) # The y-value of the bisector at the left boundry
			boundLt = tAtXandY(point,  defaultBounds[0][0], boundLy)
			boundRy = yAtX(point, site2, defaultBounds[0][1]) # The y-value of the bisector at the right boundry
			boundRt = tAtXandY(point,  defaultBounds[0][1], boundRy)

			boundTx = xAtY(point, site2, defaultBounds[1][0]) # The x-value of the bisector at the top boundry
			boundTt = tAtXandY(point,  boundTx, defaultBounds[1][0])
			boundBx = xAtY(point, site2, defaultBounds[1][1]) # The x-value of the bisector at the bottom boundry
			boundBt = tAtXandY(point,  boundBx, defaultBounds[1][1])

			# Pairing up each of the values found above with their respective boundry value to form points
			pts = [[defaultBounds[0][0], boundLy], [defaultBounds[0][1], boundRy], [boundTx, defaultBounds[1][0]], [boundBx, defaultBounds[1][1]]]                
			distanceTargetSort(point, pts)
			
			#I should add onto this list so that the list of verticies will also include the corner
			# I forgot about this section and it is no longer necessary to add the corners here, though it may save time or simplify later steps
			#	I am not going to try adding corners because I don't want to spend time doing that

			site1 = f"{str(point).replace(', ', '_')}"
			tempPair = [pts[0], pts[1]]
			sortByY(tempPair)

			if tempPair not in finalCell[site1]["vertices"]:
				finalCell[site1]["vertices"].append(tempPair)
			
			# The following two lines are exactly the same, just changed for slightly better clarity
			#finalCell[f"{str(relative[1]).replace(', ', '_')}"]["vertices"].append([pts[0], pts[1]])
			finalCell[f"{str(site2).replace(', ', '_')}"]["vertices"].append([pts[0], pts[1]])
			# I am not entirely sure why I do the above line, but stuff breaks if I remove it


# def rotate(pt, origin, amount):   
# 	x = ((pt[0] - origin[0]) * math.cos(amount)) - ((pt[1] - origin[1]) * math.sin(amount))
# 	y = ((pt[1] - origin[1]) * math.cos(amount)) + ((pt[0] - origin[0]) * math.sin(amount))
# 	x += origin[0]
# 	y += origin[1]        
# 	return [x, y]           

# def angle(pt1, pt2, origin): #gets the interior/smaller angle
# 	a, b, c, d, e, f = origin[0], origin[1], pt1[0], pt1[1], pt2[0], pt2[1]
# 	#theta = math.acos( ( ((e -a) * (c-a)) + ((f-b) * (d-b)) ) / ( ( ( ((e-a)**2) + ((f-b)**2) ) * ( ((c-a)**2) + ((b-d)**2) ) ) ** 0.5 ) )
# 	theta = math.acos( ( ((e -a) * (c-a)) + ((f-b) * (d-b)) ) / ( ( (( ((e-a)**2) + ((f-b)**2) ) ** 0.5) * (( ((c-a)**2) + ((b-d)**2) ) ** 0.5) ) ) )    
# 	return theta

#normalTheta + angle == 2pi most of the time
def normalTheta(pt, origin): #gets the exterior/larger angle (basically)
	a, b, c, d = pt[0], pt[1], origin[0], origin[1]
	x = a-c
	y = b-d
	
	theta = 0
	if x != 0:
		theta = math.atan(y/x)
	elif b > d:
		theta = math.pi / 2
	elif b < d:
		theta = (3 * math.pi)/2

	if y == 0 and x < 0:
		theta = math.pi

	if x < 0 and y < 0:
		theta += math.pi
	if x < 0 and y > 0:
		theta += math.pi
	if x > 0 and y < 0:
		theta += 2 * math.pi

	return theta


#since arctan is from -pi/2 to pi/2 and I want values in the range 0 to 2pi, I need to code for that seperately, which is what is in normalTheta
# def rectToPolar(pt, origin):
# 	a, b, c, d = pt[0], pt[1], origin[0], origin[1]
# 	#theta = math.atan(b/a)
# 	#r = ( (a**2) + (b**2) ) ** 0.5
# 	#theta = math.atan((b-d)/(a-c))
# 	theta = normalTheta(pt, origin)
# 	r = ( ((a-c)**2) + ((b-d)**2) ) ** 0.5
# 	#if (theta < 0):
# 	#    theta = (2 * math.pi) + theta
# 	return [r, theta]

# def polarToRect(pt, origin):
# 	#x = pt[0] * math.cos(pt[1])
# 	#y = pt[0] * math.sin(pt[1])
# 	x = (pt[0] * math.cos(pt[1])) + origin[0]
# 	y = (pt[0] * math.sin(pt[1])) + origin[1]
# 	return [x, y]

for site in cell: # Finds vertices
	for entry in cell[site]:
		pt1 = entry["point1"]
		pt2 = entry["point2"]
		pt3 = entry["point3"]

		try:
			site2 = cell[f"{str(pt2).replace(', ', '_')}"]
			for entry2 in site2:
				if entry2["point1"] == pt1 or entry2["point2"] == pt1 or entry2["point3"] == pt1:
					if entry2["at"] != entry["at"] and [entry["at"], entry2["at"]] not in finalCell[site]["vertices"]:

						finalCell[site]["vertices"].append([entry["at"], entry2["at"]]) # for some reason sorting it by y here messes something up

						atName = f"{str(entry['at']).replace(', ', '_')}"

						if atName not in vertices:
							tempSites = [pt1, pt2, pt3]
							sortByY(tempSites)
							vertices.update({atName : {"sites":tempSites, "with":[], "at":[]}})
						
						# These check if the respective site is shared by the first cell but has not already been used to create this vertex
						if entry2["point1"] in [pt2, pt3] and [pt1, entry2["point1"]] not in vertices[atName]["with"] and [entry2["point1"], pt1] not in vertices[atName]["with"]:
							vertices[atName]["with"].append([pt1, entry2["point1"]])
							vertices[atName]["at"].append(entry2["at"])
							
						elif entry2["point2"] in [pt2, pt3] and [pt1, entry2["point2"]] not in vertices[atName]["with"] and [entry2["point2"], pt1] not in vertices[atName]["with"]:
							vertices[atName]["with"].append([pt1, entry2["point2"]])
							vertices[atName]["at"].append(entry2["at"])
							
						elif entry2["point3"] in [pt2, pt3] and [pt1, entry2["point3"]] not in vertices[atName]["with"] and [entry2["point3"], pt1] not in vertices[atName]["with"]:
							vertices[atName]["with"].append([pt1, entry2["point3"]])
							vertices[atName]["at"].append(entry2["at"])
																	   
		except Exception as e:
			print(f"site2: {e} not in cell")


# Modifies convex hull so that it has edges extending to the boundries of the specified area
for vert in vertices: 
	
	tempVertPt = str(vert).removeprefix("[").removesuffix("]").split("_")
	vertPt = [float(tempVertPt[0]), float(tempVertPt[1])]

	if vertices[vert]["at"].__len__() == 1:
		site1 = vertices[vert]["sites"][0]
		site2 = vertices[vert]["sites"][1]
		site3 = vertices[vert]["sites"][2]

		pickedSites = [[site1, site2], [site1, site3], [site2, site3]]
		pickedSites.remove(vertices[vert]["with"][0])
		
		dist1 = distancePt(pickedSites[0][0], pickedSites[0][1])
		dist2 = distancePt(pickedSites[1][0], pickedSites[1][1])

		if dist1 < dist2:
			pickedSites = pickedSites[0]
		else:
			pickedSites = pickedSites[1]

		throughPt = midPoint(pickedSites[0], pickedSites[1])

		if throughPt != []:
			nearestBound = nearestBoundry(vertPt, throughPt)

			vertices[vert]["with"].append([pickedSites[0], pickedSites[1]])
			vertices[vert]["at"].append(nearestBound)
			finalCell[f"{str(pickedSites[0]).replace(', ', '_')}"]["vertices"].append([vertPt, nearestBound])
			finalCell[f"{str(pickedSites[1]).replace(', ', '_')}"]["vertices"].append([vertPt, nearestBound])

	if vertices[vert]["at"].__len__() == 2:
		site1 = vertices[vert]["sites"][0]
		site2 = vertices[vert]["sites"][1]
		site3 = vertices[vert]["sites"][2]

		vertPtT = tAtXandY(site1, vertPt[0], vertPt[1])

		pickedSites = [[site1, site2], [site1, site3], [site2, site3]]
		pickedSites.remove(vertices[vert]["with"][0])
		pickedSites.remove(vertices[vert]["with"][1])
		pickedSites = pickedSites[0]
		
		sortByY(pickedSites)
		notInPair = []

		if site1 != pickedSites[0] and site1 != pickedSites[1]:
			notInPair = site1
		elif site2 != pickedSites[0] and site2 != pickedSites[1]:
			notInPair = site2
		elif site3 != pickedSites[0] and site3 != pickedSites[1]:
			notInPair = site3

		dists = [vertPtT - pickedSites[0][1], vertPtT - pickedSites[1][1], vertPtT - notInPair[1]]
		dists.sort()
		
		deltaT = dists[0] / 2

		# for some reason when pickedSites = [[167, 95], [188, 191]], both beforeTx and afterTx are less than vertPt[0]
		#	This is because there are two locations where the two parabolas intersect, so there are 4 possible points.
		#	Using getXAtTimeRef instead of getXAtTime ensures that the x picked is the one closest to the target intersection point
		#	getXAtTime works in most cases because the second option for an intersection point is usaully really far away from the other one
		#		and the midpoint, but that is not the case for the above scenario
		beforeTx = getXAtTimeRef(pickedSites[0], pickedSites[1], vertPtT - deltaT, vertPt[0])
		afterTx = getXAtTimeRef(pickedSites[0], pickedSites[1], vertPtT + deltaT, vertPt[0])

		throughPt = []

		beforeTy1 = getYAtTimeAndX(pickedSites[0], vertPtT - deltaT, beforeTx)
		beforeTy2 = getYAtTimeAndX(notInPair, vertPtT - deltaT, beforeTx)
		afterTy1 = getYAtTimeAndX(pickedSites[0], vertPtT + deltaT, afterTx)
		afterTy2 = getYAtTimeAndX(notInPair, vertPtT + deltaT, afterTx)
		
		if beforeTy1 > beforeTy2:
			throughPt = [beforeTx, beforeTy1]
		elif afterTy1 > afterTy2:
			throughPt = [afterTx, afterTy1]

		if throughPt != []:

			if vertPt[0] < defaultBounds[0][0] or vertPt[0] > defaultBounds[0][1] or vertPt[1] < defaultBounds[1][1] or vertPt[1] > defaultBounds[1][0]:
				nearestBound = nearestBoundry(vertPt, throughPt)

				newBound1 = nearestOutsideBoundry(vertPt, throughPt)
				newBound2 = nearestOutsideBoundry(vertPt, vertices[vert]["at"][0])
				newBound3 = nearestOutsideBoundry(vertPt, vertices[vert]["at"][1])

				finalCell[f"{str(vertices[vert]['with'][0][0]).replace(', ', '_')}"]["vertices"].append([vertices[vert]["at"][0], newBound2])
				finalCell[f"{str(vertices[vert]['with'][0][1]).replace(', ', '_')}"]["vertices"].append([vertices[vert]["at"][0], newBound2])
				finalCell[f"{str(vertices[vert]['with'][1][0]).replace(', ', '_')}"]["vertices"].append([vertices[vert]["at"][1], newBound3])
				finalCell[f"{str(vertices[vert]['with'][1][1]).replace(', ', '_')}"]["vertices"].append([vertices[vert]["at"][1], newBound3])
				
				# I could put both of these statements into one, but they are so big that I split them into two for readability
				if (nearestBound[0] == defaultBounds[0][0] or nearestBound[0] == defaultBounds[0][1]) and (nearestBound[1] <= defaultBounds[1][0] and nearestBound[1] >= defaultBounds[1][1]):
					finalCell[f"{str(pickedSites[0]).replace(', ', '_')}"]["vertices"].append([newBound1, nearestBound])
					finalCell[f"{str(pickedSites[1]).replace(', ', '_')}"]["vertices"].append([newBound1, nearestBound])
				elif (nearestBound[1] == defaultBounds[1][0] or nearestBound[1] == defaultBounds[1][1]) and (nearestBound[0] >= defaultBounds[0][0] and nearestBound[0] <= defaultBounds[0][1]):
					finalCell[f"{str(pickedSites[0]).replace(', ', '_')}"]["vertices"].append([newBound1, nearestBound])
					finalCell[f"{str(pickedSites[1]).replace(', ', '_')}"]["vertices"].append([newBound1, nearestBound])
				  
			else:
				nearestBound = nearestBoundry(vertPt, throughPt)

				# Stuff should be fine when removing these two commented lines since the vertices dictionary is never used again after this, only finalCell
				#vertices[vert]["with"].append([pickedSites[0], pickedSites[1]])
				#vertices[vert]["at"].append(nearestBound)
				finalCell[f"{str(pickedSites[0]).replace(', ', '_')}"]["vertices"].append([vertPt, nearestBound])
				finalCell[f"{str(pickedSites[1]).replace(', ', '_')}"]["vertices"].append([vertPt, nearestBound])


# removes duplicate information
for cell3 in finalCell:
	
	tempVerts = finalCell[cell3]["vertices"].copy()
	sortByY(tempVerts)
	for vert in tempVerts:
		sortByY(vert)

	formatVertex(tempVerts)

	unique = []

	for vert in tempVerts:
		if vert not in unique and vert[0] != vert[1]:
			unique.append(vert)

	finalCell[cell3]["vertices"] = unique

for cell4 in finalCell:

	verts = finalCell[cell4]["vertices"].copy()
	for vert in verts:

		startPt = []
		throughPt = []
		validVert1 = withinBounds(vert[0], defaultBounds)
		validVert2 = withinBounds(vert[1], defaultBounds)

		if validVert1 and not validVert2:
			startPt = vert[0]
			throughPt = vert[1]
		elif not validVert1 and validVert2:
			startPt = vert[1]
			throughPt = vert[0]
		
		if startPt != []:
			boundry = nearestBoundry(startPt, throughPt)
				
			if boundry[0] == startPt[0] and boundry[1] == startPt[1]: # If it just turns int a single point, which is not valid
				finalCell[cell4]["vertices"].remove(vert)
			else: # If it is valid, replace pair that it was
				pair1 = [startPt, throughPt]
				sortByY(pair1)
				i = finalCell[cell4]["vertices"].index(pair1)

				pair2 = [startPt, boundry]
				sortByY(pair2)

				if pair2 not in finalCell[cell4]["vertices"]: # This is true most of the time, but sometimes there is a duplicate
					finalCell[cell4]["vertices"][i] = pair2
				else:
					finalCell[cell4]["vertices"].remove(pair1) # since the pair is not being replaced by a new valid one, it needs to be removed
		
		# If both points are outside of the selected area
		elif not validVert1 and not validVert2: # might be able to be an else:
			midPt = midPoint(vert[0], vert[1])
			boundry1 = nearestOutsideBoundry(midPt, vert[0])
			boundry2 = nearestOutsideBoundry(midPt, vert[1])
			
			# If they both turn into one point, it means that they are on the same side of the boundry and are therefore not useful
			# I think any points that are beyond different boundry edges (and would thus make a valid edge) should have been dealt with by now, not sure though
			if boundry1[0] == boundry2[0] and boundry1[1] == boundry2[1]: 
				finalCell[cell4]["vertices"].remove(vert)


# Finds edges is cases where there are no intersection points
for cell5 in finalCell:
	if finalCell[cell5]["vertices"].__len__() == 0 and points.__len__() > 1:
		otherPoints = points.copy()
		distanceTargetSort(finalCell[cell5]["site"], otherPoints)
		
		site1 = finalCell[cell5]["site"]
		site2 = otherPoints[1]

		midPt = midPoint(site1, site2)
		leftY = yAtX(site1, site2, midPt[0] - 0.5)
		rightY = yAtX(site1, site2, midPt[0] + 0.5)
		
		# Since there are no intersection points, can just find the boundry intersections in both directions
		bound1 = nearestBoundry(midPt, [midPt[0] - 0.5, leftY])
		bound2 = nearestBoundry(midPt, [midPt[0] + 0.5, rightY])

		boundPair = [bound1, bound2]
		sortByY(boundPair)

		finalCell[cell5]["vertices"].append(boundPair)
		
		dictSite2 = f"{str(site2).replace(', ', '_')}"
		if boundPair not in finalCell[dictSite2]["vertices"]:
			finalCell[dictSite2]["vertices"].append(boundPair)

		
		if points.index(site1) != points.__len__() - 1 and points.index(site1) != 0: # If it is not the highest point or the lowest
			site3 = otherPoints[2]
			
			midPt = midPoint(site1, site3)
			leftY = yAtX(site1, site3, midPt[0] - 0.5)
			rightY = yAtX(site1, site3, midPt[0] + 0.5)
		
			bound1 = nearestBoundry(midPt, [midPt[0] - 0.5, leftY])
			bound2 = nearestBoundry(midPt, [midPt[0] + 0.5, rightY])

			boundPair = [bound1, bound2]
			sortByY(boundPair)

			finalCell[cell5]["vertices"].append(boundPair)
		
			dictSite3 = f"{str(site3).replace(', ', '_')}"
			if boundPair not in finalCell[dictSite3]["vertices"]:
				finalCell[dictSite3]["vertices"].append(boundPair)
		

def makeEdges(onBoundry, curSite):
	siteInside = False
	vert1Theta = normalTheta(onBoundry[0], curSite)
	vert2Theta = normalTheta(onBoundry[1], curSite)

	minTheta = min(vert1Theta, vert2Theta)
	maxTheta = max(vert1Theta, vert2Theta)
				
	# Checks if there is a site within the sector formed by the two boundry vertices
	for pt in points:
		if pt != curSite:
			ptTheta = normalTheta(pt, curSite)
			if ptTheta > minTheta and ptTheta < maxTheta:
				siteInside = True
				break

	withCorners = [[onBoundry[0], vert1Theta], [onBoundry[1], vert2Theta]]

	if siteInside == False: # If there is not a site between the angles of the two boundry vertices

		for i in range(0, corners.__len__()): # Finds corners that are within the area
			cornerTheta = normalTheta(corners[i], curSite)

			if cornerTheta > minTheta and cornerTheta < maxTheta:
				withCorners.append([corners[i], cornerTheta])

		sortByY(withCorners)

	else:

		# If there is a site within the angle between the two boundry vertices, use the area between the upper angle and the lower angle (opposite of between lower angle and upper)
		for i in range(0, corners.__len__()):
			cornerTheta = normalTheta(corners[i], curSite)
			
			if cornerTheta < minTheta or cornerTheta > maxTheta:
				tempAngle = cornerTheta - vert1Theta # Rotates the corner angle so that the upper boundry angle becomes 0 degrees
				if tempAngle < 0:
					tempAngle += 2 * math.pi
							
				withCorners.append([corners[i], tempAngle])

		if vert1Theta == maxTheta:
			withCorners[0] = [onBoundry[0], 0] # Makes the upper boundry angle 0 degrees
			withCorners[1] = [onBoundry[1], ((2 * math.pi) - vert1Theta) + vert2Theta] # Changes the lower boundry angle to be the new upper bound
		else:
			withCorners[0] = [onBoundry[1], 0]
			withCorners[1] = [onBoundry[0], ((2 * math.pi) - vert1Theta) + vert2Theta]

		sortByY(withCorners)

	for i in range(0, withCorners.__len__()-1):
		finalCell[cell2]["vertices"].append([withCorners[i][0], withCorners[i+1][0]])

# Finds edges that are on the boundry of the target area
for cell2 in finalCell:
	onBoundry = []
	for vert in finalCell[cell2]["vertices"]:
		boundSize = [defaultBounds[0][0], defaultBounds[0][1], defaultBounds[1][0], defaultBounds[1][1]] # Flattened version of defaultBounds array
		if (vert[0][0] in boundSize or vert[0][1] in boundSize) and vert[0] not in onBoundry:
			onBoundry.append(vert[0])
		if (vert[1][0] in boundSize or vert[1][1] in boundSize) and vert[1] not in onBoundry:
			onBoundry.append(vert[1])
				
	if onBoundry != []:
		curSite = finalCell[cell2]["site"]

		sortByY(onBoundry)
      
		if onBoundry.__len__() == 2:
			if onBoundry[0][0] == onBoundry[1][0] or onBoundry[0][1] == onBoundry[1][1]: # If the two vertices are on the same edge, they can just be added to finalCell without any extra work
				finalCell[cell2]["vertices"].append([onBoundry[0], onBoundry[1]])
			else: # if the two vertices are not on the same edge
				makeEdges(onBoundry, curSite)

		else: # if it greater than 2, it would ALMOST have to be a multiple of 2, with verts on different edges

			if onBoundry.__len__() % 2 == 0: # might be redundant, not sure if it is possible for a site to have more than 2 boundry edges
				#		left, right, top, bottom
				sides = [[], [], [], []]
				for point in onBoundry:
					if point[0] == defaultBounds[0][0]:
						sides[0].append(point)
					elif point[0] == defaultBounds[0][1]:
						sides[1].append(point)
					elif point[1] == defaultBounds[1][0]:
						sides[2].append(point)
					else:
						sides[3].append(point)

				single = []

				for edge in sides:
					if edge.__len__() == 2:
						finalCell[cell2]["vertices"].append([edge[0], edge[1]])

					elif edge.__len__() == 1:
						single.append(edge[0])
			
				if single.__len__() > 0:
					makeEdges(single, curSite)

if points.__len__() == 1:
	
	A = [corners[0], corners[2]]
	B = [corners[2], corners[3]]
	C = [corners[3], corners[1]]
	D = [corners[0], corners[1]]
	
	finalCell[f"{str(points[0]).replace(', ', '_')}"]["vertices"].extend([A, B, C, D])

# ---------------- End of voronoi calculations ----------------

for pt in points:
	plt.plot(pt[0], pt[1], "ro")
	#plt.plot(pt[0], pt[1], color=(1,0,0), marker="o") # works	

# for site in cell:  
# 	for entry in cell[site]:
        
# 		plt.plot(entry["at"][0], entry["at"][1], "go")

# 		plt.plot([entry["point2"][0], entry["at"][0], entry["point3"][0], entry["at"][0], entry["point1"][0]], [entry["point2"][1], entry["at"][1], entry["point3"][1], entry["at"][1], entry["point1"][1]], "g") 

	
for cell in finalCell:

	used = []

	for pairs in finalCell[cell]["vertices"]:    

		plt.plot([pairs[0][0], pairs[1][0]], [pairs[0][1], pairs[1][1]], "b")
		#plt.plot([pairs[0][0], pairs[1][0]], [pairs[0][1], pairs[1][1]], "bo")
		
		if pairs[0] not in used:
			used.append(pairs[0])
		if pairs[1] not in used:
			used.append(pairs[1])									

	temp = used.copy()
	temp2 = []
	curSite = finalCell[cell]["site"]
	for i in range(0, temp.__len__()):
		temp2.append([temp[i], normalTheta(temp[i],curSite)])
		
	sortByY(temp2)

	vertsX = []
	vertsY = []	

	for point in temp2:
		vertsX.append(point[0][0])
		vertsY.append(point[0][1])		
	
	plt.fill(vertsX, vertsY, color=(random.random(), random.random(), random.random(), 0.5))																								                        
		
plt.show()

