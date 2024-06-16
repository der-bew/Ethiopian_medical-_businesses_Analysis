import torch
from pathlib import Path

# Load the YOLO model
model = torch.hub.load('ultralytics/yolov5', 'yolov5s')  

# Directory with images
image_dir = Path('../data/images')

# Process each image
for image_path in image_dir.glob('*.jpg'):
    results = model(image_path)
    results.save()  # Save the result to disk
    print(results.pandas().xyxy[0])  # Print detection results
