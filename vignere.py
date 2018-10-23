import random
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
        #message=''.join(e for e in message if e.isalnum())
        
    
        #choice given by user in file
    userInput1 = input("enter the key you want to use:")
    key= userInput1
    userInput = input("Welcome to VAMP\n(type 'e' to encrypt)\n(type 'd' to decrypt):-")
    if userInput == 'e':
           
            fout.write(encrypt(message, key) + '\n')   
    else:
        if userInput == 'd':
            fout.write(decrypt(message, key) + '\n')
    
    fout.close()
    
import time
def encrypt(message, key):
    
    start = time.clock()
    encrypted_message = ""
    keyindex=0
    key=key.upper()
    for i in message:
        num=LETTERS.find(i.upper())
        if num!=-1:
            num+=LETTERS.find(key[keyindex])
            num %=len(LETTERS)
            if i.isupper():
             encrypted_message+=LETTERS[num]
            elif i.islower():
             encrypted_message+=LETTERS[num].lower()
            keyindex +=1
            if keyindex==len(key):
             keyindex=0
        else: 
         encrypted_message+=i      
    

   
    print("YOUR ENCRYPTION PROCESS IS COMPLETED\n")
    print("CHECK THE Cipher.txt FILE\n")
    end = time.clock()
    print('Time taken in encryption process(sec): ', end - start)  
    return encrypted_message


def decrypt(message, key):
    start = time.clock()
    decrypted_message = ""
    keyindex=0
    key=key.upper()
    for i in message:
        num=LETTERS.find(i.upper())
        if num!=-1:
            num-=LETTERS.find(key[keyindex])
            num %=len(LETTERS)
            if i.isupper():           
             decrypted_message+=LETTERS[num]
            elif i.islower():
             decrypted_message+=LETTERS[num]
             decrypted_message.lower
            keyindex +=1
            if keyindex==len(key):
             keyindex=0
        else: 
         decrypted_message+=i      
    print("YOUR DECRYPTION PROCESS IS COMPLETED\n")
    print("CHECK THE Cipher.txt FILE\n")
    end = time.clock()
    print('Time taken in decryption process(sec): ', end - start) 
    return decrypted_message

def main():
    roaming()
    
if __name__ == "__main__":
    main()




