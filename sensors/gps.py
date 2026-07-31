import random

class Lidar:

    def get_distance(self):

        distance = round(random.uniform(0.5, 10.0), 2)

        return distance

    import random

class GPS:

    def get_location(self):
        latitude = round(28.6139 + random.uniform(-0.001, 0.001), 6)
        longitude = round(77.2090 + random.uniform(-0.001, 0.001), 6)

        return latitude, longitude