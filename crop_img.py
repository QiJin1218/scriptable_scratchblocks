from PIL import Image
import numpy as np
import os
from os import listdir

cropped_img_dir = 'cropped_img_files/'

def crop(image_name):
	im = image_name.split('/')
	myImage = Image.open(image_name)
	black = Image.new('RGBA', myImage.size)
	myImage = Image.composite(myImage, black, myImage)
	myCroppedImage = myImage.crop(myImage.getbbox())
	myCroppedImage.save(cropped_img_dir + im[1])

directory = 'img_files/'
files = os.listdir(directory)
if '.DS_Store' in files:
	files.remove('.DS_Store')
for img in files:
	crop(directory + img)
