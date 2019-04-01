#! /usr/bin/env python3

import math
import numpy as np
import matplotlib.pylab as plt

# our own stuff
import encoding
import channel
import decoding
import _aux as aux

#Define random seed
np.random.seed(1)

# ----------------------------- parameters

# the specific values given below are just examples, and you can try different ones

# number of simulated frames (realizations of the transmission)
n_frames = 100

# length of each frame
n_bits_per_frame = 1000

# generating matrix
G = [[1, 0, 1], [1, 1, 1]]

# Eb/N0's (in dBs) to be tested (this is just an example, a different range can be explored)
Eb_N0s_dBs = np.arange(12)

# ----------------------------- processing

# EbN0s are converted to natural units
Eb_N0s = 10 ** (Eb_N0s_dBs / 10)

# a `numpy` array to store every computed BER [<with/without coding>, <EbN0>, <frame>]
BER = np.empty((2, len(Eb_N0s_dBs), n_frames))

# for every simulated frame...
for i_frame in range(n_frames):

	print('processing frame {}'.format(i_frame))

	# A random sequence of bits is generated
	sequence = np.random.randint(0,2,n_bits_per_frame)


	# the sequence is encoded
	encoded_sequence = encoding.conv_encoding(G, sequence)

	# print(encoded_sequence)

	# for every EbN0 to be tested...
	for i_ebn0, ebn0 in enumerate(Eb_N0s):

		# ================= *with* coding
		#print("Eb_N0: ", ebn0)
		r=1.0/len(G) ##Para cualquier G

		m=1

		# the probability of error is computed from the EbN0
		Pe = aux.q_function(math.sqrt(ebn0 * 2 * m * r))

		# transmission is simulated
		received_sequence = channel.binary_symmetric(encoded_sequence, Pe)

		# decoding
		decoded_sequence = decoding.hard(received_sequence, G)

		BER[0, i_ebn0, i_frame] = aux.hamming_distance(sequence, decoded_sequence)/n_bits_per_frame

		# ================= *without* coding

		# the probability of error is computed from the EbN0
		Pe = aux.q_function(math.sqrt(2*m*ebn0))

		# the simulated sequence is transmitted as is
		received_sequence = channel.binary_symmetric(sequence, Pe)

		# TODO: the BER is computed
		BER[1, i_ebn0, i_frame] = aux.hamming_distance(received_sequence, sequence)/n_bits_per_frame

# average BER over all the frames
average_BER = BER.mean(axis=2)

# TODO: plotting
fig, ax = plt.subplots()
ax.semilogy(Eb_N0s_dBs,average_BER[0,:], Eb_N0s_dBs,average_BER[1,:])
ax.set_title('BER vs. SNR')
ax.set_xlabel('SNR (dB)')
ax.set_ylabel('BER')
ax.xaxis.grid(True)
ax.grid(which = 'minor')
plt.legend(['Without coding', 'With coding'], loc='best')

# figure is saved
plt.savefig('BER{}.pdf'.format(n_bits_per_frame))
