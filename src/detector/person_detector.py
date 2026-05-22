from ultralytics import YOLO

# 카메라 프레임을 받아서 사람만 골라내서 위치와 신뢰도를 반환하는 클래스
class PersonDetector:

    def __init__(
        self,
        model_name="yolov8n.pt",
        confidence_threshold=0.5 # "이게 사람이다"라고 확신하는 정도. 0.5면 50% 이상 확신할 때만 검출한다.
    ):

        self.model = YOLO(model_name) # 모델 로딩 
        self.confidence_threshold = confidence_threshold

    def detect(self, frame):
        # YOLO 모델에 이미지를 넣어서 객체 탐지를 수행한다.
        results = self.model(frame, verbose=False)

        detections = []

        for result in results:

            boxes = result.boxes

            for box in boxes:

                class_id = int(box.cls[0]) # 이 객체가 무엇인지 가져온다.
                confidence = float(box.conf[0])

                # COCO Dataset 기준 person class id = 0
                if class_id == 0 and confidence >= self.confidence_threshold:
                    
                    # 사람 위치 좌표를 가져온다.
                    x1, y1, x2, y2 = map(int, box.xyxy[0])

                    detections.append({
                        "bbox": (x1, y1, x2, y2),
                        "confidence": confidence
                    })

        return detections