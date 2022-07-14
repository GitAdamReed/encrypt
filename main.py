# -*- coding: utf-8 -*-
"""
Created on Sun Apr 18 22:49:35 2021

@author: Adam
"""

from functions import init, genRandom, encrypt, decrypt

running = True
decision = 1

init()

while running:

    decision = input("0 = EXIT | 1 = ENCRYPT | 2 = DECRYPT: ")
    
    if decision == "0":   running = False
    elif decision == "1":
        textString = input("Enter phrase to encrypt: ")
        seed = genRandom(textString)
        phrase = encrypt(textString)
    elif decision == "2":
        textString = input("Enter phrase to decrypt: ")
        genRandom(textString, decision)
        decrypt(textString)
    else:
        print("Invalid input!")