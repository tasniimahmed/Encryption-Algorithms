def dec_to_bin(n,bits):
    n= int(n)
    s= bin(n & int("1"*bits,2))[2:]
    return ("{0:0>%s}" % (bits)).format(s)

def Permutation( key_pos_dic, permu_num):
    new_key=[]
    permutation_choice1= [57,49,41,33,25,17,9,
    1,58,50,42,34,26,18,10,2,59,51,43,35,27,19,11,3,60,
    52,44,36,63,55,47,39,31,23,15,7,62,54,46,38,30,
    22,14,6,61,53,45,37,29,21,13,5,28,20,12,4]

    permutation_choice2 = [14,17,11,24,1,5,3,28,15,6,21,10,23
    ,19,12,4,26,8,16,7,27,20,13,2,41,52,31,37,47,55,30,40,51,45,33,48,44,
    49,39,56,34,53,46,42,50,36,29,32]

    if permu_num == 1:
        permutation_choice= permutation_choice1
    else:
        permutation_choice=permutation_choice2
    
    #print("LIIIIk")
    #print(key_pos_dic.keys())

    for i in permutation_choice:
        bit=key_pos_dic.get(i)
        new_key.append(bit)
    #print("new key", new_key)
    return new_key

def left_circ_shift(key, round):
    key_1 = key[:28]
    key_2 = key[28:]
    if round == 1 or round == 2 or round == 9 or round == 16 : 
    #shifting by 1 bit
        first_bit = key_1[0]
        del key_1[0]
        key_1.append(first_bit)

        first_bit2 = key_2[0]
        del key_2[0]
        key_2.append(first_bit2)
        key_1.extend(key_2)
        
    #shifting by two bits
    else:
        first_bit = key_1[0]
        second_bit = key_1[1]
        del key_1[0]
        del key_1[1]
        key_1.append(first_bit)
        key_1.append(second_bit)

        first_bit2 = key_2[0]
        second_bit2 = key_2[1]
        del key_2[0]
        del key_2[1]
        key_2.append(first_bit2)
        key_2.append(second_bit2)

        key_1.extend(key_2)
    return key_1

def fill_dic_indices(key):
    key_pos_dic= {}
    index=1
    #filling a dictionary with the position of each bit for permutation
    for k in key:
        key_pos_dic[index] = k
        index += 1
    return key_pos_dic

def generate_keys(key, round):

    keys_16 = []

    key_in_bin= str()
    key= "0123456789ABCDEF"
    scale = 16 ## equals to hexadecimal
    for i in range (len(key)):
        key_in_bin+=bin(int(key[i], scale))[2:].zfill(4)
    
    #key is 64
    #filling a dictionary with the position of each bit for permutation
    key_pos_dic= fill_dic_indices(key_in_bin)
    #1st permutation
    first_permutation_output= Permutation( key_pos_dic,1)

    #generating the 16 keys
    for i in range(16):
        shifted_key = left_circ_shift(first_permutation_output,i+1)
        key_pos_dic2= fill_dic_indices(shifted_key)
        final_key= Permutation( key_pos_dic2,2)
        keys_16.append(final_key)
    
    return keys_16


x=generate_keys(1,3)
print(len(x))