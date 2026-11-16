from ultralytics import YOLO

# Load a pretrained model
model = YOLO("yolo11n.pt")

# Run detection on an image
results = model("pos.jpg")

# Display the result
results = model (r"C:\Users\ayton\OneDrive\Desktop\Py\pos.jpg", show=True)

#results = model (r"C:\Users\ayton\OneDrive\Desktop\Py\pos.jpg", show=True, save=True)
for box in results [0].boxes:
    label = model.names[int(box.cls[0])]
    confidence = float(box.conf[0])
    coords = box.xyxy[0].tolist()  # Get the bounding box coordinates
    print(f"Detected {label} with confidence {confidence:.2f} at coordinates {coords}")