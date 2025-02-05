import tkinter as tk
from tkinter import filedialog
import cv2
from ultralytics import YOLO
from PIL import Image, ImageTk

# Load trained model
model = YOLO("../models/best.pt")  # Adjust path

class ObjectDetectionApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Object Detection Demo")
        self.root.geometry("800x600")

        # Create buttons
        self.load_button = tk.Button(root, text="Load Video", command=self.load_video, height=2, width=20)
        self.load_button.pack()

        self.start_camera_button = tk.Button(root, text="Start Camera", command=self.start_camera, height=2, width=20)
        self.start_camera_button.pack()

        self.exit_button = tk.Button(root, text="Exit", command=root.quit, height=2, width=20)
        self.exit_button.pack()

        self.canvas = tk.Canvas(root, width=640, height=480)
        self.canvas.pack()

    def load_video(self):
        file_path = filedialog.askopenfilename(filetypes=[("MP4 files", "*.mp4"), ("AVI files", "*.avi")])
        if file_path:
            self.detect_objects(file_path)

    def detect_objects(self, source):
        cap = cv2.VideoCapture(source)
        while cap.isOpened():
            ret, frame = cap.read()
            if not ret:
                break

            results = model(frame)
            annotated_frame = results.render()[0]

            frame_rgb = cv2.cvtColor(annotated_frame, cv2.COLOR_BGR2RGB)
            img = Image.fromarray(frame_rgb)
            img_tk = ImageTk.PhotoImage(image=img)

            self.canvas.create_image(0, 0, anchor=tk.NW, image=img_tk)
            self.root.update()

        cap.release()

    def start_camera(self):
        self.detect_objects(0)  # 0 for webcam

root = tk.Tk()
app = ObjectDetectionApp(root)
root.mainloop()
