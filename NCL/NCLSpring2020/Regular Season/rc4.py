#!/bin/env python

import base64

rc4 = ''


S = range(256)
j = 0
out = []

infile = open('rc4Pass.txt', 'r')
passwds = []

for line in infile:

    tmp = line.split()
    passwds.append(tmp)

#KSA Phase

for i in range(len (passwds)):
    key = passwds[i]
    for k in range(256):
        j = (j + S[i] + ord( key[k % len(key)] )) % 256
        S[i] , S[j] = S[j] , S[i]

#PRGA Phase
i = j = 0
for char in data:
    i = ( i + 1 ) % 256
    j = ( j + S[i] ) % 256
    S[i] , S[j] = S[j] , S[i]
    out.append(chr(ord(char) ^ S[(S[i] + S[j]) % 256]))

print ''.join(out)