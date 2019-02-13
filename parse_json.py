import os
import json
import re
import util.clean_opcodes as co

def parse_json(jsonfile):

	with open(jsonfile) as f:
		events = json.load(f)

	commands = []

	for key in events:
		# import ipdb
		# ipdb.set_trace()
		val = events[key]
		try:
			oc = val['opcode']
			sbcode = op_codes[oc][0]
			ipval = val['inputs']
			if len(ipval) == 0:
				ipval = None
			cm = (sbcode, ipval)
			commands.append(cm)
		except:
			continue

	return commands

def parse_commands(commands):

	lencm = len(commands)
	result = ""

	for i in range(lencm):
		val = commands[i][0]
		inputs = commands[i][1]
		if inputs is None:
			result += val + "%0A"
		else:
			result += val + "%0A"

	result = result.replace(" ", "%20")

	with open('scratch_code.txt', 'w') as f:
		f.write(result)
	return result

def create_script(default_script, data):

	f = open(default_script, "r")
	script = f.readlines()

	custom_script = open("custom_script.js", "w")
	for line in script:
		code = "const block_code = \'" + data + "\';"
		line = line.replace("const block_code = \'\';", code)
		custom_script.write(line)

jsonfile = "util/test_0.json"
default_script = "script.js"
op_codes = co.clean_opcodes("opcodes.csv")
commands = parse_json(jsonfile)
scratchblocks_commands = parse_commands(commands)
create_script(default_script, scratchblocks_commands)
