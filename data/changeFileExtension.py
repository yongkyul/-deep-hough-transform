#import libraries
import glob as glob
import os
import numpy as np

from PIL import Image

# Freiburg_forest default labels RGB values
# Import an image from directory:
read_path = './changeNameExtensionFilesHere/'
save_path = './changedNamesExtensions/'
for file in glob.glob(os.path.join(read_path, '*.png')):
	
    filename = os.path.split(file)[1]
    filename = os.path.splitext(filename)[0]
    input_image = Image.open(file)

    # Saving the final output
    input_image.save(save_path+filename+".jpg")
  
