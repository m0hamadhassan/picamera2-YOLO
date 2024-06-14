from ObjectDetector import ObjectDetector

# Define your custom actions for each class
def handle_person():
    print("persondetected")
# More functions can be defined as needed

# Map class names to functions
function_map = {
    "person": handle_person,
    # Add other functions for the rest of the classes as defined in classes_file
}

# Path to the YOLO model and class list file
model_path = 'yolov8n.pt'
classes_file_path = 'coco.txt'

# Initialize the detector with the model path, classes file path, confidence threshold, and function map
detector = ObjectDetector(model_path, classes_file_path, 0.8, function_map)

# Start the detection
detector.run()

