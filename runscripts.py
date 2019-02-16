#!/usr/bin/python
from subprocess import call
import os
import json

directory = "scripts/"
files = os.listdir(directory)
if '.DS_Store' in files:
	files.remove('.DS_Store')

c = 0
filedir = {}
for filename in files:
	filedir[c] = filename
	call(["node", directory + filename])

writedir = open("filedirectory.txt", "w")
writedir.write(json.dumps(filedir))