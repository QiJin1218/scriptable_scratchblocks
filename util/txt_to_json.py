import os
import json

def txt_to_json(directory, filename):

	txtfile = open(os.path.relpath(directory + filename), 'r')
	fn = filename.split('.')[0]
	c = 0
	for line in txtfile:
		if(len(line) > 1):
			jsonfile = open(fn + '_' + str(c) + '.json', 'w')
			import ipdb
			ipdb.set_trace()
			jsonfile.write(line)
			c += 1

def parse_json(jsonfile):
	# parsed = json.load(jsonfile)
	import ipdb
	ipdb.set_trace()
	print(json)

directory = '../sample_scratchcode/'
filename = "test.txt"
txt_to_json(directory, filename)
jsonfile = 'test0.txt'
parse_json(jsonfile)