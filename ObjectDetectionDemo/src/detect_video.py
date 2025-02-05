import cv2
from ultralytics import YOLO

# Load trained model
model = YOLO("../models/best.pt")  # Adjust path

# Load video
video_path = "../resources/sample_video.mp4"  # Change to actual video path
cap = cv2.VideoCapture(video_path)

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    # Run detection
    results = model(frame)

    # Render the detection results on the frame
    annotated_frame = results.render()[0]

    # Display the output
    cv2.imshow("Object Detection - Video", annotated_frame)
    
    # Press 'q' to exit
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
