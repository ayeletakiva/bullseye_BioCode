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

def find_cows(sub_rand, sub_gussed):
    cows = 0
    rand_list = list(sub_rand)
    for char in sub_gussed:
        if char in rand_list:
            cows += 1
            rand_list.remove(char)         
    return cows





### main program ###

rand = create_quartet()
print(rand)
test = input("Please try to guess a four DNA combination composed from A,T,C,G:\n")
bulls, sub_rand, sub_gussed = find_bulls(rand, test)
cows = find_cows(sub_rand, sub_gussed)
print("bulls = %d \n cows= %d " % (bulls, cows))