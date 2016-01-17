import math

class Point():

    def __init__(self, latitude, longitude):
        self.latitude = latitude
        self.longitude = longitude

# Calculated Using the Haversine Function
def calculate_distance(PointX, PointY):
    RADIUS_EARTH = 6371.0  # in km
    lat1 = toRads(PointX.latitude)
    lat2 = toRads(PointY.latitude)
    long1 = toRads(PointX.longitude)
    long2 = toRads(PointY.longitude)

    return 2 * RADIUS_EARTH * math.asin(math.sin((lat1 - lat2)/2.0)**2 + math.cos(lat1) * math.cos(lat2) * math.sin((long1 - long2)/2)**2)**0.5


def toRads(degrees):
    return degrees * math.pi/180.0

def calculate_shorter_pair(A, B, C, D):
    distance_AB = calculate_distance(A, B)
    distance_CD = calculate_distance(C, D)

    if distance_AB > distance_CD:
        print "Travelling from Point A to Point B is shorter than Point C to Point D"
    elif distance_AB < distance_CD:
        print "Travelling from Point C to Point D is shorter than Point A to Point B"
    else:
        print "The distances are equal"

def main():
    A = Point(1, 1)
    B = Point(2, 2)
    C = Point(1, 1)
    D = Point(2, 2)

    calculate_shorter_pair(A, B, C, D)

if __name__ == "__main__":
    main()
