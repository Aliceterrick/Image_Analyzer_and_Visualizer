# 🖼️ Image_Analyzer-Vizualizer

## 📌 Overview

This project demonstrates a complete image processing and visualization pipeline, comparing local analysis (YOLO / OpenCV) with cloud analysis (AWS Rekognition).
It includes:

- a Python module for local and cloud image analysis,

- a .NET (C#) backend exposing a REST API,

- an Angular frontend providing an interactive dashboard to visualize results and annotated images.

This project was designed to explore different image processing architectures (embedded vs. cloud) and to discover angular.

## 🔍 Part 1 — Local Analysis with YOLO (Python)

- Loads images from a public dataset (MS COCO).

- Object detection using YOLOv5.

- Generates JSON output:

``` json
{
  "image": "000000163118.jpg",
  "local": [
    {
      "label": "person",
      "confidence": 0.9,
      "bbox": [151, 75, 294, 377]
    },
    {
      "label": "frisbee",
      "confidence": 0.87,
      "bbox": [274, 54, 321, 84]
    }
  ]
}
```

- Generates annotated images (bounding boxes + labels).

## ☁️ Part 2 — Cloud Analysis with AWS Rekognition

- Uses the AWS Rekognition API through boto3.

- For each image:

 - Instance detection (specific objects with bounding boxes),

 - Concept detection (general categories like People, Clothing).

- Results are stored in JSON:

``` json
"cloud": {
  "instances": [
    { "label": "Person", "confidence": 0.99, "bbox": [151, 79, 293, 375] }
  ],
  "concepts": [
    { "label": "Clothing", "confidence": 0.97 }
  ]
}
```

- Generates annotated images equivalent to YOLO for side-by-side comparison.

## 🖥️ Part 3 — Backend .NET (C#)

- REST API developed with ASP.NET Core 7.

- Provides:

 - List of available results (/api/results),

 - Analysis details (/api/results/{id}),

 - Static files (original images, annotated images, JSON).

- Manages JSON storage in /data/results/ and serves /data/images/ and /data/annotated_images/.

- Configured with CORS to allow requests from Angular.

## 🌐 Part 4 — Angular Frontend

- Main features:

 - List of available results (selection buttons).

 - Display of the original image.

 - Side-by-side comparison:

   - Local annotated image + YOLO detections,

   - Cloud annotated image + Rekognition detections.

- Modern and responsive SCSS styling:

  - Styled buttons,

  - White rounded cards,

  - Light gray background,

  - Grid layout for comparisons.

## 🚀 Installation & Execution

1. Local / Cloud Analysis (Python)

``` bash
cd analyzer
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python analyze.py --input ./data/images --output ./data/results
```

2. Backend .NET

```bash
cd Backend
dotnet restore
dotnet run
```
API available at http://localhost:5102

3. Frontend Angular

``` bash
cd frontend
npm install
ng serve
```
Dashboard available at http://localhost:4200