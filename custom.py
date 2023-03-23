import torch
import matplotlib as plt
import numpy as np
import cv2
import uuid
import os 
import time 



model = torch.hub.load("ultralytics/yolov5",'yolov5s')

IMAGES_PATH = os.path.join("data","images")
labels = ["awake","drowsy"]
number_images = 5

cap = cv2.VideoCapture(0)

for label in labels:
    print("Collecting images for {}".format(label))
    time.sleep(5)
    
    for img_num in range(number_images):
        print("Collecting images for {} , image number {}".format(label, img_num))

        ret,frame = cap.read()
        
        imgname = os.path.join(IMAGES_PATH,label+'.'+str(uuid.uuid1())+".jpg")
        
        cv2.imwrite(imgname,frame)

        cv2.imshow("Image Collection",frame)
        
        time.sleep(2)

        if cv2.waitKey(10) & 0xFF == ord("q"):
            break


cap.release()
cv2.destroyAllWindows()    


#pip install pyqt5 lxml  and git clone https://github.com/heartexlabs/labelImg

# then in yolov5 run python train.py --img 320 --batch 16 16 --epochs 500 --data dataset.yl --weigths yolov5s.pt --workers 2

#Edit dataset.yaml file after labeling the images 

#Load custom model
"""

model =  torch.hub.load("ultalytics/yolov5",'custom',path = 'yolov5/runs/train/exp15/wieghts/lat.pt',force_reload = True)

while cap.isOpened():

    ret, frame = cap.read()

    results = model(frame)

    cv2.imshow("Yolo",frame)

"""