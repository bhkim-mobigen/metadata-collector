import cv2
from ultralytics import YOLO
# pip install ultralytics opencv-python
"""
pip install --upgrade pip
pip install opencv-python-headless
pip install ultralytics
"""

def test_image_object():
    # 1. YOLOv8 모델 불러오기 (사전 학습된 모델)
    model = YOLO("yolov8n.pt")  # 또는 yolov8s.pt, yolov8m.pt 등

    # 2. 이미지 불러오기
    image_path = "/Users/hayoung/Downloads/1.jpeg"
    # image_path = "/Users/hayoung/Downloads/8dpbor7pPRIBoOYHSZbe47R0P1E.jpg"
    image = cv2.imread(image_path)

    # 3. 객체 탐지 수행
    results = model(image)

    # 5. 탐지된 객체 정보 출력
    print("탐지된 객체 목록:")
    for box in results[0].boxes:
        # 클래스 ID → 이름
        cls_id = int(box.cls[0])
        class_name = model.names[cls_id]

        # 신뢰도
        confidence = float(box.conf[0])

        # 바운딩 박스 좌표 (x1, y1, x2, y2)
        x1, y1, x2, y2 = map(int, box.xyxy[0].tolist())

        # 출력
        print(f"- {class_name} ({confidence:.2f}) 위치: ({x1}, {y1}), ({x2}, {y2})")

    # # 4. 탐지 결과 시각화 (bounding box 그리기)
    # annotated_frame = results[0].plot()
    #
    # # 5. 결과 출력
    # cv2.imshow("YOLOv8 Detection", annotated_frame)
    # cv2.waitKey(0)
    # cv2.destroyAllWindows()
