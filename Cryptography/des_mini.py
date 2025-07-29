input_48_bits = "11000010011100110111100111110001111000101100110111100"
group_of_6bit = []
print(f"Splitting {input_48_bits} into 8 groups of 6 bits")
for i in range(0,48,6):
    group_of_6bit.append(input_48_bits[i:i+6])
s_box = [
            [14, 4, 13, 1, 2, 15, 11, 8, 3, 10, 6, 12, 5, 9, 0, 7],
            [0, 15, 7, 4, 14, 2, 13, 1, 10, 6, 12, 11, 9, 5, 3, 8],
            [4, 1, 14, 8, 13, 6, 2, 11, 15, 12, 9, 7, 3, 10, 5, 0],
            [15, 12, 8, 2, 4, 9, 1, 7, 5, 11, 3, 14, 10, 0, 6, 13]
 ]

result = []  
    
 
row_of_group = int(str(group_of_6bit[0][0])+str(group_of_6bit[0][5]),2)
column_of_group = int(group_of_6bit[0][1:5],2)
s_box_result = s_box[row_of_group][column_of_group]
s_box_result_in_4bit_binary = bin(s_box_result).replace("0b","").zfill(4) 
result.append(s_box_result_in_4bit_binary)
print("Result of first sbox \n"+group_of_6bit[0]+"->"+s_box_result_in_4bit_binary+" using 1st Sbox")

