import pandas as pd
from pathlib import Path

import torch

# Directory with images
image_dir = Path('../data/images')

# Initialize an empty list to store results
detection_results = []

# Load the YOLO model
model = torch.hub.load('ultralytics/yolov5', 'yolov5s') 

# Process each image
for image_path in image_dir.glob('*.jpg'):
    results = model(image_path)
    for _, row in results.pandas().xyxy[0].iterrows():
        detection_results.append({
            'image': image_path.name,
            'xmin': row['xmin'],
            'ymin': row['ymin'],
            'xmax': row['xmax'],
            'ymax': row['ymax'],
            'confidence': row['confidence'],
            'class': row['class'],
            'name': row['name']
        })

# Convert to DataFrame
df = pd.DataFrame(detection_results)

# Save to CSV
df.to_csv('detection_results.csv', index=False)
