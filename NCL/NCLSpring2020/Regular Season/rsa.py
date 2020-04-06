#!/bin/env python3

def main():

    p = int(input('Enter an p value: '))
    q = int(input('Enter an q value: '))
    e = int(input('Enter an e value: '))

    n = p * q
    d = 29
    phi = (p - 1) * (q - 1)
    k = 1 % phi


    c = [153, 75, 309, 310, 74, 203, 208, 401, 310, 371, 363, 451, 125]

    for i in range(len(c)):
        
        data = (c[i] ** d) % n 
        print (chr(data))

main()
