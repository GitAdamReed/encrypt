# -*- coding: utf-8 -*-
"""
Created on Tue Apr 20 03:42:03 2021

@author: Adam
"""

import random
import secrets

array = []

def init():
    print("**DEVELOPED BY ADAM REED**")
    print("Please choose an option")

def genRandom(string, decision="1"):
    
    seed = ""
    if decision == "1":
                
        seed = secrets.token_hex(nbytes=16)
        print("Seed: " + seed)
                
    else:
                
        seed = input("Please enter seed: ")
    
    random.seed(seed)
    array.clear()
    for x in string:
        
        num = random.randint(1, 47)
        array.append(num)
    
    return seed

# 33 in ascii table is the start of valid chars for this
# 126 is the end for valid chars

def encrypt(string):
    
    nString = ""
    x = 0
    for char in string:
        nAsc = ord(char) + array[x]
        if nAsc > 126:
            nAsc -= 93
        nChar = chr(nAsc)
        
        x += 1
        
        nString += nChar
    print("Encrypted phrase: " + nString)
    print("**TAKE NOTE OF SEED AND ENCRYPTED PHRASE**")
    return nString

def decrypt(string):
    
    nString = ""
    x = 0
    for char in string:
        nAsc = ord(char) - array[x]
        if nAsc < 33:
            nAsc += 93
        nChar = chr(nAsc)
        
        x += 1
        
        nString += nChar
    print("Decrypted phrase: " + nString)
    return nString
    
    
    