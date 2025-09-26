import sys
import os
import json
from cloud_detect import cloud_detect
from local_detect import local_detect

if len(sys.argv) != 2 or not os.path.exists(sys.argv[1]):
    print("Please provide a valid image path")
    sys.exit(1)
    
image_path = sys.argv[1]
image_name = os.path.basename(image_path)

local_detect = local_detect(image_path)
cloud_detect = cloud_detect(image_path)
json_data = {
    "image": image_name,
    "local": local_detect,
    "cloud": cloud_detect
}

json_path = os.path.join("../data/results", f"detections_{os.path.splitext(image_name)[0]}.json")
with open(json_path, 'w', encoding='utf-8') as f:
    json.dump(json_data, f, indent=2, ensure_ascii=False)