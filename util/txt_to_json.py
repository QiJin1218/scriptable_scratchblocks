import os
import json
import re

def txt_to_json(directory, filename):

	txtfile = open(os.path.relpath(directory + filename), 'r')
	fn = filename.split('.')[0]
	c = 0
	for l in txtfile:
		if(len(l) > 1):
			print(fn)
			jsonfile = open(fn + '.json', 'w')
			l2 = l.replace("u\'","\"")
			line = l2.replace("\'","\"")
			line = line.replace("None","null")
			line = line.replace("True","\"True\"")
			line = line.replace("False","\"False\"")
			while True:
				try:
					result = json.loads(line)
					break
				except Exception as e:
					print(e)
				c += 1
			json.dump(result, jsonfile)
			jsonfile.close()

	jsonfilename = fn + '.json'

	return jsonfilename