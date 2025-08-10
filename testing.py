from ultralytics import YOLO

try:
    model = YOLO("hand.pt")
    print("✅ Loaded as YOLOv8")
except Exception as e:
    print("❌ Not a YOLOv8 model:", e)
