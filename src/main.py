import cv2 

def main ():

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
        
        # 윈도우 창을 띄워서 프레임을 화면에 출력하는 것이다. 
        cv2.imshow('Webcam Test', frame)

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