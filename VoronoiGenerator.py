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

#points = []
#for i in range(1, 8):
#      points.append([random.randint(0, 200), random.randint(0, 200)])  

#points = [[59, 55], [30, 88], [1, 93]] #[[186, 15], [162, 127], [25, 144]] this is pretty much just a bigger version of the first set
#points = [[186, 15], [162, 127], [25, 144]]
#points = [[19, 27], [131, 44], [38, 130]]
#points = [[57, 67], [21, 80], [79, 198]]
#points = [[17, 45], [62, 54], [152, 194]]

#points = [[71, 79], [167, 127], [178, 141]]#[[57, 67], [21, 80], [79, 198]]#[[17, 45], [62, 54], [152, 194]]#[[159, 66], [100, 166], [73, 197]]#[[71, 79], [167, 127], [178, 141]]
#points = [[159, 66], [100, 166], [73, 197]]

#points = [[106, 6], [88, 11], [9, 18], [2, 105], [20, 105], [115, 140], [52, 168]] #causes division by zero in getTimeAtX
#points = [[13, 23], [181, 40], [129, 55], [93, 100], [59, 127], [12, 160], [156, 163]] #---
points = [[76, 30], [196, 40], [165, 47], [104, 66], [128, 120], [88, 159], [166, 180]] #easy to see graph. In a previous, more broken version of the program, another line and intersection point near the one on the far right existed, which is necessary to correctly complete the graph

#points = [[194, 2], [94, 30], [11, 91], [88, 92], [57, 143], [43, 190], [6, 198]]
#points = [[12, 1], [97, 12], [168, 24], [98, 58], [182, 111], [102, 111], [72, 122]]


#		bottomleft, topleft, bottomright, topright
corners = [[0, 0], [0, 200], [200, 0], [200, 200]] #[ [defaultBounds[0][0], defaultBounds[1][1]], [defaultBounds[0][0], defaultBounds[0][1]], [defaultBounds[1][0], defaultBounds[1][1]], [defaultBounds[0][1], defaultBounds[1][0]] ]

cell = {}
#activeSites = []
#allVerts = []
removeVerts = []
finalCell = {}

plt.figure(figsize=(7, 7))
plt.ylim(defaultBounds[1][1], defaultBounds[1][0])
plt.xlim(defaultBounds[0][0], defaultBounds[0][1])
plt.title("pixel_plot")

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
    a, b, c, d, = pt1[0], pt1[1], pt2[0], pt2[1]
    n = (2 * ((-1 * c * b) + (c * t) + (a * d) - (a * t))) / (b-d)
    m = (-1 * (b-t) * (d-t)) + (( (c**2) * (b-t) ) + ( (a**2) * (d-t) )) / (b-d)
    x = ((-1 * n) - ( (n**2) - (4 * m))**0.5) / 2
    return x                

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
    a, b = pt1[0], pt1[1]
    y = (((x-a)**2) / (2 * (b-t))) + (0.5 * (b+t))
    return y   

def yAtX(pt1, pt2, x):
    a, b, c, d, = pt1[0], pt1[1], pt2[0], pt2[1]
    y = ((c-a) / (b-d)) * (x - ( (a+c)/2) ) + ((b+d)/2)
    return y
    
def xAtY(pt1, pt2, y):
    a, b, c, d, = pt1[0], pt1[1], pt2[0], pt2[1]
    x = ( (2 * y * (d-b)) - ((d**2) - (b**2)) + ((a**2) - (c**2)) ) / (2 * (a-c))
    return x

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
                                                                            
#print(allVerts)

#activeSites.extend([points[0], points[1]])
#activeSites.append(points[0])
#for i in range(2, points.__len__()):
#    activeSites.append(points[i])
#    for site1 in activeSites:
#        for site2 in activeSites:
#            if site2 != site1:
#                for site3 in activeSites:
#                    if site3 != site2 and site3 != site1:
                                                                                                            
#    print(activeSites)    
        

#for site in points:
#    for point2 in points:
#        if point2 != site:        
#            for point3 in points:   
#                if point3 != site and point3 != point2: #this system somehow gets one correct point, tho it has an incorrect point at several different times
#                    # the point found at time=13.6624 is in the correct location but was found in an incorrect way as the sweepline had not reached any sites yet, let alone one that could produce that normally
#                    #   (the point was produced by 3 of the parabolas opening upwards (since the sweepline was below them), so it was formed correctly but not under the correct circumstances)
#                    # the point found at time=75.009121 is the result of 3 parabolas intersecting when one of them should have been cut off by a circle event                    
#                    x = find3Intersect(site, point2, point3)
#                    t = getTimeAtX(site, point2, point3, x)
#                    y = getYAtTime(site, t, x)
#                    if t > defaultBounds[1][1] and t < defaultBounds[1][0]: #this somehow worked better
#                    #if t > points[0][1] and t < defaultBounds[1][0]:                    
#                        print(f"({site[0]}, {site[1]}) ({point2[0]}, {point2[1]}) ({point3[0]}, {point3[1]}) time: {t} at ({x}, {y})")
#                        cell.update({f"{str(site).replace(', ', '_')}" : {"point1":site, "point2":point2, "point3":point3, "time":t, "at":[x, y]}})

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
            print("removing", cell[site][cell[site].index(vert)])                    
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
                

def slope(pt1, pt2):
    return (pt1[1] - pt2[1]) / (pt1[0] - pt2[0])

def midPoint(pt1, pt2):
    return [ (pt1[0] + pt2[0]) / 2,  (pt1[1] + pt2[1]) / 2]        

def rotate(pt, origin, amount):
    x = ((pt[0] - origin[0]) * math.cos(amount)) - ((pt[1] - origin[1]) * math.sin(amount))
    y = ((pt[1] - origin[1]) * math.cos(amount)) + ((pt[0] - origin[0]) * math.sin(amount))
    x += origin[0]
    y += origin[1]        
    return [x, y]           

for site in cell:
    continue 
    for entry in cell[site]:    
        point1 = entry["point1"]
        point2 = entry["point2"]
        point3 = entry["point3"]

        temp = [point1, point2, point3]
        sortByY(temp)

        x = xAtY(temp[0], temp[1], defaultBounds[1][1]) #works for a majority of cases, broken by [[59, 55], [30, 88], [1, 93]] and [[21, 12], [27, 43], [174, 79]]
        plt.plot([x, entry["at"][0]], [0, entry["at"][1]], "m")

        #x = xAtY(temp[1], temp[2], defaultBounds[1][1])
        #plt.plot([x, entry["at"][0]], [0, entry["at"][1]], "m")        

        #x = xAtY(temp[0], temp[2], defaultBounds[1][1]) #works for several cases, but not all
        #plt.plot([x, entry["at"][0]], [0, entry["at"][1]], "m") 
        
        #x = xAtY(temp[0], temp[2], defaultBounds[1][0]) #works for several cases, but not all
        #plt.plot([x, entry["at"][0]], [200, entry["at"][1]], "c") 

        x = xAtY(temp[1], temp[2], defaultBounds[1][0])
        plt.plot([x, entry["at"][0]], [200, entry["at"][1]], "c")        

        

        start1x = find2IntersectAtTime(temp[0], temp[1], temp[1][1])
        start2x = find2IntersectAtTime(temp[0], temp[2], temp[2][1])
        start3x = find2IntersectAtTime(temp[1], temp[2], temp[2][1])
        
        start1y = yAtX(temp[0], temp[1], start1x)
        start2y = yAtX(temp[0], temp[2], start2x)
        start3y = yAtX(temp[1], temp[2], start3x)

        plt.plot([start1x, start2x, start3x], [start1y, start2y, start3y], "yo")
        plt.plot([temp[0][0], start1x, temp[1][0]], [temp[0][1], start1y, temp[1][1]], "y")
        plt.plot([temp[0][0], start2x, temp[2][0]], [temp[0][1], start2y, temp[2][1]], "y")
        plt.plot([temp[1][0], start3x, temp[2][0]], [temp[1][1], start3y, temp[2][1]], "y")

        slope1 = slope(entry["at"], [start1x, start1y])

        #x = (0 - start1y + (slope1 * start1x)) / slope1
        #plt.plot([x, entry["at"][0]], [0, entry["at"][1]], "k") 
        
        #x = (0 - start1y + (slope1 * start1x)) / slope1
        plt.plot([start1x, entry["at"][0]], [start1y, entry["at"][1]], "k")


        angle1 = math.atan(distance(entry["at"][0], entry["at"][1], temp[1][0], temp[1][1])/distance(entry["at"][0], entry["at"][1], temp[0][0], temp[0][1]))
        newPoint = rotate(temp[0], entry["at"], angle1)
        print(temp[0], angle1)                

        plt.plot([newPoint[0], entry["at"][0]], [newPoint[1], entry["at"][1]], "r")
           
        
        continue        

        #x = xAtY(temp[0], temp[1], defaultBounds[1][1])
        #plt.plot([x, entry["at"][0]], [0, entry["at"][1]], "m")

        mid1 = midPoint(temp[0], temp[1])
        mid2 = midPoint(temp[0], temp[2])
        mid3 = midPoint(temp[1], temp[2])

        slope1 = slope(mid1, [start1x, start1y])
        slope2 = slope(mid2, [start2x, start2y])
        slope3 = slope(mid3, [start3x, start3y])

        dist1i = distance(mid1[0], mid1[1], entry["at"][0], entry["at"][1])
        dist1s = distance(mid1[0], mid1[1], start1x, start1y)

        if dist1i < dist1s:
            if slope1 < 0:
                x = xAtY(temp[0], temp[1], defaultBounds[1][1])
                plt.plot([x, entry["at"][0]], [0, entry["at"][1]], "m")
            else:                                                                                                                                                                                             
                x = xAtY(temp[0], temp[1], defaultBounds[1][0])
                plt.plot([x, entry["at"][0]], [0, entry["at"][1]], "m")


#print(finalCell)

for site in cell:
        
    for entry in cell[site]:
        at = entry["at"]
        pt1 = entry["point1"]
        pt2 = entry["point2"]
        pt3 = entry["point3"]                           
        #f"{str(point).replace(', ', '_')}"
        print(pt1, pt2, pt3)
        try:
            site2 = cell[f"{str(pt2).replace(', ', '_')}"]
            for entry2 in site2:
                if entry2["point2"] == pt1 or entry2["point3"] == pt1:# or entry2["point2"] == pt3 or entry2["point3"] == pt3:
                    #finalCell[f"{str(pt2).replace(', ', '_')}"]["vertices"].append([entry["at"], entry2["at"]])
                    finalCell[site]["vertices"].append([entry["at"], entry2["at"]])
        except Exception as e:
            print(f"site2: {e} not in cell")                                

        #site3 = cell[f"{str(pt2).replace(', ', '_')}"]
        #print()
        #try:
        #    site3 = cell[f"{str(pt3).replace(', ', '_')}"]
        #    for entry3 in site3:
        #        if entry3["point2"] == pt1 or entry3["point3"] == pt1:# or entry2["point2"] == pt3 or entry2["point3"] == pt3:
                    #finalCell[f"{str(pt2).replace(', ', '_')}"]["vertices"].append([entry["at"], entry2["at"]])
        #            finalCell[site]["vertices"].append([entry["at"], entry3["at"]])
        #except Exception as e:
        #    print(f"site3: {e} not in cell")                                
                                                                                                         



for pt in points:
    plt.plot(pt[0], pt[1], "ro")

for site in cell:  
    #print(cell[site])
    #clr1, clr2, clr3 = random.random(), random.random(), random.random() 
    for entry in cell[site]:
        #if entry["at"][1] > 120 and entry["at"][1] < 130:       
        #    print(entry)
        print(entry)
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
        
plt.show()


