#!/usr/bin/env python
#encoding:UTF-8
import struct
import random
import checksum
def ip(ip_src, ip_des, data):
    temp=""
    for i in ip_src.split('.'):
        temp=temp+struct.pack('B', int(i.strip()))
    ip_src=temp
    temp=""
    for i in ip_des.split('.'):
        temp=temp+struct.pack('B', int(i.strip()))
    ip_des=temp

    version_headlength="\x45"
    server_type="\x00"

    ip_length=20+8+len(data)
    ip_length=struct.pack("!H", ip_length)

    """
    IP总长度576 \x02\x40 字节 头20字节  载荷556字节
    """

    ip_id=struct.pack("!H", random.randint(0, 65535))

    "ip是否可分片  片偏移量"
    ip_fff="\x00\x00"

    ip_ttl="\x80"
    ip_pro="\x11"
 
    src_des=ip_src+ip_des

    temp=version_headlength+server_type+ip_length+ip_id+ip_fff+ip_ttl+ip_pro+"\x00\x00"+src_des

    return temp[:10]+checksum.check(temp)+src_des

