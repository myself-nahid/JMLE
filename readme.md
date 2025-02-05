# **JMLE Task**

## ** Project Overview**
This project consists of four main tasks designed to evaluate skills in **data annotation, object detection model training, research analysis, and proof-of-concept development**. The tasks include:
1. **Data Annotation and Dataset Preparation**
2. **Algorithm Development and Model Training**
3. **Research and Literature Review**
4. **Proof-of-Concept Demonstration**

---

## **1️⃣ Data Annotation and Dataset Preparation**
### **📝 Task Description**
- Annotate **150 images** containing **vehicles, pedestrians, and traffic signs**.
- Use **LabelImg** (Pascal VOC XML) or **CVAT** (COCO JSON) for annotation.
- Ensure annotations are properly formatted for training.

### **✅ Deliverables**
- Annotated images and annotation files (**VOC XML or COCO JSON**).
- A report detailing the annotation process and challenges faced.

### **🚀 Steps to Run**
```bash
# Install annotation tools
pip install labelImg
# Run the annotation tool
labelImg
```
---

## **2️⃣ Algorithm Development and Model Training**
### **📝 Task Description**
- Train an **object detection model** using **YOLOv8** or **Faster R-CNN**.
- Split the dataset into **80% training and 20% validation**.
- Train the model on **NVIDIA GPU** for better performance.

### ** Deliverables**
- Source code of the model training process.
- A report summarizing the **model architecture, training methodology, and results**.

### **🚀 Steps to Train the Model**
```bash
# Install dependencies
pip install ultralytics opencv-python numpy torch

# Train YOLOv8 model
yolo train model=yolov8s.pt data=dataset.yaml epochs=50 imgsz=640
```
---

## **3️⃣ Research and Literature Review**
### **📝 Task Description**
- Select a **recent (last two years) research paper** on **object detection**.
- Write a **1-2 page summary** covering **key contributions, methodology, and applications**.

### ** Deliverables**
- A written **research summary (PDF format)**.

### **🚀 Suggested Research Papers**
- [YOLOv8: A State-of-the-Art Object Detector](https://arxiv.org/abs/2301.00704)
- [DEtection TRansformer (DETR)](https://arxiv.org/abs/2005.12872)

---

## **4️⃣ Proof-of-Concept Demonstration**
### **📝 Task Description**
- Develop a **real-time object detection application**.
- Implement a **Graphical User Interface (GUI)** using **Tkinter** or **PyQt**.
- Enable detection from **webcam or video file**.

### ** Deliverables**
- Source code of the **demo application**.
- A **user guide** explaining how to run the application and interpret results.

### **🚀 Steps to Run the Application**
```bash
# Install dependencies
pip install ultralytics opencv-python numpy pillow tkinter

# Run the GUI application
python ObjectDetectionDemo/src/gui_app.py
```

---

## **📌 Project Structure**
```
ObjectDetectionProject/
│── notebook               
│── Dataset/                # Annotated dataset
│── ObjectDetectionDemo/   
│   ├── src/                # Source code
│   │   ├── detect_live.py      # Real-time webcam detection
│   │   ├── detect_video.py     # Video file detection
│   │   ├── gui_app.py          # GUI Application
│── reports/                # Task reports
│── README.md               # Project guide
│── requirements.txt        # Dependencies
│── .gitignore              # Ignore File
```
