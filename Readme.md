---

# Height Detection App

The Height Detection App is a Python application that uses computer vision techniques to detect and measure the distance of objects from a camera, based on a reference object of known dimensions. This README provides instructions on how to set up the environment, run the script, and use the application effectively.

## Requirements

Before running the app, ensure you have Python installed on your system. The necessary Python packages are listed in `requirements.txt`. Install them using the following command:

```bash
pip install -r requirements.txt
```

## Usage

### 1. Prepare Reference Image

Before running the script (`ex.py`), prepare a reference image (`ref_img.jpg`) that contains a known object with its dimensions specified. This reference image will be used for calibration to measure distances accurately.

### 2. Run the Script

To use the Height Detection App:

- Open a terminal or command prompt.
- Navigate to the directory containing `ex.py`.

Run the script using the following command format:

```bash
python ex.py
```

The script will prompt you to provide the path to the image you want to analyze and the path to the reference image (`ref_img.jpg`).

Example:

```bash
python ex.py --image path/to/your/image.jpg --reference path/to/ref_img.jpg
```

Replace `path/to/your/image.jpg` with the path to the image you want to analyze.

### 3. Output

The script will process the specified image, detect objects, measure their distance from the camera using the known dimensions from the reference image, and display the distance in centimeters on the video feed.

## Notes

- Ensure the reference object in `ref_img.jpg` is clearly visible and its dimensions (width) are accurately known.
- The script uses OpenCV for face detection and distance calculation, and pyttsx3 for speech synthesis.
- Adjust any parameters or configurations in `ex.py` as necessary for your specific use case or camera setup.

---

