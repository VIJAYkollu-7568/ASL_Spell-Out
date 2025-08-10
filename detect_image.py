from ultralytics import YOLO

# Load trained model
model = YOLO("best (1).pt")

# Run prediction on a sample image
results = model.predict(source="test_image.png", conf=0.5, save=True)

print("✅ Prediction complete. Check 'runs/detect/predict' folder.")
