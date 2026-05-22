import cv2


def draw_detection(
    frame,
    bbox,
    label,
    color
):

    x1, y1, x2, y2 = bbox

    # Bounding Box
    cv2.rectangle(
        frame,
        (x1, y1),
        (x2, y2),
        color,
        2
    )

    # Label
    cv2.putText(
        frame,
        label,
        (x1, y1 - 10),
        cv2.FONT_HERSHEY_SIMPLEX,
        0.7,
        color,
        2
    )


def draw_status_panel(
    frame,
    risk_level,
    person_count,
    action
):

    # 상태별 색상
    if risk_level == "SAFE":

        color = (0, 255, 0)

    elif risk_level == "WARNING":

        color = (0, 255, 255)

    else:

        color = (0, 0, 255)

    # 상단 상태 패널 배경
    cv2.rectangle(
        frame,
        (0, 0),
        (frame.shape[1], 60),
        (30, 30, 30),
        -1
    )

    # 상태 텍스트
    status_text = (
        f"STATUS : {risk_level} | "
        f"ACTION : {action} | "
        f"COUNT : {person_count}"
    )

    # 상태 텍스트 출력
    cv2.putText(
        frame,
        status_text,
        (20, 38),
        cv2.FONT_HERSHEY_SIMPLEX,
        0.55,
        color,
        2
    )