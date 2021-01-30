import numpy as np
def caesar(plain,key):
    cipher=str()
    plain=plain.upper()
    for i in range (len(plain)):
        cipher+=chr((((ord(plain[i])+key) -65 )% 26) +65 )
    return cipher

def get_indices(letter,matrix):
    for i in range(5):
        for j in range(5):
            if(matrix[i][j] == letter):
                return i, j

def playfair(plain,key):
    cipher=str()
    plain=plain.upper()
    key = key.upper()
    matrix=[]
    key=key.replace('J','I')
    plain=plain.replace('J','I')
    alphabets=['A','B','C','D','D','E','F','G','H','I','K','L','M','N','O','P','Q',
    'R','S','T','U','V','W','X','Y','Z']

    #getting plain ready
    plain=list(plain)
    for i in range(0,len(plain),2):
        if(plain[i] == plain[i+1]):
            plain.insert(i+1,'X')
    if (len(plain) %2) != 0:
        plain.append("X")
    print(plain)

    #filling the matrix
    for j in range (len(key)):
        if key[j] not in matrix:
            matrix.append(key[j])
    for i in range(len(alphabets)):
        if alphabets[i] not in matrix:
            matrix.append(alphabets[i])
    
    matrix=np.asarray(matrix)
    print(matrix)
    matrix=np.array_split(matrix,5)
    #encrypt
    for i in range(0,len(plain),2):
        print(plain[i])
        row,col=get_indices(plain[i],matrix)
        row2,col2=get_indices(plain[i+1],matrix)

        #shift down
        if(col == col2):
            cipher+=matrix[(row+1) % 5][col]
            cipher+= matrix[(row2+1) %5][col]
        #shift right
        elif (row== row2):
            print(col)
            print("***",(col+1) %5 )
            cipher+=matrix[row][(col+1) %5]
            cipher+= matrix[row2][(col2+1)%5]
        
        else:#print(row,col,row2,col2)
            cipher+=matrix[row][col2]
            cipher+=matrix[row2][col]

    return cipher
print(playfair("ipmxxpzw","rats"))
