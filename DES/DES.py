import numpy as np 

S_BOX= [# S1
		[[14, 4, 13, 1, 2, 15, 11, 8, 3, 10, 6, 12, 5, 9, 0, 7],
		 [0, 15, 7, 4, 14, 2, 13, 1, 10, 6, 12, 11, 9, 5, 3, 8],
		 [4, 1, 14, 8, 13, 6, 2, 11, 15, 12, 9, 7, 3, 10, 5, 0],
		 [15, 12, 8, 2, 4, 9, 1, 7, 5, 11, 3, 14, 10, 0, 6, 13]],

		# S2
		[[15, 1, 8, 14, 6, 11, 3, 4, 9, 7, 2, 13, 12, 0, 5, 10],
		 [3, 13, 4, 7, 15, 2, 8, 14, 12, 0, 1, 10, 6, 9, 11, 5],
		 [0, 14, 7, 11, 10, 4, 13, 1, 5, 8, 12, 6, 9, 3, 2, 15],
		 [13, 8, 10, 1, 3, 15, 4, 2, 11, 6, 7, 12, 0, 5, 14, 9]],

		# S3
		[[10, 0, 9, 14, 6, 3, 15, 5, 1, 13, 12, 7, 11, 4, 2, 8],
		 [13, 7, 0, 9, 3, 4, 6, 10, 2, 8, 5, 14, 12, 11, 15, 1],
		 [13, 6, 4, 9, 8, 15, 3, 0, 11, 1, 2, 12, 5, 10, 14, 7],
		 [1, 10, 13, 0, 6, 9, 8, 7, 4, 15, 14, 3, 11, 5, 2, 12]],

		# S4
		[[7, 13, 14, 3, 0, 6, 9, 10, 1, 2, 8, 5, 11, 12, 4, 15],
		 [13, 8, 11, 5, 6, 15, 0, 3, 4, 7, 2, 12, 1, 10, 14, 9],
		 [10, 6, 9, 0, 12, 11, 7, 13, 15, 1, 3, 14, 5, 2, 8, 4],
		 [3, 15, 0, 6, 10, 1, 13, 8, 9, 4, 5, 11, 12, 7, 2, 14]],

		# S5
		[[2, 12, 4, 1, 7, 10, 11, 6, 8, 5, 3, 15, 13, 0, 14, 9],
		 [14, 11, 2, 12, 4, 7, 13, 1, 5, 0, 15, 10, 3, 9, 8, 6],
		 [4, 2, 1, 11, 10, 13, 7, 8, 15, 9, 12, 5, 6, 3, 0, 14],
		 [11, 8, 12, 7, 1, 14, 2, 13, 6, 15, 0, 9, 10, 4, 5, 3]],

		# S6
		[[12, 1, 10, 15, 9, 2, 6, 8, 0, 13, 3, 4, 14, 7, 5, 11],
		 [10, 15, 4, 2, 7, 12, 9, 5, 6, 1, 13, 14, 0, 11, 3, 8],
		 [9, 14, 15, 5, 2, 8, 12, 3, 7, 0, 4, 10, 1, 13, 11, 6],
		 [4, 3, 2, 12, 9, 5, 15, 10, 11, 14, 1, 7, 6, 0, 8, 13]],

		# S7
		[[4, 11, 2, 14, 15, 0, 8, 13, 3, 12, 9, 7, 5, 10, 6, 1],
		 [13, 0, 11, 7, 4, 9, 1, 10, 14, 3, 5, 12, 2, 15, 8, 6],
		 [1, 4, 11, 13, 12, 3, 7, 14, 10, 15, 6, 8, 0, 5, 9, 2],
		 [6, 11, 13, 8, 1, 4, 10, 7, 9, 5, 0, 15, 14, 2, 3, 12]],

		# S8
		[[13, 2, 8, 4, 6, 15, 11, 1, 10, 9, 3, 14, 5, 0, 12, 7],
		 [1, 15, 13, 8, 10, 3, 7, 4, 12, 5, 6, 11, 0, 14, 9, 2],
		 [7, 11, 4, 1, 9, 12, 14, 2, 0, 6, 10, 13, 15, 3, 5, 8],
		 [2, 1, 14, 7, 4, 10, 8, 13, 15, 12, 9, 0, 3, 5, 6, 11]]
         ]
 
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

    permutation_choice3=[58,50,42,34,26,18,10,2,
            60,52,44,36,28,20,12,4,
            62,54,46,38,30,22,14,6,
            64,56,48,40,32,24,16,8,
            57,49,41,33,25,17,9,1,
            59,51,43,35,27,19,11,3,
            61,53,45,37,29,21,13,5,
            63,55,47,39,31,23,15,7]
    
    expansion_choice=[32,1,2,3,4,5,
                  4,5,6,7,8,9,
                  8,9,10,11,12,13,
                 12,13,14,15,16,17,
                 16,17,18,19,20,21,
                 20,21,22,23,24,25,
                 24,25,26,27,28,29,
                 28,29,30,31,32,1]

    permutation_choice4=[16,7,20,21,
                         29,12,28,17,
                          1,15,23,26,
                          5,18,31,10,
                          2,8,24,14,
                         32,27,3,9,
                         19,13,30,6,
                         22,11,4,25]
    
    permutation_choice5 = [40,8,48,16,56,24,64,32,
            39,7,47,15,55,23,63,31,
            38,6,46,14,54,22,62,30,
            37,5,45,13,53,21,61,29,
            36,4,44,12,52,20,60,28,
            35,3,43,11,51,19,59,27,
            34,2,42,10,50,18,58,26,
            33,1,41,9,49,17,57,25]

    if permu_num == 1:
        permutation_choice= permutation_choice1
    elif permu_num ==2:
        permutation_choice=permutation_choice2
    elif permu_num == 3:
        permutation_choice=permutation_choice3
    elif permu_num == 4:
        permutation_choice=expansion_choice
    elif permu_num == 5:
        permutation_choice=permutation_choice4
    elif permu_num == 6:
        permutation_choice= permutation_choice5

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

def generate_keys(key):

    keys_16 = []
    key_in_bin= str()
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


def SBOX_get_value(bits_6,sbox):
    r="0b"+str(bits_6[0])+ str(bits_6[5])
    c="0b"+str(bits_6[1])+str(bits_6[2])+str(bits_6[3])+str(bits_6[4])
    row= int(r,2)
    col = int(c,2)
    value =sbox[row][col]
    return value


def to_sbox(bits_64):
    values=[]
    bits_64=np.asarray(bits_64)
    bits_64_splitted= np.array_split(bits_64, 8)
    for i in range(8):
        value =SBOX_get_value(bits_64_splitted[i],S_BOX[i])
        values.append(value)
    return values

def recursive_DES(L,R,key, stop,key_index,decrypt):
    if stop == 16:
        return L, R
    else:
        R0_dic=fill_dic_indices(R)
        #expand R
        R0_expanded= Permutation(R0_dic,4)
        #xor R with key
        
        output=[]
        for i in range (len(R0_expanded)):
            out=int(R0_expanded[i]) ^ int(key[key_index][i])
            output.append(out)
        
        #SBOX
        values=to_sbox(output)
        values_in_bin=str()
        for i in range(len(values)):
            values_in_bin+=dec_to_bin(values[i],4)
        values_pos_dic= fill_dic_indices(values_in_bin)
        #final permutation
        final_permutation_output= Permutation(values_pos_dic,5)

        R1=[]
        for i in range (len(L)):
            out=int(final_permutation_output[i]) ^ int(L[i])
            R1.append(out)
        stop+=1
        if(decrypt):
            key_index-=1
        else:
            key_index+=1
        return recursive_DES( R,R1,key,stop,key_index,decrypt)

def DES(plain, key, repeat,decrypt):
    if repeat-1 == 0:
        P_in_bin= str()
        #convert hexa to binary
        for i in range (len(plain)):
            P_in_bin+=bin(int(plain[i], 16))[2:].zfill(4)
        
        #key is 64
        #filling a dictionary with the position of each bit for permutation
        plain_pos_dic= fill_dic_indices(P_in_bin)
        #intial permutation
        first_permutation_output= Permutation( plain_pos_dic,3)
        #splitting
        L0=first_permutation_output[:32]
        R0= first_permutation_output[32:]
        keys= generate_keys(key)

        if (decrypt):
            L,R=recursive_DES(L0,R0,keys,0,15,1)
        else:
            L,R=recursive_DES(L0,R0,keys,0,0,0)
        encrypted_text=[]
        encrypted_text.extend(R)
        encrypted_text.extend(L)
        #final permutation
        enc_pos_dic= fill_dic_indices(encrypted_text)
        out_final_permu=Permutation(enc_pos_dic,6)
        to_numpy = np.asarray(out_final_permu)
        to_numpy=np.array_split(to_numpy, 16)
        cipher =[]
        for i in range(len(to_numpy)):
            s= "0b"+str(to_numpy[i][0])+str(to_numpy[i][1])+str(to_numpy[i][2])+str(to_numpy[i][3])
            n='%X' % int(s, 2)
            cipher.append(n)
        return cipher
    else:
        P_in_bin= str()
        #convert hexa to binary
        for i in range (len(plain)):
            P_in_bin+=bin(int(plain[i], 16))[2:].zfill(4)
        
        #key is 64
        #filling a dictionary with the position of each bit for permutation
        plain_pos_dic= fill_dic_indices(P_in_bin)
        #intial permutation
        first_permutation_output= Permutation( plain_pos_dic,3)
        #splitting
        L0=first_permutation_output[:32]
        R0= first_permutation_output[32:]
        #key generation
        keys= generate_keys(key)

        if (decrypt):
            L,R=recursive_DES(L0,R0,keys,0,15,1)
        else:
            L,R=recursive_DES(L0,R0,keys,0,0,0)
        encrypted_text=[]
        encrypted_text.extend(R)
        encrypted_text.extend(L)
        #final permutation
        enc_pos_dic= fill_dic_indices(encrypted_text)
        out_final_permu=Permutation(enc_pos_dic,6)
        to_numpy = np.asarray(out_final_permu)
        to_numpy=np.array_split(to_numpy, 16)
        cipher =[]
        for i in range(len(to_numpy)):
            s= "0b"+str(to_numpy[i][0])+str(to_numpy[i][1])+str(to_numpy[i][2])+str(to_numpy[i][3])
            n='%X' % int(s, 2)
            cipher.append(n)
        repeat= repeat-1
        return DES(cipher,key,repeat,decrypt)

    

while(1):
    enc_dec=input("press 0 for encryption \npress 1 for decryption \npress 2 to exit:")
    if(2== int(enc_dec)):
        break
    key=input("Enter the key:")
    plain=input("Enter text:")
    num = input("Enter number of encryption/decryption: ") 
    x=DES(plain,key,int(num),enc_dec)
    print("output:")
    print(''.join(x))
    

#key = input("Enter The key: ") 
#plain = input("Enter The plain text: ") 
#num = input("Enter number of encryption: ") 
#x=DES(plain,key,int(num),0)

#print("DECRYPTION:")
#y=DES(x,key,int(num),1)
#print(''.join(y))
