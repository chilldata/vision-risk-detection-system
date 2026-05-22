from ultralytics import YOLO


class PersonDetector:

    def __init__(
        self,
        model_name="yolov8n.pt",
        confidence_threshold=0.5
    ):

        self.model = YOLO(model_name)
        self.confidence_threshold = confidence_threshold

    def detect(self, frame):

        results = self.model(
            frame,
            verbose=False
        )

        detections = []

        for result in results:

            boxes = result.boxes

            for box in boxes:

                class_id = int(box.cls[0])
                confidence = float(box.conf[0])

                # person class id = 0
                if (
                    class_id == 0 and
                    confidence >= self.confidence_threshold
                ):

                    x1, y1, x2, y2 = map(
                        int,
                        box.xyxy[0]
                    )

                    detections.append({
                        "bbox": (x1, y1, x2, y2),
                        "confidence": confidence
                    })

        return detections