class RiskCalculator:

    def __init__(
        self,
        safe_threshold=0.08,
        warning_threshold=0.20
    ):

        self.safe_threshold = safe_threshold
        self.warning_threshold = warning_threshold

    def calculate(self, bbox, frame_shape):

        x1, y1, x2, y2 = bbox

        # Bounding Box 크기 계산
        width = x2 - x1
        height = y2 - y1

        bbox_area = width * height

        # 전체 화면 크기 계산
        frame_height, frame_width = frame_shape[:2]

        frame_area = frame_width * frame_height

        # 화면 점유율 계산
        occupancy_ratio = bbox_area / frame_area

        # 위험 상태 판단
        if occupancy_ratio < self.safe_threshold:

            return {
                "risk_level": "SAFE",
                "color": (0, 255, 0),
                "occupancy_ratio": occupancy_ratio
            }

        elif occupancy_ratio < self.warning_threshold:

            return {
                "risk_level": "WARNING",
                "color": (0, 255, 255),
                "occupancy_ratio": occupancy_ratio
            }

        else:

            return {
                "risk_level": "STOP",
                "color": (0, 0, 255),
                "occupancy_ratio": occupancy_ratio
            }