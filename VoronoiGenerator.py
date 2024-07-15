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
for i in range(1, 100):
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
#points = [[20, 25], [40, 100], [70, 160], [95, 190]] # no intersections within the target area

#points = [[73, 8], [62, 92], [37, 95], [80, 139], [154, 147], [84, 177], [85, 177]] # broke finding boundry edges with outside angles

#points = [[25, 25], [75, 75], [50, 50]]

#points = [[136, 20], [21, 25], [62, 26], [17, 39], [131, 45], [165, 47], [104, 52], [151, 67], [28, 72], [84, 72], [34, 73], [186, 73], [165, 75], [8, 75], [33, 76], [35, 81], [105, 83], [196, 89], [162, 101], [11, 103], [105, 109], [135, 109], [8, 114], [18, 114], [164, 116], [12, 119], [148, 123], [138, 127], [80, 157]]
#points = [[17, 39], [8, 75], [28, 72], [34, 73], [33, 76], [35, 81]]

#points = [[0, 8], [35, 8], [126, 11], [192, 14], [35, 18], [144, 20], [34, 30], [145, 31], [132, 51], [49, 86], [91, 86], [101, 95], [126, 98], [116, 105], [142, 116], [183, 139], [139, 143], [180, 151], [177, 156], [77, 161], [115, 162], [15, 163], [141, 163], [170, 163], [46, 164], [18, 164], [172, 164], [14, 175], [18, 175]]
#points = [[198, 11], [109, 11], [155, 20], [194, 21], [119, 22], [152, 29], [81, 34], [175, 36], [165, 41], [3, 50], [190, 54], [164, 55], [152, 56], [11, 59], [72, 62], [33, 74], [9, 80], [110, 82], [164, 82], [157, 98], [141, 100], [90, 102], [156, 111], [15, 120], [42, 125], [115, 126], [40, 147], [139, 178], [10, 184]]

#points = [[149, 2], [121, 8], [13, 12], [195, 25], [176, 34], [181, 42], [66, 49], [187, 66], [178, 66], [130, 67], [175, 75], [6, 82], [63, 89], [101, 95], [194, 97], [18, 105], [65, 105], [80, 105], [175, 112], [77, 113], [175, 120], [113, 130], [37, 130], [87, 142], [143, 146], [86, 149], [151, 160], [112, 177], [78, 198]]

#points = [[16, 0], [29, 8], [178, 9], [174, 9], [131, 21], [110, 32], [191, 40], [65, 47], [182, 66], [57, 78], [31, 88], [184, 95], [60, 114], [28, 115], [143, 117], [181, 126], [116, 129], [131, 135], [143, 140], [127, 143], [57, 148], [158, 150], [11, 155], [122, 159], [108, 162], [176, 162], [189, 166], [8, 181], [194, 192]]

#points = [[20, 4], [169, 5], [31, 16], [13, 21], [27, 22], [101, 31], [111, 32], [136, 50], [126, 59], [192, 67], [172, 68], [69, 83], [45, 97], [150, 116], [91, 117], [40, 120], [49, 130], [116, 138], [4, 144], [156, 149], [88, 150], [10, 150], [58, 151], [16, 153], [163, 161], [157, 186], [190, 193], [54, 195], [194, 200]]

#vertices is 0
#points = [[22, 299], [23, 299], [12, 273], [25, 25]]
#points = [[22, 199], [23, 199], [12, 173], [25, 25]]
#points = [[20, 199], [25, 199], [12, 173], [25, 25]]

#points = [[69, 228], [77, 228], [73, 239], [63, 244], [62, 220], [84, 203], [81, 243]]
#points = [[69, 228], [77, 228], [73, 239]]

#------------- 100 points
#points = [[64, 3], [56, 4], [20, 8], [8, 9], [59, 12], [88, 14], [27, 20], [3, 22], [26, 23], [99, 29], [29, 32], [56, 37], [29, 38], [50, 38], [22, 39], [56, 40], [11, 52], [92, 52], [90, 58], [79, 69], [97, 70], [32, 71], [46, 71], [7, 73], [18, 74], [89, 79], [58, 80], [51, 84], [17, 88], [13, 94], [24, 99], [94, 101], [43, 101], [45, 106], [50, 111], [17, 112], [41, 114], [89, 115], [80, 118], [33, 123], [74, 123], [88, 131], [19, 133], [29, 137], [20, 138], [40, 139], [60, 140], [49, 144], [1, 157], [67, 160], [95, 164], [50, 165], [38, 166], [58, 170], [52, 174], [34, 177], [12, 179], [25, 184], [91, 185], [62, 185], [80, 189], [56, 192], [28, 196], [19, 196], [84, 203], [52, 204], [66, 206], [23, 206], [34, 207], [41, 215], [100, 217], [46, 218], [40, 220], [62, 220], [17, 222], [77, 228], [69, 228], [15, 229], [45, 237], [73, 239], [19, 240], [81, 243], [63, 244], [13, 258], [1, 259], [43, 261], [42, 264], [44, 268], [78, 268], [11, 269], [12, 273], [50, 274], [68, 278], [37, 278], [75, 281], [92, 295], [23, 299], [22, 299], [91, 300]]

#-------------with box that is 100 wide and 300 tall
#points = [[75, 14], [85, 22], [86, 26], [94, 32], [92, 45], [32, 71], [0, 127], [50, 132], [10, 134], [28, 134], [21, 134], [95, 147], [38, 152], [63, 162], [70, 168], [7, 175], [4, 176], [65, 179], [12, 187], [87, 190], [23, 197], [7, 206], [91, 209], [100, 234], [73, 236], [33, 267], [10, 273], [20, 278], [96, 298]]
#points = [[86, 16], [33, 30], [49, 32], [27, 36], [98, 40], [23, 47], [11, 49], [69, 59], [67, 66], [81, 75], [75, 78], [6, 81], [1, 108], [4, 133], [100, 151], [30, 165], [86, 189], [30, 226], [54, 244], [15, 253], [41, 255], [52, 267], [11, 269], [27, 271], [13, 272], [49, 293], [84, 294], [2, 298], [46, 300]]
# ^ I think caused by the fact that when the x-values are the same, it just picks a slope without much good reasoning behind it, here causing the slope to be on the wrong side of the intersection

#points = [[7, 34], [87, 254], [91, 265], [86, 16]]
#points = [[30, 226], [30, 165], [86, 189]]
#points = [[7, 34], [87, 254], [91, 265]]

#points = [[45, 70], [61, 100], [13, 162], [84, 208], [99, 233], [73, 270], [6, 281]]
#points = [[15, 38], [22, 55], [25, 158], [75, 197], [0, 225], [68, 248], [83, 249]]

#points = [[72, 20], [10, 69], [85, 72], [80, 78], [26, 88], [63, 100], [83, 104], [96, 117], [84, 126], [93, 131], [91, 136], [67, 144], [54, 147], [41, 149], [94, 179], [56, 182], [23, 197], [75, 213], [18, 217], [36, 252], [60, 256], [41, 259], [38, 266], [36, 267], [55, 269], [85, 270], [44, 286], [22, 289], [75, 299]]

#points = [[67, 13], [55, 26], [0, 31], [78, 33], [50, 41], [47, 52], [99, 54], [16, 55], [38, 88], [24, 94], [14, 114], [0, 122], [5, 123], [14, 129], [85, 134], [84, 137], [33, 137], [28, 141], [24, 167], [89, 199], [54, 202], [67, 208], [90, 217], [8, 221], [98, 235], [52, 252], [15, 255], [38, 258], [50, 297]]

#points = [[128, 141], [33, 137], [84, 137], [85, 134], [24, 167], [54, 202]]

#points = [[104, 95], [167, 95], [142, 136]]

#points = [[104, 95], [167, 95], [20, 95]]
#points = [[104, 95], [167, 95], [20, 95], [180, 95]]
#points = [[40, 10], [40, 20], [40, 30], [40, 75]]

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
	#a, b, c, d, e, f = pt1[0], pt1[1], pt2[0], pt2[1], pt3[0], pt3[1]
	#if (2 * ( ((a-e)*(b-d)) - ((a-c)*(b-f))) ) != 0:
	# If the y-values of two of the points are the same, this will give the x-value of the midpoint of the two points that have the same y-value
	try:
		a, b, c, d, e, f = pt1[0], pt1[1], pt2[0], pt2[1], pt3[0], pt3[1]
		x = ( ( ((a**2) - (e**2))*(b-d) ) - ( ((a**2) - (c**2)) * (b-f) ) - ( (d-f)*(b-f)*(b-d) )) / (2 * ( ((a-e)*(b-d)) - ((a-c)*(b-f))) )
		return float("%.10f" % x)
	except ZeroDivisionError:
		# Division by 0 happens if the lines are parallel
	#else: # I need to have it return the midpoint between the site and nearest site if there is division by zero, because that means that the two lines are parallel and the farther site will not be valid
		# Seems to not usually break anything despite the fact that the division by 0 is not handled properly
		# The above statement is wrong. It has always broken something, it is just usually hard to tell
		# division by zero happens with the points: 
		# [50, 50] [25, 25] [75, 75]
		# [7, 34] [87, 254] [91, 265]
		# using [[7, 34], [87, 254], [91, 265], [86, 16]] will show that it does cause issues
		# Divides by 0 if (a-e)*(b-d) = (a-c)*(b-f) or if all 3 points have either the same x or y value
		print(f"division by zero in find3IntersectX with {pt1} {pt2} {pt3}")
		#print(( ( ((a**2) - (e**2))*(b-d) ) - ( ((a**2) - (c**2)) * (b-f) ) - ( (d-f)*(b-f)*(b-d) )), (2 * ( ((a-e)*(b-d)) - ((a-c)*(b-f))) ))
		#print(f"({a}, {b}) ({c}, {d}) ({e}, {f})")
		#print(a-e, b-d, a-c, b-f)
		#print((a-e)*(b-d), (a-c)*(b-f))
		#print(-1/slope(pt1, pt2), -1/slope(pt1, pt3), -1/slope(pt2, pt3))
		#print("b",(a - c)/2)
		#return (a - c)/2   #returning (a-c)/2 or 0 doesn't seem to make a difference
		#return 0
		# midPt = midPoint(pt1, pt2)
		# plt.plot([a,c],[b,d], "y")
		# plt.plot(midPt[0], midPt[1], "yo")
		#return -1000000
		#return defaultBounds[0][0] - 5
		#return float("%.10f" % midPoint(pt1, pt2)[0])
		return None

def otherXOnBisectorAtT(pt1, pt2, pt3, t): # pt1 and pt2 form the bisector and pt3 makes the parabola that it intersects with
	try:
		a, b, c, d, e, f = pt1[0], pt1[1], pt2[0], pt2[1], pt3[0], pt3[1]
		
		m = d-b
		n = 2 * ( ( (a-c) * (t-f) ) + (e * (b-d)) )
		o = -1 * ( ( (b-d) * ( (e**2) + (f**2) - (t**2) ) ) - ( (t-f) * ( (d**2) - (b**2) - (a**2) + (c**2) ) ) )

		x = ( (-1 * n) - ( ( (n**2) - (4 * m * o) )**0.5 ) ) / (2 * m)#( (-1 * n) + ( ( (n**2) - (4 * m * o) )**0.5 ) ) / (2 * m) 
		return float("%.10f" % x)
	except ZeroDivisionError:
		# Divides by 0 if m = 0, so if the first two points have the same y-value
		# So the correct x-value would be the midpoint between the two since the bisector is a vertical line, causing the y-values to be different with t, but not x
		print(f"division by zero in otherXOnBisectorAtT with {pt1} {pt2} {pt3} t={t}")        
		#return defaultBounds[1][1] -5  
		return (a + c) / 2

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
		# Divides by 0 if m = 0, so if the two points have the same y-value
		# So the correct x-value would be the midpoint between the two
		print(f"division by zero in getXAtTime with {pt1} {pt2} t={t}")
		#return defaultBounds[1][1] -5
		return (a + c) / 2

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
		# Divides by 0 if m = 0, so if the two points have the same y-value
		# So the correct x-value would be the midpoint between the two
		print(f"division by zero in find2IntersectAtTime with {pt1} {pt2} t={t}")
		#return defaultBounds[1][1] -5
		return (a + c) / 2

def getTimeAtX(pt1, pt2, pt3, x): # finds time when parabola pt1 has given x value, sensitive to order, (pt1, pt2, pt3) != (pt1, pt3, pt2) #(pt1, pt2, pt3) = (pt1, pt3, pt2)
	# What does this even mean? A parabola extends infinitely, so it covers all x-values at all times
	# Also, the graph of this function on desmos goes to a vertical asymptote towards -y at x = midpoint(pt1, pt2) but stops at y=0 (this is if pt1 and pt2 have the same y-value)
	# This can only be used with find3IntersectX
	# If the y-values of the first two points are the same, this function = 0 at x = midpoint(pt1, pt2)
	try:
		a, b, c, d, e, f = pt1[0], pt1[1], pt2[0], pt2[1], pt3[0], pt3[1]
		j = b-d
		k = -( (a**2) + (b**2) - (c**2) - (d**2) + (2 * x * (c-a)))#-1 * ( (a**2) + (-2 * x * a) + (b**2) - (d**2) + (b * d) - (c**2) + (2 * x * c) - (d * b) )#-( (a**2) + (b**2) ) + (c**2) + (d**2) + (2 * x * (a-c)) #this last one is incorrect
		L = f * ( (a**2) + (b**2) - (c**2) - (d**2) - (2 * x * (a - c) ) ) - ( ( (x**2) + (e**2) + (f**2) - (2 * x * e) ) * j )#f * ( (a**2) + (b**2) - (c**2) - (d**2) - (2 * x * (a - c) ) ) - ( ( (x**2) + (e**2) + (f**2) - (2 * x * e) ) * (b - d) ) #f*( (a**2) - (c**2) + (b**2) - (d**2) - (2 * x * (a-c)) ) - (( ((x-e)**2) + (f**2) )*(b-d))
		t = ((-1 * k) - ( (k**2) - (4 * j * L))**0.5) / (2 * j) # division by 0 if j = 0, j = 0 if b-d = 0, so if the first 2 points have the same y value
		return float("%.10f" % t)
	except ZeroDivisionError:
		#print(f"division by zero in getTimeAtX with {pt1} {pt2} {pt3} x={x} j={j} k={k} L={L}") # j, k, and L will always be 0 in this event
		print(f"division by zero in getTimeAtX with {pt1} {pt2} {pt3} x={x}")
		#return pt1[1]
		return None

def getYAtTimeAndX(pt1, t, x): # just the y-value of the parabola at the given t and x, which may different than yAtX since that is locked to the bisector
	try:
		a, b = pt1[0], pt1[1]
		y = (((x-a)**2) / (2 * (b-t))) + (0.5 * (b+t)) # divides by 0 if b-t = 0
		return float("%.10f" % y)
	except ZeroDivisionError:
		print(f"division by zero in getYAtTimeAndX with {pt1} t={t} x={x}")
		#return defaultBounds[1][1] -5
		return None

def yAtX(pt1, pt2, x): # gives y value of bisector between two parabolas at given x value
	try:
		a, b, c, d = pt1[0], pt1[1], pt2[0], pt2[1]
		y = ((c-a) / (b-d)) * (x - ( (a+c)/2) ) + ((b+d)/2) # divides by 0 if b-d = 0 (points have same y value), so the valid y value would also be the same
		return float("%.10f" % y)
	except ZeroDivisionError:
		print(f"division by zero in yAtX with {pt1} {pt2} x={x}")
		return pt1[1]
	
def xAtY(pt1, pt2, y): # gives x value of bisector between two parabolas at given y value
	try:
		a, b, c, d = pt1[0], pt1[1], pt2[0], pt2[1]
		x = ( (2 * y * (d-b)) - ((d**2) - (b**2)) + ((a**2) - (c**2)) ) / (2 * (a-c)) # divides by 0 if a-c = 0 (points have the same x value), so the correct x value would be the same as well
		return float("%.10f" % x)
	except ZeroDivisionError:
		print(f"division by zero in xAtY with {pt1} {pt2} y={y}")
		return pt1[0]

def tAtXandY(pt1, x, y):
	a, b = pt1[0], pt1[1]
	#t = ((2 * y) + (( (4 * (y**2)) + 4*( ((x-a)**2) - (2 * y * b) + (b**2 ) ) ) ** 0.5)) / 2
	k = -2 * y
	l = -1 * ( ( (x-a) ** 2 ) - (2 * y * b) + (b ** 2) )
	t = ( (-1 * k) + ( ( (k ** 2) - (4 * l) ) ** 0.5 ) ) / 2

	return float("%.10f" % t)

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


# Seems to always do case3 for some reason
def pointSlope(pt, slope, x):
	match slope:
		case None:
			#print("case1")
			return None
		case 0:
			#print("case2")
			return pt[1]
		case _:
			#print("case3")
			return float("%.10f" % ((slope * (x - pt[0])) + pt[1]) )
		
	#return float("%.10f" % ((slope * (x - pt[0])) + pt[1]) )

def pointSlopeX(pt, slope, y): # This hasn't errored for some reason
	match slope:
		case None:
			#print("case1")
			return None
		case 0:
			#print("case2")
			return pt[1]
		case _:
			#print("case3")
			return float("%.10f" % ( (y - pt[1] + (slope * pt[0])) / slope) )
	#return float("%.10f" % ( (y - pt[1] + (slope * pt[0])) / slope) )

def nearestBoundry(startPt, throughPt):

	if startPt[1] == throughPt[1]: # Horizontal line
		if throughPt[0] > startPt[0]:
			return [defaultBounds[0][1], startPt[1]]
		else: # If throughPt[0] < startPt[0]
			return [defaultBounds[0][0], startPt[1]]
		
	elif startPt[0] == throughPt[0]: # Vertical line
		if throughPt[1] > startPt[1]:
			return [startPt[0], defaultBounds[1][0]]
		else: # If throughPt[1] < startPt[1]
			return [startPt[0], defaultBounds[1][1]]
		
	else:
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

		#else: # throughPt and startPt have the same y. This will never be considered now
		#	choice = [[defaultBounds[0][0], throughPt[1]], [defaultBounds[0][1], throughPt[1]]]
	
		distanceTargetSort(startPt, choice)
	
		return choice[0]

def nearestOutsideBoundry(startPt, throughPt):
	
	# if startPt[1] == throughPt[1]:
	# 	dist1 = abs(startPt[0] - defaultBounds[0][0])
	# 	dist2 = abs(startPt[0] - defaultBounds[0][1])

	# 	if dist1 < dist2:
	# 		return [defaultBounds[0][0], startPt[1]]
	# 	else:
	# 		return [defaultBounds[0][1], startPt[1]]
		
	# elif startPt[0] == throughPt[0]:
	# 	dist1 = abs(startPt[1] - defaultBounds[1][0])
	# 	dist2 = abs(startPt[1] - defaultBounds[1][1])

	# 	if dist1 < dist2:
	# 		return [startPt[0], defaultBounds[1][0]]
	# 	else:
	# 		return [startPt[0], defaultBounds[1][1]]
		
	# else:
	
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
		# if (pt1[1] - pt2[1]) / (pt1[0] - pt2[0]) == 0: # Just having 'pt1[0] - pt2[0] == 0' doesn't work as it allows for a slope of 0
		# 	if pt1[1] - pt2[1] < 0: # Parts of my code can not handle a slope of 0, so this is here to make it almost 0
		# 		return -0.0000001 # This is kinda arbitrary
		# 	else:
		# 		return 0.0000001
		# else:
		# 	return (pt1[1] - pt2[1]) / (pt1[0] - pt2[0])
		return (pt1[1] - pt2[1]) / (pt1[0] - pt2[0])
	except ZeroDivisionError: 
		print(f"zero division error in slope with {pt1} {pt2}")
		# if pt1[1] - pt2[1] < 0: # This is diffrent from the above since here the two points have the same x-value, so one is right above the other and the slope needs to be extremely big
		# 	return -100000
		# else:
		# 	return 100000
		return None

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

def toKey(point):
	return f"{str(point).replace(', ', '_')}"

def fromKey(key):
	result = key.replace("[", "").replace("]", "").split("_")#key.replace("[", "").replace("]", "").split("_")
	#result = [float(result[0]), float(result[1])]
	#result = [float("%.10f" % result[0]), float("%.10f" % result[1])]
	#print("lin524", result)
	#print("." in key)
	
	if "." in key:
		result = [float(result[0]), float(result[1])]
		result = [float("%.10f" % result[0]), float("%.10f" % result[1])]
	else:
		result = [int(result[0]), int(result[1])]

	

	return result

def sort2ByY(pair):
	if pair[0][1] > pair[1][1]:
		pair[0], pair[1] = pair[1], pair[0]

def scanSortByX(array):
	
	for i in range(0, array.__len__()):
		#print("line544",array[i])
		if array[i][0][1] == array[i][1][1] and array[i][0][0] > array[i][1][0]:
			#print("line545",array[i])
			array[i][0], array[i][1] = array[i][1], array[i][0]
			#print("line547",array)

def scanSort2ByX(array):
	if array[0][1] == array[1][1] and array[0][0] > array[1][0]:
		array[0], array[1] = array[1], array[0]

def scanSortByXSwap(focus, other):
	
	for i in range(0, focus.__len__()):
		#print("line557",focus[i])
		if focus[i][0][1] == focus[i][1][1] and focus[i][0][0] > focus[i][1][0]:
			#print("line559",focus[i])
			focus[i][0], focus[i][1] = focus[i][1], focus[i][0]
			other[i], other[i+1] = other[i+1], other[i]
			#print("line562",focus[i])
			

sortByY(points)
#scanSortByX(points) # not sure if sorting by x here helps anything
print(points)

# These two loops try to ensure that there are no points with the same y-value,
# could probably just do the random.random() to avoid having two loops, if that was necessary
# for i in range(0, points.__len__() -1):
# 	if points[i][1] == points[i + 1][1]:
# 		points[i + 1][1] += 1
# sortByY(points)
# for i in range(0, points.__len__() -1):
# 	if points[i][1] == points[i + 1][1]:
# 		points[i + 1][1] += random.random()



tmp = []
for point in points:   
	finalCell.update({f"{str(point).replace(', ', '_')}" : {"site":point, "vertices":[]}})
	tmp.extend(point)

print(tmp) # this tmp is never used after this, it just used to print the points in a different format here
print()
#print(finalCell.keys())
# Finds intersection points of sites, including some that are invalid
for site1 in points:
	for site2 in points:
		if site1 != site2:
			for site3 in points:
				if site3 != site2 and site3 != site1:
					site1Key = f"{str(site1).replace(', ', '_')}"
					sites = [site1, site2, site3]
					sortByY(sites)

					x = find3IntersectX(sites[0], sites[1], sites[2])
					#print("line458",x)
					if x != None: # x is None if the lines are parallel, which will be handled later
						#print(sites)
						t = getTimeAtX(sites[0], sites[1], sites[2], x)

						if t != None: # t is None if at least two of the sites have the same y-value
						
							y = getYAtTimeAndX(sites[0], t, x)

							#if site1 == [24, 167]:
							#	print("---",x,y,t)
					
							if y != None: # y is None if t is equal to the y-value of the point

								# bufferBounds just increases the bounds of the selected area by a certain amount so that intersection points can happen within it and are not outright rejected
								#	but need to be accounted for seperately and fixed
								# The size of bufferWidth and bufferHeight are kind of arbitrary, I just went with 1/4 of the their respective dimension
								bufferWidth = (defaultBounds[0][0] + defaultBounds[0][1])/4 # the midpoint divided by 2
								bufferHeight = (defaultBounds[1][1] + defaultBounds[1][0])/4
								bufferBounds = [[defaultBounds[0][0] - bufferWidth, defaultBounds[0][1] + bufferHeight], [defaultBounds[1][0] + bufferHeight, defaultBounds[1][1] - bufferHeight]]
					
								if t > site1[1] and t > site2[1] and t > site3[1] and withinBounds([x, y], bufferBounds):
									#site1Key = f"{str(site1).replace(', ', '_')}"

									# if site1Key in cell:
									# 	# Prevents duplicates (duplicates don't break anything, just makes stuff slower (probably))
									# 	test1 = {"point1":site1, "point2":site2, "point3":site3, "time":float("%.10f" % t), "at":[float("%.10f" % x), float("%.10f" % y)]}
									# 	test2 = {"point1":site1, "point2":site3, "point3":site2, "time":float("%.10f" % t), "at":[float("%.10f" % x), float("%.10f" % y)]}
									# 	if test1 not in cell[site1Key] and test2 not in cell[site1Key]:
									# 		cell[site1Key].append({"point1":site1, "point2":site2, "point3":site3, "time":float("%.10f" % t), "at":[float("%.10f" % x), float("%.10f" % y)]})
									# else:
									# 	cell.update({site1Key : [{"point1":site1, "point2":site2, "point3":site3, "time":float("%.10f" % t), "at":[float("%.10f" % x), float("%.10f" % y)]}]})
							
									# if f"{str(site1).replace(', ', '_')}" in cell:
									# 	cell[f"{str(site1).replace(', ', '_')}"].append({"point1":site1, "point2":site2, "point3":site3, "time":float("%.10f" % t), "at":[float("%.10f" % x), float("%.10f" % y)]})
									# else:
									# 	cell.update({f"{str(site1).replace(', ', '_')}" : [{"point1":site1, "point2":site2, "point3":site3, "time":float("%.10f" % t), "at":[float("%.10f" % x), float("%.10f" % y)]}]})
	
									# For some reason trying to prevent duplicates causes things to break
									# if site1Key in cell:
									# 	cell[site1Key].append({"point1":site1, "point2":site2, "point3":site3, "time":float("%.10f" % t), "at":[float("%.10f" % x), float("%.10f" % y)]})
									# else:
									# 	cell.update({site1Key : [{"point1":site1, "point2":site2, "point3":site3, "time":float("%.10f" % t), "at":[float("%.10f" % x), float("%.10f" % y)]}]})
									# if site1Key in cell:
									# 	#print({"point1":sites[0], "point2":sites[1], "point3":sites[2], "time":float("%.10f" % t), "at":[float("%.10f" % x), float("%.10f" % y)]} in cell[site1Key])
									# 	if {"point1":sites[0], "point2":sites[1], "point3":sites[2], "time":float("%.10f" % t), "at":[float("%.10f" % x), float("%.10f" % y)]} not in cell[site1Key]:
									# 		cell[site1Key].append({"point1":sites[0], "point2":sites[1], "point3":sites[2], "time":float("%.10f" % t), "at":[float("%.10f" % x), float("%.10f" % y)]})
									# else:
									# 	cell.update({site1Key : [{"point1":sites[0], "point2":sites[1], "point3":sites[2], "time":float("%.10f" % t), "at":[float("%.10f" % x), float("%.10f" % y)]}]})

									sites.remove(site1)
									scanSort2ByX(sites)
									
									if site1Key in cell:
										#print({"point1":sites[0], "point2":sites[1], "point3":sites[2], "time":float("%.10f" % t), "at":[float("%.10f" % x), float("%.10f" % y)]} in cell[site1Key])
										
										if {"sites":[site1, sites[0], sites[1]], "time":float("%.10f" % t), "at":[float("%.10f" % x), float("%.10f" % y)]} not in cell[site1Key]:
											cell[site1Key].append({"sites":[site1, sites[0], sites[1]], "time":float("%.10f" % t), "at":[float("%.10f" % x), float("%.10f" % y)]})
									else:
										cell.update({site1Key : [{"sites":[site1, sites[0], sites[1]], "time":float("%.10f" % t), "at":[float("%.10f" % x), float("%.10f" % y)]}]})
										
						else:
							y = yAtX(sites[0], sites[2], x)
							t = tAtXandY(sites[0], x, y)
							#print("line677",x,y,t)

							# bufferBounds just increases the bounds of the selected area by a certain amount so that intersection points can happen within it and are not outright rejected
							#	but need to be accounted for seperately and fixed
							# The size of bufferWidth and bufferHeight are kind of arbitrary, I just went with 1/4 of the their respective dimension
							bufferWidth = (defaultBounds[0][0] + defaultBounds[0][1])/4 # the midpoint divided by 2
							bufferHeight = (defaultBounds[1][1] + defaultBounds[1][0])/4
							bufferBounds = [[defaultBounds[0][0] - bufferWidth, defaultBounds[0][1] + bufferHeight], [defaultBounds[1][0] + bufferHeight, defaultBounds[1][1] - bufferHeight]]
					
							# This is >= instead of > since if the 3rd site is exactly at the x-value of the intersection point and the y-values of the other two sites are equal,
							#	then a t-value equal to the y-value of the higest site is valid
							if t >= site1[1] and t >= site2[1] and t >= site3[1] and withinBounds([x, y], bufferBounds):
								#site1Key = f"{str(site1).replace(', ', '_')}"
	
								# For some reason trying to prevent duplicates causes things to break
								# if site1Key in cell:
								# 	if {"point1":sites[0], "point2":sites[1], "point3":sites[2], "time":float("%.10f" % t), "at":[float("%.10f" % x), float("%.10f" % y)]} not in cell[site1Key]:
								# 		cell[site1Key].append({"point1":sites[0], "point2":sites[1], "point3":sites[2], "time":float("%.10f" % t), "at":[float("%.10f" % x), float("%.10f" % y)]})
								# 	#cell[site1Key].append({"point1":sites[0], "point2":sites[1], "point3":sites[2], "time":float("%.10f" % t), "at":[float("%.10f" % x), float("%.10f" % y)]})
								# else:
								# 	cell.update({site1Key : [{"point1":sites[0], "point2":sites[1], "point3":sites[2], "time":float("%.10f" % t), "at":[float("%.10f" % x), float("%.10f" % y)]}]})

								sites.remove(site1)
								scanSort2ByX(sites)
									
								if site1Key in cell:
									#print({"point1":sites[0], "point2":sites[1], "point3":sites[2], "time":float("%.10f" % t), "at":[float("%.10f" % x), float("%.10f" % y)]} in cell[site1Key])
										
									if {"sites":[site1, sites[0], sites[1]], "time":float("%.10f" % t), "at":[float("%.10f" % x), float("%.10f" % y)]} not in cell[site1Key]:
										cell[site1Key].append({"sites":[site1, sites[0], sites[1]], "time":float("%.10f" % t), "at":[float("%.10f" % x), float("%.10f" % y)]})
								else:
									cell.update({site1Key : [{"sites":[site1, sites[0], sites[1]], "time":float("%.10f" % t), "at":[float("%.10f" % x), float("%.10f" % y)]}]})
										
print("Deleting invalid cell vertices...")
for others in points:
	
	for site1 in cell:
		removeVerts = []
		for entry in cell[site1]:
			#if entry["point1"] != others and entry["point2"] != others and entry["point3"] != others and others[1] < entry["time"]:
			if others not in entry["sites"] and others[1] < entry["time"]:
				otherPointY = getYAtTimeAndX(others, entry["time"], entry["at"][0])
				
				if otherPointY > entry["at"][1]:
					#plt.plot(entry["at"][0], entry["at"][1], "yo")
					#plt.plot([entry["point2"][0], entry["at"][0], entry["point3"][0], entry["at"][0], entry["point1"][0]], [entry["point2"][1], entry["at"][1], entry["point3"][1], entry["at"][1], entry["point1"][1]], "y")
					removeVerts.append(entry)
		#print(site1, removeVerts)
		for rmv in removeVerts:
			try:
				del cell[site1][cell[site1].index(rmv)]
			except Exception:
				pass

# for tmp in cell:
# 	for tmp2 in cell[tmp]:
# 		print(tmp, "-", tmp2)

#print(cell["[16_0]"])
#print(finalCell["[20_4]"]["vertices"])
# There are 3 cases that have to be dealth with seperately: 1 site, 3 sites, and 2 or 3+ sites 
# (technically 2 sites have to be dealt with seperately but are the same as having a cell in a corner so can be dealt with later)
if points.__len__() == 3 and cell.keys().__len__() != 0:
	kys = list(cell.keys())
	#print("line503",kys)
	#if kys.__len__() != 0: # This check is redundant now
	current = cell[kys[0]][0]
	#print(cell)
	#print("line646",kys[0])
		
	vert = f"{str(current['at']).replace(', ', '_')}"
	#print(vert)
	sites = current["sites"]#[current["point1"], current["point2"], current["point3"]]
	distanceTargetSort(fromKey(kys[0]), sites)
		
	#bound = nearestBoundry(current["at"], midPoint(current["point1"], current["point2"]))
	bound = nearestBoundry(current["at"], midPoint(sites[0], sites[1]))
	#midPt = midPoint(current["point1"], current["point2"])
	#bound = nearestBoundry(current["at"], midPt)
	#print(current["point1"], current["point2"], midPoint(current["point1"], current["point2"]))
	#print("bound",bound)
	#plt.plot(midPt[0], midPt[1], "yo")
	#plt.plot([current["point1"][0], current["point2"][0]], [current["point1"][1], current["point2"][1]], "y")
	
	#vertices[vert] = {"sites":[current["point1"], current["point2"], current["point3"]], "with":[[current["point1"], current["point2"]]], "at":[bound]}
	#vertices[vert] = {"sites":[current["point1"], current["point2"], current["point3"]], "with":[[sites[0], sites[1]]], "at":[bound]}
	#vertices[vert] = {"sites":current["sites"], "with":[[sites[0], sites[1]]], "at":[bound]}	
	#finalCell[kys[0]]["vertices"].append([current["at"], bound])
	#finalCell[kys[1]]["vertices"].append([current["at"], bound])

	vertices[vert] = {"sites":current["sites"], "at":current["at"], "with":[[sites[0], sites[1]]], "to":[bound]}
	edgePair = [current["at"], bound]
	sort2ByY(edgePair)
	scanSort2ByX(edgePair)
	finalCell[kys[0]]["vertices"].append(edgePair)
	finalCell[kys[1]]["vertices"].append(edgePair)
		
	# else: # This isn't necessary, other parts handle 2 parallel lines correctly
	# 	site1 = points[0]
	# 	site2 = points[1]
	# 	site3 = points[2]
		
	# 	site1Key = f"{str(site1).replace(', ', '_')}"
	# 	site2Key = f"{str(site2).replace(', ', '_')}"
	# 	site3Key = f"{str(site3).replace(', ', '_')}"

	# 	slp = -1/slope(site1, site2)
	# 	midPt1 = midPoint(site1, site2)
	# 	midPt2 = midPoint(site2, site3)

	# 	ptSlope1y = pointSlope(midPt1, slp, midPt1[0] + 0.5)
	# 	ptSlope2y = pointSlope(midPt1, slp, midPt1[0] - 0.5)
	# 	ptSlope3y = pointSlope(midPt2, slp, midPt2[0] + 0.5)
	# 	ptSlope4y = pointSlope(midPt2, slp, midPt2[0] - 0.5)

	# 	bound1 = nearestBoundry(midPt1, [midPt1[0] + 0.5, ptSlope1y])
	# 	bound2 = nearestBoundry(midPt1, [midPt1[0] - 0.5, ptSlope2y])
	# 	bound3 = nearestBoundry(midPt2, [midPt2[0] + 0.5, ptSlope3y])
	# 	bound4 = nearestBoundry(midPt2, [midPt2[0] - 0.5, ptSlope4y])

	# 	finalCell[site1Key]["vertices"].append([bound1, bound2])
	# 	finalCell[site2Key]["vertices"].append([bound1, bound2])
	# 	finalCell[site2Key]["vertices"].append([bound3, bound4])
	# 	finalCell[site3Key]["vertices"].append([bound3, bound4])

 # Trying to handle 1 site here will cause the boundry edge finding section to duplicate two sides, 
#	and not handling this here breaks nothing, so it is handled after everything else	
elif points.__len__() == 1:
	pass
else:
	# Deals with cases where lines are parallel or have no intersection point within the buffer but are still valid
	# usedSites = []
	# for entry in cell:
	# 	for vert in cell[entry]:
	# 		# if vert["point1"] not in usedSites:
	# 		# 	usedSites.append(vert["point1"])
	# 		# if vert["point2"] not in usedSites:
	# 		# 	usedSites.append(vert["point2"])
	# 		# if vert["point3"] not in usedSites:
	# 		# 	usedSites.append(vert["point3"])
	# 		if vert["sites"][0] not in usedSites:
	# 			usedSites.append(vert["sites"][0])
	# 		if vert["sites"][1] not in usedSites:
	# 			usedSites.append(vert["sites"][1])
	# 		if vert["sites"][2] not in usedSites:
	# 			usedSites.append(vert["sites"][2])

	for site in points:

		#test1 = False
		#test2 = False
		#test3 = False

		test = False
		
		# if site not in usedSites:
		# 	#test1 = True
		# 	test = True
		# elif cell[toKey(site)].__len__() == 1:
		# 	if not withinBounds(cell[toKey(site)][0]["at"], defaultBounds):
		# 		#test2 = True
		# 		test = True
		# elif cell[toKey(site)].__len__() == 2:
		# 	if not withinBounds(cell[toKey(site)][0]["at"], defaultBounds) and not withinBounds(cell[toKey(site)][1]["at"], defaultBounds):
		# 		test = True
		#print(usedSites)
		#print(cell)
		if cell.__len__() == 0:
			test = True
		elif cell[toKey(site)].__len__() == 0:
			test = True
		elif cell[toKey(site)].__len__() == 1:
			if not withinBounds(cell[toKey(site)][0]["at"], defaultBounds):
				test = True
		elif cell[toKey(site)].__len__() == 2:
			if not withinBounds(cell[toKey(site)][0]["at"], defaultBounds) and not withinBounds(cell[toKey(site)][1]["at"], defaultBounds):
				test = True
		

		#test1 = site not in usedSites
		#test2 = cell[toKey(site)].__len__() == 1 and not withinBounds(cell[toKey(site)][0]["at"], defaultBounds)
		#test3 = cell[toKey(site)].__len__() == 2 and not withinBounds(cell[toKey(site)][0]["at"], defaultBounds) and not withinBounds(cell[toKey(site)][1]["at"], defaultBounds)
		#if site not in usedSites:
		if test == True:
			#print("line798", site)
			points2 = points.copy()
			distanceTargetSort(site, points2)

			nearest = []
			boundPair = []
			bound1 = []
			bound2 = []

			if points2[0] == site:
				nearest = points2[1]
			else:
				nearest = points2[0]

			midPt = midPoint(site, nearest)
			#diff = distancePt(site, midPt)/2
			diff = 0.5

			if site[1] == nearest[1]:
				bound1 = nearestBoundry(midPt, [midPt[0], midPt[1] + diff])
				bound2 = nearestBoundry(midPt, [midPt[0], midPt[1] - diff])
			elif site[0] == nearest[0]:
				bound1 = nearestBoundry(midPt, [midPt[0] + diff, midPt[1]])
				bound2 = nearestBoundry(midPt, [midPt[0] - diff, midPt[1]])
			else:
			
				leftY = yAtX(site, nearest, midPt[0] - diff)
				rightY = yAtX(site, nearest, midPt[0] + diff)

				#leftBound = nearestBoundry(midPt, [midPt[0] - 0.5, leftY])
				#rightBound = nearestBoundry(midPt, [midPt[0] + 0.5, rightY])

				#boundPair = [leftBound, rightBound]
				#sortByY(boundPair)

				bound1 = nearestBoundry(midPt, [midPt[0] - diff, leftY])
				bound2 = nearestBoundry(midPt, [midPt[0] + diff, rightY])

			boundPair = [bound1, bound2]
			#print("line863",boundPair)
			sort2ByY(boundPair)
			#print("line865",boundPair)
			scanSort2ByX(boundPair)
			print("line873", site, boundPair)

			siteKey = f"{str(site).replace(', ', '_')}"
			nearestKey = f"{str(nearest).replace(', ', '_')}"
			
			if boundPair not in finalCell[siteKey]["vertices"]:
				finalCell[siteKey]["vertices"].append(boundPair)

			if boundPair not in finalCell[nearestKey]["vertices"]:
				finalCell[nearestKey]["vertices"].append(boundPair)
			#finalCell[f"{str(nearest).replace(', ', '_')}"]["vertices"].append(boundPair)
#print(finalCell["[20_4]"]["vertices"])
#for tmp in cell.keys():
#	print(tmp, "-", cell[tmp])



	
usedSitePairs = []
for site1Key in cell:
	# Could probably optimize this so that it doesn't search the same point multiple times
	#print("site1Key",site1Key)
	for entry1 in cell[site1Key]:
		entryPts = entry1["sites"].copy()#[entry1["point1"], entry1["point2"], entry1["point3"]]
		#print(entry1)
		site1 = fromKey(site1Key)
		site2 = entryPts[1]
		site2Key = toKey(site2)
		#print("site1key",site1Key)
		#print(entryPts)
		#print(site2Key)
		# if entry1["point2"] != site1:
		# 	site2 = entry1['point2']
		# else:
		# 	site2 = entry1['point1']

		#site2Key = toKey(site2)
		#print("site2Key",site2Key)
		#for entry2 in site2:

		checkPair = [site1, site2]
		sort2ByY(checkPair)
		scanSort2ByX(checkPair)

		if checkPair not in usedSitePairs:
			for entry2 in cell[site2Key]:

				entry2Pts = entry2["sites"].copy() # Since all lists in Python are passed by reference, this is required as to not mess up entry2["sites"]
			
				if site1 in entry2Pts and entry1["at"] != entry2["at"]:
					edgePair = [entry1["at"], entry2["at"]]
					sort2ByY(edgePair)
					scanSort2ByX(edgePair)
					
					if edgePair not in finalCell[site1Key]["vertices"]: # For some reason this loop gets to this check many fewer times than the other loop

						finalCell[site1Key]["vertices"].append(edgePair)

						if edgePair not in finalCell[site2Key]["vertices"]:
							finalCell[site2Key]["vertices"].append(edgePair)

						sitePair = [site1, site2]
						sort2ByY(sitePair)
						scanSort2ByX(sitePair)
						usedSitePairs.append(sitePair)

						vert1 = f"{str(entry1['at']).replace(', ', '_')}"
						if vert1 not in vertices:
							tempSites = entryPts
							sortByY(tempSites)
							#scanScortByX(tempSites)
							vertices.update({vert1 : {"sites":tempSites, "at":entry1['at'], "with":[], "to":[]}})
					
							vertices[vert1]["with"].append(sitePair)
							vertices[vert1]["to"].append(entry2["at"])
						elif entry2["at"] not in vertices[vert1]["to"]:
							vertices[vert1]["with"].append(sitePair)
							vertices[vert1]["to"].append(entry2["at"])
							

						vert2 = f"{str(entry2['at']).replace(', ', '_')}"
						if vert2 not in vertices:
							tempsites = entry2Pts
							sortByY(tempsites)
							#scanScortByX(tempSites)
							vertices.update({vert2 : {"sites":tempsites, "at":entry2['at'], "with":[], "to":[]}})
						
						vertices[vert2]["with"].append(sitePair)
						vertices[vert2]["to"].append(entry1["at"])

						break # Since there can only ever be 1 edge between two given sites, can just break the loop once one is found

		site3 = entryPts[2]
		site3Key = toKey(site3)

		checkPair = [site1, site3]
		sort2ByY(checkPair)
		scanSort2ByX(checkPair)
		
		if checkPair not in usedSitePairs:
			for entry3 in cell[site3Key]:
				entry3Pts = entry3["sites"].copy()
			
				if site1 in entry3Pts and entry1["at"] != entry3["at"]:
					edgePair = [entry1["at"], entry3["at"]]
					sort2ByY(edgePair)
					scanSort2ByX(edgePair)

					if edgePair not in finalCell[site1Key]["vertices"]:
					
						finalCell[site1Key]["vertices"].append(edgePair)

						if edgePair not in finalCell[site3Key]["vertices"]:
							finalCell[site3Key]["vertices"].append(edgePair)
						
						sitePair = [site1, site3]
						sort2ByY(sitePair)
						scanSort2ByX(sitePair)
						
						usedSitePairs.append(sitePair)
						#print("sitePair2",sitePair)
						vert3 = f"{str(entry1['at']).replace(', ', '_')}"
						if vert3 not in vertices:
							tempSites = entryPts
							sortByY(tempSites)
							#scanScortByX(tempSites)
							vertices.update({vert3 : {"sites":tempSites, "at":entry1['at'], "with":[], "to":[]}})
					
							vertices[vert3]["with"].append(sitePair)
							vertices[vert3]["to"].append(entry3["at"])
						elif entry3["at"] not in vertices[vert3]["to"]:
							vertices[vert3]["with"].append(sitePair)
							vertices[vert3]["to"].append(entry3["at"])

						vert4 = f"{str(entry3['at']).replace(', ', '_')}"
						if vert4 not in vertices:
							tempSites = entry3Pts
							sortByY(tempSites)
							#scanScortByX(tempSites)
							vertices.update({vert4 : {"sites":tempSites, "at":entry3['at'], "with":[], "to":[]}})
					
						vertices[vert4]["with"].append(sitePair)
						vertices[vert4]["to"].append(entry1["at"])

						break
#print(vertices)
#for vert1 in vertices: # I don't know if this is more efficient than sorting the vertices by x within the loop that they are created
#	scanSortByXSwap(vertices[vert1]["with"], vertices[vert1]["to"])


# Splits vertices that are outside of bounds into two vertices that are at the boundries
removeVerts = []
for vert1 in vertices:
	vertPt = vertices[vert1]["at"]
	#print("line1093",vertPt)
	if not withinBounds(vertPt, defaultBounds):
		for other in vertices[vert1]["to"]:
			if toKey(other) in vertices: # If it is not in 'vertices', then 'other' is a boundry vertice
				
				otherVert = vertices[toKey(other)]
				i = otherVert["to"].index(vertPt)
				otherWith = otherVert["with"][i]
				
				originalPair = [otherVert["at"], otherVert["to"][i]]
				sort2ByY(originalPair)
				scanSort2ByX(originalPair)
				
				if withinBounds(otherVert["at"], defaultBounds):

					bound = nearestBoundry(otherVert["at"], vertPt)
					
					otherVert["to"][i] = bound

					newPair = [otherVert["at"], bound]
					sort2ByY(newPair)
					scanSort2ByX(newPair)

					j = finalCell[toKey(otherWith[0])]["vertices"].index(originalPair)
					finalCell[toKey(otherWith[0])]["vertices"][j] = newPair

					j = finalCell[toKey(otherWith[1])]["vertices"].index(originalPair)
					finalCell[toKey(otherWith[1])]["vertices"][j] = newPair

				else: # This happens if there are two intersection points outside of bounds and one is connected to the other
					#print(otherVert["at"], "not within bounds")
					cell1 = finalCell[toKey(otherWith[0])]["vertices"]
					cell2 = finalCell[toKey(otherWith[1])]["vertices"]

					if originalPair in cell1:
						cell1.remove(originalPair)
					if originalPair in cell2:
						cell2.remove(originalPair)

		removeVerts.append(vert1)

for rmv in removeVerts:
	del vertices[rmv]

# This works, but it might be better to try to remove the edges where both vertices are outside of bounds in the previous loop
# for siteKey in finalCell:
# 	removeVerts = []
# 	for vertice in finalCell[siteKey]["vertices"]:
# 		if not withinBounds(vertice[0], defaultBounds) or not withinBounds(vertice[1], defaultBounds):
# 			removeVerts.append(vertice)

# 	for rmv in removeVerts:
# 		finalCell[siteKey]["vertices"].remove(rmv)

# Creates a vertex in cases where there there is only one intersection vertex and no other vertices are registered
#	This happens with [[7, 34], [87, 254], [91, 265], [86, 16]] but not [[50, 50], [25, 25], [75, 75], [98, 70]] because it has an intersection within the buffer zone
#	Also happens with [[25, 25], [12, 173], [22, 199], [23, 199]]
if vertices.__len__() == 0:
	print("vertices has 0 elements")
	#print(cell.keys())
	kys = list(cell.keys())
	i = 0
	while True:

		if i >= kys.__len__():
			break
		
		if cell[kys[i]].__len__() != 0:
			current = cell[kys[i]][0]
			
			pt1, pt2, pt3 = current["sites"]#current["point1"], current["point2"], current["point3"]
			print("line924",pt1, pt2, pt3)
			vert = f"{str(current['at']).replace(', ', '_')}"
			
			tempSites = [pt1, pt2, pt3]
			sortByY(tempSites)
			
			vertices.update({vert : {"sites":tempSites, "at":current["at"], "with":[], "to":[]}})

			tempSites = [tempSites[0], tempSites[1]]
			scanSort2ByX(tempSites)

			throughPt = midPoint(tempSites[0], tempSites[1])

			bound = nearestBoundry(current['at'], throughPt)

			vertices[vert]["with"].append([tempSites[0], tempSites[1]])
			vertices[vert]["to"].append(bound)
			
			tempEdge = [current['at'], bound]
			sort2ByY(tempEdge)
			scanSort2ByX(tempEdge)

			finalCell[f"{str(tempSites[0]).replace(', ', '_')}"]["vertices"].append(tempEdge)
			finalCell[f"{str(tempSites[1]).replace(', ', '_')}"]["vertices"].append(tempEdge)

			#print(vertices[vert])
			break
		i += 1



# Modifies convex hull so that it has edges extending to the boundries of the specified area
for vert in vertices: 
	#tempVertPt = str(vert).removeprefix("[").removesuffix("]").split("_")
	#vertPt = [float(tempVertPt[0]), float(tempVertPt[1])]
	vertPt = vertices[vert]["at"]
	
	if vertices[vert]["to"].__len__() == 1:

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
			boundryPair = [vertPt, nearestBound]
			sort2ByY(boundryPair)
			scanSort2ByX(boundryPair)

			sort2ByY(pickedSites)
			scanSort2ByX(pickedSites)

			#print("line1123",pickedSites)

			#vertices[vert]["with"].append([pickedSites[0], pickedSites[1]])
			vertices[vert]["with"].append(pickedSites)
			vertices[vert]["to"].append(nearestBound)
			#finalCell[f"{str(pickedSites[0]).replace(', ', '_')}"]["vertices"].append([vertPt, nearestBound])
			#finalCell[f"{str(pickedSites[1]).replace(', ', '_')}"]["vertices"].append([vertPt, nearestBound])
			finalCell[f"{str(pickedSites[0]).replace(', ', '_')}"]["vertices"].append(boundryPair)
			finalCell[f"{str(pickedSites[1]).replace(', ', '_')}"]["vertices"].append(boundryPair)
		

	if vertices[vert]["to"].__len__() == 2:
		
		site1 = vertices[vert]["sites"][0]
		site2 = vertices[vert]["sites"][1]
		site3 = vertices[vert]["sites"][2]

		vertPtT = tAtXandY(site1, vertPt[0], vertPt[1])

		pickedSites = [[site1, site2], [site1, site3], [site2, site3]]
		
		#withVerts = vertices[vert]["with"].copy()
		#scanSortByX(withVerts)
		scanSortByX(pickedSites)
		#print("picked",pickedSites)
		print("--------",vertPt)
		print(vertices[vert]["with"])
		print(vertices[vert])
		print(pickedSites)
		pickedSites.remove(vertices[vert]["with"][0])
		pickedSites.remove(vertices[vert]["with"][1])
		#pickedSites.remove(withVerts[0])
		#pickedSites.remove(withVerts[1])
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
			# The points aren't added to the 'vertices' dictionary since it is not used after this part of this function, so there is point to
			nearestBound = nearestBoundry(vertPt, throughPt)
			finalCell[f"{str(pickedSites[0]).replace(', ', '_')}"]["vertices"].append([vertPt, nearestBound])
			finalCell[f"{str(pickedSites[1]).replace(', ', '_')}"]["vertices"].append([vertPt, nearestBound])


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
			# I'm not handling the case where the intersection point is on the boundry since that is extremely unlikely to happen naturally
			#if onBoundry.__len__() % 2 == 0: # might be redundant, not sure if it is possible for a site to have more than 2 boundry edges
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

# If there is only one point, then the whole area is one cell
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

for site in cell:  
	for entry in cell[site]:
        
		plt.plot(entry["at"][0], entry["at"][1], "go")

		#plt.plot([entry["point2"][0], entry["at"][0], entry["point3"][0], entry["at"][0], entry["point1"][0]], [entry["point2"][1], entry["at"][1], entry["point3"][1], entry["at"][1], entry["point1"][1]], "g") 
		plt.plot([entry["sites"][1][0], entry["at"][0], entry["sites"][2][0], entry["at"][0], entry["sites"][0][0]], [entry["sites"][1][1], entry["at"][1], entry["sites"][2][1], entry["at"][1], entry["sites"][0][1]], "g") 

for vert3key in vertices:
	vert3 = vertices[vert3key]
	
	plt.plot([vert3["sites"][0][0], vert3["at"][0], vert3["sites"][1][0], vert3["at"][0], vert3["sites"][2][0]], [vert3["sites"][0][1], vert3["at"][1], vert3["sites"][1][1], vert3["at"][1], vert3["sites"][2][1]], "y")

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
	curSite = finalCell[cell]["site"]
	for i in range(0, temp.__len__()):
		temp2.append([temp[i], normalTheta(temp[i],curSite)])
		
	sortByY(temp2)

	vertsX = []
	vertsY = []	

	for point in temp2:
		vertsX.append(point[0][0])
		vertsY.append(point[0][1])

	def clamp(n, lower, upper):
		return max(lower, min(n, upper))
	
	#plt.fill(vertsX, vertsY, color=(random.random(), random.random(), random.random(), 0.5))
	plt.fill(vertsX, vertsY, color=(clamp(random.random(), 0.1, 0.8), clamp(random.random(), 0.1, 0.8), clamp(random.random(), 0.1, 0.8), 0.5))
		
plt.show()

