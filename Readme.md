# AI Sensor Fusion Project

## Overview

This project demonstrates AI-based sensor fusion using:

- Camera
- LiDAR (simulated)
- Ultrasonic Sensor (simulated)
- GPS (simulated)
- YOLOv8 Object Detection
- Kalman Filter
- Flask Dashboard

---

## Features

- Real-time camera feed
- Object detection using YOLOv8
- Sensor fusion with Kalman Filter
- Simulated LiDAR and Ultrasonic sensors
- GPS location simulation
- Decision-making system
- Dashboard

---

## Installation

```bash
pip install -r requirements.txt
```

---

## Download YOLO Model

Download the YOLOv8 nano model and place it in the `models` folder as:

```
models/yolo.pt
```

Example command:

```bash
yolo detect predict model=yolov8n.pt
```

(or download `yolov8n.pt` and rename it to `yolo.pt`)

---

## Run Dashboard

```bash
python dashboard/app.py
```

Open:

```
http://127.0.0.1:5000
```

---

## Run Main Program

```bash
python main.py
```

Press **Q** to exit.

---

## Folder Structure

```
AI-SensorFusion/
│
├── ai/
├── dashboard/
├── fusion/
├── models/
├── sensors/
├── dataset/
├── main.py
├── requirements.txt
└── README.md
```