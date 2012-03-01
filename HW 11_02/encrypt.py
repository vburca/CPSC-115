#
# File: encrypt.py
# Author: Vlad Burca
#
# Created:  10/30/10
# Modified: 10/30/10
#

def encrypt(s):
    t = ''
    l = len(s)
    for i in range(l):
        if s[i].isalpha():
            t = t + chr((ord(s[i]) - 97 + 3) % 26 + 97 - 32)
        else:
            t = t + s[i]
    return t        

plaintext = raw_input(' Enter a plaintext message: ')
ciphertext = encrypt(plaintext)
print ' Your message is encrypted as: ', ciphertext