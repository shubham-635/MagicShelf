import cv2
from datetime import datetime
from ultralytics import YOLO
import logging
import os

log_directory = "logs"
os.makedirs(log_directory, exist_ok=True)

log_file_path = os.path.join(log_directory, "application.log")

logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    handlers=[
        logging.FileHandler(log_file_path),
        logging.StreamHandler()
    ]
)

logger = logging.getLogger("MagicShelf")

model = YOLO('yolov8s.pt')

TARGET_CLASSES = ['bottle', 'box', 'can']

def detect_and_track(video_path):
    cap = cv2.VideoCapture(video_path)
    if not cap.isOpened():
        print("Error: Could not open video file.")
        return

    frame_width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    frame_height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    fps = cap.get(cv2.CAP_PROP_FPS)
    # total_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))

    timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
    output_file = f"output_{timestamp}.mp4"
    fourcc = cv2.VideoWriter_fourcc(*'mp4v')
    out = cv2.VideoWriter(output_file, fourcc, int(fps), (frame_width, frame_height))

    print(f"Processing video... Output will be saved as {output_file}")

    previous_objects = set()
    frame_counter = 0

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        frame_counter += 1
        video_time = frame_counter / fps

        results = model(frame)
        detections = results[0].boxes.data.cpu().numpy()
        current_objects = set()

        for detection in detections:
            x1, y1, x2, y2, confidence, class_id = detection
            class_id = int(class_id)
            label = model.names[class_id]

            if label in TARGET_CLASSES:
                current_objects.add(label)

                cv2.rectangle(frame, (int(x1), int(y1)), (int(x2), int(y2)), (0, 255, 0), 2)
                cv2.putText(frame, label, (int(x1), int(y1) - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)

        disappeared_objects = previous_objects - current_objects
        if disappeared_objects:
            for obj in disappeared_objects:
                log_message = f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] Product '{obj}' disappeared at video time {video_time:.2f} seconds."
                logger.info(log_message)

        previous_objects = current_objects

        out.write(frame)

        cv2.imshow('Detection', frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    out.release()
    cv2.destroyAllWindows()

    print(f"Processing complete. Output saved to {output_file}")

if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description="Detect products on a shelf and log when they disappear.")
    parser.add_argument("video", 
                        help="Path to the input video file.",   # Make the input argument 'video' optional
                        default="MagicShelf.mp4", # Default video file if not provided
                        nargs="?")
    args = parser.parse_args()

    detect_and_track(args.video)
