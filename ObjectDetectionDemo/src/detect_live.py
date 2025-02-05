import cv2
from ultralytics import YOLO

# Load trained model
model = YOLO("../models/best.pt")  # Adjust path if needed

# Open webcam
cap = cv2.VideoCapture(0)

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    # Run detection
    results = model(frame)

    # Render the detection results on the frame
    annotated_frame = results.render()[0]
    
    # Display the output
    cv2.imshow("Object Detection - Live", annotated_frame)
    
    # Press 'q' to exit
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
