import cv2

from detector.person_detector import PersonDetector
from detector.risk_calculator import RiskCalculator

from utils.draw_utils import (
    draw_detection,
    draw_status_panel
)


def get_overall_risk(
    risk_results,
    person_count
):

    # 사람이 없으면 SAFE
    if not risk_results:

        return {
            "risk_level": "SAFE",
            "action": "MOVE"
        }

    priority = {
        "SAFE": 0,
        "WARNING": 1,
        "STOP": 2
    }

    # 가장 위험한 상태 선택
    highest_risk = max(
        risk_results,
        key=lambda x: priority[x]
    )

    # WARNING 사람이 3명 이상이면 STOP
    warning_count = risk_results.count(
        "WARNING"
    )

    if warning_count >= 3:

        return {
            "risk_level": "STOP",
            "action": "STOP"
        }

    # 상태별 행동 결정
    if highest_risk == "SAFE":

        return {
            "risk_level": "SAFE",
            "action": "MOVE"
        }

    elif highest_risk == "WARNING":

        return {
            "risk_level": "WARNING",
            "action": "SLOW"
        }

    else:

        return {
            "risk_level": "STOP",
            "action": "STOP"
        }


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

        # 사람 탐지
        detections = detector.detect(
            frame
        )

        risk_results = []

        for detection in detections:

            bbox = detection["bbox"]

            confidence = detection["confidence"]

            # 위험도 계산
            risk_result = risk_calculator.calculate(
                bbox,
                frame.shape
            )

            risk_level = risk_result[
                "risk_level"
            ]

            color = risk_result[
                "color"
            ]

            occupancy_ratio = (
                risk_result[
                    "occupancy_ratio"
                ] * 100
            )

            # 전체 위험도 계산용 저장
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

        # 전체 위험도 계산
        overall_result = get_overall_risk(
            risk_results,
            len(detections)
        )

        # 상단 상태 패널 출력
        draw_status_panel(
            frame,
            overall_result["risk_level"],
            len(detections),
            overall_result["action"]
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