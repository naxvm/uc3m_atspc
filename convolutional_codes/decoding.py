import _aux as aux
import math
import numpy as np

def hard(sequences, G):

	# the *trellis* for this matrix is obtained
	state_and_input_to_state, state_and_input_to_output = aux.trellis_from_generating_matrix(G)

	#Outputs of the system
	n_outputs = len(G) #Numero de columnas de G

	#Trerllis states.
	states = list(state_and_input_to_state.copy().keys()) #grado del polinomio - 1

	#Inputs from Trellis.
	inputs =  list(state_and_input_to_state[states[0]].copy().keys())

	#Stages of the system.
	n_stages = math.floor(len(sequences) / n_outputs)

	#Distance Array per state
	prev_dist = np.zeros(len(states))
	next_dist = np.zeros(len(states))

	#We set values to something not possible to start measuring distance
	prev_dist[1:] = -1
	next_dist[:] = -1

	#Initialize Sequences Arrays
	prev_sequence = ["" for x in range(len(states))]
	next_sequence = ["" for x in range(len(states))]

	# for every stage in the algorithm...
	for i_stage in range(n_stages):
		# for every possible state...
		for i_state, state in enumerate(states):
			# for every possible input...
			for i_input, input in enumerate(inputs):
				#Check if state is available for iteration in the distance array
				if  prev_dist[i_state] >= 0:

					#Search the output in the trellis.
					output = state_and_input_to_output[state][input]

					#We 'move' our sequence windows given te stage.
					seq_window = range(i_stage * n_outputs, i_stage * n_outputs + n_outputs)

					#We measure the distance and update the old one (We need to do that to concat the sequence to check distance)
					dist = prev_dist[i_state]+aux.hamming_distance(''.join([str(bit) for bit in sequences[seq_window]]),output)

					#We get our next state and index for distance array
					next_state = state_and_input_to_state[state][input]
					index_state = states.index(next_state)
				#Check if distances are smaller or if they do exist and we update
					if next_dist[index_state] == -1 or dist < next_dist[index_state]:
						next_dist[index_state] = dist
						#We start copying the sequence for each distance index looking at the previous one
						next_sequence[index_state] = prev_sequence[i_state] + str(input)

		#Reset arrays after each stage is done.
		prev_dist=next_dist.copy()
		prev_sequence = next_sequence.copy()
		next_dist[:] = -1

	#Get the minimum distance
	min_sequence = np.argmin(prev_dist)
	#Get the sequence for that distance
	decoded_sequence = list(map(int, next_sequence[min_sequence]))

	return decoded_sequence