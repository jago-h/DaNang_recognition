from ultralytics import YOLO 

#load pre-trained model
model = YOLO("yolov8x-cls.pt")
data_dir = 'PATH TO YOUR DATASET'

results = model.train(
    data=data_dir,
    epochs=10,          # Number of training epochs
    imgsz=416,          # Image size
    batch=8,           # Batch size !!!!!!
    workers=1,          # Number of data loading workers (adjust based on your CPU) !!!!!!
    save_period=1,
    device='mps',         # Specify GPU device, 'cpu' if no GPU is available
    project='yolov8_training',  # Project folder to save logs and models
    name='danang_model',  # Name of the model
    pretrained=True,    # Use pre-trained weights
    lr0=0.0001          # learning rate
)

# Save the model
model.save('yolov8n_danang_best.pt')