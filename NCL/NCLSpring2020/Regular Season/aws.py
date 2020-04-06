#!/bin/env python3

def main():

    infile = open('aws_vpc_flow.log', 'r')

    parse = [] 

    flows = 0
    packets = 0 
    totalBytes = 0

    for line in infile:
        
        line = line.strip()
        parse = line.split()

        flows += 1
        packets += int.from_bytes(parse[8], byteorder='big')
        totalBytes += int.from_bytes(parse[9], byteorder='big')

        #print(parse)
    flows = flows / 2 
    print ('Number of flows: ' + str(flows))
    print ('Number of packets: ' + str(packets))
    print ('Number of bytes: ' + str(totalBytes))

main()