#!/usr/bin/python
from subprocess import call
import os
import json
import re
import crop_img

call(["python3", "parse_json.py"])

img_directory = "img_files/"
cropped_img_dir = "cropped_img_files/"

directory = "scripts/"
files = os.listdir(directory)
if '.DS_Store' in files:
	files.remove('.DS_Store')

c = 0
filedir = {}
for filename in files:
	filedir[c] = filename
	call(["node", directory + filename])
	print(filename + "," + str(c))
	old_name = img_directory + "scratchblocks.png"
	new_name = img_directory + filename + ".png"
	if "script" not in filename:
		new_name = img_directory + filename + "_script0" + ".png"
	os.rename(old_name, new_name)
	crop_img.crop(new_name, img_directory)
	c += 1

writedir = open("filedirectory.json", "w")
writedir.write(json.dumps(filedir))

# filedir = json.load(open("filedirectory.json"))

# imgs = os.listdir(img_directory)
# if '.DS_Store' in imgs:
# 	imgs.remove('.DS_Store')
# for png in imgs:
# 	n = re.findall(r'\d+', png)
# 	if len(n) == 0:
# 		img_counter = str(0)
# 		img_name = "scratchblocks.png"
# 	else:
# 		img_counter = str(n[0])
# 		img_name = "scratchblocks (" + img_counter + ").png"
# 	filename = filedir[img_counter]
# 	fn = filename[:-3]
# 	old_name = img_directory + img_name
# 	new_name = img_directory + fn + ".png"
# 	if "q7" in fn:
# 		new_name = img_directory + fn + "_script0" + ".png"
# 	os.rename(old_name, new_name)
# 	crop_img.crop(new_name, cropped_img_dir)