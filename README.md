# Ethiopian Medical Business Analysis
This repository contains code and data for analyzing Ethiopian medical businesses, focusing on extracting and processing data from Telegram channels using object detection with YOLOv5. The project is structured to handle data scraping, object detection, data processing, and serving the processed data via a FastAPI web service.

## Repository Structure

```
    Ethiopian_medical_businesses_Analysis/
    ├── .dvc/
    ├── .github/
    ├── data/
    ├── notebooks/
    │ └── EDA.ipynb
    ├── src/
    │ ├── Scrape_scripts/
    │ │ ├── main.py
    │ │ ├── tg_data_scrape.py
    │ │ └── tg_image_scrape.py
    │ ├── model/
    │ │ ├── detect_objects.py
    │ │ ├── handler.py
    │ │ ├── insert_data.py
    │ │ ├── process_results.py
    │ │ └── visualizer.py
    │ ├── transformation/ethio_medical_business/
    ├── analyses/
    ├── macros/
    ├── models/
    ├── seeds/
    │ └── seeds.yml
    ├── snapshots/
    ├── tests/
    ├── web_service/
    ├── .dvcignore
    ├── .gitignore
    ├── README.md
    ├── requirements.txt
    ├── test.db
    ├── yolov5s.pt
    └── dbt_project.yml

```


## Setup Instructions

### 1. Set Up the Environment

Create a virtual environment and install the required dependencies:

```bash
# Create a virtual environment
python -m venv venv

# Activate the virtual environment
# On Windows:
venv\Scripts\activate
# On macOS/Linux:
source venv/bin/activate

# Install the necessary packages
pip install -r requirements.txt
```

### 2. Clone the YOLOv5 Repository

```
git clone https://github.com/ultralytics/yolov5.git
cd yolov5
pip install -r requirements.txt
cd ..
```

### 3. Download Images from Telegram

Edit `tg_image_scrape.py` with your own Telegram API credentials and run the script to download images:

```
python src/Scrape_scripts/tg_image_scrape.py
```
### 4. Detect Objects in Images

Run the detect_objects.py script to detect objects in the downloaded images:

```
python src/model/detect_objects.py
```

### 5. Process Detection Results

Run the process_results.py script to process detection results:

```
python src/model/process_results.py
```

### 6. Insert Detection Data into Database

Run the insert_data.py script to insert the processed data into the database:

```
python src/model/insert_data.py
```

### 7. Run the FastAPI Web Service

Run the FastAPI application to serve the processed data:

```
uvicorn src/web_service.main:app --reload
```
Access the API endpoints:

    To get detections: http://127.0.0.1:8000/detections/
    To create a detection: Use an HTTP client like Postman or cURL to POST data to http://127.0.0.1:8000/detections/.

### Project Components
#### Data Scraping

Scripts for scraping data from Telegram channels:

- src/Scrape_scripts/main.py
- src/Scrape_scripts/tg_data_scrape.py
- src/Scrape_scripts/tg_image_scrape.py

#### Object Detection and Processing

Scripts for detecting objects in images and processing the results:

- src/model/detect_objects.py
- src/model/handler.py
- src/model/insert_data.py
- src/model/process_results.py
    - src/model/visualizer.py

#### Notebooks

Exploratory Data Analysis (EDA):

- notebooks/EDA.ipynb

#### Web Service

FastAPI web service for serving the processed data:

- src/web_service/main.py

#### Database and Configuration

    - test.db: SQLite database file
    - dbt_project.yml: DBT project configuration
    - seeds.yml: Seeds configuration

### License

This project is licensed under the MIT License. See the [LICENSE]() file for details.
