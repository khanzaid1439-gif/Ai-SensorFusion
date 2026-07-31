class Predictor:

    def decide(self, detections, distance):

        if distance < 1.0:
            return "STOP"

        if distance < 2.0:
            return "SLOW DOWN"

        if len(detections) == 0:
            return "MOVE FORWARD"

        for obj in detections:

            if obj["label"] == "person":
                return "TURN LEFT"

            if obj["label"] == "car":
                return "TURN RIGHT"

        return "MOVE FORWARD"