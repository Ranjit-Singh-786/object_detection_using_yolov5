import os

# Get the current script's directory
script_dir = os.path.dirname(os.path.realpath(__file__))

# Change the current working directory to the 'yolov5/' directory
yolo_path = os.path.join(script_dir, 'yolov5')
os.chdir(yolo_path)

# Now you can run the YOLOv5 detection script
os.system("python3 detect.py --weights runs/train/training_result22/weights/best.pt --img 416 --conf 0.6 --source 0")
