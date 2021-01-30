import numpy as np 

S_BOX = [
    ["63", "7C", "77", "7B", "F2", "6B", "6F", "C5", "30", "01", "67", "2B", "FE", "D7", "AB", "76"],
    ["CA", "82", "C9", "7D", "FA", "59", "47", "F0", "AD", "D4", "A2", "AF", "9C", "A4", "72", "C0"],
    ["B7", "FD", "93", "26", "36", "3F", "F7", "CC", "34", "A5", "E5", "F1", "71", "D8", "31", "15"],
    ["04", "C7", "23", "C3", "18", "96", "05", "9A", "07", "12", "80", "E2", "EB", "27", "B2", "75"],
    ["09", "83", "2C", "1A", "1B", "6E", "5A", "A0", "52", "3B", "D6", "B3", "29", "E3", "2F", "84"],
    ["53", "D1", "00", "ED", "20", "FC", "B1", "5B", "6A", "CB", "BE", "39", "4A", "4C", "58", "CF"],
    ["D0", "EF", "AA", "FB", "43", "4D", "33", "85", "45", "F9", "02", "7F", "50", "3C", "9F", "A8"],
    ["51", "A3", "40", "8F", "92", "9D", "38", "F5", "BC", "B6", "DA", "21", "10", "FF", "F3", "D2"],
    ["CD", "0C", "13", "EC", "5F", "97", "44", "17", "C4", "A7", "7E", "3D", "64", "5D", "19", "73"],
    ["60", "81", "4F", "DC", "22", "2A", "90", "88", "46", "EE", "B8", "14", "DE", "5E", "0B", "DB"],
    ["E0", "32", "3A", "0A", "49", "06", "24", "5C", "C2", "D3", "AC", "62", "91", "95", "E4", "79"],
    ["E7", "C8", "37", "6D", "8D", "D5", "4E", "A9", "6C", "56", "F4", "EA", "65", "7A", "AE", "08"],
    ["BA", "78", "25", "2E", "1C", "A6", "B4", "C6", "E8", "DD", "74", "1F", "4B", "BD", "8B", "8A"],
    ["70", "3E", "B5", "66", "48", "03", "F6", "0E", "61", "35", "57", "B9", "86", "C1", "1D", "9E"],
    ["E1", "F8", "98", "11", "69", "D9", "8E", "94", "9B", "1E", "87", "E9", "CE", "55", "28", "DF"],
    ["8C", "A1", "89", "0D", "BF", "E6", "42", "68", "41", "99", "2D", "0F", "B0", "54", "BB", "16"]
]

inv_SBOX = [
    ["52", "09", "6A", "D5", "30", "36", "A5", "38", "BF", "40", "A3", "9E", "81", "F3", "D7", "FB"],
    ["7C", "E3", "39", "82", "9B", "2F", "FF", "87", "34", "8E", "43", "44", "C4", "DE", "E9", "CB"],
    ["54", "7B", "94", "32", "A6", "C2", "23", "3D", "EE", "4C", "95", "0B", "42", "FA", "C3", "4E"],
    ["08", "2E", "A1", "66", "28", "D9", "24", "B2", "76", "5B", "A2", "49", "6D", "8B", "D1", "25"],
    ["72", "F8", "F6", "64", "86", "68", "98", "16", "D4", "A4", "5C", "CC", "5D", "65", "B6", "92"],
    ["6C", "70", "48", "50", "FD", "ED", "B9", "DA", "5E", "15", "46", "57", "A7", "8D", "9D", "84"],
    ["90", "D8", "AB", "00", "8C", "BC", "D3", "0A", "F7", "E4", "58", "05", "B8", "B3", "45", "06"],
    ["D0", "2C", "1E", "8F", "CA", "3F", "0F", "02", "C1", "AF", "BD", "03", "01", "13", "8A", "6B"],
    ["3A", "91", "11", "41", "4F", "67", "DC", "EA", "97", "F2", "CF", "CE", "F0", "B4", "E6", "73"],
    ["96", "AC", "74", "22", "E7", "AD", "35", "85", "E2", "F9", "37", "E8", "1C", "75", "DF", "6E"],
    ["47", "F1", "1A", "71", "1D", "29", "C5", "89", "6F", "B7", "62", "0E", "AA", "18", "BE", "1B"],
    ["FC", "56", "3E", "4B", "C6", "D2", "79", "20", "9A", "DB", "C0", "FE", "78", "CD", "5A", "F4"],
    ["1F", "DD", "A8", "33", "88", "07", "C7", "31", "B1", "12", "10", "59", "27", "80", "EC", "5F"],
    ["60", "51", "7F", "A9", "19", "B5", "4A", "0D", "2D", "E5", "7A", "9F", "93", "C9", "9C", "EF"],
    ["A0", "E0", "3B", "4D", "AE", "2A", "F5", "B0", "C8", "EB", "BB", "3C", "83", "53", "99", "61"],
    ["17", "2B", "04", "7E", "BA", "77", "D6", "26", "E1", "69", "14", "63", "55", "21", "0C", "7D"]
]

R_const = [
     "01", "02", "04", "08","10",
    "20", "40", "80", "1B","36"
]

def SBOX_get_value(row, col, decr=0):
    if(decr):
        byte=inv_SBOX[int(row,16)][int(col,16)][0]
        byte2=inv_SBOX[int(row,16)][int(col,16)][1]
        return byte,byte2
    byte=S_BOX[int(row,16)][int(col,16)][0]
    byte2=S_BOX[int(row,16)][int(col,16)][1]
    return byte,byte2


def byte_shift(w):
    z=[]
    for i in range (len(w)-2):
        z.append(w[i+2])
    z.append(w[0])
    z.append(w[1])
    return z

def byte_shift_true(w, decrypt=0):
    z=[]
    if(decrypt==0):
        for i in range (len(w)-1):
            z.append(w[i+1])
        z.append(w[0])
    else:
        z.append(w[len(w)-1])
        for i in range (len(w)-1):
            z.append(w[i])
    return z

def XOR_R_const(byte1, byte2,round_n):
    R_byte1=R_const[round_n][0]
    R_byte2 =R_const[round_n][1]
    byte1= int(byte1,16) ^ int(R_byte1,16)
    byte2= int(byte2,16) ^ int(R_byte2,16)
    return str('%X' % byte1), str( '%X' % byte2)

def generate_keys(key):
    keys_10=[]
    
    #key="5468617473206D79204B756E67204675"
    keys_10.append(key)

    for i in range(10):
        key=list(keys_10[i])

        #splitting key to Ws
        w=[]
        index=0
        for e in range (4):
            w.append(key[index:index+8])
            index+=8
        #byte shifting
        g_w3=w[3]
        g_w3=byte_shift(g_w3)
        #sbox
        for j in range (0,8,2):
            g_w3[j], g_w3[j+1] = SBOX_get_value(g_w3[j],g_w3[j+1])
        #XOR with Rconst
        g_w3[0],g_w3[1]= XOR_R_const(g_w3[0],g_w3[1],i)
        str_gw=str()
        str_gw+=g_w3[0]+g_w3[1]+g_w3[2]+g_w3[3]+g_w3[4]+g_w3[5]+g_w3[6]+g_w3[7]

        #key2 generation
        #converting the weights to one string
        str_w= []
        
        for x in range (4):
            str_w0=str()
            str_w0+=w[x][0]+w[x][1]+w[x][2]+w[x][3]+w[x][4]+w[x][5]+w[x][6]+w[x][7]
            str_w.append(str_w0)
        new_w=[]
    
        new_w.append(str('{:08x}'.format (int(str_w[0],16) ^ int(str_gw,16))))
        new_w.append(str('{:08x}'.format (int(new_w[0],16) ^ int(str_w[1],16))))
        new_w.append(str('{:08x}'.format (int(new_w[1],16) ^ int(str_w[2],16))))
        new_w.append(str('{:08x}'.format (int(new_w[2],16) ^ int(str_w[3],16))))
        
        str_key=str()
        for y in range(len(new_w)):
            str_key+=new_w[y]
        
        keys_10.append(str_key)
    return keys_10

def to_SBOX(plain,decr=0):
    if (decr):
        for i in range(len(plain)):
            for j in range(len(plain)):
                to_2bytes=str()
                x, y = SBOX_get_value(plain[i][j][0],plain[i][j][1],decr)
                to_2bytes+=x+y
                plain[i][j]=to_2bytes
        return plain
    w=[]
    final=[]
    
    index=0
    plain=list(plain)
    for e in range (4):
        w.append(plain[index:index+8])
        index+=8
    for i in range(len(w)):
        for j in range (0,8,2):
            to_2bytes=str()
            w[i][j], w[i][j+1] = SBOX_get_value(w[i][j],w[i][j+1])
            to_2bytes+=w[i][j]+w[i][j+1]
            
            final.append(to_2bytes)
    return final

def to_shifting_bytes(plain):
    x=np.asarray(plain)
    x=np.asarray(np.array_split(plain, 4))
    x=x.transpose()
    for i in range(len(x)):
      for j in range(i):
          x[i]=byte_shift_true(x[i])
    return x

def to_shifting_bytes_decr(plain,decr):
    for i in range(len(plain)):
      for j in range(i):
          plain[i]=byte_shift_true(plain[i],decr)
    return plain


xtime = lambda a: (((a << 1) ^ 0x1B) & 0xFF) if (a & 0x80) else (a << 1)


def mix_one_col(a):
    t = int(a[0],16) ^ int(a[1],16) ^ int(a[2],16) ^ int(a[3],16)
    u = int(a[0],16)
    a[0] = '{:02x}'.format (int(a[0],16) ^ t ^ xtime(int(a[0],16) ^ int(a[1],16)))
    a[1] = '{:02x}'.format (int(a[1],16) ^ t ^ xtime(int(a[1],16) ^ int(a[2],16)))
    a[2] = '{:02x}'.format (int(a[2],16) ^ t ^ xtime(int(a[2],16) ^ int(a[3],16)))
    a[3] = '{:02x}'.format (int(a[3],16) ^ t ^ xtime(int(a[3],16) ^ u))
    return a



def mix_cols(s,decr=0):
    final_list=[]
    if(decr == 0):
        s=s.transpose()
    #s=s.transpose()
    for i in range(4):
        if(decr == 1):
            final_list.append(mix_one_col(s[i].tolist()))
        else:
            final_list.append(mix_one_col(s[i]))
    return final_list

def inv_mix_columns(s):
    final_list=[]
    s=s.transpose()
    #s=list(s)
    for i in range(4):
        s[i]=s[i].tolist()
        u = xtime(xtime(int(s[i][0],16) ^ int(s[i][2],16)))
        v = xtime(xtime(int(s[i][1],16) ^ int(s[i][3],16)))
        s[i][0] ='{:02x}'.format (int(s[i][0],16) ^ u)
        s[i][1] ='{:02x}'.format (int(s[i][1],16) ^ v)
        s[i][2] ='{:02x}'.format (int(s[i][2],16) ^ u)
        s[i][3] = '{:02x}'.format (int(s[i][3],16) ^ v)
    #print(mix_cols(s))
    return mix_cols(s,1)

def key_to_numpy(key):
    w=[]
    index=0
    key=list(key)
    bytes_list=[]
    for j in range (0,32,2):
        two_bytes=str()
        two_bytes+= key[j]+key[j+1]
        bytes_list.append(two_bytes)
    for e in range (4):
        w.append(bytes_list[index:index+4])
        index+=4
    x=np.asarray(w)
    x=np.asarray(np.array_split(x, 4))
    x=x.transpose()
    return x

"""
def mix_columns(plain):
    output=[[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0],]
    mix_cols=[["02", "03", "01", "01" ],
                      ["01" ,"02" ,"03" ,"01" ],
                      ["01" ,"01" ,"02" ,"03" ],
                      ["03", "01", "01" ,"02"]]
    for row in range(len(mix_cols)):
        temp=[]
        for i in range(len(plain[0])):
            temp2=0
            for j in range (len(plain)):
                temp2+= int(mix_cols[row][j],16) * int(plain[j][i],16)
                print(mix_cols[row][j])
                print(plain[j][i])
                output[row][i] ^= int(mix_cols[row][j],16) and int(plain[j][i],16)
        #temp.append(str('{:02x}'.format (int(mix_cols[row][col],16) * int(plain[col][row],16))))
        #temp.append(temp2)
        #output.append(temp)
    #print(output)
    return output
"""
def XOR(plain, key,decr=0):
    out=str()
    for i in range(4):
        for j in range(4):
            out+= str('{:02x}'.format (int(plain[j][i],16) ^ int(key[j][0][i],16)))
    return out

def str_2_matrix(plain):
    w=[]
    final=[]
    index=0
    plain=list(plain)
    for e in range (4):
        w.append(plain[index:index+8])
        index+=8
    for i in range(len(w)):
        for j in range (0,8,2):
            to_2bytes=str()
            to_2bytes+=w[i][j]+w[i][j+1]
            
            final.append(to_2bytes)
    x=np.asarray(final)
    x=np.asarray(np.array_split(final, 4))
    x=x.transpose()
    return x

def AES(plain,key,decr=0):
    keys=generate_keys(key)

    if(decr==0):
        #first XOR
        output_XOR= str('{:032x}'.format (int(plain,16) ^ int(keys[0],16)))
        #print(output_XOR)
        input_sbox=[]
        input_sbox.append(output_XOR)
        for i in range(10):
            output_SBOX=to_SBOX(input_sbox[i])
            output_shifting=to_shifting_bytes(output_SBOX)
            
            if i != 9:
                output_mix=mix_cols(output_shifting)
                output_mix=np.asarray(output_mix)
                output_mix=output_mix.transpose()
            new_key=key_to_numpy(keys[i+1])
            if i == 9:
                out_xor2=XOR(output_shifting,new_key)
            else:
                out_xor2=XOR(output_mix,new_key)
            input_sbox.append(out_xor2)
            #output_XOR2= str('{:032x}'.format (int(output_mix,16) ^ int(new_key,16)))
            #print(out_xor2)
        return out_xor2
    else:
        #first XOR
        output_XOR= str('{:032x}'.format (int(plain,16) ^ int(keys[len(keys)-1],16)))
        #print("xor")
        #print(output_XOR)
        input_shift=str_2_matrix(output_XOR)
        input_shift_list=[]
        input_shift_list.append(input_shift)
        for i in range(10):
            output_shifting=to_shifting_bytes_decr(input_shift_list[i],1)
            #print("shiftrows")
            #print(output_shifting)
            output_SBOX=to_SBOX(output_shifting,1)
            #print("sbox")
            #print(output_SBOX)
            new_key=key_to_numpy(keys[len(keys)-(i+2)])
            out_xor=XOR(output_SBOX,new_key,1)
            #print("xor")
            #print(out_xor)
            in_mix=str_2_matrix(out_xor)
            
            if i !=9 :
                out_mix=inv_mix_columns(in_mix)
            out_mix=np.asarray(out_mix)
            out_mix=out_mix.transpose()
            input_shift_list.append(out_mix)
            #print("mix")
            #print(out_mix)
            
        return out_xor


while(1):
    enc_dec=input("press 0 for encryption \npress 1 for decryption \npress 2 to exit:")
    if(2== int(enc_dec)):
        break
    key=input("Enter key in hex:")
    texts=input("Enter text in hex:")
    cipher=AES(texts,key,int(enc_dec))
    print("output:")
    print(cipher)
    



#cipher=AES("54776F204F6E65204E696E652054776F","5468617473206D79204B756E67204675",0)
#cipher=AES("29C3505F571420F6402299B31A02D73A","5468617473206D79204B756E67204675",1)

