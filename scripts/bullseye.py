import random

def create_quartet():
    rand_seq = ''
    nucleotides = ['A','C','T','G']
    length = 4
    for i in range(length):
        rand_seq += random.choice(nucleotides)
    return rand_seq

def find_bulls(rand_str, gussed_str):
    bulls = 0
    sub_rand = ''
    sub_gussed = ''
    for i in range(len(rand_str)):
        if rand_str[i] == gussed_str[i]:
            bulls += 1
        else:
            sub_rand += rand_str[i]
            sub_gussed += gussed_str[i]
    return bulls, sub_rand, sub_gussed





### main program ###

rand = create_quartet()
print(rand)
test = input("Please try to guess a four DNA combination composed from A,T,C,G:\n")
bulls, sub_rand, sub_gussed = find_bulls(rand, test)
print(bulls, sub_rand, sub_gussed)