# -*- coding: utf-8 -*-

import string
string.ascii_lowercase
'''
The below code is a long form of the Caesar Cipher
def caesar(message, key):
    coded_message = ""
    alphabet = string.ascii_lowercase + " "
    letters = dict(enumerate(alphabet))
    key = 3
    code = {letter: (place + key) % 27 for (place, letter)
        in enumerate(alphabet)}
    num = []
    for char in message:
        num.append(code[char])
    for mun in num:
        coded_message += letters[mun]
    print(coded_message)
    return(coded_message)        
'''

alphabet = string.ascii_lowercase + " "
letters = dict(enumerate(alphabet))
def caesar(message, key):
    """
    This is a Caesar cipher.  Each letter in a message is shifted by a few
    characters in the alphabet, and returned.

    message: A string you would like to encode or decode.  Must consist of
             lowercase letters and spaces.
    key:     An integer, indicating how many characters each letter in the
             message will be shifted.
    """
    
    coded_message = {letter: (place + key) % 27 for (place, letter) in enumerate(alphabet)}
    coded_message_string = "".join([letters[coded_message[letter]] for letter in message])
    return coded_message_string
    
message = "hi my name is caesar"
key = -3
caesar(message,key)

coded_message = caesar(message, key=3)
print(coded_message)
    
#decoded_message = caesar(coded_message, key=-3)
#print(decoded_message)

def decaesar(message, key):
    lett = {v:k for k,v in letters.items()}
    decoded_message =  {(place + key) % 27: letter for (place, letter) in enumerate(alphabet)}
    dec = "".join([decoded_message[lett[letter]]for letter in coded_message])
    return dec
