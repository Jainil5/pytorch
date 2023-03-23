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
number_images = 20

cap = cv2.VideoCapture(0)

for label in labels:
    print("Collecting images")
    time.sleep(5)
    
    for img_num in range(number_images):
        print("Collecting images for {} , image number{}",format(label, img_num))

    ret,frame = cap.read()
    
    imgname = os.path.join(IMAGES_PATH,label+'.'+str(uuid.uuid1()))
    print(imgname)

    if cv2.waitKey(10) & 0xFF == ord("q"):
        break
cap.release()
cv2.destroyAllWindows()    