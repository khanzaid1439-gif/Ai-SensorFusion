import random

class Ultrasonic:

    def get_distance(self):

        distance = round(random.uniform(0.2, 4.0), 2)

        return distance