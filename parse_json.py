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

	result = result.replace("(", "%5B")
	result = result.replace(")", "%5D")
	result = result.replace("For", " for")
	result = result.replace("'m", " am")
	result = result.replace("t's", "t is")
	result = result.replace("'", "")
	result = result.replace(" ", "%20")

	# with open('scratch_code.txt', 'w') as f:
	# 	f.write(result)
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
			if inputval == "sound":
				inputval = "sound v"
			elif inputval == "costume":
				inputval = "costume v"
			elif inputval is not None:
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
			message = inputs['MESSAGE'][1][1]
			if len(message) >= 25:
				message = message[:22] + "..."
			return message
	if 'SECS' in inputs:
		if counter == 1:
			return inputs['SECS'][1][1]
	if 'STEPS' in inputs:
		return inputs['STEPS'][1][1]
	if 'DURATION' in inputs:
		return inputs['DURATION'][1][1]
	if 'SOUND_MENU' in inputs:
		return "sound"
	if 'COSTUME' in inputs:
		return "costume"
	return None

def findfieldval(fields):

	if 'KEY_OPTION' in fields:
		return fields['KEY_OPTION'][0] + " v"

def create_script(directory, default_script, data, filename):

	f = open(default_script, "r")
	script = f.readlines()
	fn = filename.split(".")
	script_name = directory + fn[0] + ".js"

	custom_script = open(script_name, "w")
	for line in script:
		code = "const block_code = \'" + data + "\';"
		line = line.replace("const block_code = \'\';", code)
		custom_script.write(line)

def find_files(directory):

	files = os.listdir(directory)
	return files

directory = "sample_scratchcode/"
files = find_files(directory)
files.remove('.DS_Store')
op_codes = co.clean_opcodes("opcodes.csv")
script_directory = "scripts/"
output_directory = "cleaned_json/"
for filename in files:
	jsonfile = txtjson.txt_to_json(directory, output_directory, filename)
	default_script = "script.js"
	commands = parse_json(jsonfile)
	scratchblocks_commands = parse_commands(commands)
	create_script(script_directory, default_script, scratchblocks_commands, filename)
	break
