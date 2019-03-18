import scipy.special
import math
import numpy as np
import encoding

def q_function(x):

	return 0.5 * scipy.special.erfc(x / math.sqrt(2))


def trellis_from_generating_matrix(G):

	state_and_input_to_state ={} #declaramos diccionarios vacios
	state_and_input_to_output={}

	states=[]##Declaramos el vector de estados posibles (Ver hoja cuadriculada)

	n_states=2**len(G[0]) ##Calculamos el 2^al numero de estados como numero de columnas del G
	for n in range(n_states):
		states.append(np.binary_repr(n).zfill(len(G[0]))) ##Creamos todos los posibles estados con sus entradas.

	for state in states: ##Recorremos los estados
		##Primer Diccionario
		bit_state = [int(x) for x in state] ##Iteramos para convertirlos en lista de enteros.
		aux_output=encoding.conv_encoding(G, bit_state)[-1] ##Usamos el encoding y separamos los dos ultimos como la salida del Trellis
		if not state[1:] in state_and_input_to_output.keys():##Rellenamos el diccionario de estados-salidas. Comprobamos que no se sobreescriban las keys.
			state_and_input_to_output[state[1:]]={}##Incializamos el diccionario interno.
		state_and_input_to_output[state[1:]][state[0]]="".join(map(str, aux_output))

		##Segundo diccionario
		if not state[1:] in state_and_input_to_state.keys():
			state_and_input_to_state[state[1:]]={}
		state_and_input_to_state[state[1:]][state[0]]=state[:-1]



	# a dictionary of dictionaries, the keys in the "outer one" being states and those in the "inner" one being inputs,
	# so that `state_and_input_to_state[s][i]` will give you the *state* the machine moves to when it is at state `s`
	# and input `i` is received
	# TODO: this is just an example, not the real thing
	# TODO 2: this is *hardwired* in the code, but this should actually be obtained from G

	## {'Estado actual' : { 'Entrada' : 'Estado final' } }
	#state_and_input_to_state = {'00': {'0': '00'}}

	# a dictionary of dictionaries, the keys in the "outer" one being states and those in the "inner" one being inputs,
	# so that `state_and_input_to_output[s][i]` will give you the *output* produced by the machine when it is at state
	# `s` and input `i` is received
	# TODO: see above TODO's

	## {'Estado actual' : { 'Entrada' : 'Salida' } }
	#state_and_input_to_output = {'00': {'0': '01'}}

	return state_and_input_to_state, state_and_input_to_output
