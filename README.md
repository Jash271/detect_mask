# Detect Mask in input photo :mask:
# Install module for use by this command https://pypi.org/project/detect-mask/
## Stable Build for windows

### Fast AI required to run this module
### Just Import detect_mask module : 
```
import detect_mask
from detect_mask import Mask
````

### call the method Determine and pass the path of the photo of the variable : 
```
Mask.Determine(path)
```
### Returns a Tuple :
###  (0,'No Mask')
###  (1,'Mask')


### Pull Out the Camera to Detect Mask, Real Time
```
Mask.Cam()
```
### It's that simple 
