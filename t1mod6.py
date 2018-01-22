from math import*

class point(object):
	"""represents a point in 2-D space"""

def distance(p1, p2):
	distance =sqrt((p2.x - p1.x)**2 + (p2.y - p1.y)**2)
	return distance

p1 = point()
p2 = point()

p1.x = 3
p1.y = 6
p2.x= 8
p2.y = 4

print(distance(p1, p2))



