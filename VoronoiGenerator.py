import math
def returnCircleCenter(point1, point2, point3):
    temp = point2[0] * point2[0] + point2[1] * point2[1]
    bc = (point1[0] * point1[0] + point1[1] * point1[1] - temp) / 2
    cd = (temp - point3[0] * point3[0] - point3[1] * point3[1]) / 2
    det = (point1[0] - point2[0]) * (point2[1] - point3[1]) - (point2[0] - point3[0]) * (point1[1] - point2[1])

    if abs(det) < 1.0e-6:
        return (None, math.inf)

    # Center of circle
    cx = (bc * (point2[1] - point3[1]) - cd * (point1[1] - point2[1])) / det
    cy = ((point1[0] - point2[0]) * cd - (point2[0] - point3[0]) * bc) / det

    radius = math.sqrt((cx - point1[0]) ** 2 + (cy - point1[1]) ** 2)
    return [(cx, cy), radius]