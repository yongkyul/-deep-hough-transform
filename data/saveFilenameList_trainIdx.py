#import libraries
import glob as glob
import os
import numpy as np

from PIL import Image

# Freiburg_forest default labels RGB values
# Import an image from directory:
read_path = './agriNav_data/'

with open('agriNav_train.txt', 'w') as f:
    for file in glob.glob(os.path.join(read_path, '*.jpg')):
	
        filename = os.path.split(file)[1]
        filename = os.path.splitext(filename)[0]
   
        f.write('custom_agriNav_resize_100_100/'+filename+"\n")
        f.write('custom_agriNav_resize_100_100/'+filename+"_flip"+"\n")
  
