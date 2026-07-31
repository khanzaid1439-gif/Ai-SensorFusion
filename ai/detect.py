from ultralytics import YOLO
import cv2


class ObjectDetector:

    def __init__(self):
        self.model = YOLO("yolov8n.pt")

    def detect(self, frame):

        results = self.model(frame, verbose=False)

        detections = []

        for result in results:
            for box in result.boxes:

                x1, y1, x2, y2 = map(int, box.xyxy[0])

                confidence = float(box.conf[0])

                class_id = int(box.cls[0])

                label = self.model.names[class_id]

                detections.append({
                    "label": label,
                    "confidence": confidence,
                    "box": (x1, y1, x2, y2)
                })

                cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 2)

                cv2.putText(
                    frame,
                    f"{label} {confidence:.2f}",
                    (x1, y1 - 10),
                    cv2.FONT_HERSHEY_SIMPLEX,
                    0.5,
                    (0, 255, 0),
                    2
                )

        return frame, detections