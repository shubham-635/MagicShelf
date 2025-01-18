  Object Detection and Tracking with YOLOv8

Object Detection and Tracking with YOLOv8
=========================================

This project detects and tracks objects (such as bottles, boxes, and cans) in a video stream. It uses the **YOLOv8** object detection model for identifying objects and OpenCV for video processing. Additionally, the script logs when a target object disappears from the video feed.

Features
--------

*   Object detection with **YOLOv8** for predefined classes (`'bottle'`, `'box'`, and `'can'`).
*   Real-time tracking and bounding box annotation.
*   Logs the disappearance of objects in a `logs/application.log` file.
*   Saves the processed video with annotations to an output file.

Requirements
------------

Before you run the script, make sure you have the necessary dependencies installed.

### Dependencies

*   **Python 3.8+**
*   **OpenCV**: For video processing and display.
*   **YOLOv8 model**: Pre-trained weights for object detection.
*   **Ultralytics**: For YOLOv8 model loading and inference.

### Install Dependencies

You can install the required dependencies by using `pip`. Here's a list of installation commands:

1.  Clone the repository (or download the script):
    
        git clone [<repository_url>](https://github.com/shubham-635/MagicShelf)
        cd MagicShelf
    
2.  Create a virtual environment (optional but recommended):
    
        python -m venv venv
        source venv/bin/activate  # For Windows, use `venv\Scripts\activate`
    
3.  Install required packages:
    
        pip install -r requirements.txt
    
4.  Alternatively, you can install the dependencies manually:
    
        pip install opencv-python ultralytics
    

### YOLOv8 Pre-trained Model

The script uses the pre-trained **YOLOv8** model. You need to download the weights file (`yolov8s.pt`) before running the script.

*   Download the weights from the [Ultralytics YOLOv8 releases](https://github.com/ultralytics/yolov8).
*   Save the weights file (e.g., `yolov8s.pt`) in the same directory as the script or update the path in the code accordingly.

Usage
-----

Once you have installed the dependencies and set up the environment, you can run the script using the following instructions.

### Command Line Usage

You can run the script with an optional video file input. If no video is provided, the script will default to using `MagicShelf.mp4` as the input video.

#### To specify a video file:

    python main.py /path/to/video.mp4

#### To use the default video file (`MagicShelf.mp4`):

    python main.py

### Output

The script will process the video and save an output video with detected objects and bounding boxes. The processed video will be saved in the current directory with a filename like `output_YYYYMMDD_HHMMSS.mp4`.

Additionally, a log file (`logs/application.log`) will store entries for any detected objects that disappear during the video. For example:

    [2025-01-18 14:32:15] Product 'bottle' disappeared at video time 120.50 seconds.

Script Explanation
------------------

### Key Features:

*   **Target Classes**: The script is configured to track the following objects:
    *   Bottle
    *   Box
    *   Can
*   **Detection**: Uses the YOLOv8 model to detect objects in each video frame.
*   **Tracking**: Keeps track of objects across frames and logs when they disappear.
*   **Logging**: Disappearing objects are logged with timestamps in `logs/application.log`.
*   **Output Video**: The processed video is saved with annotated bounding boxes around detected objects.

### Optional Arguments:

*   **\--video**: Path to the input video file. If not provided, the default video (`MagicShelf.mp4`) is used.

Troubleshooting
---------------

*   **Error: Could not open video file**: This may occur if the video path is incorrect or the file format is not supported. Ensure the video file exists and is in a supported format (e.g., `.mp4`).
*   **Model Loading Issues**: If you encounter issues loading the model, make sure the YOLOv8 weights (`yolov8s.pt`) are correctly downloaded and available in the script's directory.
