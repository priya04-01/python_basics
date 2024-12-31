# area and circumference of circle
import math
def circle(r):
    area = math.pi * r * r
    circum = 2 * math.pi * r
    return area, circum
print(circle(7))