from ast import NotIn
from decimal import DivisionByZero
#from re import S
import matplotlib.pyplot as plt
import random
import math
from math import *
#from sklearn.neighbors import NearestNeighbors
#                 width     height
defaultBounds = [[0, 200], [200, 0]]


points = []
for i in range(1, 8):
	  points.append([random.randint(0, 200), random.randint(0, 200)])  

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

points = [[159, 14], [49, 18], [63, 32], [87, 48], [191, 60], [131, 99], [150, 183]] # breaks stuff, not sure what exactly
#points = [[59, 65], [194, 108], [134, 152], [147, 155], [75, 166], [64, 172], [180, 195]] # breaks stuff, not sure what exactly

#points = [[25, 25], [175, 175], [25, 175], [175, 25], [100, 100]]
#points = [[50, 50], [75, 75], [195, 195]]	  

#points = [[43, 20], [10, 32], [91, 55], [136, 72], [123, 79], [52, 99], [0, 174]]

#		bottomleft, topleft, bottomright, topright
corners = [[0, 0], [0, 200], [200, 0], [200, 200]] #[ [defaultBounds[0][0], defaultBounds[1][1]], [defaultBounds[0][0], defaultBounds[0][1]], [defaultBounds[1][0], defaultBounds[1][1]], [defaultBounds[0][1], defaultBounds[1][0]] ]

cell = {}
#activeSites = []
vertices = {}
removeVerts = []
finalCell = {}

plt.figure(figsize=(7, 7))
plt.ylim(defaultBounds[1][1], defaultBounds[1][0])
plt.xlim(defaultBounds[0][0], defaultBounds[0][1])
plt.title("pixel_plot")

def distance(x1, y1, x2, y2):
	return (((x1 - x2) ** 2) + ((y1 - y2) ** 2)) ** 0.5

def distancePt(pt1, pt2):
	return (((pt1[0] - pt2[0]) ** 2) + ((pt1[1] - pt2[1]) ** 2)) ** 0.5   

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

#https://www.geeksforgeeks.org/python-program-for-insertion-sort/
def insertionSort(arr): #Not used but a good template
	n = len(arr)  # Get the length of the array
	  
	if n <= 1:
		return  # If the array has 0 or 1 element, it is already sorted, so return
 
	for i in range(1, n):  # Iterate over the array starting from the second element
		key = arr[i]  # Store the current element as the key to be inserted in the right position
		j = i-1
		while j >= 0 and key < arr[j]:  # Move elements greater than key one position ahead
			arr[j+1] = arr[j]  # Shift elements to the right
			j -= 1
		arr[j+1] = key  # Insert the key in the correct position

def distanceVertTargetSortShort(target, array): #good for small arrays #I don't know how to use this
	n = len(array)  # Get the length of the array
	  
	if n <= 1:
		return  # If the array has 0 or 1 element, it is already sorted, so return
 
	for i in range(1, n):  # Iterate over the array starting from the second element
		key = array[i]  # Store the current element as the key to be inserted in the right position
		j = i-1
		while j >= 0 and key < array[j]:  # Move elements greater than key one position ahead
			array[j+1] = array[j]  # Shift elements to the right
			j -= 1
		array[j+1] = key  # Insert the key in the correct position
		
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

def find3IntersectX(pt1, pt2, pt3): # division by zero happens with the points (50, 50) (25, 25) (75, 75) # finds x-value of intersection of 3 parabolas
	a, b, c, d, e, f = pt1[0], pt1[1], pt2[0], pt2[1], pt3[0], pt3[1]
	if (2 * ( ((a-e)*(b-d)) - ((a-c)*(b-f))) ) != 0:
		x = ( ( ((a**2) - (e**2))*(b-d) ) - ( ((a**2) - (c**2)) * (b-f) ) - ( (d-f)*(b-f)*(b-d) )) / (2 * ( ((a-e)*(b-d)) - ((a-c)*(b-f))) )
		return float("%.10f" % x)#x
	else: # i need to have it return the midpoint between the site and nearest site if there is division by zero, because that means that the two lines are parallel and the farther site will not be valid
		#print(( ( ((a**2) - (e**2))*(b-d) ) - ( ((a**2) - (c**2)) * (b-f) ) - ( (d-f)*(b-f)*(b-d) )), (2 * ( ((a-e)*(b-d)) - ((a-c)*(b-f))) ))
		#print(f"({a}, {b}) ({c}, {d}) ({e}, {f})")
		#print(a-e, b-d, a-c, b-f)
		#print("b",(a - c)/2)                      
		#return (a - c)/2   #returning (a-c)/2 or 0 doesn't seem to make a difference
		#return 0
		print(f"zero division error in find3IntersectX with {pt1} {pt2} {pt3}")
		return defaultBounds[0][0] - 5       
		#return midPoint(pt1, pt2)

#def find3IntersectY(pt1)

#def find3IntersectPt()

def otherXOnBisectorAtT(pt1, pt2, pt3, t): # pt1 and pt2 form the bisector and pt3 makes the parabola that it intersects with
	try:
		a, b, c, d, e, f = pt1[0], pt1[1], pt2[0], pt2[1], pt3[0], pt3[1]
		
		m = d-b
		n = 2 * ( ( (a-c) * (t-f) ) + (e * (b-d)) )        
		o = -1 * ( ( (b-d) * ( (e**2) + (f**2) - (t**2) ) ) - ( (t-f) * ( (d**2) - (b**2) - (a**2) + (c**2) ) ) )

#         x = 0
#         if pt1[0] < pt2[0]:
#             x = ( (-1 * n) - ( ( (n**2) - (4 * m * o) )**0.5 ) ) / (2 * m)
#         else:
#             x = ( (-1 * n) + ( ( (n**2) - (4 * m * o) )**0.5 ) ) / (2 * m)                        
		x = ( (-1 * n) - ( ( (n**2) - (4 * m * o) )**0.5 ) ) / (2 * m)#( (-1 * n) + ( ( (n**2) - (4 * m * o) )**0.5 ) ) / (2 * m) 
		return float("%.10f" % x)#x
	except ZeroDivisionError:
		print(f"zero division error in otherXOnBisectorAtT with {pt1} {pt2} {pt3} t={t}")        
		return defaultBounds[1][1] -5  

def getXAtTime(pt1, pt2, t): # finds x-value of intersection of two parabolas at given time, imaginary if it doesn't exist
	try:    
		a, b, c, d = pt1[0], pt1[1], pt2[0], pt2[1]
		# n = ( 2 * ( (c * (t-b)) + (a * (d-t)) ) ) / (b-d)#(2 * ((-1 * c * b) + (c * t) + (a * d) - (a * t))) / (b-d)
		# m = (-1 * (b-t) * (d-t) ) + ( (( (c**2) * (b-t) ) + ( (a**2) * (t-d) )) / (b-d) )#-1 * ( ( (b - t) * (d - t) ) - ( ( (c * c * b) - (c * c * t) - (a * a * d) + (a * a * t) ) / (b - d) ) ) #(-1 * (b-t) * (d-t)) + (( (c**2) * (b-t) ) + ( (a**2) * (d-t) )) / (b-d)
		# x = ((-1 * n) + ( (n**2) - (4 * m))**0.5) / 2#((-1 * n) - ( (n**2) - (4 * m))**0.5) / 2
		# Math is the same as otherXOnBisectorAtT except e is replaced with a and f is replaced with b        
		m = d-b
		n = 2 * ( ( (a-c) * (t-b) ) + (a * (b-d)) )        
		o = -1 * ( ( (b-d) * ( (a**2) + (b**2) - (t**2) ) ) - ( (t-b) * ( (d**2) - (b**2) - (a**2) + (c**2) ) ) )
		#x = ( (-1 * n) + ( ( (n**2) - (4 * m * o) )**0.5 ) ) / (2 * m)
#         x = 0
#         if pt1[0] < pt2[0]:
#             x = ( (-1 * n) - ( ( (n**2) - (4 * m * o) )**0.5 ) ) / (2 * m)
#         else:
#             x = ( (-1 * n) + ( ( (n**2) - (4 * m * o) )**0.5 ) ) / (2 * m)                                                            
		
		mid = midPoint(pt1, pt2)
		x1 = ( (-1 * n) + ( ( (n**2) - (4 * m * o) )**0.5 ) ) / (2 * m)
		x2 = ( (-1 * n) - ( ( (n**2) - (4 * m * o) )**0.5 ) ) / (2 * m)                
		dist1 = abs(mid[0] - x1)
		dist2 = abs(mid[0] - x2)
		if dist1 < dist2:
			return float("%.10f" % x1)#x1
		else:
			return float("%.10f" % x2)#x2

		#return x
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
		return float("%.10f" % t)#t
	except ZeroDivisionError:
		print(f"zero division error in getTimeAtX with {pt1} {pt2} {pt3} x={x} j={j} k={k} L={L}")        
		return pt1[1]#defaultBounds[1][1] -5            

def getYAtTimeAndX(pt1, t, x): # just the y-value of the parabola at the given t and x, which may different than yAtX since that is locked to the bisector
	try:    
		a, b = pt1[0], pt1[1]
		y = (((x-a)**2) / (2 * (b-t))) + (0.5 * (b+t)) # divides by 0 if b+t = 0 and b-t = 0, which is not possible
		return float("%.10f" % y)#y
	except ZeroDivisionError:
		print(f"zero division error in getYAtTimeAndX with {pt1} t={t} x={x}")
		return defaultBounds[1][1] -5                       

def yAtX(pt1, pt2, x): # gives y value of bisector between two parabolas at given x value
	try:    
		a, b, c, d = pt1[0], pt1[1], pt2[0], pt2[1]
		y = ((c-a) / (b-d)) * (x - ( (a+c)/2) ) + ((b+d)/2) # divides by 0 if b-d = 0 (points have same y value), so the valid y value would also be the same
		return float("%.10f" % y)#y
	except ZeroDivisionError:
		print(f"zero division error in yAtX with {pt1} {pt2} x={x}")
		return pt1[1]#defaultBounds[1][1] -5                    
	
def xAtY(pt1, pt2, y): # gives x value of bisector between two parabolas at given y value
	try:    
		a, b, c, d = pt1[0], pt1[1], pt2[0], pt2[1]
		x = ( (2 * y * (d-b)) - ((d**2) - (b**2)) + ((a**2) - (c**2)) ) / (2 * (a-c)) # divides by 0 uf a-c = 0 (points have the same x value), so the correct x value would be the same as well
		return float("%.10f" % x)#x
	except ZeroDivisionError:
		print(f"zero division error in xAtY with {pt1} {pt2} y={y}")
		return pt1[0]#defaultBounds[0][0] -5    

def tAtXandY(pt1, x, y):   
	a, b = pt1[0], pt1[1]
	t = ((2 * y) + (( (4 * (y**2)) + 4*( ((x-a)**2) - (2 * y * b) + (b**2 ) ) ) ** 0.5)) / 2
	return float("%.10f" % t)#t    


def pointSlope(pt, slope, x):
	return float("%.10f" % ((slope * (x - pt[0])) + pt[1]) )#(slope * (x - pt[0])) + pt[1]

def pointSlopeX(pt, slope, y):
	return float("%.10f" % ( (y - pt[1] + (slope * pt[0])) / slope) )#(y - pt[1] + (slope * pt[0])) / slope      

def nearestBoundry(startPt, throughPt):
	m = slope(startPt, throughPt)
		
	topX = pointSlopeX(startPt, m, defaultBounds[1][0])#(defaultBounds[1][0] - startPt[1] + (m * startPt[0])) / m # the x-coordinate of the line when its y equals the top y
	bottomX = pointSlopeX(startPt, m, defaultBounds[1][1])#(defaultBounds[1][1] - startPt[1] + (m * startPt[0])) / m
	leftY = pointSlope(startPt, m, defaultBounds[0][0])#m * (defaultBounds[0][0] - startPt[0]) + startPt[1] # the y-coordinate of the line when its x equals the left x
	rightY = pointSlope(startPt, m, defaultBounds[0][1])#m * (defaultBounds[0][1] - startPt[0]) + startPt[1]
	choice = []

	if throughPt[1] > startPt[1] and throughPt[0] > startPt[0]:
		#print('a')        
		choice = [[topX, defaultBounds[1][0]], [defaultBounds[0][1], rightY]] #top and right
		distanceTargetSort(startPt, choice)
		#return choice[0]
	elif throughPt[1] < startPt[1] and throughPt[0] > startPt[0]:
		#print('b')
		choice = [[bottomX, defaultBounds[1][1]], [defaultBounds[0][1], rightY]] #bottom and right
		distanceTargetSort(startPt, choice)
		#return choice[0]
	elif throughPt[1] > startPt[1] and throughPt[0] < startPt[0]:
		#print('c')        
		choice = [[topX, defaultBounds[1][0]], [defaultBounds[0][0], leftY]] #top and left
		distanceTargetSort(startPt, choice)
		#return choice[0]
	elif throughPt[1] < startPt[1] and throughPt[0] < startPt[0]:
		#print('d')
		choice = [[bottomX, defaultBounds[1][1]], [defaultBounds[0][0], leftY]] #bottom and left
		distanceTargetSort(startPt, choice)
		#return choice[0]
	else: # throughPt and startPt have the same y
		choice = [[defaultBounds[0][0], throughPt[1]], [defaultBounds[0][1], throughPt[1]]]
		distanceTargetSort(startPt, choice)        
	
	return choice[0]    

def nearestOutsideBoundry(startPt, throughPt):
	m = slope(startPt, throughPt)
		
	topX = pointSlopeX(startPt, m, defaultBounds[1][0])#(defaultBounds[1][0] - startPt[1] + (m * startPt[0])) / m # the x-coordinate of the line when its y equals the top y
	bottomX = pointSlopeX(startPt, m, defaultBounds[1][1])#(defaultBounds[1][1] - startPt[1] + (m * startPt[0])) / m
	leftY = pointSlope(startPt, m, defaultBounds[0][0])#m * (defaultBounds[0][0] - startPt[0]) + startPt[1] # the y-coordinate of the line when its x equals the left x
	rightY = pointSlope(startPt, m, defaultBounds[0][1])#m * (defaultBounds[0][1] - startPt[0]) + startPt[1]
	choice = [[topX, defaultBounds[1][0]], [bottomX, defaultBounds[1][1]], [defaultBounds[0][0], leftY], [defaultBounds[0][1], rightY]]
	#choice = []        

	distanceTargetSort(startPt, choice)    

	#print("line320",topX,bottomX,leftY,rightY)

	if choice[0][1] >= defaultBounds[1][1] and choice[0][1] <= defaultBounds[1][0] and choice[0][0] >= defaultBounds[0][0] and choice[0][0] <= defaultBounds[0][1]:
		return choice[0]
	elif choice[1][1] >= defaultBounds[1][1] and choice[1][1] <= defaultBounds[1][0] and choice[1][0] >= defaultBounds[0][0] and choice[1][0] <= defaultBounds[0][1]:                 
		return choice[1]
	else:
		return None
				
def slope(pt1, pt2):
	try:
		if (pt1[1] - pt2[1]) / (pt1[0] - pt2[0]) == 0:
			if pt1[1] - pt2[1] < 0:
				return -0.0000001
			else:
				return 0.0000001
		else:
			return (pt1[1] - pt2[1]) / (pt1[0] - pt2[0])
	except ZeroDivisionError:
		print(f"zero division error in slope with {pt1} {pt2}")
		if pt1[1] - pt2[1] < 0:
			return -100000#-0.00000000001
		else:
			return 100000#0.00000000001

def midPoint(pt1, pt2):
	return [ (pt1[0] + pt2[0]) / 2,  (pt1[1] + pt2[1]) / 2]    

def withinBounds(vert, bounds):
	return vert[0] >= bounds[0][0] and vert[0] <= bounds[0][1] and vert[1] >= bounds[1][1] and vert[1] <= bounds[1][0]

def formatVertex(vertices):
	for i in range(0, vertices.__len__()):
		print("line383",vertices)
		
		for j in range(0, vertices[i].__len__()):
			if type(vertices[i][j]) == list:
				vertices[i][j][0] = float("%.10f" % vertices[i][j][0])
				vertices[i][j][1] = float("%.10f" % vertices[i][j][1])
			else:
				vertices[i][j] = float("%.10f" % vertices[i][j])


sortByY(points)
print(points)

tmp = []
for i in range(0, points.__len__() -1):
	if points[i][1] == points[i + 1][1]:
		points[i + 1][1] += 1            

outsideBoundry = {}

for point in points:   
	finalCell.update({f"{str(point).replace(', ', '_')}" : {"site":point, "vertices":[]}})
	tmp.extend(point)
	outsideBoundry.update({f"{str(point).replace(', ', '_')}" : {"site":point, "vertices":[]}})    

print(tmp)            

for site1 in points: # Sets sites of cells
	for site2 in points:
		if site1 != site2:                       
			for site3 in points:
				if site3 != site2 and site3 != site1:
					sites = [site1, site2, site3]
					sortByY(sites)                    

					x = find3IntersectX(sites[0], sites[1], sites[2])
					t = getTimeAtX(sites[0], sites[1], sites[2], x)
					y = getYAtTimeAndX(sites[0], t, x)
					
					halfWidth = (defaultBounds[0][0] + defaultBounds[0][1])/2
					halfHeight = (defaultBounds[1][1] + defaultBounds[1][0])/2
					if t > site1[1] and t > site2[1] and t > site3[1] and x >= defaultBounds[0][0] - (halfWidth/2) and x <= defaultBounds[0][1] + (halfWidth/2) and y >= defaultBounds[1][1] - (halfHeight/2) and y <= defaultBounds[1][0] + (halfHeight/2):                     

						#if x < defaultBounds[0][0] or x > defaultBounds[0][1] or y < defaultBounds[1][1] or y > defaultBounds[1][0]:
							

						if f"{str(site1).replace(', ', '_')}" in cell:
							cell[f"{str(site1).replace(', ', '_')}"].append({"point1":site1, "point2":site2, "point3":site3, "time":float("%.10f" % t), "at":[float("%.10f" % x), float("%.10f" % y)]})
						else:                            
							cell.update({f"{str(site1).replace(', ', '_')}" : [{"point1":site1, "point2":site2, "point3":site3, "time":float("%.10f" % t), "at":[float("%.10f" % x), float("%.10f" % y)]}]})
	

for site1 in cell: # Finds invalid intersects and marks them for removal
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

#print(cell)
if points.__len__() == 3:
	kys = list(cell.keys())

	current = cell[kys[0]][0]
	vert = f"{str(current['at']).replace(', ', '_')}"     
	bound = nearestBoundry(current["at"], midPoint(current["point1"], current["point2"]))
	
	vertices[vert] = {"sites":[current["point1"], current["point2"], current["point3"]], "with":[[current["point1"], current["point2"]]], "at":[bound]}
	finalCell[kys[0]]["vertices"].append([current["at"], bound])
	finalCell[kys[1]]["vertices"].append([current["at"], bound])
	
elif points.__len__() == 1:
	pass    
else:    
	usedPoints = []
	for entry in cell:
		for vert in cell[entry]:    
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
		
			site2 = relative[1]
		
			#print(point, site2)
			boundLy = yAtX(point, site2, defaultBounds[0][0])
			boundLt = tAtXandY(point,  defaultBounds[0][0], boundLy)
			boundRy = yAtX(point, site2, defaultBounds[0][1])
			boundRt = tAtXandY(point,  defaultBounds[0][1], boundRy)

			boundTx = xAtY(point, site2, defaultBounds[1][0])
			boundTt = tAtXandY(point,  boundTx, defaultBounds[1][0])
			boundBx = xAtY(point, site2, defaultBounds[1][1])
			boundBt = tAtXandY(point,  boundBx, defaultBounds[1][1])

			pts = [[defaultBounds[0][0], boundLy], [defaultBounds[0][1], boundRy], [boundTx, defaultBounds[1][0]], [boundBx, defaultBounds[1][1]]]                
			#print(pts)
			distanceTargetSort(point, pts)       
			#print(pts)
			#print(f"{str(point).replace(', ', '_')}")        
			#finalCell.update({f"{str(point).replace(', ', '_')}":{"site":point, "vertices":[ #I should add onto this list so that the list of verticies will also include the corner
			#    [pts[0], pts[1]]
			#    ]}})
			#finalCell[f"{str(point).replace(', ', '_')}"]["vertices"].append([pts[0], pts[1]])
			print("line508",pts[0], pts[1])
			if not f"{str(point).replace(', ', '_')}" in finalCell:        
				finalCell.update({f"{str(point).replace(', ', '_')}":{"site":point, "vertices":[ #I should add onto this list so that the list of verticies will also include the corner
				[pts[0], pts[1]]
				]}})

			finalCell[f"{str(relative[1]).replace(', ', '_')}"]["vertices"].append([pts[0], pts[1]])


# def rotate(pt, origin, amount):   
# 	x = ((pt[0] - origin[0]) * math.cos(amount)) - ((pt[1] - origin[1]) * math.sin(amount))
# 	y = ((pt[1] - origin[1]) * math.cos(amount)) + ((pt[0] - origin[0]) * math.sin(amount))
# 	x += origin[0]
# 	y += origin[1]        
# 	return [x, y]           

														
			

def angle(pt1, pt2, origin): #gets the interior/smaller angle
	a, b, c, d, e, f = origin[0], origin[1], pt1[0], pt1[1], pt2[0], pt2[1]
	#theta = math.acos( ( ((e -a) * (c-a)) + ((f-b) * (d-b)) ) / ( ( ( ((e-a)**2) + ((f-b)**2) ) * ( ((c-a)**2) + ((b-d)**2) ) ) ** 0.5 ) )
	theta = math.acos( ( ((e -a) * (c-a)) + ((f-b) * (d-b)) ) / ( ( (( ((e-a)**2) + ((f-b)**2) ) ** 0.5) * (( ((c-a)**2) + ((b-d)**2) ) ** 0.5) ) ) )    
	return theta           

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

	#print("line653",x,y,theta)
	return theta

#def simpleAngle(pt1, pt2, origin): #same as normalTheta somehow
	#a, b, c, d, e, f = pt1[0], pt1[1], pt2[0], pt2[1], origin[0], origin[1] 

#     theta1 = normalTheta(pt1, origin)
#     theta2 = normalTheta(pt2, origin)
#     theta = max(theta1, theta2) - min(theta1, theta2) 
#     print(theta1, theta2)
#     return theta       
		

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

for site in cell: # Finds edges for cells  
	for entry in cell[site]:
		#at = entry["at"]
		pt1 = entry["point1"]
		pt2 = entry["point2"]
		pt3 = entry["point3"]                           
		#f"{str(point).replace(', ', '_')}"
		#print(pt1, pt2, pt3)
		try:
			site2 = cell[f"{str(pt2).replace(', ', '_')}"]
			for entry2 in site2:
				if entry2["point1"] == pt1 or entry2["point2"] == pt1 or entry2["point3"] == pt1:# or entry2["point2"] == pt3 or entry2["point3"] == pt3:
					#finalCell[f"{str(pt2).replace(', ', '_')}"]["vertices"].append([entry["at"], entry2["at"]])
					if entry2["at"] != entry["at"] and [entry["at"], entry2["at"]] not in finalCell[site]["vertices"]:
#                         tempPair = [entry["at"], entry2["at"]]
#                         sortByY(tempPair)
#                         if tempPair not in finalCell[site]["vertices"]:
#                             finalCell[site]["vertices"].append(tempPair)
											
						#tempPair = [entry["at"], entry2["at"]]
						#sortByY(tempPair)
						
						#midPt = midPoint(entry["at"], entry2["at"])
						#bound1 = nearestBoundry(midPt, tempPair[0])
						#bound2 = nearestBoundry(midPt, tempPair[1])
						
						#finalCell[site]["vertices"].append([bound1, bound2])
						#finalCell[site]["vertices"].append(tempPair)

						finalCell[site]["vertices"].append([entry["at"], entry2["at"]]) # for some reason sorting it by y here messes something up
						#print(site, [pt1, pt2, pt3], [entry2["point1"], entry2["point2"], entry2["point3"]])
						#print("line594",entry["at"],entry2["at"])
						#print(site, entry["at"])
						#print(site, entry["at"], entry2["at"])

						
						
						#print()
						atName = f"{str(entry['at']).replace(', ', '_')}"

						if atName not in vertices:
							tempSites = [pt1, pt2, pt3]
							sortByY(tempSites)
							vertices.update({atName : {"sites":tempSites, "with":[], "at":[]}})
						
						if entry2["point1"] in [pt2, pt3] and [pt1, entry2["point1"]] not in vertices[atName]["with"] and [entry2["point1"], pt1] not in vertices[atName]["with"]:
							vertices[atName]["with"].append([pt1, entry2["point1"]])#vertices[atName]["with"].append([pt1, entry2["point1"]])
							vertices[atName]["at"].append(entry2["at"])#vertices[atName]["at"].append(entry2["at"])
							
						elif entry2["point2"] in [pt2, pt3] and [pt1, entry2["point2"]] not in vertices[atName]["with"] and [entry2["point2"], pt1] not in vertices[atName]["with"]:
							vertices[atName]["with"].append([pt1, entry2["point2"]])#vertices[atName]["with"].append([pt1, entry2["point2"]])
							vertices[atName]["at"].append(entry2["at"])#vertices[atName]["at"].append(entry2["at"])
							
						elif entry2["point3"] in [pt2, pt3] and [pt1, entry2["point3"]] not in vertices[atName]["with"] and [entry2["point3"], pt1] not in vertices[atName]["with"]:
							vertices[atName]["with"].append([pt1, entry2["point3"]])#vertices[atName]["with"].append([pt1, entry2["point3"]])
							vertices[atName]["at"].append(entry2["at"])#vertices[atName]["at"].append(entry2["at"])
																	   
		except Exception as e:
			print(f"site2: {e} not in cell") 

#formatVertex(vertices)

for vert in vertices: # modifies convex hull so that it has edges extending to the boundries of the specified area
	#print("vert",vert, vertices[vert])
	#print()

	if vertices[vert]["at"].__len__() == 1:
		#print("vert",vert, vertices[vert])
		tempVertPt = str(vert).removeprefix("[").removesuffix("]").split("_")
		vertPt = [float(tempVertPt[0]), float(tempVertPt[1])]

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
			#print("line716bounds",nearestBound)            
			vertices[vert]["with"].append([pickedSites[0], pickedSites[1]])
			vertices[vert]["at"].append(nearestBound)
			finalCell[f"{str(pickedSites[0]).replace(', ', '_')}"]["vertices"].append([vertPt, nearestBound])
			finalCell[f"{str(pickedSites[1]).replace(', ', '_')}"]["vertices"].append([vertPt, nearestBound])

	if vertices[vert]["at"].__len__() == 2:
		tempVertPt = str(vert).removeprefix("[").removesuffix("]").split("_")
		vertPt = [float(tempVertPt[0]), float(tempVertPt[1])]

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
		#print(pickedSites)

		if site1 != pickedSites[0] and site1 != pickedSites[1]:
			#pickedSites.append([site1, pickedSites[0][1]])
			notInPair = site1
		elif site2 != pickedSites[0] and site2 != pickedSites[1]:
			#pickedSites.append([site2, pickedSites[0][1]])
			notInPair = site2
		elif site3 != pickedSites[0] and site3 != pickedSites[1]:
			#pickedSites.append([site3, pickedSites[0][1]])
			notInPair = site3
			
		print(pickedSites)
		print(site1, site2, site3)

		test1x = getXAtTime(site1, site2, vertPtT)
		test1y = getYAtTimeAndX(site1, vertPtT, test1x)

		print(test1x, test1y, vertPt, vertPtT)

		test2x = getXAtTime(site1, site2, vertPtT + 0.5)

		print(getYAtTimeAndX(site1, vertPtT + 0.5, test2x), getYAtTimeAndX(site2, vertPtT + 0.5, test2x), getYAtTimeAndX(site3, vertPtT + 0.5, test2x))
		test3x = getXAtTime(site1, site2, vertPtT - 0.5)
		print(getYAtTimeAndX(site1, vertPtT - 0.5, test3x), getYAtTimeAndX(site2, vertPtT - 0.5, test3x), getYAtTimeAndX(site3, vertPtT - 0.5, test3x))
		
		#print()
		#print(getXAtTime(pickedSites[0][0], pickedSites[0][1], vertPtT - 0.5), getXAtTime(pickedSites[0][1], pickedSites[0][0], vertPtT - 0.5))

		beforeTx = getXAtTime(pickedSites[0], pickedSites[1], vertPtT - 0.5)
		afterTx = getXAtTime(pickedSites[0], pickedSites[1], vertPtT + 0.5)

		throughPt = []
		
		beforeTy1 = getYAtTimeAndX(pickedSites[0], vertPtT - 0.5, beforeTx)
		beforeTy2 = getYAtTimeAndX(notInPair, vertPtT - 0.5, beforeTx)
		afterTy1 = getYAtTimeAndX(pickedSites[0], vertPtT + 0.5, afterTx)
		afterTy2 = getYAtTimeAndX(notInPair, vertPtT + 0.5, afterTx)

		print(afterTy1, afterTy2)
		print(beforeTy1, beforeTy2)
		

		if vertPtT - 0.5 < notInPair[1]: # If the intersection point time - 0.5 is less than the 3rd point's y, so it should not be considered yet, just use that point
			throughPt = [beforeTx, beforeTy1]
			print("throughA", beforeTx, beforeTy1)
			
		else:
			if beforeTy1 > beforeTy2:
				throughPt = [beforeTx, beforeTy1]
				print("throughB", beforeTx, beforeTy1)
			elif afterTy1 > afterTy2: # can't be an else
				throughPt = [afterTx, afterTy1]
				print("throughC", beforeTx, beforeTy1)

		if throughPt != []:
			#nearestBound = nearestBoundry(vertPt, throughPt)
			
			#finalCell[f"{str(pickedSites[0][0]).replace(', ', '_')}"]["vertices"].append([vertPt, nearestBound])
			#finalCell[f"{str(pickedSites[0][1]).replace(', ', '_')}"]["vertices"].append([vertPt, nearestBound])

			if vertPt[0] < defaultBounds[0][0] or vertPt[0] > defaultBounds[0][1] or vertPt[1] < defaultBounds[1][1] or vertPt[1] > defaultBounds[1][0]:
			#if withinBounds(vertPt, defaultBounds):
				nearestBound = nearestBoundry(vertPt, throughPt)

				newBound1 = nearestOutsideBoundry(vertPt, throughPt)
				newBound2 = nearestOutsideBoundry(vertPt, vertices[vert]["at"][0])
				newBound3 = nearestOutsideBoundry(vertPt, vertices[vert]["at"][1])
				print("line765", vertices[vert]["at"])

				finalCell[f"{str(vertices[vert]['with'][0][0]).replace(', ', '_')}"]["vertices"].append([vertices[vert]["at"][0], newBound2])
				finalCell[f"{str(vertices[vert]['with'][0][1]).replace(', ', '_')}"]["vertices"].append([vertices[vert]["at"][0], newBound2])
				finalCell[f"{str(vertices[vert]['with'][1][0]).replace(', ', '_')}"]["vertices"].append([vertices[vert]["at"][1], newBound3])
				finalCell[f"{str(vertices[vert]['with'][1][1]).replace(', ', '_')}"]["vertices"].append([vertices[vert]["at"][1], newBound3])
						
				if (nearestBound[0] == defaultBounds[0][0] or nearestBound[0] == defaultBounds[0][1]) and (nearestBound[1] <= defaultBounds[1][0] and nearestBound[1] >= defaultBounds[1][1]):
					finalCell[f"{str(pickedSites[0]).replace(', ', '_')}"]["vertices"].append([newBound1, nearestBound])
					finalCell[f"{str(pickedSites[1]).replace(', ', '_')}"]["vertices"].append([newBound1, nearestBound])
				elif (nearestBound[1] == defaultBounds[1][0] or nearestBound[1] == defaultBounds[1][1]) and (nearestBound[0] >= defaultBounds[0][0] and nearestBound[0] <= defaultBounds[0][1]):
					finalCell[f"{str(pickedSites[0]).replace(', ', '_')}"]["vertices"].append([newBound1, nearestBound])
					finalCell[f"{str(pickedSites[1]).replace(', ', '_')}"]["vertices"].append([newBound1, nearestBound])
				  
			else:                            
				nearestBound = nearestBoundry(vertPt, throughPt)
				#print("nearestBound",nearestBound)                
				vertices[vert]["with"].append([pickedSites[0], pickedSites[1]])
				vertices[vert]["at"].append(nearestBound)
				finalCell[f"{str(pickedSites[0]).replace(', ', '_')}"]["vertices"].append([vertPt, nearestBound])
				finalCell[f"{str(pickedSites[1]).replace(', ', '_')}"]["vertices"].append([vertPt, nearestBound])

		print()

	continue
	if vertices[vert]["at"].__len__() == 1:
		#print("vert",vert, vertices[vert])
		tempVertPt = str(vert).removeprefix("[").removesuffix("]").split("_")
		vertPt = [float(tempVertPt[0]), float(tempVertPt[1])]

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
			#print("line716bounds",nearestBound)            
			vertices[vert]["with"].append([pickedSites[0], pickedSites[1]])
			vertices[vert]["at"].append(nearestBound)
			finalCell[f"{str(pickedSites[0]).replace(', ', '_')}"]["vertices"].append([vertPt, nearestBound])            
			finalCell[f"{str(pickedSites[1]).replace(', ', '_')}"]["vertices"].append([vertPt, nearestBound])

			#outsideBoundry[f"{str(pickedSites[0]).replace(', ', '_')}"]["vertices"].append(nearestBound)
	
	if vertices[vert]["at"].__len__() == 2:
		#print("vert",vert, vertices[vert])
		tempVertPt = str(vert).removeprefix("[").removesuffix("]").split("_")
		vertPt = [float(tempVertPt[0]), float(tempVertPt[1])]                 
					
		site1 = vertices[vert]["sites"][0]
		site2 = vertices[vert]["sites"][1]
		site3 = vertices[vert]["sites"][2]

		pickedSites = [[site1, site2], [site1, site3], [site2, site3]]
		pickedSites.remove(vertices[vert]["with"][0])
		pickedSites.remove(vertices[vert]["with"][1])        
		
		dist1 = distancePt(pickedSites[0][0], pickedSites[0][1])
		dist2 = distancePt(vertices[vert]["with"][0][0], vertices[vert]["with"][0][1])
		dist3 = distancePt(vertices[vert]["with"][1][0], vertices[vert]["with"][1][1])        

		throughPt = []
		pair3 = []        

		if dist1 < dist2 and dist1 < dist3:
			pickedSites = pickedSites[0]
			throughPt = midPoint(pickedSites[0], pickedSites[1])
			pair3 = pickedSites
		else:
			pair3 = pickedSites[0]            
			tVertPt = tAtXandY(pair3[0], vertPt[0], vertPt[1])
	
			notInPair = vertices[vert]["sites"].copy()
			notInPair.remove(pair3[0])
			notInPair.remove(pair3[1])
			notInPair = notInPair[0]

			test1y1 = yAtX(pair3[0], pair3[1], vertPt[0] + 0.5)
			test2y1 = yAtX(pair3[0], notInPair, vertPt[0] + 0.5)
			test3y1 = yAtX(pair3[1], notInPair, vertPt[0] + 0.5)

			test1y2 = getYAtTimeAndX(pair3[0], tVertPt, vertPt[0] + 0.5) 
			test2y2 = getYAtTimeAndX(pair3[1], tVertPt, vertPt[0] + 0.5) 
			test3y2 = getYAtTimeAndX(notInPair, tVertPt, vertPt[0] + 0.5)
	   
			pair1 = vertices[vert]["with"][0]
			pair2 = vertices[vert]["with"][1]        
		
			midPt1 = midPoint(pair1[0], pair1[1])
			midPt2 = midPoint(pair2[0], pair2[1])

			angle1 = angle(midPt1, midPt2, vertPt)

			midPt3 = midPoint(pair3[0], pair3[1])             
		
			tVertPt = tAtXandY(pair3[0], vertPt[0], vertPt[1])
			tXAfterVert = getTimeAtX(pair3[0], pair3[1], notInPair, vertPt[0] + 5)

			at1 = vertices[vert]["at"][0]
			at2 = vertices[vert]["at"][1]

			theta1 = normalTheta(at1, vertPt)
			theta2 = normalTheta(at2, vertPt)        

			testPt1 = [vertPt[0] + 0.5, yAtX(pair3[0], pair3[1], vertPt[0] + 0.5)]
			testPt2 = [vertPt[0] - 0.5, yAtX(pair3[0], pair3[1], vertPt[0] - 0.5)]

			throughPt = []             

			test1Theta = normalTheta(testPt1, vertPt)
			test2Theta = normalTheta(testPt2, vertPt)
			minTheta = min(theta1, theta2)
			maxTheta = max(theta1, theta2)        

			if abs(theta1 - theta2) > math.pi:
				if test1Theta > min(theta1, theta2) and test1Theta < max(theta1, theta2):
					throughPt = testPt1
				else:
					throughPt = testPt2
			else:
				if test1Theta > max(theta1, theta2) or test1Theta < min(theta1, theta2):
					throughPt = testPt1
				else:
					throughPt = testPt2


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
						
				if (nearestBound[0] == defaultBounds[0][0] or nearestBound[0] == defaultBounds[0][1]) and (nearestBound[1] <= defaultBounds[1][0] and nearestBound[1] >= defaultBounds[1][1]):
					finalCell[f"{str(pair3[0]).replace(', ', '_')}"]["vertices"].append([newBound1, nearestBound])
					finalCell[f"{str(pair3[1]).replace(', ', '_')}"]["vertices"].append([newBound1, nearestBound])
				elif (nearestBound[1] == defaultBounds[1][0] or nearestBound[1] == defaultBounds[1][1]) and (nearestBound[0] >= defaultBounds[0][0] and nearestBound[0] <= defaultBounds[0][1]):
					finalCell[f"{str(pair3[0]).replace(', ', '_')}"]["vertices"].append([newBound1, nearestBound])
					finalCell[f"{str(pair3[1]).replace(', ', '_')}"]["vertices"].append([newBound1, nearestBound])
				  
			else:                            
				nearestBound = nearestBoundry(vertPt, throughPt)
				#print("nearestBound",nearestBound)                
				vertices[vert]["with"].append([pair3[0], pair3[1]])
				vertices[vert]["at"].append(nearestBound)
				finalCell[f"{str(pair3[0]).replace(', ', '_')}"]["vertices"].append([vertPt, nearestBound])
				finalCell[f"{str(pair3[1]).replace(', ', '_')}"]["vertices"].append([vertPt, nearestBound])


				
	#return [float("%.10f" % vert[0]), float("%.10f" % vert[1])]

#print("-----",finalCell["[52_99]"]["vertices"])
#print("-----",finalCell["[0_174]"]["vertices"])
#print("-----",finalCell["[13_23]"]["vertices"])
#print("-----",finalCell["[156_163]"]["vertices"])
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
	print("line956", unique)

	
	continue
	tempVerts = finalCell[cell3]["vertices"].copy()
	sortByY(tempVerts)
	for vert in tempVerts:
		sortByY(vert)
	
	formatVertex(tempVerts)

	unique = []
	outsideUnique = []
	bufferWidth = (defaultBounds[0][0] + defaultBounds[0][1])/2
	bufferHeight = (defaultBounds[1][1] + defaultBounds[1][0])/2
	bufferWidth = bufferWidth/2
	bufferHeight = bufferHeight/2
	
	curSite = cell3.replace("[","").replace("]","").split("_")
	curSite = [float(curSite[0]), float(curSite[1])]
	
	#print("site",cell3)
	for vert in tempVerts:
		#print("vert",vert)        
		if vert not in unique and vert[0] != vert[1] and vert not in outsideUnique:
			# if vert[0][0] >= defaultBounds[0][0] and vert[0][0] <= defaultBounds[0][1] and vert[0][1] >= defaultBounds[1][1] and vert[0][1] <= defaultBounds[1][0]:
			# 	if vert[1][0] >= defaultBounds[0][0] and vert[1][0] <= defaultBounds[0][1] and vert[1][1] >= defaultBounds[1][1] and vert[1][1] <= defaultBounds[1][0]:
			# 		pass
			# 	elif vert[1][0] >= defaultBounds[0][0] - halfWidth and vert[1][0] <= defaultBounds[0][1] + halfWidth and vert[1][1] >= defaultBounds[1][1] - halfHeight and vert[1][1] <= defaultBounds[1][0] + halfHeight:
			# 		pass
					
			# elif vert[0][0] >= defaultBounds[0][0] - halfWidth and vert[0][0] <= defaultBounds[0][1] + halfWidth and vert[0][1] >= defaultBounds[1][1] - halfHeight and vert[0][1] <= defaultBounds[1][0] + halfHeight:
			# 	#if vert[1][0] >= defaultBounds[0][0] and vert[1][0] <= defaultBounds[0][1] and vert[1][1] >= defaultBounds[1][1] and vert[1][1] <= defaultBounds[1][0]:
			# 	if vert[1][0] >= defaultBounds[0][0] - halfWidth and vert[1][0] <= defaultBounds[0][1] + halfWidth and vert[1][1] >= defaultBounds[1][1] - halfHeight and vert[1][1] <= defaultBounds[1][0] + halfHeight:
			# 		#print("								unique",vert)
			# 		unique.append(vert)
			boundsBuffer = [[defaultBounds[0][0] - bufferWidth, defaultBounds[0][1] + bufferWidth], [defaultBounds[1][0] + bufferHeight, defaultBounds[1][1] - bufferHeight]]

			if withinBounds(vert[0], defaultBounds) and withinBounds(vert[1], defaultBounds):
				unique.append(vert)
			elif withinBounds(vert[0], boundsBuffer) and withinBounds(vert[1], boundsBuffer):
				outsideUnique.append(vert)

	if unique == []:

		pts = points.copy()
		distanceTargetSort(curSite, pts)

		#i = points.index(curSite)

		#other = []
		#if i == points.__len__()-1:
		#	other = points[i - 1]
		#else:                    
		#	other = points[i + 1]

		other = pts[1]

		midPt = midPoint(curSite, other)
		before = [midPt[0]-0.5, yAtX(curSite, other, midPt[0]-0.5)]
		after = [midPt[0]+0.5, yAtX(curSite, other, midPt[0]+0.5)]

		bound1 = nearestBoundry(midPt, before)
		bound2 = nearestBoundry(midPt, after)

		unique = [[bound1, bound2]]
		#print("line819 unique",unique)
		sortByY(unique[0])
		#print("line1022",unique)
		formatVertex(unique)
		#print("line1024",unique)
		finalCell[f"{str(other).replace(', ', '_')}"]["vertices"].append(unique[0])

	elif outsideUnique != []: # This fixed some stuff and broke others
		#print("line1014",curSite, "-", outsideUnique[0])
		outsideUnique = outsideUnique[0]
		valid = []
		if withinBounds(outsideUnique[0], defaultBounds):
			valid = outsideUnique[0]
		else:
			valid = outsideUnique[1]

		tmp = outsideUnique.copy()
		tmp.remove(valid)
		boundry = nearestBoundry(valid, tmp[0])

		tempPair = [boundry, valid]
		sortByY(tempPair)
		formatVertex(tempPair)

		if tempPair not in unique:
			unique.append(tempPair)

	if points.__len__() > 1:
		finalCell[cell3]["vertices"] = unique
		

print()
#print("-----",finalCell["[52_99]"]["vertices"])
#print("-----",finalCell["[0_174]"]["vertices"])
#print("-----",finalCell["[13_23]"]["vertices"])
#print("-----",finalCell["[12_160]"]["vertices"])
#print("-----",finalCell["[156_163]"]["vertices"])
#print()
print(vertices.keys())
for cell4 in finalCell:
	for vert in finalCell[cell4]["vertices"]:
		print(vert)
		print(f"{str(vert[0]).replace(', ', '_')}" in list(vertices.keys()), f"{str(vert[1]).replace(', ', '_')}" in list(vertices.keys()))
		if not withinBounds(vert[0], defaultBounds):
			if f"{str(vert[0]).replace(', ', '_')}" in list(vertices.keys()):
				print(vertices[f"{str(vert[0]).replace(', ', '_')}"])

def makeEdges(onBoundry, curSite):
	inside = False
	vert1Theta = normalTheta(onBoundry[0], curSite)
	vert2Theta = normalTheta(onBoundry[1], curSite)
				
	minTheta = min(vert1Theta, vert2Theta)
	maxTheta = max(vert1Theta, vert2Theta)
				
	#print("theta",vert1Theta,vert2Theta)
	# Checks if there is a site within the sector formed by the two boundry vertices
	for pt in points:
		if pt != curSite:
			ptTheta = normalTheta(pt, curSite)                    
			#if ptTheta > vert2Theta and ptTheta < vert1Theta:
			if ptTheta > minTheta and ptTheta < maxTheta:
				inside = True
				break
						
	withCorners = [[onBoundry[0], vert1Theta], [onBoundry[1], vert2Theta]]

	if inside == False: # If there is not a site between the angles of the two boundry vertices

		#withCorners = [[onBoundry[1], vert2Theta], [onBoundry[0], vert1Theta]]

		for i in range(0, corners.__len__()): # Finds corners that are within the area
			cornerTheta = normalTheta(corners[i], curSite)
			#print("line1058",corners[i],cornerTheta)
			#if cornerTheta > vert2Theta and cornerTheta < vert1Theta:
			if cornerTheta > minTheta and cornerTheta < maxTheta:
				withCorners.append([corners[i], cornerTheta])

		sortByY(withCorners)

		#print("rangeIn", withCorners)
					
		#for i in range(0, withCorners.__len__()-1):
		#	finalCell[cell2]["vertices"].append([withCorners[i][0], withCorners[i+1][0]])

	else:
					
		#withCorners = [[onBoundry[0], vert1Theta], [onBoundry[1], vert2Theta]]
		# If there is a site within the angle between the two boundry vertices, use the area between the upper angle and the lower angle (opposite of between lower angle and upper)
		for i in range(0, corners.__len__()):
			cornerTheta = normalTheta(corners[i], curSite)
			#if cornerTheta < vert2Theta or cornerTheta > vert1Theta:
			if cornerTheta < minTheta or cornerTheta > maxTheta:
				tempAngle = cornerTheta - vert1Theta # Rotates the corner angle so that the upper boundry angle becomes 0 degrees
				if tempAngle < 0:
					tempAngle += 2 * math.pi
							
				withCorners.append([corners[i], tempAngle])
				#withCorners.append([corners[i], angle(onBoundry[0], corners[i], curSite)])

		withCorners[0] = [onBoundry[0], 0] # Makes the upper boundry angle 0 degrees
		withCorners[1] = [onBoundry[1], ((2 * math.pi) - vert1Theta) + vert2Theta] # Changes the lower boundry angle to be the new upper bound

		sortByY(withCorners)

		#print("rangeOut", withCorners)
					
		#for i in range(0, withCorners.__len__()-1):
		#	finalCell[cell2]["vertices"].append([withCorners[i][0], withCorners[i+1][0]])

	for i in range(0, withCorners.__len__()-1):
		finalCell[cell2]["vertices"].append([withCorners[i][0], withCorners[i+1][0]])

# Finds edges that are on the boundry of the target area
boundryEdges = [] 
for cell2 in finalCell:
	  
	#print("info",cell2,"-",finalCell[cell2]["vertices"])    
	onBoundry = []
	for vert in finalCell[cell2]["vertices"]:
		boundSize = [defaultBounds[0][0], defaultBounds[0][1], defaultBounds[1][0], defaultBounds[1][1]] # Flattened version of defaultBounds array
		if (vert[0][0] in boundSize or vert[0][1] in boundSize) and vert[0] not in onBoundry:
			onBoundry.append(vert[0])
		if (vert[1][0] in boundSize or vert[1][1] in boundSize) and vert[1] not in onBoundry:
			onBoundry.append(vert[1])            

	#print(onBoundry)
				
	if onBoundry != []:     
		#print("info",cell2,"-",finalCell[cell2]["vertices"])
		curSite = cell2.replace("[","").replace("]","").split("_")
		curSite = [float(curSite[0]), float(curSite[1])]

		sortByY(onBoundry)
      
		if onBoundry.__len__() == 2:
			if onBoundry[0][0] == onBoundry[1][0] or onBoundry[0][1] == onBoundry[1][1]: # If the two vertices are on the same edge, they can just be added to finalCell without any extra work
				finalCell[cell2]["vertices"].append([onBoundry[0], onBoundry[1]])
				
			else: # if the two vertices are not on the same edge

				makeEdges(onBoundry, curSite)

		else: # if it greater than 2, it would ALMOST have to be a multiple of 2, with verts on different edges
			#print("greater than 2")

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

				#used = []
				single = []

				for edge in sides:
					if edge.__len__() == 2:
						#print(edge)
						finalCell[cell2]["vertices"].append([edge[0], edge[1]])
						#used.extend(edge)
					elif edge.__len__() == 1:
						single.append(edge[0])
			
				if single.__len__() > 0:
					
					#print(single)
					
					makeEdges(single, curSite)

		#print()





for pt in points:
	plt.plot(pt[0], pt[1], "ro")
	#plt.plot(pt[0], pt[1], color=(1,0,0), marker="o") # works	

for site in cell:  
	#print(cell[site])
	#clr1, clr2, clr3 = random.random(), random.random(), random.random() 
	for entry in cell[site]:
        
		plt.plot(entry["at"][0], entry["at"][1], "go")#, color=(clr1, clr2, clr3))

		plt.plot([entry["point2"][0], entry["at"][0], entry["point3"][0], entry["at"][0], entry["point1"][0]], [entry["point2"][1], entry["at"][1], entry["point3"][1], entry["at"][1], entry["point1"][1]], "g") 
      
	
for cell in finalCell:

	used = []
			
	for pairs in finalCell[cell]["vertices"]:    

		plt.plot([pairs[0][0], pairs[1][0]], [pairs[0][1], pairs[1][1]], "b")
		plt.plot([pairs[0][0], pairs[1][0]], [pairs[0][1], pairs[1][1]], "bo")                
		
		if pairs[0] not in used:
			used.append(pairs[0])
		if pairs[1] not in used:
			used.append(pairs[1])									

	temp = used.copy()
	temp2 = []
	curSite = cell.replace("[","").replace("]","").split("_")
	curSite = [float(curSite[0]), float(curSite[1])]
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



