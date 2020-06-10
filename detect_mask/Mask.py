import cv2
from fastai import *
from fastai.vision import *
import imp
import sys
import os 
from pathlib import Path
warnings.filterwarnings("ignore")

class Mask:
    
    


    def Determine(path):
        prefix=sys.prefix
    
    
        learn=load_learner(imp.find_module('detect_mask')[1])
        img=open_image(path)
        k=learn.predict(img)[1]
        if k==1:
            return (0,'No Mask')
        else:
            return (1,'Mask')
    


    def Cam():
        path=imp.find_module('detect_mask')[1]
        path=os.path.join(path,'haarcascade_frontalface_default.xml')
        face_cascade= cv2.CascadeClassifier(path)
        cap=cv2.VideoCapture(0)


        learn=load_learner(imp.find_module('detect_mask')[1])
        while True:
            ret,image=cap.read()
    
            k=learn.predict(Image(pil2tensor(image, np.float32).div_(225)))[1]
            if k==1:
                value='No Mask'
            else:
                value='Mask'
            font = cv2.FONT_HERSHEY_SIMPLEX
            gray=cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
            faces=face_cascade.detectMultiScale(gray,1.1,5)
            cv2.putText(image,value,(150,450),font,1,(0,0,225),2,cv2.LINE_AA)
            for (x,y,w,h) in faces:
        
                cv2.rectangle(image,(x,y),(x+w,y+h),(0,0,255),3)
        
        
    
            cv2.imshow('frame',image)

            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
    
    
        cap.release()
        cap.destroy.AllWindows()
    
