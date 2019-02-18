#!/usr/bin/python
from subprocess import call
import os
import json
import re
import crop_img

directory = "scripts/"
files = os.listdir(directory)
if '.DS_Store' in files:
	files.remove('.DS_Store')

c = 0
filedir = {}
for filename in files:
	filedir[c] = filename
	call(["node", directory + filename])
	c += 1

img_directory = "img_files/"
cropped_img_dir = "cropped_img_files/"
imgs = os.listdir(img_directory)
if '.DS_Store' in imgs:
	imgs.remove('.DS_Store')
for png in imgs:
	n = re.findall(r'\d+', png)
	if len(n) == 0:
		img_counter = 0
	else:
		img_counter = int(n[0])
	filename = filedir[img_counter]
	os.rename(img_directory+png, img_directory+filename)
	crop_img.crop(img_directory+filename, cropped_img_dir)

writedir = open("filedirectory.txt", "w")
writedir.write(json.dumps(filedir))