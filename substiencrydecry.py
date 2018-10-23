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
        message=''.join(e for e in message if e.isalnum())
        
    key = getRandomKey()
        #choice given by user in file
    userInput = input("Welcome to VAMP\n(type 'e' to encrypt)\n(type 'd' to decrypt):-")
    
    if userInput == 'e':
           
            fout.write(encrypt(message, key) + '\n')   
    else:
        if userInput == 'd':
            fout.write(decrypt(message, key) + '\n')
    
    fout.close()
#random key generator   
def getRandomKey():
 key = list(LETTERS)
 random.shuffle(key)
 print('using key:',key)
 return ''.join(key)


import time
def encrypt(message, key):
    
    start = time.clock()
    encrypted_message = "" #Finally, concatenate the letter at this location to the final message.
    

    for i in message:
        #If the character is a space, add it to the final message.
        if i == ' ':
            #Concatenate the space to the final message
            encrypted_message += ' '
        else:
           charsA = LETTERS
           charsB = key         
           # For decrypting, we can use the same code as encrypting. We
           # just need to swap where the key and LETTERS strings are used.
           #charsA, charsB = charsB, charsA          
    
        if i.upper() in charsA:
        # encrypt/decrypt the symbol
         symIndex = charsA.find(i.upper())
         if i.isupper():
          encrypted_message += charsB[symIndex].upper()
         else:
          encrypted_message += charsB[symIndex].lower()
        else:
        # symbol is not in LETTERS, just add it
         encrypted_message += i
    print("YOUR ENCRYPTION PROCESS IS COMPLETED\n")
    print("CHECK THE Cipher.txt FILE\n")
    end = time.clock()
    print('Time taken in encryption process(sec): ', end - start)  
    return encrypted_message


def decrypt(message, key):
    start = time.clock()
    decrypted_message = ""
    for i in message:
        #If the character is a space, add it to the final message.
        if i == ' ':
            #Concatenate the space to the final message
            decrypted_message += ' '
        else:
           charsA = LETTERS
           charsB = key         
           # For decrypting, we can use the same code as encrypting. We
           # just need to swap where the key and LETTERS strings are used.
           charsA, charsB = charsB, charsA          
    
        if i.upper() in charsA:
        # encrypt/decrypt the symbol
         symIndex = charsA.find(i.upper())
         if i.isupper():
          decrypted_message += charsB[symIndex].upper()
         else:
          decrypted_message += charsB[symIndex].lower()
        else:
        # symbol is not in LETTERS, just add it
         decrypted_message += i
    print("YOUR DECRYPTION PROCESS IS COMPLETED\n")
    print("CHECK THE Cipher.txt FILE\n")
    end = time.clock()
    print('Time taken in decryption process(sec): ', end - start) 
    return decrypted_message

def main():
    roaming()
    
if __name__ == "__main__":
    main()



