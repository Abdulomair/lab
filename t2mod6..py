class rectangle():
    """defined class for rectangle"""

class Point():
    """point"""
rec=rectangle()
rec.width=100
rec.height=200
rec.corn=Point()
rec.corn.x=0
rec.corn.y=0


def find_center(rec):
    p = Point()
    p.x = rec.corn.x + rec.width / 2.0
    p.y = rec.corn.y + rec.height / 2.0
    return p

center=(find_center(rec))
print((center.x,center.y))