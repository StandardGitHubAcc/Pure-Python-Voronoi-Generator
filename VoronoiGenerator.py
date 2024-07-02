from ast import NotIn
from decimal import DivisionByZero
#from re import S
import matplotlib.pyplot as plt
import random
import math
from math import *

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
#points = [[13, 23], [181, 40], [129, 55], [93, 100], [59, 127], [12, 160], [156, 163]] #---
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

points = [[59, 65], [194, 108], [134, 152], [147, 155], [75, 166], [64, 172], [180, 195]]

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
                
def find3IntersectX(pt1, pt2, pt3): # division by zero happens with the points (50, 50) (25, 25) (75, 75) # finds x-value of intersection of 3 parabolas
    a, b, c, d, e, f = pt1[0], pt1[1], pt2[0], pt2[1], pt3[0], pt3[1]
    if (2 * ( ((a-e)*(b-d)) - ((a-c)*(b-f))) ) != 0:
        x = ( ( ((a**2) - (e**2))*(b-d) ) - ( ((a**2) - (c**2)) * (b-f) ) - ( (d-f)*(b-f)*(b-d) )) / (2 * ( ((a-e)*(b-d)) - ((a-c)*(b-f))) )
        #print("a",x)        
        return x
    else: # i need to have it return the midpoint between the site and nearest site if there is division by zero, because that means that the two lines are parallel and the farther site will not be valid
        #print(( ( ((a**2) - (e**2))*(b-d) ) - ( ((a**2) - (c**2)) * (b-f) ) - ( (d-f)*(b-f)*(b-d) )), (2 * ( ((a-e)*(b-d)) - ((a-c)*(b-f))) ))
        #print(f"({a}, {b}) ({c}, {d}) ({e}, {f})")
        #print(a-e, b-d, a-c, b-f)
        #print("b",(a - c)/2)                      
        #return (a - c)/2   #returning (a-c)/2 or 0 doesn't seem to make a difference
        #return 0
        return defaultBounds[0][0] - 5       

#def find3IntersectY(pt1)

#def find3IntersectPt()

def find2IntersectAtTime(pt1, pt2, t): # finds x-value of intersection of two parabolas at given time, imaginary if it doesn't exist (this is diff than getTimeAtX(?))
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
            return x1
        else:
            return x2                                                        

        #return x
    except ZeroDivisionError:
        print(f"zero division error in find2IntersectAtTime with {pt1} {pt2} {pt3} t={t}")        
        return defaultBounds[1][1] -5                    

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
        return x        
    except ZeroDivisionError:
        print(f"zero division error in otherXOnBisectorAtT with {pt1} {pt2} {pt3} t={t}")        
        return defaultBounds[1][1] -5                    

def getTimeAtX(pt1, pt2, pt3, x): # finds time when parabola pt1 has given x value, (pt1, pt2, pt3) = (pt1, pt3, pt2)
    try:    
        a, b, c, d, e, f = pt1[0], pt1[1], pt2[0], pt2[1], pt3[0], pt3[1]
        j = b-d
        k = -( (a**2) + (b**2) - (c**2) - (d**2) + (2 * x * (c-a)))#-1 * ( (a**2) + (-2 * x * a) + (b**2) - (d**2) + (b * d) - (c**2) + (2 * x * c) - (d * b) )#-( (a**2) + (b**2) ) + (c**2) + (d**2) + (2 * x * (a-c)) #this last one is incorrect
        L = f * ( (a**2) + (b**2) - (c**2) - (d**2) - (2 * x * (a - c) ) ) - ( ( (x**2) + (e**2) + (f**2) - (2 * x * e) ) * j )#f * ( (a**2) + (b**2) - (c**2) - (d**2) - (2 * x * (a - c) ) ) - ( ( (x**2) + (e**2) + (f**2) - (2 * x * e) ) * (b - d) ) #f*( (a**2) - (c**2) + (b**2) - (d**2) - (2 * x * (a-c)) ) - (( ((x-e)**2) + (f**2) )*(b-d))
        t = ((-1 * k) - ( (k**2) - (4 * j * L))**0.5) / (2 * j) # division by 0 if j = 0, j = 0 if b-d = 0, so if the first 2 points have the same y value
        return t        
    except ZeroDivisionError:
        print(f"zero division error in getTimeAtX with {pt1} {pt2} {pt3} x={x} j={j} k={k} L={L}")        
        return pt1[1]#defaultBounds[1][1] -5            
    

def getYAtTimeAndX(pt1, t, x): # just the y-value of the parabola at the given t and x, which may different than yAtX since that is locked to the bisector
    try:    
        a, b = pt1[0], pt1[1]
        y = (((x-a)**2) / (2 * (b-t))) + (0.5 * (b+t)) # divides by 0 if b+t = 0 and b-t = 0, which is not possible
        return y
    except ZeroDivisionError:
        print(f"zero division error in getYAtTimeAndX with {pt1} t={t} x={x}")
        return defaultBounds[1][1] -5                       

def yAtX(pt1, pt2, x): # gives y value of bisector between two parabolas at given x value
    try:    
        a, b, c, d = pt1[0], pt1[1], pt2[0], pt2[1]
        y = ((c-a) / (b-d)) * (x - ( (a+c)/2) ) + ((b+d)/2) # divides by 0 if b-d = 0 (points have same y value), so the valid y value would also be the same
        return y
    except ZeroDivisionError:
        print(f"zero division error in yAtX with {pt1} {pt2} x={x}")
        return pt1[1]#defaultBounds[1][1] -5                    
    
def xAtY(pt1, pt2, y): # gives x value of bisector between two parabolas at given y value
    try:    
        a, b, c, d = pt1[0], pt1[1], pt2[0], pt2[1]
        x = ( (2 * y * (d-b)) - ((d**2) - (b**2)) + ((a**2) - (c**2)) ) / (2 * (a-c)) # divides by 0 uf a-c = 0 (points have the same x value), so the correct x value would be the same as well
        return x
    except ZeroDivisionError:
        print(f"zero division error in xAtY with {pt1} {pt2} y={y}")
        return pt1[0]#defaultBounds[0][0] -5    

def tAtXandY(pt1, x, y):   
    a, b = pt1[0], pt1[1]
    t = ((2 * y) + (( (4 * (y**2)) + 4*( ((x-a)**2) - (2 * y * b) + (b**2 ) ) ) ** 0.5)) / 2
    return t    


def pointSlope(pt, slope, x):
    return (slope * (x - pt[0])) + pt[1]

def pointSlopeX(pt, slope, y):
    return (y - pt[1] + (slope * pt[0])) / slope      

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
                    #print(site1)
                    #x = find3IntersectX(site1, site2, site3) # the order of the points put in matters (?)
                    #t = getTimeAtX(site1, site2, site3, x) # the order of the points put in matters
                    #y = getYAtTimeAndX(site1, t, x)

                    x = find3IntersectX(sites[0], sites[1], sites[2])
                    t = getTimeAtX(sites[0], sites[1], sites[2], x)
                    y = getYAtTimeAndX(sites[0], t, x)                                        
                    
                    #if site1[1] == site2[1]:
                    #        print("site1 y == site2 y",x, y, t) 

                    #print(f"-- ({site1[0]}, {site1[1]}) ({site2[0]}, {site2[1]}) ({site3[0]}, {site3[1]}) time: {t} at ({x}, {y})")
#                     if site1 == [72, 122] or site1 == [182, 111] or site2 == [72, 122] or site2 == [182, 111] or site3 == [72, 122] or site3 == [182, 111]:                                                                    
#                         print(f"    ({site1[0]}, {site1[1]}) ({site2[0]}, {site2[1]}) ({site3[0]}, {site3[1]}) time: {t} at ({x}, {y})")                    
                    #if t > defaultBounds[1][1] and t < defaultBounds[1][0] and t < boundLt: #having the t < boundLt fixes some issues but seems like it will cause some later on
                    #if t > defaultBounds[1][1] and t < defaultBounds[1][0] and x >= defaultBounds[0][0] and x <= defaultBounds[0][1]:
                    #if t > points[0][1] and t < defaultBounds[1][0] and x >= defaultBounds[0][0] and x <= defaultBounds[0][1] and y >= defaultBounds[1][1] and y <= defaultBounds[1][0]:                    
                    #print(site1, points[0][1])
                    #if t > points[0][1] and x >= defaultBounds[0][0] and x <= defaultBounds[0][1] and y >= defaultBounds[1][1] and y <= defaultBounds[1][0]:
                    #if t > site1[1] and t > site2[1] and t > site3[1] and x >= defaultBounds[0][0] and x <= defaultBounds[0][1] and y >= defaultBounds[1][1] and y <= defaultBounds[1][0]:
                    halfWidth = (defaultBounds[0][0] + defaultBounds[0][1])/2
                    halfHeight = (defaultBounds[1][1] + defaultBounds[1][0])/2                                       
                    if t > site1[1] and t > site2[1] and t > site3[1] and x >= defaultBounds[0][0] - (halfWidth/2) and x <= defaultBounds[0][1] + (halfWidth/2) and y >= defaultBounds[1][1] - (halfHeight/2) and y <= defaultBounds[1][0] + (halfHeight/2):                     

#                         if x >= defaultBounds[0][0] and x <= defaultBounds[0][1] and y >= defaultBounds[1][1] and y <= defaultBounds[1][0]: # If it is within the normal bounds
#                             if f"{str(site1).replace(', ', '_')}" in cell:
#                                 cell[f"{str(site1).replace(', ', '_')}"].append({"point1":site1, "point2":site2, "point3":site3, "time":float("%.10f" % t), "at":[float("%.10f" % x), float("%.10f" % y)]})
#                             else:                            
#                                 cell.update({f"{str(site1).replace(', ', '_')}" : [{"point1":site1, "point2":site2, "point3":site3, "time":float("%.10f" % t), "at":[float("%.10f" % x), float("%.10f" % y)]}]})      
#                         
#                         else: # if it is outside the normal bounds but within the buffer bounds
#                             #print("line354",[float("%.10f" % x), float("%.10f" % y)])
# 
# #                             midPt1 = midPoint(site1, site2)
# #                             midPt2 = midPoint(site1, site3)
# 
#                             #bound1 = nearestBoundry([x, y], midPt1)
#                             #bound2 = nearestBoundry([x, y], midPt2)
# 
# #                             slope1 = slope([x, y], midPt1)
# #                             slope2 = slope([x, y], midPt2)                            
# 
# #                             bound1 = nearestOutsideBoundry([x, y], midPt1)
# #                             bound2 = nearestOutsideBoundry([x, y], midPt2)
# 
# #                             print("bounds",bound1,bound2)                                                        
#                                                                                                            
#                             if f"{str(site1).replace(', ', '_')}" in cell:
#                                 cell[f"{str(site1).replace(', ', '_')}"].append({"point1":site1, "point2":site2, "point3":site3, "time":float("%.10f" % t), "at":[float("%.10f" % x), float("%.10f" % y)]})
#                             else:                            
#                                 cell.update({f"{str(site1).replace(', ', '_')}" : [{"point1":site1, "point2":site2, "point3":site3, "time":float("%.10f" % t), "at":[float("%.10f" % x), float("%.10f" % y)]}]})

                        if f"{str(site1).replace(', ', '_')}" in cell:
                            cell[f"{str(site1).replace(', ', '_')}"].append({"point1":site1, "point2":site2, "point3":site3, "time":float("%.10f" % t), "at":[float("%.10f" % x), float("%.10f" % y)]})
                        else:                            
                            cell.update({f"{str(site1).replace(', ', '_')}" : [{"point1":site1, "point2":site2, "point3":site3, "time":float("%.10f" % t), "at":[float("%.10f" % x), float("%.10f" % y)]}]})


                                
                        #cell[f"{str(site1).replace(', ', '_')}"].append({"point1":site1, "point2":site2, "point3":site3, "time":t, "at":[x, y]})
            #         elif site1[1] == site2[1]:
            #             if f"{str(site1).replace(', ', '_')}" in cell:
            #                 cell[f"{str(site1).replace(', ', '_')}"].append({"point1":site1, "point2":site2, "point3":site3, "time":float("%.10f" % t), "at":[float("%.10f" % x), float("%.10f" % y)]})
            #             else:                            
            #                 cell.update({f"{str(site1).replace(', ', '_')}" : [{"point1":site1, "point2":site2, "point3":site3, "time":float("%.10f" % t), "at":[float("%.10f" % x), float("%.10f" % y)]}]})                                                    
                        
                                       
    

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
    #print("line475",cell[kys[0]][0])
    #print(kys)    
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
    #         tempPair = [pts[0], pts[1]]
    #         sortByY(tempPair)                     
        
    #         if f"{str(point).replace(', ', '_')}" not in finalCell:    #I should add onto this list so that the list of verticies will also include the corner     
    #             finalCell.update({f"{str(point).replace(', ', '_')}":{"site":point, "vertices":[tempPair]}})
    #             #pass            
    #         elif tempPair not in finalCell[f"{str(relative[1]).replace(', ', '_')}"]["vertices"]:
    #             finalCell[f"{str(point).replace(', ', '_')}"]["vertices"].append(tempPair)
    #             #pass                        
            #print("line388",sortByY)            
            #relative = points.copy()
            #distanceTargetSort(point, points)
            #distanceTargetSort(point, relative)        
            #print(f"relative:{relative}")
            #if f"{str(relative[1]).replace(', ', '_')}" in finalCell:
            #    finalCell[f"{str(relative[1]).replace(', ', '_')}"]["vertices"].append([pts[0], pts[1]])
            #else:
            #    finalCell.update({f"{str(relative[1]).replace(', ', '_')}":{"site":relative[1], "vertices":[
            #    [pts[0], pts[1]]
            #    ]}})                                          
            finalCell[f"{str(relative[1]).replace(', ', '_')}"]["vertices"].append([pts[0], pts[1]])

#print(cell)
                

# def makePerpLine(p1, p2):
#     m = slope(p1, p2)
#     if m != 0:
#         m = -1/m
#     else:
#         m = 100000

#     midPt = midPoint(p1, p2)
#     return [[midPt[0], midPt[1]], [midPt[0] + 5, yAtX(p1, p2, midPt[0] + 5)]]

# def make2ndEdge(intersect, midPt):                            
# #     T1 = [intersect[0] - 5, yAtX(p1, p2, intersect[0] - 5)]
# #     T2 = [intersect[0] + 5, yAtX(p1, p2, intersect[0] + 5)]
#     m = slope(intersect, midPt)
#     T1 = [intersect[0] - 5, pointSlope(intersect, m, intersect[0] - 5)] 
#     T2 = [intersect[0] + 5, pointSlope(intersect, m, intersect[0] + 5)]    
#     newPoint = []
# #     print("T1", T1, "T2",T2)    
# #     print("line474", distancePt(T1, midPt), distancePt(T2, midPt))
# 
#  #    if T1[1] == T2[1]:
#  #        m = slope(intersect, midPt)
#  #        T1 = [intersect[0] - 5, pointSlope(intersect, m, intersect[0] - 5)] 
#  #        T2 = [intersect[0] + 5, pointSlope(intersect, m, intersect[0] + 5)]
#      
#     if distancePt(T1, midPt) < distancePt(T2, midPt):#distance(T1[0], T1[1], midPt[0], midPt[1]) < distance(T2[0], T2[1], midPt[0], midPt[1]):
#         newPoint = T1
#     else:
#         newPoint = T2
# 
# #     print("newPt",newPoint)        
# 
#     nearestBound = nearestBoundry(intersect, newPoint)
#     #print("nearestBound",nearestBound)
#     return nearestBound                                                    

def rotate(pt, origin, amount):   
    x = ((pt[0] - origin[0]) * math.cos(amount)) - ((pt[1] - origin[1]) * math.sin(amount))
    y = ((pt[1] - origin[1]) * math.cos(amount)) + ((pt[0] - origin[0]) * math.sin(amount))
    x += origin[0]
    y += origin[1]        
    return [x, y]           

#normalTheta + angle == 2pi most of the time
def normalTheta(pt, origin): #gets the exterior/larger angle (basically)
    a, b, c, d = pt[0], pt[1], origin[0], origin[1]
    x = a-c
    y = b-d
    #print("line477",x,y)
    theta = math.atan(y/x)
    #print("line479",theta)
    if y < 0 and x > 0:
        theta += (2 * math.pi)
    elif y < 0 or x < 0:
        theta += math.pi
    return theta                                                        
            

def angle(pt1, pt2, origin): #gets the interior/smaller angle
    a, b, c, d, e, f = origin[0], origin[1], pt1[0], pt1[1], pt2[0], pt2[1]
    #theta = math.acos( ( ((e -a) * (c-a)) + ((f-b) * (d-b)) ) / ( ( ( ((e-a)**2) + ((f-b)**2) ) * ( ((c-a)**2) + ((b-d)**2) ) ) ** 0.5 ) )
    theta = math.acos( ( ((e -a) * (c-a)) + ((f-b) * (d-b)) ) / ( ( (( ((e-a)**2) + ((f-b)**2) ) ** 0.5) * (( ((c-a)**2) + ((b-d)**2) ) ** 0.5) ) ) )    
    return theta           

#def simpleAngle(pt1, pt2, origin): #same as normalTheta somehow
    #a, b, c, d, e, f = pt1[0], pt1[1], pt2[0], pt2[1], origin[0], origin[1] 

#     theta1 = normalTheta(pt1, origin)
#     theta2 = normalTheta(pt2, origin)
#     theta = max(theta1, theta2) - min(theta1, theta2) 
#     print(theta1, theta2)
#     return theta       
        

#since arctan is from -pi/2 to pi/2 and I want values in the range 0 to 2pi, I need to code for that seperately, which is what is in normalTheta
def rectToPolar(pt, origin):
    a, b, c, d = pt[0], pt[1], origin[0], origin[1]
    #theta = math.atan(b/a)
    #r = ( (a**2) + (b**2) ) ** 0.5
    #theta = math.atan((b-d)/(a-c))
    theta = normalTheta(pt, origin)    
    r = ( ((a-c)**2) + ((b-d)**2) ) ** 0.5
    #if (theta < 0):
    #    theta = (2 * math.pi) + theta                   
    return [r, theta]

def polarToRect(pt, origin):
    #x = pt[0] * math.cos(pt[1])
    #y = pt[0] * math.sin(pt[1])
    x = (pt[0] * math.cos(pt[1])) + origin[0]
    y = (pt[0] * math.sin(pt[1])) + origin[1]     
    return [x, y]                            

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
                                            
                        finalCell[site]["vertices"].append([entry["at"], entry2["at"]])
                        #print(site, [pt1, pt2, pt3], [entry2["point1"], entry2["point2"], entry2["point3"]])
                        #print("line656",entry["at"],entry2["at"])
                        atName = f"{str(entry['at']).replace(', ', '_')}"

                        if atName not in vertices:
                            tempSites = [pt1, pt2, pt3]
                            sortByY(tempSites)                                                        
                            vertices.update({atName : {"sites":tempSites, "with":[], "at":[]}})                            
                        
                        if entry2["point1"] in [pt2, pt3] and [pt1, entry2["point1"]] not in vertices[atName]["with"] and [entry2["point1"], pt1] not in vertices[atName]["with"]:
                            vertices[atName]["with"].append([pt1, entry2["point1"]])
                            vertices[atName]["at"].append(entry2["at"])                                                        
                        elif entry2["point2"] in [pt2, pt3] and [pt1, entry2["point2"]] not in vertices[atName]["with"] and [entry2["point2"], pt1] not in vertices[atName]["with"]:
                            vertices[atName]["with"].append([pt1, entry2["point2"]])
                            vertices[atName]["at"].append(entry2["at"])                            
                        elif entry2["point3"] in [pt2, pt3] and [pt1, entry2["point3"]] not in vertices[atName]["with"] and [entry2["point3"], pt1] not in vertices[atName]["with"]:
                            vertices[atName]["with"].append([pt1, entry2["point3"]])
                            vertices[atName]["at"].append(entry2["at"])                                                                                    
                        #if entry2["point1"] in [pt1, pt2, pt3] and entry2["point1"] != pt1 and [pt1, entry2["point1"]] not in vertices[atName]["with"] and [entry2["point1"], pt1] not in vertices[atName]["with"]:
                        #    vertices[atName]["with"].append([pt1, entry2["point1"]])
                        #elif entry2["point1"] in [pt1, pt2, pt3] and entry2["point2"] != pt1 and [pt1, entry2["point2"]] not in vertices[atName]["with"] and [entry2["point2"], pt1] not in vertices[atName]["with"]:
                        #    vertices[atName]["with"].append([pt1, entry2["point2"]])
                        #elif entry2["point1"] in [pt1, pt2, pt3] and entry2["point3"] != pt1 and [pt1, entry2["point3"]] not in vertices[atName]["with"] and [entry2["point3"], pt1] not in vertices[atName]["with"]:                                                                                            
                        #    vertices[atName]["with"].append([pt1, entry2["point3"]])                                                                                                                                         
                    #print(str(entry["at"]))                    
                    #if f"{str(entry['at']).replace(', ', '_')}" not in vertices and pt1 != entry2["point2"] and entry2["point2"] in [pt1, pt2, pt3]:
                    #    vertices.update({f"{str(entry['at']).replace(', ', '_')}" : {"sites":[pt1, pt2, pt3], "with":[[pt1, entry2["point2"]]]}})
                    #elif [pt1, entry2["point2"]] not in vertices[f"{str(entry['at']).replace(', ', '_')}"]["with"] and [entry2["point2"], pt1] not in vertices[f"{str(entry['at']).replace(', ', '_')}"]["with"] and pt1 != entry2["point2"]:
                    #    vertices[f"{str(entry['at']).replace(', ', '_')}"]["with"].append([pt1, entry2["point2"]])
                                                                       
        except Exception as e:
            print(f"site2: {e} not in cell") 

#for a in finalCell:
#    print("finalCell",a,finalCell[a])
#print()    
#for b in vertices:
#    print("vertices",b,vertices[b])
#print()    
#for c in cell:
#    print("cell",c,cell[c])                    

#print()


            
for vert in vertices:
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
        
        #print("throughPt",throughPt)
        #plt.plot(throughPt[0], throughPt[1], "yo")

        

                
        continue
        boundryEdges = []
        #center = vertPt#midPoint(defaultBounds[0], defaultBounds[1])    
        #for cell2 in finalCell:
            #print(finalCell[cell2]["vertices"])
        #     for vert1 in finalCell[cell2]["vertices"]:
        #         for vert2 in finalCell[cell2]["vertices"]:
        #             if vert1 != vert2:
        #                 if vert1[0] == vert2[0] or vert1[0] == vert2[0] or vert1[1] == vert2[0] or vert1[1] == vert2[1]:                 
        #                     if vert1[0][0] == defaultBounds[0][0] or vert1[0][0] == defaultBounds[0][1]: 
        #                         boundryEdges.append({"cell":cell2, "vert1":vert1, "vert2":vert2})
            #continue    
        #print("info",cell2,"-",finalCell[cell2]["vertices"])    
        onBoundry = []
        for vert in finalCell[f"{str(pair3[0]).replace(', ', '_')}"]["vertices"]:
            boundSize = [defaultBounds[0][0], defaultBounds[0][1], defaultBounds[1][0] ,defaultBounds[1][1]]        
            if vert[0][0] in boundSize or vert[0][1] in boundSize:
                onBoundry.append([vert[0], normalTheta(vert[0], vertPt)])
            elif vert[1][0] in boundSize or vert[1][1] in boundSize:
                onBoundry.append([vert[1], normalTheta(vert[1], vertPt)])            

        print("onBoundry",onBoundry, onBoundry.__len__())
        print("site", pair3[0])
        print("vertPt", vertPt)                
        if onBoundry != []:
            #print(nearestBoundry(onBoundry[0], onBoundry[1]))
            withCorners = onBoundry.copy()        
            withCorners.append([corners[0], normalTheta(corners[0], vertPt)])
            withCorners.append([corners[1], normalTheta(corners[1], vertPt)])
            withCorners.append([corners[2], normalTheta(corners[2], vertPt)])
            withCorners.append([corners[3], normalTheta(corners[3], vertPt)])
                                
            sortByY(onBoundry)
            sortByY(withCorners)                

            indexes = []
            within = []
            boundries = []
        
            print("withcorners",withCorners)        
            plt.plot([vertPt[0]-5, vertPt[0]+5], [vertPt[1], vertPt[1]], "yo")

            siteTheta = normalTheta(pair3[0], vertPt)
            print("siteTheta", siteTheta)                          

        print()                                                                                                                       

                                                       
# removes duplicate information
for cell3 in finalCell:
    tempVerts = finalCell[cell3]["vertices"].copy()
    sortByY(tempVerts)
    for vert in tempVerts:
        sortByY(vert)
    unique = []
    #print("site",cell3)
    for vert in tempVerts:
        #print("vert",vert)        
        if vert not in unique and vert[0] != vert[1]:
            if vert[0][0] >= defaultBounds[0][0] and vert[0][0] <= defaultBounds[0][1] and vert[0][1] >= defaultBounds[1][1] and vert[0][1] <= defaultBounds[1][0]:            
                if vert[1][0] >= defaultBounds[0][0] and vert[1][0] <= defaultBounds[0][1] and vert[1][1] >= defaultBounds[1][1] and vert[1][1] <= defaultBounds[1][0]:             
                    unique.append(vert)                       
    
    if unique == []:
        curSite = cell3.replace("[","").replace("]","").split("_")
        curSite = [float(curSite[0]), float(curSite[1])]

        i = points.index(curSite)

        other = []
        if i == points.__len__()-1:
            other = points[i - 1]
        else:                    
            other = points[i + 1]

        midPt = midPoint(curSite, other)
        before = [midPt[0]-0.5, yAtX(curSite, other, midPt[0]-0.5)]
        after = [midPt[0]+0.5, yAtX(curSite, other, midPt[0]+0.5)]

        bound1 = nearestBoundry(midPt, before)
        bound2 = nearestBoundry(midPt, after)

        unique = [[bound1, bound2]]
        sortByY(unique[0])                                                                              

    if points.__len__() > 1:
        finalCell[cell3]["vertices"] = unique                        


boundryEdges = []
#center = midPoint(defaultBounds[0], defaultBounds[1])    
for cell2 in finalCell:
    #print(finalCell[cell2]["vertices"])
#     for vert1 in finalCell[cell2]["vertices"]:
#         for vert2 in finalCell[cell2]["vertices"]:
#             if vert1 != vert2:
#                 if vert1[0] == vert2[0] or vert1[0] == vert2[0] or vert1[1] == vert2[0] or vert1[1] == vert2[1]:                 
#                     if vert1[0][0] == defaultBounds[0][0] or vert1[0][0] == defaultBounds[0][1]: 
#                         boundryEdges.append({"cell":cell2, "vert1":vert1, "vert2":vert2})
    #continue  
    
    
      
    print("info",cell2,"-",finalCell[cell2]["vertices"])    
    onBoundry = []
    for vert in finalCell[cell2]["vertices"]:
        boundSize = [defaultBounds[0][0], defaultBounds[0][1], defaultBounds[1][0] ,defaultBounds[1][1]]
        #print("boundsize",boundSize)
        #print(vert)                        
        if (vert[0][0] in boundSize or vert[0][1] in boundSize) and vert[0] not in onBoundry:
            onBoundry.append(vert[0])
        if (vert[1][0] in boundSize or vert[1][1] in boundSize) and vert[1] not in onBoundry:
            onBoundry.append(vert[1])            

    #print(onBoundry)
    if onBoundry != []:
        #print(nearestBoundry(onBoundry[0], onBoundry[1]))
        #withCorners = onBoundry.copy()        
        #withCorners.append([corners[0], normalTheta(corners[0], center)])
        #withCorners.append([corners[1], normalTheta(corners[1], center)])
        #withCorners.append([corners[2], normalTheta(corners[2], center)])
        #withCorners.append([corners[3], normalTheta(corners[3], center)])
        #withCorners.extend(corners[0], corners[1], corners[2], corners[3])        
        
        curSite = cell2.replace("[","").replace("]","").split("_")
        curSite = [float(curSite[0]), float(curSite[1])]

        #print("onboundry", onBoundry)
        sortByY(onBoundry)
        if onBoundry.__len__() == 2:
            if onBoundry[0][0] == onBoundry[1][0] or onBoundry[0][1] == onBoundry[1][1]:
                finalCell[cell2]["vertices"].append([onBoundry[0], onBoundry[1]])
            else: # if the two vertices are not on the same edge
#                 center = [(onBoundry[0][0] + onBoundry[1][0] + curSite[0])/3, (onBoundry[0][1] + onBoundry[1][1] + curSite[1])/3]#midPoint(onBoundry[0], onBoundry[1])
#                 vert1Test = []
#                 vert2Test = []

#                 if onBoundry[0][0] == defaultBounds[0][0] or onBoundry[0][0] == defaultBounds[0][1]:
#                     vert1Test = [[onBoundry[0][0], onBoundry[0][1] - 0.5], [onBoundry[0][0], onBoundry[0][1] + 0.5]]
#                 else:                                    
#                     vert1Test = [[onBoundry[0][0] - 0.5, onBoundry[0][1]], [onBoundry[0][0] + 0.5, onBoundry[0][1]]]

#                 if onBoundry[0][0] == defaultBounds[0][0] or onBoundry[0][0] == defaultBounds[0][1]:
#                     vert1Test = [[onBoundry[0][0], onBoundry[0][1] - 0.5], [onBoundry[0][0], onBoundry[0][1] + 0.5]]
#                 else:                                    
#                     vert1Test = [[onBoundry[0][0] - 0.5, onBoundry[0][1]], [onBoundry[0][0] + 0.5, onBoundry[0][1]]]

#                 vert1 = []
#                 vert2 = []                
#                 if distancePt(vert1Test[0], center) < distancePt(vert1Test[1], center):
#                     vert1 = vert1Test[0]
#                 else:
#                     vert1 = vert1Test[1]
#                     
#                 if distancePt(vert2Test[0], center) < distancePt(vert2Test[1], center):
#                     vert2 = vert2Test[0]
#                 else:
#                     vert2 = vert2Test[1]                                                                                                                                                    

                

                inside = False
                vert1Theta = normalTheta(onBoundry[0], curSite)
                vert2Theta = normalTheta(onBoundry[1], curSite)
                #print("theta", vert1Theta, vert2Theta)
                for pt in points:
                    if pt != curSite:
                        ptTheta = normalTheta(pt, curSite)
                        if ptTheta > vert2Theta and ptTheta < vert1Theta:
                            inside = True
                            break
    
                withCorners = onBoundry.copy()
                withCorners.extend([corners[0], corners[1], corners[2], corners[3]])

                for i in range(0, withCorners.__len__()):
                    withCorners[i] = [withCorners[i], normalTheta(withCorners[i], curSite)]                                    
    
                sortByY(withCorners)

                for i in range(0, withCorners.__len__()-1):
                    if withCorners[i][1] == withCorners[i+1][1]:
                        if withCorners[i][0] > withCorners[i+1][0]:
                            withCorners[i], withCorners[i+1] = withCorners[i+1], withCorners[i]                                                                               
                
                #print(withCorners)
                if inside == False:
                    index1 = withCorners.index([onBoundry[0], vert1Theta])
                    index2 = withCorners.index([onBoundry[1], vert2Theta])
                    if index1 > index2:
                        index1, index2 = index2, index1                                            
                    vertSet = withCorners[index1:index2+1]                    
                    print("rangeIn",index1, index2, vertSet)
                    for i in range(0, vertSet.__len__()-1):
                        finalCell[cell2]["vertices"].append([vertSet[i][0], vertSet[i+1][0]])                                            
                                                                                
                else:                                                                                                                                                                                                             
                    index1 = withCorners.index([onBoundry[0], vert1Theta])
                    index2 = withCorners.index([onBoundry[1], vert2Theta])
                    if index1 > index2:
                        index1, index2 = index2, index1                                            
                    vertSet = withCorners[index2:]
                    vertSet.extend(withCorners[:index1+1])                                        
                    print("rangeOut",index1, index2, vertSet)
                    for i in range(0, vertSet.__len__()-1):
                        finalCell[cell2]["vertices"].append([vertSet[i][0], vertSet[i+1][0]])                                                
        else: # if it greater than 2, it would ALMOST have to be a multiple of 2, with verts on different edges
            pass                        
        
        continue
                        
        sortByY(onBoundry)
        sortByY(withCorners)                

        indexes = []
        within = []
        boundries = []
        
        curSite = cell2.replace("[","").replace("]","").split("_")
        curSite = [float(curSite[0]), float(curSite[1])]
        print(curSite)        
        siteTheta = normalTheta(curSite, center)
        print("line933",onBoundry[0][1])
        print("line935",onBoundry)
        print("siteTheta",siteTheta)                
        if siteTheta > onBoundry[0][1]:
            print("withCorners",withCorners)    
            for point in onBoundry:
                #print(normalTheta(point, center))
                #print(withCorners.index(point))
                indexes.append(withCorners.index(point))

            for i in range(0, indexes.__len__(), 2):
                #print(indexes[i], indexes[i+1])
                #print(withCorners[indexes[i]:indexes[i+1]+1])
                #print(indexes[i], indexes[i+1]+1)
                #print(withCorners[indexes[i]:indexes[i+1]+1])                        
                within.extend(withCorners[indexes[i]:indexes[i+1]+1])                                                
                                    
            print("within",within[0])
            for i in range(0, within.__len__()-1):
                #print(within[i])            
                boundries.append([within[i][0], within[i+1][0]])

            print("boundries",boundries)
        else:                    
             pass   
        
        print() 


for pt in points:
    plt.plot(pt[0], pt[1], "ro")

for site in cell:  
    #print(cell[site])
    #clr1, clr2, clr3 = random.random(), random.random(), random.random() 
    for entry in cell[site]:
        #if entry["at"][1] > 120 and entry["at"][1] < 130:       
        #    print(entry)
        #print(entry)
        #print(site)                
        plt.plot(entry["at"][0], entry["at"][1], "go")#, color=(clr1, clr2, clr3))
        #plt.plot(cell[site]["at"][0], cell[site]["at"][1], color=(0.5, 0.5, 0.5))
        plt.plot([entry["point2"][0], entry["at"][0], entry["point3"][0], entry["at"][0], entry["point1"][0]], [entry["point2"][1], entry["at"][1], entry["point3"][1], entry["at"][1], entry["point1"][1]], "g") 
        #print(clr1, clr2, clr3)
    #plt.plot(cell[site]["at"][0], cell[site]["at"][1], "go")#, color=(clr1, clr2, clr3))
    #plt.plot(cell[site]["at"][0], cell[site]["at"][1], color=(0.5, 0.5, 0.5))
    #plt.plot([cell[site]["point2"][0], cell[site]["at"][0], cell[site]["point3"][0], cell[site]["at"][0], cell[site]["point1"][0]], [cell[site]["point2"][1], cell[site]["at"][1], cell[site]["point3"][1], cell[site]["at"][1], cell[site]["point1"][1]], "g") 
    #print(clr1, clr2, clr3)        
    
for cell in finalCell:
    for pairs in finalCell[cell]["vertices"]:    
        #plt.plot([finalCell[cell]["vertices"][pairs][0][0], finalCell[cell]["vertices"][pairs][1][0]], [finalCell[cell]["vertices"][pairs][0][1], finalCell[cell]["vertices"][pairs][1][1]], "bo")
        #plt.plot([pairs[0][0], pairs[1][0]], [pairs[0][1], pairs[1][1]], "bo")
        plt.plot([pairs[0][0], pairs[1][0]], [pairs[0][1], pairs[1][1]], "b")
        plt.plot([pairs[0][0], pairs[1][0]], [pairs[0][1], pairs[1][1]], "bo")                
        #print(pairs[0][0], pairs[1][0], pairs[0][1], pairs[1][1])
        #x1 = [pairs[0][0], pairs[1][0]]
        #y1 = [pairs[0][1], pairs[1][1]]
        #plt.plot(x1, y1, "b")
        #print(pairs)                        
        
plt.show()

