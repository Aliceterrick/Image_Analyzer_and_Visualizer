import boto3
import os
import math
import cv2

def draw_bbox(image, bbox, label, confidence, color=(0, 255, 0)):
    
    x_min, y_min, x_max, y_max = bbox

    cv2.rectangle(image, (x_min, y_min), (x_max, y_max), color, 2)

    text = f"{label} {confidence}"

    (text_width, text_height), baseline = cv2.getTextSize(text, cv2.FONT_HERSHEY_SIMPLEX, 0.5, 2)

    cv2.rectangle(
        image,
        (x_min, y_min - text_height - baseline),
        (x_min + text_width, y_min),
        color,
        thickness=-1
    )

    cv2.putText(
        image,
        text,
        (x_min, y_min - baseline),
        cv2.FONT_HERSHEY_SIMPLEX,
        0.5,
        (0, 0, 0),
        2
    )

    return image

def annotate_image(image, instances, image_path):
    """ draw the bounding boxes for the detected objects on a new image """

    for i in instances:
        draw_bbox(image, i["bbox"], i["label"], i["confidence"])

    image_name = os.path.basename(image_path)
    output_image_path = os.path.join("../data/annotated_images", f"cloud_annotated_{image_name}") 
    cv2.imwrite(output_image_path, image)

def cloud_detect(image_path, output_dir='output'):

    client = boto3.client('rekognition', region_name='us-east-1')

    with open(image_path, "rb") as image:
        response = client.detect_labels(Image={'Bytes': image.read()}, MaxLabels=10, MinConfidence=70)

    image = cv2.imread(image_path)
    h, w, _ = image.shape

    instances = []
    concepts = []

    for l in response['Labels']:

        if len(l["Instances"]) == 0:
            normalized = l["Confidence"] / 100
            concepts.append({
                "label": l["Name"].lower(),
                "confidence": math.floor(normalized * 100) / 100
            })

        for i in l["Instances"]:
            normalized = i["Confidence"] / 100
            instances.append({
                "label": l["Name"].lower(),
                "confidence": math.floor(normalized * 100) / 100,
                "bbox": [
                    int(i["BoundingBox"]["Left"] * w),
                    int(i["BoundingBox"]["Top"] * h),
                    int((i["BoundingBox"]["Left"] + i["BoundingBox"]["Width"]) * w),
                    int((i["BoundingBox"]["Top"] + i["BoundingBox"]["Height"]) * h)
                ]
            })

    annotate_image(image, instances, image_path)
    detections = {"instances": instances, "concepts": concepts}

    return detections