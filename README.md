# PiCamera Object Detection with Dynamic Class Configuration

This repository features the `ObjectDetector` class, designed to enable real-time object detection on Raspberry Pi devices using PiCamera2 and a YOLO model. The class is uniquely designed to dynamically load class names from a text file and execute custom actions based on detected objects, allowing for easy customization and scalability.

## Features

- **Dynamic Class Loading:** Load class names from a text file, making it easy to switch between different models or datasets.
- **Real-Time Object Detection:** Uses the YOLO model integrated with PiCamera2 for detecting objects in video streams in real-time.
- **Custom Action Execution:** Associate custom functions with detected object classes, which are executed based on the confidence threshold.

## Requirements

- Raspberry Pi (3/4/5) with Camera Module
- raspian os Bookworm
- Python 3.6 or higher
- OpenCV
- pandas
- ultralytics YOLO
- cvzone
- picamera2

Ensure your PiCamera is correctly set up and tested on your Raspberry Pi before proceeding.

## Installation

First, clone this repository to your Raspberry Pi:

```bash
git clone https://github.com/m0hamadhassan/picamera2-YOLO
cd picamera2-YOLO
```

Install the necessary Python packages if they are not already installed:

```bash
pip install opencv-python-headless pandas ultralytics cvzone picamera2
```

## Usage

To use the `ObjectDetector`, perform the following steps:

1. **Create a Text File for Classes:** Create a text file listing the classes your YOLO model can detect, one per line. This file will be read by the `ObjectDetector`.
2. **Define Functions for Actions:** Write Python functions that define what should happen when each class is detected.
3. **Configure and Run the Detector:** Initialize the `ObjectDetector` with your model, classes file, confidence threshold, and a map of functions.

### Example

```python
from object_detector import ObjectDetector

def handle_green_light():
    print("Green Light detected: Go")

def handle_hump():
    print("Hump detected: Slow down")

# Add other necessary functions

function_map = {
    "Green Light": handle_green_light,
    "Hump": handle_hump,
    # Map other classes to their functions
}

# Initialize the detector
detector = ObjectDetector('model/newTrain.pt', 'config/classes.txt', 0.8, function_map)

# Start the detection process
detector.run()
```

### ObjectDetector Class

#### Initialization Parameters:

- **model_path**: Path to the trained YOLO model file.
- **classes_file_path**: Path to the text file containing class names.
- **confidence_threshold**: Minimum confidence level to trigger actions.
- **function_map**: Dictionary mapping class names to functions.

#### Methods:

- **run()**: Starts the camera, detects objects, and executes associated actions based on detections.

## Contributing

Contributions are welcome! Here's how you can contribute:

1. Report bugs and request features.
2. Improve the documentation.
3. Submit pull requests with improvements to the code.

Please use the issue tracker for feedback and discussions.

---

### Saving the README

Create a `README.md` file in the root of your repository and copy the content above into it. This README will provide a comprehensive guide to setting up and using the `ObjectDetector`, making it accessible for both users looking to implement object detection in their projects and potential contributors interested in enhancing the functionality.
