# -*- coding: utf-8 -*-
import string
from math import sqrt
import numpy as np
LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
def roaming():
    #reading file
    fin = open('C:/Users/Vamp/myceaser/message.txt', 'r')
    fout = open('C:/Users/Vamp/myceaser/cipher.txt', 'w')
    fout.write('thanks for using vamp\n')
    fout.write('your output data is:\n')
    container = fin.readlines() #Create a list that holds each line

    
    for i in container:
        #Each element of the list becomes a list (words)
        words = i.split()
        message = ' '.join(words)
        message = message.upper()
        
    m=message
    m=''.join(e for e in m if e.isalnum())
        #choice given by user in file
    userInput1 = input("enter the key you want to use:")
    key=userInput1
    
    
    userInput = input("Welcome to VAMP\n(type 'e' to encrypt)\n(type 'd' to decrypt):-")
    if userInput == 'e':
           
            fout.write(encrypt(m, key) + '\n')   
    else:
        if userInput == 'd':
            fout.write(decrypt(m, key) + '\n')
    
    fout.close()
#checking validity of key
def keyvalid(key):
    n = int(sqrt(len(key)))
    if n * n != len(key):
        raise Exception("Invalid key length, should be square-root-able like")
        
#checking validity of message       
def messagevalid(key,message):
    n = int(sqrt(len(key)))
    p=len(message) 
    if(n!=p):
        raise Exception("key should be of length:",p*p)
    
def generate_table(key):
    key=key.upper() # because the input key is in lower form and leeters are in upper
    n = int(sqrt(len(key)))
    print ("[letter LENGTH]: ", len(LETTERS))
    genList = dict([(LETTERS[i], i * 1) for i in range(len(LETTERS))])
    print(genList)
    keylist = []
    for i in key:
     keylist.append(genList[i])#key list appending

    keymatrix = [] 
    for i in range(n):
        keymatrix.append(keylist[i * n : i * n + n])
    print('generated key is:\n',keymatrix)
    return keymatrix,genList

def checkdeterminant(keymatrix):
     determinant = np.linalg.det(keymatrix).round()
     print("Determinant of key is:", determinant)
     if determinant == 0:
            raise Exception("Determinant ZERO, CHANGE THE KEY!")
     elif determinant % len(LETTERS) == 0:
            raise Exception("Determinant divisible by ALPHA LENGTH, CHANGE THE KEY!")
     
import time
def encrypt(message, key):
    n = int(sqrt(len(key)))
    start = time.clock()
    keyvalid(key)
    messagevalid(key,message)
    keymatrix, genList = generate_table(key)
    checkdeterminant(keymatrix)
    encryptedtext = ''
    p=len(message) / n
    p=int(p)
    for i in range(p):
        lst = np.matrix( [[genList[a]] for a in message[i * n:i * n + n]] )
        print("message matrix is:\n",lst)
        result = keymatrix * lst
        print(result)
        encryptedtext += ''.join([LETTERS[int(result.A[j][0]) % len(LETTERS)] for j in range(len(result))])
    
    

    print("YOUR ENCRYPTION PROCESS IS COMPLETED\n")
    print("CHECK THE Cipher.txt FILE\n")
    end = time.clock()
    print('Time taken in encryption process(sec): ', end - start)  
    return encryptedtext


def decrypt(message, key):
    n = int(sqrt(len(key)))
    start = time.clock()
    keyvalid(key)
    messagevalid(key,message)
    keymatrix, genList = generate_table(key)
    checkdeterminant(keymatrix)
    inverseMatrixkey=np.linalg.inv(keymatrix)
    inverseMatrixkey=inverseMatrixkey% len(LETTERS)
    print(inverseMatrixkey)
    plaintext = ""
    p=len(message) / n
    p=int(p)
    for i in range(p):
        lst = np.matrix( [[genList[a]] for a in message[i * n:i * n + n]] )
        print(lst)
        result = inverseMatrixkey * lst
        print(result)
        plaintext += ''.join([LETTERS[int(result.A[j][0]) % len(LETTERS)] for j in range(len(result))])
    
    print("YOUR DECRYPTION PROCESS IS COMPLETED\n")
    print("CHECK THE Cipher.txt FILE\n")
    end = time.clock()
    print('Time taken in decryption process(sec): ', end - start) 
    return plaintext

def main():
    
  roaming() 
    
if __name__ == "__main__":
    main()






