import numpy as np
def conv_encoding(G, sequences):

    status = list(np.zeros(len(G[0])-1, dtype=int))
    output = []
    for bit in sequences:
        inp = [bit]+status
        aux_output = []
        for poly in G:
            aux_output.append(np.sum(np.logical_and(inp, poly))%2)
        output.append(aux_output)
        #Actualizamos estados
        status = inp[:-1]
    return output



