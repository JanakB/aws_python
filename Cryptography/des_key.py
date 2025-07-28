input_64_bits = "1001110101010100110000100111001101111001111100011110001011110100"
#discard
key_56 =""
for ind,bit in enumerate(input_64_bits):
    if((ind+1)%8!=0):
        key_56 = key_56+bit
c0 = key_56[0:28]
d0 = key_56[28:56]

pc2_table = [14, 17, 11, 24, 1, 5, 3, 28,
                 15, 6, 21, 10, 23, 19, 12, 4,
                 26, 8, 16, 7, 27, 20, 13, 2,
                 41, 52, 31, 37, 47, 55, 30, 40,
                 51, 45, 33, 48, 44, 49, 39, 56,
                 34, 53, 46, 42, 50, 36, 29, 32]
                 
for i in range(16):
    single_shift_round = [1,2,9,16]
    if((i+1)in single_shift_round):
        c0 = c0[1:28] + c0[0]
        d0 = d0[1:28] + d0[0]
        key = c0+d0
    else:
        c0 = c0[2:28] + c0[0:2]
        d0 = d0[2:28] + d0[0:2]
        key = c0+d0
    key_48 = "".join([key[i-1] for i in pc2_table])
    print(f"Key for {i+1} round is {key_48}")



