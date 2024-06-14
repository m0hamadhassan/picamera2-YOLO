import cv2
from picamera2 import Picamera2
import pandas as pd
from ultralytics import YOLO
import cvzone

class ObjectDetector:
    def __init__(self, model_path, classes_file_path, confidence_threshold, function_map):
        self.model_path = model_path
        self.confidence_threshold = confidence_threshold
        self.function_map = function_map

        # Load class names from file
        with open(classes_file_path, 'r') as file:
            self.class_list = [line.strip() for line in file.readlines()]

        # Initialize the camera
        self.picam2 = Picamera2()
        preview_config = self.picam2.preview_configuration
        preview_config.main.size = (640, 480)
        preview_config.main.format = "RGB888"
        preview_config.align()
        self.picam2.configure(preview_config)
        self.picam2.start()

        # Load the YOLO model
        self.model = YOLO(model_path)

    def run(self):
        count = 0
        try:
            while True:
                # Capture image from camera
                image = self.picam2.capture_array()

                # Increment and check the frame count
                count += 1
                if count % 3 != 0:
                    continue

                # Flip the image
                image = cv2.flip(image, -1)

                # Predict using the model
                results = self.model.predict(image)
                boxes = pd.DataFrame(results[0].boxes.data).astype("float")

                # Draw rectangles and class labels on the image
                for _, row in boxes.iterrows():
                    x1, y1, x2, y2 = int(row[0]), int(row[1]), int(row[2]), int(row[3])
                    class_idx = int(row[5])
                    confidence = float(row[4])  # Get the confidence level
                    class_name = self.class_list[class_idx]  # Use the class name from the list

                    # Draw bounding box and label with confidence level
                    cv2.rectangle(image, (x1, y1), (x2, y2), (0, 0, 255), 2)
                    cvzone.putTextRect(image, f'{class_name} {confidence:.2f}', (x1, y1), 1, 1)

                    # Execute corresponding function if confidence is above the threshold
                    if confidence > self.confidence_threshold:
                        if class_name in self.function_map:
                            self.function_map[class_name]()

                # Display the image
                cv2.imshow("Camera", image)
                if cv2.waitKey(1) & 0xFF == ord('q'):
                    break
        finally:
            # Clean up
            cv2.destroyAllWindows()
            self.picam2.stop()

