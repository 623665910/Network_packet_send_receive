#!/usr/bin/env python
#encoding:UTF-8
import struct
def request(client_mac, request_ip, xid, magic_cookie):
    """
    temp=""
    for i in request_ip.split('.'):
        temp=temp+struct.pack('B', int(i.strip()))
    request_ip=temp
    """

    op='\x01'
    htype='\x01'
    hlen='\x06' 
    hops='\x00' 
    """
    xid='\xff\xff\xff\xff'
    """
    seconds='\x00\x00'
    flags='\x00\x00'
    ciaddr='\x00'*4
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
    option1='\x35'+'\x01'+'\x03'
    #option2='\x36'+'\x04'+'\xca\x76\x30\xfc'
    option3='\x3d'+'\x07'+'\x01'+client_mac
    request_ip='\x32\x04'+request_ip
    dhcp_server_id='\x36\x04\xca\x76\x30\xfc'
    host_name='\x00'*10
    client_domain='\x51\x0b\x00\x00\x00'+host_name
    vendor_class='\x3c\x08\x4d\x53\x46\x54\x20\x35\x2e\x30'
    parameter_request='\x37\x0c\x01\x0f\x03\x06\x2c\x2e\x2f\x1f\x21\x79\xf9\x2b'
    option4='\xff'

    return op+htype+hlen+hops+xid+seconds+flags+ciaddr+yiaddr+siaddr+giaddr+client_mac+client_hardware+server_hostname+boot_file+magic_cookie+option1+option3+request_ip+dhcp_server_id+host_name+client_domain+vendor_class+parameter_request+option4
