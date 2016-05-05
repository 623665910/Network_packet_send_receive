#!/usr/bin/env python
#encoding:UTF-8
import socket
import struct
import sys

sys.path.append("layers")

import eth_layer
import ip_layer
import udp_layer

gw='\x00\x1a\xa9\x17\x83\xe5'
zzy='\x44\x8a\x5b\xea\xb7\xf3'
master='\x44\x8a\x5b\xea\xb7\x25'
node1='\x40\xa8\xf0\x01\xb2\x52'
node2='\x44\x8a\x5b\xea\xb7\xea'
mq='\xfc\xaa\x14\x4a\x9c\x5f'

rawSocket=socket.socket(socket.PF_PACKET, socket.SOCK_RAW, socket.htons(0x0800))
rawSocket.bind(("eth0", socket.htons(0x0800)))



if __name__=="__main__":

    data="hello devil"    
    des_eth=master
    src_eth=node1
    ip_src="222.26.28.103"
    ip_des="222.26.28.72"
 
    eth_header=eth_layer.eth(des_eth, src_eth)
    ip_header=ip_layer.ip(ip_src, ip_des, data)
    udp_header=udp_layer.udp(ip_src, ip_des, data)
  
    packet=eth_header+ip_header+udp_header+data

    while 1:
        rawSocket.send(packet)
