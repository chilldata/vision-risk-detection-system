import cv2

from detector.person_detector import PersonDetector
from detector.risk_calculator import RiskCalculator

from utils.draw_utils import (
    draw_detection,
    draw_status_panel
)


def get_highest_risk(
    risk_results
):

    if not risk_results:
        return "SAFE"

    priority = {
        "SAFE": 0,
        "WARNING": 1,
        "STOP": 2
    }

    highest = max(
        risk_results,
        key=lambda x: priority[x]
    )

    return highest


def main():

    detector = PersonDetector()

    risk_calculator = RiskCalculator()

    cap = cv2.VideoCapture(
        0,
        cv2.CAP_DSHOW
    )

    if not cap.isOpened():
        print("웹캠을 열 수 없습니다.")
        return

    while True:

        ret, frame = cap.read()

        if not ret:
            print("프레임을 읽을 수 없습니다.")
            break

        detections = detector.detect(frame)

        risk_results = []

        for detection in detections:

            bbox = detection["bbox"]

            confidence = detection["confidence"]

            # 위험도 계산
            risk_result = risk_calculator.calculate(
                bbox,
                frame.shape
            )

            risk_level = risk_result["risk_level"]

            color = risk_result["color"]

            occupancy_ratio = (
                risk_result["occupancy_ratio"] * 100
            )

            risk_results.append(
                risk_level
            )

            # 출력 텍스트
            label = (
                f"{risk_level} | "
                f"{occupancy_ratio:.1f}% | "
                f"{confidence:.2f}"
            )

            # Bounding Box 출력
            draw_detection(
                frame,
                bbox,
                label,
                color
            )

        # 최고 위험 상태 계산
        highest_risk = get_highest_risk(
            risk_results
        )

        # 상단 상태 패널 출력
        draw_status_panel(
            frame,
            highest_risk,
            len(detections)
        )

        cv2.imshow(
            "Vision Risk Detection System",
            frame
        )

        if cv2.waitKey(1) & 0xFF == 27:
            break

    cap.release()
    cv2.destroyAllWindows()


if __name__ == "__main__":
    main()