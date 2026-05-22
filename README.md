# Vision Risk Detection System

웹캠 기반 Vision AI 시스템을 이용하여 사람을 탐지하고,
현재 위험 상황을 판단하는 Robot Perception 데모 프로젝트이다.

단순 객체 탐지를 넘어서:

- 객체 인식
- 상황 판단
- 행동 결정

흐름을 구현하는 것을 목표로 한다.

---

# 프로젝트 목적

본 프로젝트는 웹캠 영상 기반 사람 탐지를 통해
현재 위험 상황을 분석하고 행동 상태를 결정하는
Vision AI 시스템 구현을 목표로 한다.

특히 단순 YOLO 객체 탐지 구현이 아니라:

```text
인식
→ 상황 판단
→ 행동 결정
```

구조를 직접 구현하는 것에 초점을 두었다.

향후:

- Robot Perception
- Sensor Fusion
- Scene Understanding
- Robot AI
- Embodied AI

방향으로 확장하는 것을 목표로 한다.

---

# 주요 기능

- YOLOv8 기반 사람 탐지
- Bounding Box 기반 위험도 계산
- SAFE / WARNING / STOP 상태 분류
- 실시간 웹캠 시각화
- OpenCV 기반 UI 출력

---

# 시스템 구조

```text
웹캠 입력
→ 사람 탐지
→ 위험도 계산
→ 상황 판단
→ 행동 결정
→ 시각화
```

---

# 위험 판단 로직

Bounding Box 크기를 기반으로 위험도를 계산한다.

```python
Bounding Box 작음
→ SAFE

Bounding Box 중간
→ WARNING

Bounding Box 큼
→ STOP
```

카메라 화면에서 객체가 크게 보일수록
가까이 있다고 가정하였다.

---

# 프로젝트 구조

```bash
vision-risk-detection-system/
│
├── detector/
│   ├── person_detector.py
│   └── risk_calculator.py
│
├── utils/
│   └── draw_utils.py
│
├── outputs/
│
├── main.py
├── requirements.txt
├── README.md
└── .gitignore
```

---

# 사용 기술

## Vision AI

- YOLOv8
- OpenCV

## Language

- Python

---

# 개발 환경

- Windows 11
- Python 3.10
- VSCode

---

# 설치 방법

## 1. Repository Clone

```bash
git clone https://github.com/your-id/vision-risk-detection-system.git
```

---

## 2. 가상환경 생성

```bash
python -m venv venv
```

---

## 3. 가상환경 활성화

### Windows

```bash
venv\Scripts\activate
```

---

## 4. 패키지 설치

```bash
pip install -r requirements.txt
```

---

# 실행 방법

```bash
python main.py
```

---
