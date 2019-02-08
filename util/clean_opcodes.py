import pandas as pd

def clean_opcodes(filename):

	df = pd.read_csv(filename)
	cleaned_df = df.dropna()
	opcodes = cleaned_df.set_index('Opcode').T.to_dict('list')

	# import ipdb
	# ipdb.set_trace()

	return opcodes

filename = "opcodes.csv"
clean_opcodes(filename)