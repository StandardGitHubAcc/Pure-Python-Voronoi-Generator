from decimal import DivisionByZero
import matplotlib.pyplot as plt
import random
import math
from math import *

#                 width     height
defaultBounds = [[0, 200], [200, 0]]
#points = [(50, 50), (25, 25), (75, 75), (98, 70)]
#points = [(50, 50), (25, 20), (75, 75), (98, 70)]
#points = [(30, 40), (25, 60), (80, 97)]

#points = [[30, 30], [40, 40], [10, 50]]
#points = [[90,81],[48,121],[163,120],[83,23]]

points = []
for i in range(1, 8):
      points.append([random.randint(0, 200), random.randint(0, 200)])  

#points = [[59, 55], [30, 88], [1, 93]] #[[186, 15], [162, 127], [25, 144]] this is pretty much just a bigger version of the first set
#points = [[186, 15], [162, 127], [25, 144]]
#points = [[19, 27], [131, 44], [38, 130]]
#points = [[57, 67], [21, 80], [79, 198]]
#points = [[17, 45], [62, 54], [152, 194]]

#points = [[71, 79], [167, 127], [178, 141]]#[[57, 67], [21, 80], [79, 198]]#[[17, 45], [62, 54], [152, 194]]#[[159, 66], [100, 166], [73, 197]]#[[71, 79], [167, 127], [178, 141]]
#points = [[159, 66], [100, 166], [73, 197]]

#points = [[106, 6], [88, 11], [9, 18], [2, 105], [20, 105], [115, 140], [52, 168]] #causes division by zero in getTimeAtX
#points = [[13, 23], [181, 40], [129, 55], [93, 100], [59, 127], [12, 160], [156, 163]] #---
# points = [[76, 30], [196, 40], [165, 47], [104, 66], [128, 120], [88, 159], [166, 180]] #easy to see graph. In a previous, more broken version of the program, another line and intersection point near the one on the far right existed, which is necessary to correctly complete the graph
# ^there is an issue with the plot for the line above

#points = [[194, 2], [94, 30], [11, 91], [88, 92], [57, 143], [43, 190], [6, 198]]
#points = [[12, 1], [97, 12], [168, 24], [98, 58], [182, 111], [102, 111], [72, 122]]

#[[159, 12], [197, 12], [123, 38], [145, 92], [56, 123], [85, 160], [44, 166]] #causes a division by zero in yAtX

#[[95, 52], [68, 62], [137, 79], [127, 132], [42, 155], [90, 182], [179, 183]] #might be messed up?

#[[25, 17], [109, 37], [68, 45], [35, 85], [2, 124], [138, 138], [190, 145]]

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
                
def find3Intersect(pt1, pt2, pt3): # division by zero happens with the points (50, 50) (25, 25) (75, 75)
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

def find2IntersectAtTime(pt1, pt2, t):
    try:    
        a, b, c, d, = pt1[0], pt1[1], pt2[0], pt2[1]
        n = (2 * ((-1 * c * b) + (c * t) + (a * d) - (a * t))) / (b-d)
        m = (-1 * (b-t) * (d-t)) + (( (c**2) * (b-t) ) + ( (a**2) * (d-t) )) / (b-d)
        x = ((-1 * n) - ( (n**2) - (4 * m))**0.5) / 2
        return x
    except ZeroDivisionError:
        print(f"zero division error in find2IntersectAtTime with {pt1} {pt2} {pt3} t={t}")        
        return defaultBounds[1][1] -5                    

def getTimeAtX(pt1, pt2, pt3, x):
    try:    
        a, b, c, d, e, f = pt1[0], pt1[1], pt2[0], pt2[1], pt3[0], pt3[1]
        j = b-d
        k = -( (a**2) + (b**2) ) + (c**2) + (d**2) + (2 * x * (a-c))
        L = f*( (a**2) - (c**2) + (b**2) - (d**2) - (2 * x * (a-c)) ) - (( ((x-e)**2) + (f**2) )*(b-d))
        t = ((-1 * k) - ( (k**2) - (4 * j * L))**0.5) / (2 * j)
        return t        
    except ZeroDivisionError:
        print(f"zero division error in getTimeAtX with {pt1} {pt2} {pt3} x={x} j={j} k={k} L={L}")        
        return defaultBounds[1][1] -5            
    

def getYAtTimeAndX(pt1, t, x):
    try:    
        a, b = pt1[0], pt1[1]
        y = (((x-a)**2) / (2 * (b-t))) + (0.5 * (b+t))
        return y
    except ZeroDivisionError:
        print(f"zero division error in getYAtTimeAndX with {pt1} t={t} x={x}")
        return defaultBounds[1][1] -5                       

def yAtX(pt1, pt2, x):
    try:    
        a, b, c, d, = pt1[0], pt1[1], pt2[0], pt2[1]
        y = ((c-a) / (b-d)) * (x - ( (a+c)/2) ) + ((b+d)/2)
        return y
    except ZeroDivisionError:
        print(f"zero division error in yAtX with {pt1} {pt2} x={x}")
        return defaultBounds[1][1] -5                    
    
def xAtY(pt1, pt2, y):
    try:    
        a, b, c, d, = pt1[0], pt1[1], pt2[0], pt2[1]
        x = ( (2 * y * (d-b)) - ((d**2) - (b**2)) + ((a**2) - (c**2)) ) / (2 * (a-c))
        return x
    except ZeroDivisionError:
        print(f"zero division error in xAtY with {pt1} {pt2} y={y}")
        return defaultBounds[0][0] -5    

def tAtXandY(pt1, pt2, x, y):   
    a, b, c, d, = pt1[0], pt1[1], pt2[0], pt2[1]
    t = ((2 * y) + (( (4 * (y**2)) + 4*( ((x-a)**2) - (2 * y * b) + (b**2 ) ) ) ** 0.5)) / 2
    return t    

sortByY(points)
print(points)

for point in points:
    finalCell.update({f"{str(point).replace(', ', '_')}" : {"site":point, "vertices":[]}})    

#print(f"finalCell:{finalCell}")

for site1 in points:
    for site2 in points:
        if site1 != site2: 
            #boundVerts = [] #this stuff with bounds doesn't seem to change anything
            
            #boundLy = yAtX(site1, site2, defaultBounds[0][0])
            #boundLt = tAtXandY(site1, site2, defaultBounds[0][0], boundLy)
            #boundRy = yAtX(site1, site2, defaultBounds[0][1])
            #boundRt = tAtXandY(site1, site2, defaultBounds[0][1], boundRy)

            #boundTx = xAtY(site1, site2, defaultBounds[1][0])
            #boundTt = tAtXandY(site1, site2, boundTx, defaultBounds[1][0])
            #boundBx = xAtY(site1, site2, defaultBounds[1][1])
            #boundBt = tAtXandY(site1, site2, boundBx, defaultBounds[1][1])

            #if boundLt < defaultBounds[1][0] and boundLt > defaultBounds[1][1]:            
                #allVerts.append({"type":"leftBound", "time":boundLt, "at":[defaultBounds[0][0], boundLy]})
            #    boundVerts.append({"type":"leftBound", "time":boundLt, "at":[defaultBounds[0][0], boundLy]})
            #if boundRt < defaultBounds[1][0] and boundRt > defaultBounds[1][1]:
                #allVerts.append({"type":"rightBound", "time":boundRt, "at":[defaultBounds[0][1], boundRy]})
            #    boundVerts.append({"type":"rightBound", "time":boundRt, "at":[defaultBounds[0][1], boundRy]})
            #if boundTt < defaultBounds[1][0] and boundTt > defaultBounds[1][1]:
                #allVerts.append({"type":"topBound", "time":boundTt, "at":[boundTx, defaultBounds[1][0]]})
            #    boundVerts.append({"type":"topBound", "time":boundTt, "at":[boundTx, defaultBounds[1][0]]})
            #if boundBt < defaultBounds[1][0] and boundBt > defaultBounds[1][1]:                                
                #allVerts.append({"type":"bottomBound", "time":boundBt, "at":[boundBx, defaultBounds[1][1]]})
            #    boundVerts.append({"type":"bottomBound", "time":boundBt, "at":[boundBx, defaultBounds[1][1]]})
               
            #print(boundVerts)
            #allVerts.extend([{"type":"leftBound", "time":boundLt, "at":[defaultBounds[0][0], boundLy]}, {"type":"rightBound", "time":boundRt, "at":[defaultBounds[0][1], boundRy]}, 
            #                 {"type":"topBound", "time":boundTt, "at":[boundTx, defaultBounds[1][0]]}, {"type":"bottomBound", "time":boundBt, "at":[boundBx, defaultBounds[1][1]]}])                                  
                        
            for site3 in points:
                if site3 != site2 and site3 != site1:
                    sites = [site1, site2, site3]
                    sortByY(sites)                    
                    
                    #x = find3Intersect(site1, site2, site3) # the order of the points put in matters (?)
                    #t = getTimeAtX(site1, site2, site3, x) # the order of the points put in matters
                    #y = getYAtTimeAndX(site1, t, x)

                    x = find3Intersect(sites[0], sites[1], sites[2])
                    t = getTimeAtX(sites[0], sites[1], sites[2], x)
                    y = getYAtTimeAndX(sites[0], t, x)                                        
                    
                    #print(f"-- ({site1[0]}, {site1[1]}) ({site2[0]}, {site2[1]}) ({site3[0]}, {site3[1]}) time: {t} at ({x}, {y})")
                    if site1 == [72, 122] or site1 == [182, 111] or site2 == [72, 122] or site2 == [182, 111] or site3 == [72, 122] or site3 == [182, 111]:                                                                    
                        print(f"    ({site1[0]}, {site1[1]}) ({site2[0]}, {site2[1]}) ({site3[0]}, {site3[1]}) time: {t} at ({x}, {y})")                    
                    #if t > defaultBounds[1][1] and t < defaultBounds[1][0] and t < boundLt: #having the t < boundLt fixes some issues but seems like it will cause some later on
                    #if t > defaultBounds[1][1] and t < defaultBounds[1][0] and x >= defaultBounds[0][0] and x <= defaultBounds[0][1]:
                    #if t > points[0][1] and t < defaultBounds[1][0] and x >= defaultBounds[0][0] and x <= defaultBounds[0][1] and y >= defaultBounds[1][1] and y <= defaultBounds[1][0]:                    
                    #print(site1, points[0][1])
                    #if t > points[0][1] and x >= defaultBounds[0][0] and x <= defaultBounds[0][1] and y >= defaultBounds[1][1] and y <= defaultBounds[1][0]:
                    if t > site1[1] and t > site2[1] and t > site3[1] and x >= defaultBounds[0][0] and x <= defaultBounds[0][1] and y >= defaultBounds[1][1] and y <= defaultBounds[1][0]:                    
                        if site1 == [72, 122] or site1 == [182, 111]:                                                                    
                            print(f"({site1[0]}, {site1[1]}) ({site2[0]}, {site2[1]}) ({site3[0]}, {site3[1]}) time: {t} at ({x}, {y})")
        
                        if f"{str(site1).replace(', ', '_')}" in cell:
                            cell[f"{str(site1).replace(', ', '_')}"].append({"point1":site1, "point2":site2, "point3":site3, "time":float("%.10f" % t), "at":[float("%.10f" % x), float("%.10f" % y)]})
                        else:                            
                            cell.update({f"{str(site1).replace(', ', '_')}" : [{"point1":site1, "point2":site2, "point3":site3, "time":float("%.10f" % t), "at":[float("%.10f" % x), float("%.10f" % y)]}]})
                        #cell[f"{str(site1).replace(', ', '_')}"].append({"point1":site1, "point2":site2, "point3":site3, "time":t, "at":[x, y]})
                        
                                       
    

for site1 in cell:
    #for others in points:
     for entry in cell[site1]:
#        if cell[site1]["point1"] != others and cell[site1]["point2"] != others and cell[site1]["point3"] != others:
#            #print(cell[site1]["time"], cell[site1]["at"])
#            otherPointY = getYAtTimeAndX(others, cell[site1]["time"], cell[site1]["at"][0])
#            #print(otherPointY)
#            if otherPointY > cell[site1]["at"][1]:
#                removeVerts.append(site1)
#                #print(f"remove {site1}")                                                                                         
        #for entry in cell[site1]:
         for others in points:            
            #if entry["point1"] != others and entry["point2"] != others and entry["point3"] != others:
            if entry["point1"] != others and entry["point2"] != others and entry["point3"] != others and others[1] < entry["time"]:
                                                
                #print(cell[site1]["time"], cell[site1]["at"])
                otherPointY = getYAtTimeAndX(others, entry["time"], entry["at"][0])
                #print(otherPointY)
                #if entry["at"][1] > 120 and entry["at"][1] < 130:                
                #    print(others, otherPointY, entry["at"], entry["time"])
                #print("test", otherPointY, entry["at"][1], entry)
                #if otherPointY < defaultBounds[1][0]:                                
                #    if otherPointY > entry["at"][1]:                                        
                #        removeVerts.append([site1, entry])
                #        #print(f"remove {site1} {entry}")
                if otherPointY > entry["at"][1]:
                #if otherPointY > entry["time"]:                
                    #if entry["point1"] == [12, 160] or entry["point2"] == [12, 160] or entry["point3"] == [12, 160]:                    
                    #    print("   ", others, otherPointY, entry["at"], entry["time"])
                    #print("   ", others, otherPointY, entry["at"], entry["time"])                    
                    #print(entry)
                    #print(site1)                                        
                    removeVerts.append([site1, entry])
                    #print(f"remove {site1} {entry}")

if removeVerts.__len__() > 0:
    #for vert in removeVerts:
    #    del cell[vert]
    for site, vert in removeVerts:
                
        try:
            #if 120 < cell[site][cell[site].index(vert)]["at"][1] < 130:           
            #    print("removing", cell[site][cell[site].index(vert)])
            #print("removing", cell[site][cell[site].index(vert)])                    
            del cell[site][cell[site].index(vert)]
        except Exception:
            pass                                            

usedPoints = []
for entry in cell:
    for vert in cell[entry]:    
        #if cell[entry]["point1"] not in usedPoints:
        #    usedPoints.append(cell[entry]["point1"])
        #if cell[entry]["point2"] not in usedPoints:
        #    usedPoints.append(cell[entry]["point2"])
        #if cell[entry]["point3"] not in usedPoints:
        #    usedPoints.append(cell[entry]["point3"])
        
        if vert["point1"] not in usedPoints:
            usedPoints.append(vert["point1"])
        if vert["point2"] not in usedPoints:
            usedPoints.append(vert["point2"])
        if vert["point3"] not in usedPoints:
            usedPoints.append(vert["point3"])                                                    

#print(usedPoints)                

for i in range(points.__len__()):   
    point = points[i]    
    if point not in usedPoints:
        boundVerts = []
        relative = points.copy()
        distanceTargetSort(point, relative)
        
        #site2 = 0        
        #print("a")
        #if i + 1 == points.__len__():
        #    site2 = points[i-1]
        #else:         
        #    site2 = points[i+1]
        site2 = relative[1]
        
        
        #print(point, site2)
        boundLy = yAtX(point, site2, defaultBounds[0][0])
        boundLt = tAtXandY(point, site2, defaultBounds[0][0], boundLy)
        boundRy = yAtX(point, site2, defaultBounds[0][1])
        boundRt = tAtXandY(point, site2, defaultBounds[0][1], boundRy)

        boundTx = xAtY(point, site2, defaultBounds[1][0])
        boundTt = tAtXandY(point, site2, boundTx, defaultBounds[1][0])
        boundBx = xAtY(point, site2, defaultBounds[1][1])
        boundBt = tAtXandY(point, site2, boundBx, defaultBounds[1][1])

        pts = [[defaultBounds[0][0], boundLy], [defaultBounds[0][1], boundRy], [boundTx, defaultBounds[1][0]], [boundBx, defaultBounds[1][1]]]                
        #print(pts)
        distanceTargetSort(point, pts)       
        #print(pts)
        #print(f"{str(point).replace(', ', '_')}")        
        #finalCell.update({f"{str(point).replace(', ', '_')}":{"site":point, "vertices":[ #I should add onto this list so that the list of verticies will also include the corner
        #    [pts[0], pts[1]]
        #    ]}})
        #finalCell[f"{str(point).replace(', ', '_')}"]["vertices"].append([pts[0], pts[1]])
        if not f"{str(point).replace(', ', '_')}" in finalCell:        
            finalCell.update({f"{str(point).replace(', ', '_')}":{"site":point, "vertices":[ #I should add onto this list so that the list of verticies will also include the corner
            [pts[0], pts[1]]
            ]}})
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
                
def nearestBoundry(startPt, throughPt):
    m = slope(startPt, throughPt)
    topX = (defaultBounds[1][0] - startPt[1] + (m * startPt[0])) / m
    bottomX = (defaultBounds[1][1] - startPt[1] + (m * startPt[0])) / m
    leftY = m * (defaultBounds[0][0] - startPt[0]) + startPt[1]
    rightY = m * (defaultBounds[0][1] - startPt[0]) + startPt[1]
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
    
    return choice[0]    

def slope(pt1, pt2):
    return (pt1[1] - pt2[1]) / (pt1[0] - pt2[0])

def midPoint(pt1, pt2):
    return [ (pt1[0] + pt2[0]) / 2,  (pt1[1] + pt2[1]) / 2]        


def makePerpLine(p1, p2):
    m = slope(p1, p2)
    if m != 0:
        m = -1/m
    else:
        m = 1000

    midPt = midPoint(p1, p2)
    return [[midPt[0], midPt[1]], [midPt[0] + 5, yAtX(p1, p2, midPt[0] + 5)]]

def make2ndEdge(p1, p2, intersect, midPt):                            
    T1 = [intersect[0] - 5, yAtX(p1, p2, intersect[0] - 5)]
    T2 = [intersect[0] + 5, yAtX(p1, p2, intersect[0] + 5)]
    newPoint = []

    if distance(T1[0], T1[1], midPt[0], midPt[1]) < distance(T2[0], T2[1], midPt[0], midPt[1]):
        newPoint = T1
    else:
        newPoint = T2

    nearestBound = nearestBoundry(intersect, newPoint)
    #print("nearestBound",nearestBound)
    return nearestBound                                                    

def rotate(pt, origin, amount):   
    x = ((pt[0] - origin[0]) * math.cos(amount)) - ((pt[1] - origin[1]) * math.sin(amount))
    y = ((pt[1] - origin[1]) * math.cos(amount)) + ((pt[0] - origin[0]) * math.sin(amount))
    x += origin[0]
    y += origin[1]        
    return [x, y]           

def angle(pt1, pt2, origin):
    a, b, c, d, e, f = origin[0], origin[1], pt1[0], pt1[1], pt2[0], pt2[1]
    #theta = math.acos( ( ((e -a) * (c-a)) + ((f-b) * (d-b)) ) / ( ( ( ((e-a)**2) + ((f-b)**2) ) * ( ((c-a)**2) + ((b-d)**2) ) ) ** 0.5 ) )
    theta = math.acos( ( ((e -a) * (c-a)) + ((f-b) * (d-b)) ) / ( ( (( ((e-a)**2) + ((f-b)**2) ) ** 0.5) * (( ((c-a)**2) + ((b-d)**2) ) ** 0.5) ) ) )    
    return theta           

#converting from rectangular to polar to rectangular works for some points but not for others, idk why
def rectToPolar(pt, origin):
    a, b, c, d = pt[0], pt[1], origin[0], origin[1]
    #theta = math.atan(b/a)
    #r = ( (a**2) + (b**2) ) ** 0.5
    theta = math.atan((b-d)/(a-c))
    r = ( ((a-c)**2) + ((b-d)**2) ) ** 0.5
    if (theta < 0):
        theta = (2 * math.pi) + theta                   
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
                        finalCell[site]["vertices"].append([entry["at"], entry2["at"]])
                        #print(site, [pt1, pt2, pt3], [entry2["point1"], entry2["point2"], entry2["point3"]])

                        atName = f"{str(entry['at']).replace(', ', '_')}"

                        if atName not in vertices:
                            vertices.update({atName : {"sites":[pt1, pt2, pt3], "with":[], "at":[]}})                            
                        
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


for vert in vertices:
    #print("vert",vert, vertices[vert])
    print()
    if vertices[vert]["at"].__len__() == 1:
        #print("vert",vert, vertices[vert])
        tempVertPt = str(vert).removeprefix("[").removesuffix("]").split("_")
        vertPt = [float(tempVertPt[0]), float(tempVertPt[1])]
        
        tempSites = vertices[vert]["sites"].copy()
        sortByY(tempSites)
        pickedSites = [tempSites[0], tempSites[1]]
        if pickedSites in vertices[vert]["with"]:
            pickedSites[1] = tempSites[2]                                     
             

        #site1 = vertices[vert]["sites"][-2]
        #site2 = vertices[vert]["sites"][-1]
        #print(site1, site2)        
                        
        #nearestBound = makeEdge(site1, site2, vertPt, midPoint(site1, site2))
        #print(pickedSites[0], pickedSites[1])            
        nearestBound = make2ndEdge(pickedSites[0], pickedSites[1], vertPt, midPoint(pickedSites[0], pickedSites[1]))
        
        vertices[vert]["with"].append([pickedSites[0], pickedSites[1]])
        vertices[vert]["at"].append(nearestBound)
        finalCell[f"{str(pickedSites[0]).replace(', ', '_')}"]["vertices"].append([vertPt, nearestBound])
        finalCell[f"{str(pickedSites[1]).replace(', ', '_')}"]["vertices"].append([vertPt, nearestBound])

    if vertices[vert]["at"].__len__() == 2:
        print("vert",vert, vertices[vert])        
        tempVertPt = str(vert).removeprefix("[").removesuffix("]").split("_")
        vertPt = [float(tempVertPt[0]), float(tempVertPt[1])]
        
#         pair1 = vertices[vert]["with"][0]
#         pair2 = vertices[vert]["with"][1]        
        
#         midPt1 = midPoint(pair1[0], pair1[1])
#         midPt2 = midPoint(pair2[0], pair2[1])

 #        angle1 = angle(midPt1, midPt2, vertPt)
 #        print("info",pair1,pair2,angle1)
 #        print("polar",midPt1, rectToPolar(midPt1,vertPt))
 #        print("polar",midPt2, rectToPolar(midPt2,vertPt))
        

        pair3 = []
        site1 = vertices[vert]["sites"][0]
        site2 = vertices[vert]["sites"][1]
        site3 = vertices[vert]["sites"][2]                        
        if [site1, site2] not in vertices[vert]["with"]:
            pair3 = [site1, site2]
        elif [site1, site3] not in vertices[vert]["with"]:
            pair3 = [site1, site3]
        else:                                            
            pair3 = [site2, site3]

        midPt3 = midPoint(pair3[0], pair3[1])
        
        distp1a1 = distance(vertices[vert]["at"][0][0], vertices[vert]["at"][0][1], vertPt[0] + 5, yAtX(pair3[0], pair3[1], vertPt[0] + 5))
        distp1a2 = distance(vertices[vert]["at"][1][0], vertices[vert]["at"][1][1], vertPt[0] + 5, yAtX(pair3[0], pair3[1], vertPt[0] + 5))
        distp2a1 = distance(vertices[vert]["at"][0][0], vertices[vert]["at"][0][1], vertPt[0] - 5, yAtX(pair3[0], pair3[1], vertPt[0] - 5))
        distp2a2 = distance(vertices[vert]["at"][1][0], vertices[vert]["at"][1][1], vertPt[0] - 5, yAtX(pair3[0], pair3[1], vertPt[0] - 5))

        throughPt = []
        if distp1a1 < distp2a1 and distp1a2 < distp2a2:
           throughPt = [vertPt[0] + 5, yAtX(pair3[0], pair3[1], vertPt[0] + 5)]
        else:
            throughPt = [vertPt[0] - 5, yAtX(pair3[0], pair3[1], vertPt[0] - 5)]

        #nearestBound = makeEdge(pair3[0], pair3[1], vertPt, midPt3)    

        #finalCell[f"{str(pair3[0]).replace(', ', '_')}"]["vertices"].append([vertPt, nearestBound])
        #finalCell[f"{str(pair3[1]).replace(', ', '_')}"]["vertices"].append([vertPt, nearestBound])                                                                            

        #if distancePt(midPt3, vertices[vert]["at"][0]) < distancePt(midPt3, vertPt) or distancePt(midPt3, vertices[vert]["at"][1]) < distancePt(midPt3, vertPt):
#         print(pair3, "x",vertPt[0], "t",tAtXandY(pair3[0], pair3[1], vertPt[0], vertPt[1]))
#         print(pair3, "x",vertPt[0] + 5, "t",getTimeAtX(site1, site2, site3, vertPt[0] + 5))
#         print(pair3, "x",vertPt[0] - 5, "t",getTimeAtX(site1, site2, site3, vertPt[0] - 5))
#         print("slope", slope(vertPt, midPt3))

#         tVertPt = tAtXandY(pair3[0], pair3[1], vertPt[0], vertPt[1])
#         tXBeforeVert = getTimeAtX(site1, site2, site3, vertPt[0] + 5)
#         #tXAfterVert = getTimeAtX(site1, site2, site3, vertPt[0] - 5)

#         throughPt = []
#         if (tXBeforeVert > tVertPt):
#             throughPt = [vertPt[0] + 5, yAtX(pair3[0], pair3[1], vertPt[0] + 5)]
#         else:
#             throughPt = [vertPt[0] - 5, yAtX(pair3[0], pair3[1], vertPt[0] - 5)]

#         nearestBound = nearestBoundry(vertPt, throughPt)
#         print(nearestBound)

#         vertices[vert]["with"].append(pair3)
#         vertices[vert]["at"].append(nearestBound)
#         finalCell[f"{str(pair3[0]).replace(', ', '_')}"]["vertices"].append([vertPt, nearestBound])
#         finalCell[f"{str(pair3[1]).replace(', ', '_')}"]["vertices"].append([vertPt, nearestBound]) 

# for vert in vertices: #need to figure out how to loop through all of the intersection points and see how many edges they are a part of, might be able to use a "match: case:" statement
#     numEdges = vertices[vert]["with"].__len__()
#     aSites = vertices[vert]["sites"]

#     a = [aSites[0], aSites[1]]
#     b = [aSites[0], aSites[2]]
#     c = [aSites[1], aSites[2]]
#     sortByY(a)
#     sortByY(b)
#     sortByY(c)
#     possible = [a, b, c]                               

#     at = list(map(float, vert.replace("[", "").replace("]", "").split("_")))    
                
#     print(vert, vertices[vert], numEdges)

#     for i in range(0, numEdges):
#         try:
#             possible.remove(vertices[vert]["with"][i])
#         except Exception:
#             continue                                        
#     print("possible:",possible)

#     #match numEdges:
#     #    case 2:
#     for i in range(0, 3-numEdges):
#             print("----------case2")    
#             newPoint = []                           
#             temp = possible[0] 
#             angle1 = angle(temp[0], temp[1], at)

#             #if at[1] < temp[0][1] or (at[0] < temp[0][0] and at[0] < temp[1][0]):
#             #if at[1] < temp[0][1]:
#             if at[1] < temp[0][1] or not (at[0] > temp[0][0] and at[0] < temp[1][0]):            
#                 angle1 = (2 * math.pi) - angle1       

#             #angle1 = (2 * math.pi) - angle1

#             if at[1] < temp[0][1]:            
#                 newPoint = rotate(temp[0], at, angle1/2)
#             else:                    
#                 newPoint = rotate(temp[1], at, angle1/2)

#             boundry = nearestBoundry(at, newPoint)
#             plt.plot([newPoint[0], at[0]], [newPoint[1], at[1]], "r")
#             finalCell[f"{str(temp[0]).replace(', ', '_')}"]["vertices"].append([at, boundry])
#             finalCell[f"{str(temp[1]).replace(', ', '_')}"]["vertices"].append([at, boundry])

#             del possible[0]
#         #case 1:
#         #    print("---------case1")
#         #    print(possible)                                                            


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
        #print(pairs[0][0], pairs[1][0], pairs[0][1], pairs[1][1])
        #x1 = [pairs[0][0], pairs[1][0]]
        #y1 = [pairs[0][1], pairs[1][1]]
        #plt.plot(x1, y1, "b")
        #print(pairs)                        
        
plt.show()

