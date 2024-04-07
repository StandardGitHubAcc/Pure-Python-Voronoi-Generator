import matplotlib.pyplot as plt
import random
import math
from math import *

defaultBounds = [[0, 200], [200, 0]]
points = [(50, 50), (25, 25), (75, 75), (98, 70)]
#points = [(50, 50), (25, 20), (75, 75), (98, 70)]
#points = [(30, 40), (25, 60), (80, 97)]
#		bottomleft, topleft, bottomright, topright
corners = [[0, 0], [0, 200], [200, 0], [200, 200]] #[ [defaultBounds[0][0], defaultBounds[1][1]], [defaultBounds[0][0], defaultBounds[0][1]], [defaultBounds[1][0], defaultBounds[1][1]], [defaultBounds[0][1], defaultBounds[1][0]] ]

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
             
            # Range of the array is from 0 to n-i-1
            # Swap the elements if the element found 
            #is greater than the adjacent element
            dist1 = distance(target[0], target[1], array[j][0], array[j][1])
            dist2 = distance(target[0], target[1], array[j+1][0], array[j+1][1])
            
            if dist1 > dist2:
                array[j], array[j + 1] = array[j + 1], array[j]

def find3Intersect(pt1, pt2, pt3): # division by zero happens with the points (50, 50) (25, 25) (75, 75)
    a, b, c, d, e, f = pt1[0], pt1[1], pt2[0], pt2[1], pt3[0], pt3[1]
    if (2 * ( ((a-e)*(b-d)) - ((a-c)*(b-f))) ) != 0:
        x = ( ( ((a**2) - (e**2))*(b-d) ) - ( ((a**2) - (c**2)) * (b-f) ) - ( (d-f)*(b-f)*(b-d) )) / (2 * ( ((a-e)*(b-d)) - ((a-c)*(b-f))) )
        return x
    else: # i need to have it return the midpoint between the site and nearest site if there is division by zero, because that means that the two lines are parallel and the farther site will not be valid
        #print(( ( ((a**2) - (e**2))*(b-d) ) - ( ((a**2) - (c**2)) * (b-f) ) - ( (d-f)*(b-f)*(b-d) )), (2 * ( ((a-e)*(b-d)) - ((a-c)*(b-f))) ))
        #print(f"({a}, {b}) ({c}, {d}) ({e}, {f})")
        #print(a-e, b-d, a-c, b-f)                      
        return (a - c)/2   #returning (a-c)/2 or 0 doesn't seem to make a difference
        #return 0       

def getTimeAtX(pt1, pt2, pt3, x):
    a, b, c, d, e, f = pt1[0], pt1[1], pt2[0], pt2[1], pt3[0], pt3[1]
    j = b-d
    k = -( (a**2) + (b**2) ) + (c**2) + (d**2) + (2 * x * (a-c))
    L = f*( (a**2) - (c**2) + (b**2) - (d**2) - (2 * x * (a-c)) ) - (( ((x-e)**2) + (f**2) )*(b-d))
    t = ((-1 * k) - ( (k**2) - (4 * j * L))**0.5) / (2 * j)
    return t

def getYAtTime(pt1, t, x):
    a, b = pt1[0], pt1[1]
    y = (((x-a)**2) / (2 * (b-t))) + (0.5 * (b+t))
    return y    

for site in points:
    for point2 in points:
        if point2 != site:        
            for point3 in points:   
                if point3 != site and point3 != point2: #this system somehow gets one correct point, tho it has an incorrect point at several different times
                    # the point found at time=13.6624 is in the correct location but was found in an incorrect way as the sweepline had not reached any sites yet, let alone one that could produce that normally
                    #   (the point was produced by 3 of the parabolas opening upwards (since the sweepline was below them), so it was formed correctly but not under the correct circumstances)
                    # the point found at time=75.009121 is the result of 3 parabolas intersecting when one of them should have been cut off by a circle event                    
                    x = find3Intersect(site, point2, point3)
                    t = getTimeAtX(site, point2, point3, x)
                    y = getYAtTime(site, t, x)
                    if t > defaultBounds[1][1] and t < defaultBounds[1][0]:
                        print(f"({site[0]}, {site[1]}) ({point2[0]}, {point2[1]}) ({point3[0]}, {point3[1]}) time: {t} at ({x}, {y})")
                        cell.update({f"{str(site).replace(', ', '_')}" : {"point1":site, "point2":point2, "point3":point3, "time":t, "at":[x, y]}})

plt.figure(figsize=(7, 7))
plt.ylim(defaultBounds[1][1], defaultBounds[1][0])
plt.xlim(defaultBounds[0][0], defaultBounds[0][1])

plt.title("pixel_plot")

for pt in points:
    plt.plot(pt[0], pt[1], "ro")

for site in cell:  
    print(cell[site])
    clr1, clr2, clr3 = random.random(), random.random(), random.random() 
    
    plt.plot(cell[site]["at"][0], cell[site]["at"][1], "go")#, color=(clr1, clr2, clr3))
    #plt.plot(cell[site]["at"][0], cell[site]["at"][1], color=(0.5, 0.5, 0.5))
    plt.plot([cell[site]["point2"][0], cell[site]["at"][0], cell[site]["point3"][0], cell[site]["at"][0], cell[site]["point1"][0]], [cell[site]["point2"][1], cell[site]["at"][1], cell[site]["point3"][1], cell[site]["at"][1], cell[site]["point1"][1]], "g") 
    #print(clr1, clr2, clr3)        
    

plt.show()