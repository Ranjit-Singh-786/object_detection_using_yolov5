# object_detection_using_yolov5

To utilize the yolo v5, and to understand how we can utilize yolo v5 pretrained model
to perform object detection on custome dataset.

### Key Points to perform object detection using yolov5

1. Annotate the data, using anotation tools, like labelimg in yolo formate.
2. Keep annotated data in root current working directory, as i keep my dataset repository.
3. Clone the yolov5 repository.
4. Keep yolov5 in your root current working directory
5. First Go inside the yolov5 and install all the requirements of yolov5
6. Use the "train.py" file to train the yolov5 model on custome dataset, command mentioned below.
7. After Training, use the "detect.py" to test your model.

### Steps To execute This project

1. Git clone this repository
2. First install the yolov5 dependencies.
3. And Execute the run.py file.

#### And all are steps are mentioned in jupyter notebook called "step_notebook.ipynb"

### To clone the yolo v5 github repository.
```bash
git clone https://github.com/ultralytics/yolov5

```

### To install yolov5 dependencies.
```bash
%cd yolov5/
pip install -r requirements.txt
```

### Command To train yolov5 on custome dataset
```bash
python train.py --img 416 --batch 16 --epochs 10 --data '../dataset/data.yaml' --cfg ./models/yolov5s.yaml --weights 'yolov5s.pt' --name training_logs --cache
```

### To Perform Detection on test data point, use this command

```bash
%cd /content/drive/MyDrive/object_dete_yolo/sign-language-detection-YOLOV5/yolov5/

!python detect.py --weights runs/train/training_result22/weights/best.pt --img 416 --conf 0.1 --source ../test/images
```
### After training we will get
"yolov5/runs" directory inside that you will get your logs regarding your training,
inside the "yolov5/runs/" you will get two another directories 
1. train   <- it created when you train your model
2. detect  <- it created when you perform detection

inside the yolov5/runs/train/training_result22/weights/ you will get two another files after trainings
1. best.pt
2. last.pt

here best.pt will be your updated weight of your model.
during the training it will created, but once the training part is done.
when you will use your model to perform detection, at that time you will specifiy the
path of the file 
```bash
--weights runs/train/training_result22/weights/best.pt
```
### Thank you
