#!/usr/bin/env python
#encoding:UTF-8
import struct
def check(input):

    temp=0

    for i in range(0, len(input)-1, 2):
	temp=temp+( (ord(input[i])<<8)+(ord(input[i+1])) )


    while(temp>65535): 
	temp=(temp>>16)+int(bin(temp)[-16:], 2)

    return struct.pack("!H", 2**16-1-temp)
        
    

