#https://stackoverflow.com/questions/28504737/how-to-plot-a-single-point-in-matplotlib
#https://www.geeksforgeeks.org/create-2d-pixel-plot-in-python/
#https://stackoverflow.com/questions/66238749/how-to-find-the-closest-coordinate-from-a-list-of-points

import numpy as np
import matplotlib.pyplot as plt
#import math

# data1 = np.random.random((3,7))    
# data2 = np.random.random((4,5))  
# 
#plt.figure(figsize=(7, 7)).add_subplot().set_aspect('equal')
plt.figure(figsize=(7, 7))
plt.ylim(0, 200)
plt.xlim(0, 200)

# 
plt.title("pixel_plot")

#points = [[50, 50], [25, 25], [75, 75]]
points = [(50, 50), (25, 25), (75, 75)]

for pt in points:
	plt.plot(pt[0], pt[1], "ro")



#for i in range(0, points.__len__()):
#	print(i)
#	print(points[i])


for pt in points:

	points2 = points.copy()
	points2.remove(pt)

	xy = np.array(points2).T

	# euclidean distance
	d = ( (xy[0] - pt[0]) ** 2 + (xy[1] - pt[1]) ** 2) ** 0.5

	closest_idx = np.argmin(d)
	closest = points2[closest_idx]

	#print(pt, closest)

	a = pt[0]
	b = pt[1]
	c = closest[0]
	d = closest[1]

	def solver(a, b, c, d, x):
		m = (b - d) / (a - c)
		#y = (-1 / m) * (x - a) + b

		mPtX = (a + c) / 2
		mPtY = (b + d) / 2

		plt.plot(mPtX, mPtY, "yo")

		y = (-1 / m) * (x - mPtX) + mPtY

		#b2 = mPtY + (1 / m) * mPtX

		#y = (-1 / m) * (x - mPtX) + b2

		print((a, b), (c, d), (x, y), (-1 / m), (mPtX, mPtY))
		#plt.plot([0, mPtY + mPtX], [mPtX, mPtY], "-bo")
		#plt.plot([0, 100], [7, 30])
		#print((0, mPtY + mPtX), (mPtX, mPtY))
		return y
		#return ( -(d ** 2) - (c ** 2) + (2 * c * x) + (b ** 2) + (a ** 2) - (2 * a * x) ) / ( (-2 * d) + (2 * b) )

	x1 = a + 20
	x2 = a - 20

	y1 = solver(a, b, c, d, x1)
	y2 = solver(a, b, c, d, x2)

	plt.plot([x1, x2], [y1, y2], "-go")

	
#plt.plot([0, 50], [50, 0], "-bo")

plt.show()