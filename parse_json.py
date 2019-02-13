import os
import json
import re
import util.clean_opcodes as co
import util.txt_to_json as txtjson

def parse_json(jsonfile):

	with open(jsonfile) as f:
		events = json.load(f)

	commands = []
	startkey = None

	for key in events:
		# import ipdb
		# ipdb.set_trace()
		val = events[key]
		if(val['parent'] is None):
			startkey = key

	while(startkey is not None):
		val = events[startkey]
		oc = val['opcode']
		try:
			sbcode = op_codes[oc][0]
		except:
			continue
		ipval = val['inputs']
		if len(ipval) == 0:
			ipval = None
		fval = val['fields']
		if len(fval) == 0:
			fval = None
		cm = (sbcode, ipval, fval)
		commands.append(cm)
		startkey = val['next']

	return commands

def parse_commands(commands):

	lencm = len(commands)
	result = ""

	for i in range(lencm):
		val = commands[i][0]
		inputs = commands[i][1]
		fields = commands[i][2]
		if inputs is None and fields is None:
			result += val
		elif inputs is not None:
			partialresult = cm_input(val, inputs, "(")
			partialresult = cm_input(partialresult, inputs, "[")
			result += partialresult
		else:
			partialresult = fd_input(val, fields, "(")
			result += partialresult
		result += "%0A"

	result = result.replace(" ", "%20")

	with open('scratch_code.txt', 'w') as f:
		f.write(result)
	return result

def cm_input(val, inputs, delimiter):

	if delimiter not in val:
		return val
	vallist = val.split(delimiter)
	result = ""
	i = 0
	lenval = len(vallist)
	c = 0
	for v in vallist:
		if(i < lenval-1):
			inputval = findinputval(inputs, c)
			if inputval is not None:
				inputval = inputval.replace("(", " ")
				inputval = inputval.replace(")", " ")
			else:
				inputval = ""
			result += v + delimiter + inputval
			c += 1
		else:
			result += v
		i += 1

	return result

def fd_input(val, fields, delimiter):

	if delimiter not in val:
		return val
	vallist = val.split(delimiter)
	result = ""
	i = 0
	result += vallist[0] + delimiter + findfieldval(fields) + vallist[1]

	return result

def findinputval(inputs, counter):

	if 'MESSAGE' in inputs:
		if counter == 0:
			return inputs['MESSAGE'][1][1]
	if 'SECS' in inputs:
		if counter == 1:
			return inputs['SECS'][1][1]
	if 'STEPS' in inputs:
		return inputs['STEPS'][1][1]
	return None

def findfieldval(fields):

	if 'KEY_OPTION' in fields:
		return fields['KEY_OPTION'][0]

def create_script(default_script, data):

	f = open(default_script, "r")
	script = f.readlines()

	custom_script = open("custom_script.js", "w")
	for line in script:
		code = "const block_code = \'" + data + "\';"
		line = line.replace("const block_code = \'\';", code)
		custom_script.write(line)

directory = "sample_scratchcode/"
filename = "test_0.json"
jsonfile = txtjson.txt_to_json(directory, filename)
default_script = "script.js"
op_codes = co.clean_opcodes("opcodes.csv")
commands = parse_json(jsonfile)
scratchblocks_commands = parse_commands(commands)
create_script(default_script, scratchblocks_commands)
