from numpy import array_split, asarray, dot, multiply
from math import ceil, sqrt
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

    #filling the matrix
    for j in range (len(key)):
        if key[j] not in matrix:
            matrix.append(key[j])
    for i in range(len(alphabets)):
        if alphabets[i] not in matrix:
            matrix.append(alphabets[i])
    
    matrix=asarray(matrix)
    matrix=array_split(matrix,5)
    #encrypt
    for i in range(0,len(plain),2):
        row,col=get_indices(plain[i],matrix)
        row2,col2=get_indices(plain[i+1],matrix)

        #shift down
        if(col == col2):
            cipher+=matrix[(row+1) % 5][col]
            cipher+= matrix[(row2+1) %5][col]
        #shift right
        elif (row== row2):
            cipher+=matrix[row][(col+1) %5]
            cipher+= matrix[row2][(col2+1)%5]
        
        else:
            cipher+=matrix[row][col2]
            cipher+=matrix[row2][col]

    return cipher

def hill(plain, key):
    key=asarray(key)
    key=array_split(key,sqrt(len(key)))

    while len(plain)% len(key) != 0:
        plain += "X"
    plain=plain.upper()
    plain =list(plain)
    #convert to ascii
    plain_converted=[]
    for i in range(len(plain)):
        plain_converted.append(ord(plain[i])-65)
    
    plain_converted=asarray(plain_converted)
    plain_converted=array_split(plain_converted, (len(plain_converted)/ len(key)))

    cipher=[]
    key=asarray(key)
    for i in range(len(plain_converted)):
        #print(key)
        #print(plain_converted[i])
        r=key.dot(plain_converted[i].transpose())
        r=(r  % 26) +65
        cipher.append(r)
    
    cipher_str=str()
    for j in range(len(cipher)):
        for x in range(len(cipher[j])):
            cipher_str+= chr(cipher[j][x])
            #cipher_str+=chr((((cipher[j][x]%26) + 65) % 26) + ord("A"))
            
    return cipher_str

def vigenere(plain, key, mode):
    key=key.upper()
    plain=plain.upper()
    new_key=[]
    if mode:
        key+=plain[:len(plain)-len(key)]
        #for i in range(len(plain)-len(key)):
         #   key+="1"
    else:
        for i in range(len(plain)-len(key)):
            key+=key[:len(plain)-len(key)]
 
    for i in range(len(key)):
        new_key.append(ord(key[i])-65)

    cipher=str()
    for i in range (len(plain)):
        cipher+=caesar(plain[i],new_key[i])
    return cipher

def vernam(plain,key):
    key=key.upper()
    plain=plain.upper()
    new_key=[]
    new_plain=[]
    for i in range(len(plain)-len(key)):
            key+=key[:len(plain)-len(key)]
    for i in range(len(key)):
        new_key.append(ord(key[i])-65)
    
    for i in range(len(plain)):
        new_plain.append(ord(plain[i])-65)

    cipher=str()
    for i in range(len(plain)):
        cipher+= chr(((new_plain[i] ^ new_key[i]))+65 )
    return cipher

def write_file(file_name,lines):
    file1 = open(file_name, 'w')
    file1.writelines(lines)
    file1.close()

def read_file(file_name):
    file1 = open(file_name, 'r')
    lines = file1.readlines()
    return lines



#encrypting in files
#casear
text_ce=[]
plains=read_file('Input_Files/Caesar/caesar_plain.txt')
text_ce.append("Key is 3:\n")
for i in range(len(plains)):
    cipher = caesar(plains[i].replace("\n",""),3)
    text_ce.append(cipher)
    text_ce.append("\n")
text_ce.append("\nKey is 6:\n")
for i in range(len(plains)):
    cipher = caesar(plains[i].replace("\n",""),6)
    text_ce.append(cipher)
    text_ce.append("\n")
text_ce.append("\nKey is 12:\n")
for i in range(len(plains)):
    cipher = caesar(plains[i].replace("\n",""),12)
    text_ce.append(cipher)
    text_ce.append("\n")
write_file('output/casaer_cipher.txt',text_ce)

#playfair
text_ce.clear()
plains=read_file('Input_Files/PlayFair/playfair_plain.txt')
text_ce.append("Key is rats:\n")
for i in range(len(plains)):
    cipher = playfair(plains[i].replace("\n",""),"rats")
    text_ce.append(cipher)
    text_ce.append("\n")
text_ce.append("\nKey is archangel:\n")
for i in range(len(plains)):
    cipher = playfair(plains[i].replace("\n",""),"archangel")
    text_ce.append(cipher)
    text_ce.append("\n")
write_file('output/playfair_cipher.txt',text_ce)

#hill
text_ce.clear()
plains=read_file('Input_Files/Hill/hill_plain_2x2.txt')
key=[5,17,8,3]
for i in range(len(plains)):
    cipher =hill(plains[i].replace("\n",""),key)
    text_ce.append(cipher)
    text_ce.append("\n")
write_file('output/hill_cipher_2x2.txt',text_ce)
text_ce.clear()
plains=read_file('Input_Files/Hill/hill_plain_3x3.txt')
key=[2,4,12,9,1,6,7,5,3]
for i in range(len(plains)):
    cipher =hill(plains[i].replace("\n",""),key)
    text_ce.append(cipher)
    text_ce.append("\n")
write_file('output/hill_cipher_3x3.txt',text_ce)

#Vigenere
text_ce.clear()
plains=read_file('Input_Files/Vigenere/vigenere_plain.txt')
text_ce.append("Key is PIE (repeating mode):\n")
for i in range(len(plains)):
    cipher = vigenere(plains[i].replace("\n",""),"pie",False)
    text_ce.append(cipher)
    text_ce.append("\n")
text_ce.append("\nKey is  aether (auto mode):\n")
for i in range(len(plains)):
    cipher = vigenere(plains[i].replace("\n",""),"aether",True)
    text_ce.append(cipher)
    text_ce.append("\n")
write_file('output/vigenere_cipher.txt',text_ce)

#Vernam
text_ce.clear()
plains=read_file('Input_Files/Vernam/vernam_plain.txt')
text_ce.append("Key is SPARTANS:\n")
for i in range(len(plains)):
    cipher = vernam(plains[i].replace("\n",""),"SPARTANS")
    text_ce.append(cipher)
    text_ce.append("\n")
write_file('output/vernam_cipher.txt',text_ce)

#user input
plain= input("Enter the plain text:")
key_ce=input("Enter key of caesar:")
key_play=input("Enter key of playfair:")
key_hill = input("Key of hill separated by space:")
key_hill=key_hill.split(" ")
#key_hill=key_hill.split("\n")
print(type(key_hill))
for i in range(len(key_hill)):
    key_hill[i]=int(key_hill[i])
print(key_hill)
key_vig=input("Enter key of vigenere:")
mode=input("Mode of vigenere, press 0 for repeat, or press 1 for auto:")
key_ver=input("Enter key of vernam:")

c1=caesar(plain,int(key_ce))
c2=playfair(plain,key_play)
c3=hill(plain,key_hill)
c4=vigenere(plain,key_vig,int(mode))
c5=vernam(plain,key_ver)
print("cipher of caesar:")
print(c1)
print("cipher of playfair:")
print(c2)
print("cipher of hill:")
print(c3)
print("cipher of vigenere:")
print(c4)
print("cipher of vernam:")
print(c5)

#vigenere("mdampuaf","aether", True)
#print(playfair("ipmxxpzw","rats"))
#print(vernam("PLIVFAJW", "SPARTANS"))