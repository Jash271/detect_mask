import fastai
from fastai  import *
from fastai.vision import *
import sys
import os
import imp
warnings.filterwarnings("ignore")



def Determine(path):
    prefix=sys.prefix
    
    
    learn=load_learner(imp.find_module('detect_mask')[1])
    img=open_image(path)
    k=learn.predict(img)[1]
    if k==1:
        return (0,'No Mask')
    else:
        return (1,'Mask')
    
