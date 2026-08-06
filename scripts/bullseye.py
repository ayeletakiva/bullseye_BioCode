import random

def create_quartet():
    rand_seq = ''
    nucleotides = ['A','C','T','G']
    length = 4
    for i in range(length):
        rand_seq = rand_seq + random.choice(nucleotides)
    return rand_seq


### main program ###
