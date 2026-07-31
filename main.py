from sensors.camera import Camera
from sensors.lidar import Lidar
from sensors.ultrasonic import Ultrasonic
from sensors.gps import GPS

from fusion.kalman import SensorFusion

from ai.detect import ObjectDetector
from ai.predict import Predictor

import cv2

camera = Camera()

lidar = Lidar()

ultrasonic = Ultrasonic()

gps = GPS()

fusion = SensorFusion()

detector = ObjectDetector()

predictor = Predictor()

while True:

    frame = camera.get_frame()

    if frame is None:
        break

    lidar_distance = lidar.get_distance()

    ultrasonic_distance = ultrasonic.get_distance()

    latitude, longitude = gps.get_location()

    average_distance = (lidar_distance + ultrasonic_distance)/2

    fused_distance = fusion.fuse(average_distance)

    frame, detections = detector.detect(frame)

    decision = predictor.decide(detections, fused_distance)

    cv2.putText(
        frame,
        f"Distance : {fused_distance:.2f} m",
        (20,40),
        cv2.FONT_HERSHEY_SIMPLEX,
        0.8,
        (0,255,255),
        2
    )

    cv2.putText(
        frame,
        f"Decision : {decision}",
        (20,80),
        cv2.FONT_HERSHEY_SIMPLEX,
        0.8,
        (0,255,0),
        2
    )

    cv2.putText(
        frame,
        f"GPS : {latitude}, {longitude}",
        (20,120),
        cv2.FONT_HERSHEY_SIMPLEX,
        0.6,
        (255,255,0),
        2
    )

    cv2.imshow("AI Sensor Fusion", frame)

    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

camera.release()

cv2.destroyAllWindows()