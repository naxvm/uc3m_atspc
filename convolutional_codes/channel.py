import numpy as np

def binary_symmetric(sequences, Pe):
	aux_seq = np.asarray(sequences).ravel()
	flip_idx = np.random.randint(2, size=len(aux_seq)) > Pe
	output = np.logical_xor(list(map(bool,aux_seq)),flip_idx)

	return output.astype(int)

