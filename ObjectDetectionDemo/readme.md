# **User Guide: Object Detection Application**

## **📌 Overview**
This application allows users to:
- Detect objects **in real-time** using a webcam.
- Detect objects from **pre-recorded video files**.
- Use a **user-friendly GUI** for easy operation.

## **🚀 Installation**
### **Step 1: Install Python Dependencies**
Ensure you have Python 3.8+ installed, then run:
```bash
pip install ultralytics opencv-python numpy pillow tkinter
```

### **Step 2: Download the Pretrained Model**
Place your trained model **best.pt** inside the `models/` directory.

## **🎯 How to Run the Application**
### **1️⃣ Run Real-Time Webcam Detection**
Open a terminal and execute:
```bash
python src/detect_live.py
```
👉 This will start the webcam and detect objects in real time.

### **2️⃣ Run Object Detection on a Video File**
To analyze a pre-recorded video, run:
```bash
python src/detect_video.py
```
👉 Replace the video path inside the script to match your video file.

### **3️⃣ Launch the GUI Application**
For a user-friendly interface, start the GUI:
```bash
python src/gui_app.py
```
👉 This will open a window where you can **load a video** or **start real-time detection**.

## **📊 How to Interpret the Results**
- The application will **display bounding boxes** around detected objects.
- Labels such as **Car, Pedestrian, Traffic Sign** will be shown on the detected objects.
- Confidence scores indicate how sure the model is about each detection.
- Press **'q'** to exit the application when running video or webcam detection.

## **⚡ Troubleshooting**
- If **ultralytics is not found**, install it using `pip install ultralytics`.
- If the webcam does not start, ensure your camera is connected and not being used by another application.
- For better accuracy, train YOLOv8 on a **larger dataset** and fine-tune hyperparameters.

## **📌 Conclusion**
This object detection application efficiently detects and visualizes objects in **real-time** or **video files**. It is useful for applications like surveillance, traffic monitoring, and autonomous systems. 🚀

