import gradio as gr
from ultralytics import YOLO
from PIL import Image

# Load your YOLOv8 model
model = YOLO('PATH TO YOUR YOLO MODEL')

classes = ["Công viên APEC (APEC Park)", "Bảo tàng Mỹ thuật (Fine Art Museum)", "Công viên Asia (Asia Park)", "Nhà thờ Đà Nẵng (Cathedral)", "Cầu Rồng (Dragon Brigde)", "Chùa Linh Ứng (Lady Buddha)", "Núi Ngũ Hành Sơn (Marble Mountains)", "Cầu Trần Thị Lý (Sail Bridge)", "Chợ Cồn (Con Market)"]

def detect_places(image):
    # Perform detection
    result = model(image)
    print(result)
    # Get the detected class with the highest confidence score
    detected_class = {}
    for i, prob in enumerate(result[0].probs.numpy().data):
        detected_class[classes[i]] = prob
    # print(detected_class)
    # detected_class = results[0].names[results[0].probs.argmax()]
    return detected_class

# Create the Gradio interface
interface = gr.Interface(
    fn=detect_places,
    inputs=gr.Image(type="pil"),
    outputs="label",
    title="Da Nang Landmark Recognition",
    description="Upload an image to detect landmarks in Da Nang." ,
    css="footer {visibility:hidden}"
    
)

if __name__ == "__main__":
    interface.launch()
