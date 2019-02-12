import os
import json
import re

def txt_to_json(directory, filename):

	txtfile = open(os.path.relpath(directory + filename), 'r')
	fn = filename.split('.')[0]
	c = 0
	for l in txtfile:
		if(len(l) > 1):
			jsonfile = open(fn + '_' + str(c) + '.json', 'w')
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

def parse_json(jsonfile):
	# parsed = json.load(jsonfile)
	import ipdb
	ipdb.set_trace()
	print(json)

directory = '../sample_scratchcode/'
filename = "test.json"
txt_to_json(directory, filename)
jsonfile = 'test0.txt'
# parse_json(jsonfile)