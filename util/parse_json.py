import os
import json
import re

def parse_json(jsonfile):

	with open(jsonfile) as f:
		events = json.load(f)

	for key in events:
		print(key)
		import ipdb
		ipdb.set_trace()

jsonfile = "test_0.json"
parse_json(jsonfile)