import matplotlib.pyplot as plt
import math


def get_intersections(x0, y0, r0, x1, y1, r1):
    # circle 1: (x0, y0), radius r0
    # circle 2: (x1, y1), radius r1

    d = math.sqrt((x1 - x0) ** 2 + (y1 - y0) ** 2)

    # non intersecting
    if d > r0 + r1:
        return None
    # One circle within other
    if d < abs(r0 - r1):
        return None
    # coincident circles
    if d == 0 and r0 == r1:
        return None
    else:
        a = (r0 ** 2 - r1 ** 2 + d ** 2) / (2 * d)
        h = math.sqrt(r0 ** 2 - a ** 2)
        x2 = x0 + a * (x1 - x0) / d
        y2 = y0 + a * (y1 - y0) / d
        x3 = x2 + h * (y1 - y0) / d
        y3 = y2 - h * (x1 - x0) / d

        x4 = x2 - h * (y1 - y0) / d
        y4 = y2 + h * (x1 - x0) / d

        return [x3, y3, x4, y4]

x1 = 3
y1 = 3
r1 = 2
x2 = 5
y2 = 5
r2 = 2

color = ['red', 'red']
intersections = get_intersections(x1, y1, r1, x2, y2, r2)
points = [[intersections[0], intersections[1]], [intersections[2], intersections[3]]]

figure, axes = plt.subplots()
plt.axis('square')
# Set the range of x-axis
plt.xlim(0, 20)
# Set the range of y-axis
plt.ylim(0, 20)
# draw circles

axes.add_artist(plt.Circle((x1, y1), r1))
axes.add_artist(plt.Circle((x2, y2), r2))

    # plot intersection points
plt.scatter(points[0], points[1], c=color)

plt.show()
#for i in range(0, 10):
#    axes.add_artist(plt.Circle((x1, y1), r1))
#    r1 = r1+1
#    plt.show()



