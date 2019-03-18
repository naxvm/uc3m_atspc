import _aux as aux


def hard(sequences, G):

	# the *trellis* for this matrix is obtained
	state_and_input_to_state, state_and_input_to_output = aux.trellis_from_generating_matrix(G)

	n_outputs = len(G) #Numero de columnas de G

	states = len(G[0])-1 #grado del polinomio - 1

	# TODO: ...and the possible inputs
	inputs = ['0','1'] ##TODO

	# TODO: number of Viterbi stages is computed from the length of the sequence(s) and the number of outputs
	# n_stages =

	# TODO: initialization
	# ...

	# for every stage in the algorithm...
	for i_stage in range(n_stages):

		# for every possible state...
		for i_state, state in enumerate(states):

			# for every possible input...
			for i_input, input in enumerate(inputs):

				# TODO
				pass

	return decoded_sequence

