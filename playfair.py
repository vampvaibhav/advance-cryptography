import string
import itertools
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
# Create our empty matrix and fill it with our values
def prepare_input(message):
   
    
    message = ''.join([c.upper() for c in message if c in string.ascii_letters])
    clean = ""
    
    if len(message) < 2:
        return message
    for i in range(len(message)-1):
        clean += message[i]
        
        if message[i] == message[i+1]:
            clean += 'X'
    clean += message[-1]
    if len(clean) & 1:
        clean += 'X'

    return clean

def divider(seq, size):
    it = iter(seq)
    while True:
       lump = tuple(itertools.islice(it, size))
       if not lump:
           return
       yield lump
       
def generate_table(key):

     
    table = []

    # copy key chars into the table if they are in `alphabet` ignoring duplicates
    for char in key.upper():
        if char not in table and char in LETTERS:
            table.append(char)

    # fill the rest of the table in with the remaining alphabet chars
    for char in LETTERS:
        if char not in table:
            table.append(char)
    print('key table is:\n',table)
    return table
    
import time
def encrypt(message, key):
    
    start = time.clock()
    table = generate_table(key)
    message= prepare_input(message)
    encryptedtext = ""
    
   
    for char1, char2 in divider(message, 2):
        row1, col1 = divmod(table.index(char1), 5)
        row2, col2 = divmod(table.index(char2), 5)

        if row1 == row2:
            encryptedtext += table[row1*5+(col1+1)%5]
            encryptedtext += table[row2*5+(col2+1)%5]
        elif col1 == col2:
            encryptedtext += table[((row1+1)%5)*5+col1]
            encryptedtext += table[((row2+1)%5)*5+col2]
        else: # rectangle
            encryptedtext += table[row1*5+col2]
            encryptedtext += table[row2*5+col1]

      
    print("YOUR ENCRYPTION PROCESS IS COMPLETED\n")
    print("CHECK THE Cipher.txt FILE\n")
    end = time.clock()
    print('Time taken in encryption process(sec): ', end - start)  
    return encryptedtext


def decrypt(message, key):
    start = time.clock()
    table = generate_table(key)
    plaintext = ""

    # https://en.wikipedia.org/wiki/Playfair_cipher#Description
    for char1, char2 in divider(message, 2):
        row1, col1 = divmod(table.index(char1), 5)
        row2, col2 = divmod(table.index(char2), 5)

        if row1 == row2:
            plaintext += table[row1*5+(col1-1)%5]
            plaintext += table[row2*5+(col2-1)%5]
        elif col1 == col2:
            plaintext += table[((row1-1)%5)*5+col1]
            plaintext += table[((row2-1)%5)*5+col2]
        else: # rectangle
            plaintext += table[row1*5+col2]
            plaintext += table[row2*5+col1]
            
    print("YOUR DECRYPTION PROCESS IS COMPLETED\n")
    print("CHECK THE Cipher.txt FILE\n")
    end = time.clock()
    print('Time taken in decryption process(sec): ', end - start) 
    return plaintext

def main():
    
  roaming() 
    
if __name__ == "__main__":
    main()





