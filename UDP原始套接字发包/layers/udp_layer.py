#!/usr/bin/env python
#encoding:UTF-8 
import struct
import checksum

def udp(ip_src, ip_des, data):

    udp_length=struct.pack("!H", len(data)+8)

    temp=""
    for i in ip_src.split('.'):
        temp=temp+struct.pack('B', int(i.strip()))
    ip_src=temp
    temp=""
    for i in ip_des.split('.'):
        temp=temp+struct.pack('B', int(i.strip()))
    ip_des=temp

    src_port=34572
    des_port=10000

    src_port=struct.pack("!H", src_port)
    des_port=struct.pack("!H", des_port)

    src_des=ip_src+ip_des

    if  (len(data)%4):
        temp=src_des+"\x00"+"\x11"+udp_length+src_port+des_port+udp_length+"\x00\x00"+data+"\x00"*(4-len(data)%4)
    else:
        temp=src_des+"\x00"+"\x11"+udp_length+src_port+des_port+udp_length+"\x00\x00"+data


    return src_port+des_port+udp_length+checksum.check(temp)
