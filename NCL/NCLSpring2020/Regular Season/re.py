#!/bin/env python

import sys
 

def main():

    submission = [ 0x53, 75, 0x59, 0x2D, 0110, 0x45, 88, 83, 0x2D, 0x31, 0x32, 0x35, 0x36 ]
    processed = []

    for i in range(0, len(submission) / 2):
        processed.append((int(submission[i * 2] + submission[(i * 2) + 1]), 16))
       
    for j in range(len(submission)):
        print str(processed[i])
    
    

main()
 
