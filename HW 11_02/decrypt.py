#
# File: decrypt.py
# Author: Vlad Burca
#
# Created:  10/30/10
# Modified: 10/30/10
#

def decrypt(s):
    t = ''
    l = len(s)
    for i in range(l):
        if s[i].isalpha():
            t = t + chr((ord(s[i]) - 65 - 3) % 26 + 65 + 32)
        else:
            t = t + s[i]
    return t        

ciphertext = raw_input(' Enter a ciphertext message: ')
plaintext = decrypt(ciphertext)
print ' Your message is decrypted as: ', plaintext