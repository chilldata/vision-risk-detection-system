import cv2 
from detector.person_detector import PersonDetector

def main ():

    detector = PersonDetector()

    # 웹캠에서 영상을 받아오는 객체를 만든다. 0은 첫번째로 연결된 카메라다.
    cap = cv2.VideoCapture(0)

    # 웹캠 연결 실패 확인 
    if not cap.isOpened():
        print("웹캠을 열 수 없습니다.")
        return
    
    while True:

        # ret → 읽기 성공 여부 (True/False)
        # frame → 실제 이미지 데이터 (numpy 배열)
        ret, frame = cap.read()

        # 프레임 읽기 실패
        if not ret: 
            print("프레임을 읽을 수 없습니다.")
            break
        
        # 현재 frame을 YOLO에 넣어서 사람 탐지
        detections = detector.detect(frame)
        
        for detection in detections:

            x1, y1, x2, y2 = detection["bbox"]

            confidence = detection["confidence"]

            cv2.rectangle(
                frame,
                (x1, y1),
                (x2, y2),
                (0, 255, 0),
                2
            )

            label = f"Person {confidence:.2f}"

            # confidence 출력
            cv2.putText(
                frame,
                label,
                (x1, y1 - 10),
                cv2.FONT_HERSHEY_SIMPLEX,
                0.7,
                (0, 255, 0),
                2
            )

        cv2.imshow("Vision Risk Detection System", frame)

        # ESC 누르면 종료 
        if cv2.waitKey(1) & 0xFF == 27:
            break
    
    # 사용한 자원 반납한다.
    # 카메라는 하드웨어 자원이라 명시적으로 해제하지 않으면 다른 프로그램이 사용하지 못한다.
    cap.release()
    cv2.destroyAllWindows()

# 자원 해제 
if __name__ == "__main__":
    main()