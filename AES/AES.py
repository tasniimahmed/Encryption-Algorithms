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

R_const = [
     "01", "02", "04", "08","10",
    "20", "40", "80", "1B","36"
]

def SBOX_get_value(row, col):
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

def byte_shift_true(w):
    z=[]
    for i in range (len(w)-1):
        z.append(w[i+1])
    z.append(w[0])
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

def to_SBOX(plain):
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


xtime = lambda a: (((a << 1) ^ 0x1B) & 0xFF) if (a & 0x80) else (a << 1)


def mix_single_column(a):
    print(hex(int(a[0],16)))
    #print((int(a[0],16)+0x200) ^0x1B)
    #a=a.tolist()
    print(type(a))
    print(a)
    #a=['D4','BF','5D','30']
    t = int(a[0],16) ^ int(a[1],16) ^ int(a[2],16) ^ int(a[3],16)
    u = int(a[0],16)
    a[0] = '{:02x}'.format (int(a[0],16) ^ t ^ xtime(int(a[0],16) ^ int(a[1],16)))
    a[1] = '{:02x}'.format (int(a[1],16) ^ t ^ xtime(int(a[1],16) ^ int(a[2],16)))
    a[2] = '{:02x}'.format (int(a[2],16) ^ t ^ xtime(int(a[2],16) ^ int(a[3],16)))
    a[3] = '{:02x}'.format (int(a[3],16) ^ t ^ xtime(int(a[3],16) ^ u))
    return a

def mix_columns(s):
    final_list=[]
    s=s.transpose()
    for i in range(4):
        final_list.append(mix_single_column(s[i].tolist()))
    return final_list

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
def AES(plain,key):
    keys=generate_keys(key)
    #first XOR
    output_XOR= str('{:032x}'.format (int(plain,16) ^ int(keys[0],16)))
    for i in range(10):
        output_SBOX=to_SBOX(output_XOR)
        output_shifting=to_shifting_bytes(output_SBOX)
        print(output_shifting)
        x=mix_columns(output_shifting)
        print(x)
        x=np.asarray(x)
        x=x.transpose()
        print(x)
        break


#generate_keys(1)
AES("54776F204F6E65204E696E652054776F","5468617473206D79204B756E67204675")