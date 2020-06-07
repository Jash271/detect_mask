import fastai
from fastai  import *
from fastai.vision import *
import sys

warnings.filterwarnings("ignore")

def Determine(path):
    prefix=sys.prefix
    final=prefix + '\\Lib\\site-packages\\detect_mask'
    learn=load_learner(final)
    img=open_image(path)
    k=learn.predict(img)[1]
    if k==1:
        return (0,'No Mask')
    else:
        return (1,'Mask')
    
    


