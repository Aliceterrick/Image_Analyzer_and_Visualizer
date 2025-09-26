from ultralytics import YOLO
import cv2
import os

def local_detect(image_path):

    model = YOLO('yolov5su.pt')
    
    result = model(image_path, verbose=False)[0]

    image_name = os.path.basename(image_path)
    output_image_path = os.path.join("../data/annotated_images", f"local_annotated_{image_name}")

    result.save(output_image_path)

    detections = []


    for box in result.boxes:
        label = model.names[int(box.cls[0])]
        bbox = box.xyxy[0].tolist()
             
        detections.append({
            "label": label,
            "confidence": round(float(box.conf[0]), 2),
            "bbox": [
                int(bbox[0]),
                int(bbox[1]),
                int(bbox[2]),
                int(bbox[3])
            ]
        })

    return detections

