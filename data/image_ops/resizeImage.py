#import libraries
import glob as glob
import os
import numpy as np

from PIL import Image

# Import an image from directory:
read_path = './resizeImageFilesHere/'
save_path = './resizedImages/'
# for file in glob.glob(os.path.join(read_path, '*')):
for file in glob.glob(read_path+"*"):
	
    image = Image.open(file)
    resized_image = image.resize((400,400))

    filename = os.path.split(file)[1]
    filename = os.path.splitext(filename)[0]

    resized_image.save(save_path+filename+'.jpg')  
