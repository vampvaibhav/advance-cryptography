# -*- coding: utf-8 -*-
import sys,random,math
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
        
    
        #choice given by user in file
    userInput = input("Welcome to VAMP\n(type 'e' to encrypt)\n(type 'd' to decrypt):-")
    if userInput == 'e':
           
            fout.write(encrypt(message) + '\n')   
    else:
        if userInput == 'd':
            fout.write(decrypt(message) + '\n')
    
    fout.close()
#generating key  
def KeyGen():
    KA = int(input("enter the key you want to use for KA:"))
    KB = int(input("enter the key you want to use for KB:"))
    
    print(KA,KB)
    return (KA, KB)
#calculating gcd of number
def gcd(KA, size):
   while size:
    KA, size = size, KA % size
   return KA
#calculating inverse of number
def imod(KA,size):
    g=gcd(KA, size)
    print(g)
    if g != 1:
        raise Exception('modular inverse does not exist')
    c = 1
    while (c % KA > 0):
     c += size
    l=c // KA
    print(l)
    return l

    
#checking key validity
def KeyValid(KA, KB):
    if KA == 1:
     raise Exception('The affine cipher becomes incredibly weak when key A is set to 1. Choose a different key.')
   
    elif KB == 0:
     raise Exception('The affine cipher becomes incredibly weak when key B is set to 0. Choose a different key.')
     
    elif KA < 0 :
     raise Exception('Key A must be greater than 0 and Key B must be between 0 and %s.' % (len(LETTERS) - 1))
     
    elif gcd(KA, len(LETTERS)) != 1:
     raise Exception('Key A (%s) and the symbol set size (%s) are not relatively prime. Choose a different key.' % (KA, len(LETTERS)))
     

import time
def encrypt(message):
    
    start = time.clock()
    KA,KB=KeyGen()
    print(KA,KB)
    KeyValid(KA, len(LETTERS))
    encrypted_message = ""
    for i in message:
        if i == ' ':
            #Concatenate the space to the final message
            encrypted_message += ' '
        if i in LETTERS:
            index=LETTERS.find(i)
            encrypted_message += LETTERS[(index * KA + KB) % len(LETTERS)]
    

   
    print("YOUR ENCRYPTION PROCESS IS COMPLETED\n")
    print("CHECK THE Cipher.txt FILE\n")
    end = time.clock()
    print('Time taken in encryption process(sec): ', end - start)  
    return encrypted_message


def decrypt(message):
    start = time.clock()
    KA,KB=KeyGen()
    KeyValid(KA, KB)
    modKA=imod(KA,len(LETTERS))
    decrypted_message = ""
    for i in message:
        if i == ' ':
            #Concatenate the space to the final message
            decrypted_message += ' '
        if i in LETTERS:
            index=LETTERS.find(i)
            decrypted_message += LETTERS[(index- KB)*modKA % (len(LETTERS))]
       
    print("YOUR DECRYPTION PROCESS IS COMPLETED\n")
    print("CHECK THE Cipher.txt FILE\n")
    end = time.clock()
    print('Time taken in decryption process(sec): ', end - start) 
    return decrypted_message

def main():
    roaming()
   
    
if __name__ == "__main__":
    main()


































