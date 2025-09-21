import cv2
from ultralytics import YOLO
import os
from pathlib import Path
# pip install ultralytics opencv-python
"""
리소스? 부족 시..
pip install --upgrade pip
pip install opencv-python-headless
pip install ultralytics
"""

def get_image_object(file_path):
    import torch
    print(f">>>>>{torch.cuda.is_available()}")
    metadata = {}
    try:
        # 1. YOLOv8 모델 불러오기 (사전 학습된 모델)
        model = YOLO("yolov8n.pt")  # 또는 yolov8s.pt, yolov8m.pt 등

        # 2. 이미지 불러오기
        image = cv2.imread(file_path)

        # 3. 객체 탐지 수행
        results = model(image, imgsz=320)

        # 5. 탐지된 객체 정보 출력
        print("탐지된 객체 목록:")
        detected_objects = []
        for box in results[0].boxes:
            # 클래스 ID → 이름
            cls_id = int(box.cls[0])
            class_name = model.names[cls_id]

            # 신뢰도
            confidence = float(box.conf[0])

            # 바운딩 박스 좌표 (x1, y1, x2, y2)
            x1, y1, x2, y2 = map(int, box.xyxy[0].tolist())

            # 출력
            # print(f"- {class_name} ({confidence:.2f}) 위치: ({x1}, {y1}), ({x2}, {y2})")
            detected_objects.append({
                "class" : class_name,
                "confidence" : f"{confidence:.2f}",
                "bbox" : f"({x1}, {y1}), ({x2}, {y2})"
            })


        if len(detected_objects) > 0:
            metadata["detected_objects"] = detected_objects

        # 4. 탐지 결과 시각화 (bounding box 그리기)
        annotated_frame = results[0].plot()

        file_path_name = file_path.split(".")[0]
        detected_file_path = f"{file_path_name}_detected_object.jpeg"
        print(detected_file_path)
        cv2.imwrite(detected_file_path, annotated_frame)

        # # 5. 결과 출력
        # cv2.imshow("YOLOv8 Detection", annotated_frame)
        # cv2.waitKey(0)
        # cv2.destroyAllWindows()
    except Exception as e:
        return f"{file_path} err : {e}"

    print("\n")
    for key in metadata:
        print(f"{key} : {metadata[key]}")

    format = Path(file_path).name.split(".")[1]
    return f"{format} - meta len : {len(metadata)}"


def test_image_object():
    file_name = None
    dir_path = "/Users/hayoung/workspace/metadata_collector/tmp"

    file_name = "DStation_Cam1_7Ent_Hall_L_01_0000013.jpg"

    reports = []
    for filename in os.listdir(dir_path):

        if file_name is None:
            file_path = os.path.join(dir_path, filename)
            report = get_image_object(file_path)
            if report:
                reports.append(report)
        else:
            if file_name == filename:
                file_path = os.path.join(dir_path, filename)
                report = get_image_object(file_path)
                if report:
                    reports.append(report)
                break


    print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> report <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<")
    for s in reports:
        print(s)