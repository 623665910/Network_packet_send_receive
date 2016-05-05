#!/usr/bin/env python
#encoding:UTF-8
import struct
def release(client_mac, request_ip, server_ip, xid, magic_cookie):
    temp=""
    for i in request_ip.split('.'):
        temp=temp+struct.pack('B', int(i.strip()))
    request_ip=temp

    temp=""
    for i in server_ip.split('.'):
        temp=temp+struct.pack('B', int(i.strip()))
    server_ip=temp


    op='\x01'
    htype='\x01'
    hlen='\x06' 
    hops='\x00' 
    """
    xid='\xff\xff\xff\xff'
    """
    seconds='\x0b\x00'
    flags='\x00\x00'
    """
    request_ip
    """
    yiaddr='\x00'*4
    siaddr='\x00'*4
    giaddr='\x00'*4

    """
    client_mac='08 00 27 28 e0 a4'
    """
    client_hardware='\x00'*10
    server_hostname='\x00'*64
    boot_file='\x00'*128
    """
    magic_cookie="\xff\xff\xff\xff"
    """
    option1='\x35'+'\x01'+'\x07'
    option2='\x36'+'\x04'+server_ip
    option3='\x3d'+'\x07'+'\x01'+client_mac
    option_end='\xff'
    padding='\x00'*41
    return op+htype+hlen+hops+xid+seconds+flags+request_ip+yiaddr+siaddr+giaddr+client_mac+client_hardware+server_hostname+boot_file+magic_cookie+option1+option2+option3+option_end+padding
