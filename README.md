# Da Nang Landmark Recognition

This repository contains a project for recognizing famous landmarks in Da Nang, Vietnam, using a YOLOv8-based model. The project includes a model training script (`danang.py`) and a web application (`app.py`) built with Gradio for easy interaction.

## Table of Contents

- [Overview](#overview)
- [Installation](#installation)
- [Dataset](#dataset)
- [Model Training](#model-training)
- [Web Application](#web-application)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)

## Overview

This project aims to recognize various landmarks in Da Nang using deep learning. The YOLOv8 model is trained on a custom dataset of +/- 1000 images and can be used for classification tasks. The web application provides a simple interface for users to upload images and receive predictions about the landmarks depicted in the images.

## Installation

To run this project locally, follow these steps:

1. **Clone the repository**:

    ```bash
    git clone https://github.com/jago-h/DaNang_recognition.git
    cd DaNang_recognition
    ```

2. **Create and activate a virtual environment**:

    ```bash
    python3 -m venv yolov8-env
    source yolov8-env/bin/activate
    ```

3. **Install the required dependencies**:

    ```bash
    pip install ultralytics gradio pillow
    ```

4. (for M1/M2 Macs) **Set up TensorFlow with Metal support**:

    ```bash
    pip install tensorflow-macos tensorflow-metal
    ```
    more details: [text](https://pytorch.org/docs/stable/notes/mps.html)

## Dataset

The project expects a dataset organized in the following structure:

dataset/
│
├── train/
│ ├── class1/
│ ├── class2/
│ └── ...
│
├── valid/
│ ├── class1/
│ ├── class2/
│ └── ...
│
├── test/
│ ├── class1/
│ ├── class2/
│ └── ...


Update the `data_dir` in `danang.py` with the path to your dataset.

## Model Training

The `danang.py` script is used to train the YOLOv8 model on your custom dataset. The model is pre-trained on the `yolov8x-cls.pt` weights and fine-tuned on the provided dataset. This repository does not provide the trained model, due to its large size. Good luck with training!

### Training Command

1. Open the `danang.py` file and update the `data_dir` variable with the path to your dataset.
2. Run the script:

    ```bash
    python danang.py
    ```

The script includes customizable parameters such as:

- `epochs`: Number of training epochs (default: 10)
- `imgsz`: Image size (default: 416x416)
- `batch`: Batch size (default: 8)
- `device`: Set to `'mps'` for Apple Silicon GPUs or `'cpu'` if no GPU is available
- `lr0`: Initial learning rate (default: 0.0001)

The trained model is saved as `yolov8n_danang_best.pt` in the specified project directory.

## Web Application

The `app.py` script provides a web interface using Gradio, allowing users to upload images and receive predictions for landmarks in Da Nang.

### Running the App

1. Update the `model = YOLO('PATH TO YOUR YOLO MODEL')` line in `app.py` with the path to your trained model (e.g., `'yolov8n_danang_best.pt'`).
2. Run the app:

    ```bash
    python app.py
    ```

The app will launch in your default web browser. You can upload an image, and the app will return the predicted landmark along with confidence scores.

## Usage

- **Training the Model**: Use `danang.py` to train the model on your dataset.
- **Running the Web App**: Use `app.py` to launch a Gradio-based web interface for inference.

## Contributing

Contributions are welcome! Please open an issue or submit a pull request for any changes or improvements.

## License

This project was a part of an internship programme at FPT Software. It is intended for non-commercial use only. Commercial use of this software is strictly prohibited without prior written permission.

If you use this software in your research or other work, please cite it as follows:

**Da Nang Landmark Recognition by Jagoda Hanuszewicz and Heaymalaah Kunalan**
