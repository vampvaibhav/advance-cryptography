        #cryptanalysis on caesar cipher
def roaming():
    #reading file
    fin = open('C:/Users/Vamp/myceaser/analysis.txt', 'r')
    fout = open('C:/Users/Vamp/myceaser/analyresult.txt', 'w')
    fout.write('thanks for using vamp\n')
    fout.write('your result after brute force attack is:\n')
    container = fin.readlines() #Create a list that holds each line

    
    for i in container:
        #Each element of the list becomes a list (words)
        words = i.split()

        #Join together all the elements of the message in a string
        message = ' '.join(words)
        message = message.upper()
    reverse_alpha = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'[::-1] #notation used reverse element
    
    for key in range(26):
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
     #print('Key #%s: %s' % (key,decrypted_message))
     fout.write('Key #%s: %s'%(key,decrypted_message) + '\n') 
print("YOUR CRYPTANALYSIS PROCESS USING BRUTE FORCE IS COMPLETED\n")     
    
    

def main():
    roaming()
    
if __name__ == "__main__":
    main()



# -*- coding: utf-8 -*-

