from filterpy.kalman import KalmanFilter
import numpy as np

class SensorFusion:

    def __init__(self):

        self.kf = KalmanFilter(dim_x=1, dim_z=1)

        self.kf.x = np.array([[0.]])
        self.kf.F = np.array([[1.]])
        self.kf.H = np.array([[1.]])
        self.kf.P *= 1000.
        self.kf.R = 5
        self.kf.Q = 0.1

    def fuse(self, measurement):

        self.kf.predict()
        self.kf.update(np.array([[measurement]]))

        return float(self.kf.x[0][0])