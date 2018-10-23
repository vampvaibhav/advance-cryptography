         #message.txt contains input lines of the form
         #format for text:my name is vaibhav 3
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
        print(words)
        print(len(words))
        
        key = int(words[len(words) - 1])  #The key of the user is always the last element
        if(key<1 or key>26):
            print("unexpected key value\n")
            print("nothing is performed\n")
            return 0
        #choice = words[len(words) - 2]  #The choice of the user is always the second last element
        words.remove(str(key))
        print(words)
        #words.remove(choice)

        #Join together all the elements of the message in a string
        message = ' '.join(words)
        print(message)
        message = message.upper()
        message=''.join(e for e in message if e.isalnum())
        print(message)

        #choice given by user in file
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
    encrypted_message = "" #Finally, concatenate the letter at this location to the final message.
    alpha = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

    for i in message:
        #If the character is a space, add it to the final message.
        if i == ' ':
            #Concatenate the space to the final message
            encrypted_message += ' '
        else:
            location = key + alpha.index(i)
            location %= 26
            encrypted_message += alpha[location] ##Finally, concatenate
    print("YOUR ENCRYPTION PROCESS IS COMPLETED\n")
    print("CHECK THE Cipher.txt FILE\n")
    end = time.clock()
    print('Time taken in decryption process(sec): ', end - start) 
    return encrypted_message

def decrypt(message, key):
    start = time.clock()
    reverse_alpha = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'[::-1] #notation used reverse element
    decrypted_message = ""
    for i in message:
        if i == ' ':
            #Concatenate the space to the final message.
            decrypted_message += ' '
        else:
            location = key + reverse_alpha.index(i)
            location %= 26
            decrypted_message += reverse_alpha[location]

    decrypted_message = decrypted_message.lower()
    print("YOUR DECRYPTION PROCESS IS COMPLETED\n")
    print("CHECK THE Cipher.txt FILE\n")
    end = time.clock()
    print('Time taken in decryption process(sec): ', end - start) 
    return decrypted_message

def main():
    roaming()
    
if __name__ == "__main__":
    main()



