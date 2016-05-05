#!/usr/bin/env python
#encoding:UTF-8
import socket
import struct
import time
import sys
"""
sys.path.append("layers")
sys.path.append("actors")
"""

from layers import eth_layer
from layers import ip_layer
from layers import udp_layer
from actors import dhcp_discover
from actors import dhcp_request

ip_server='202.118.48.252'

broad="\xff\xff\xff\xff\xff\xff"
gw='\x00\x1a\xa9\x17\x83\xe5'
zzy='\x44\x8a\x5b\xea\xb7\xf3'
master='\x44\x8a\x5b\xea\xb7\x25'
node1='\x40\xa8\xf0\x01\xb2\x52'
node2='\x44\x8a\x5b\xea\xb7\xea'
mq='\xfc\xaa\x14\x4a\x9c\x5f'
test='\x08\x00\x27\x28\xe0\xa4'

rawSocket=socket.socket(socket.PF_PACKET, socket.SOCK_RAW, socket.htons(0x0800))
rawSocket.bind(("eth0", socket.htons(0x0800)))

def discover_send():
    data=dhcp_discover.discover(src_eth, ip_request, xid, magic_cookie)  

    eth_header=eth_layer.eth(des_eth, src_eth)
    ip_header=ip_layer.ip(ip_src, ip_des, data)
    udp_header=udp_layer.udp(ip_src, ip_des, data)
  
    packet=eth_header+ip_header+udp_header+data

    rawSocket.send(packet)

def request_send():
    data=dhcp_request.request(src_eth, ip_request, xid, magic_cookie)  

    eth_header=eth_layer.eth(des_eth, src_eth)
    ip_header=ip_layer.ip(ip_src, ip_des, data)
    udp_header=udp_layer.udp(ip_src, ip_des, data)
  
    packet=eth_header+ip_header+udp_header+data

    rawSocket.send(packet)

 
if __name__=="__main__":

    des_eth=broad
    src_eth=master
    ip_src="0.0.0.0"
    ip_des="255.255.255.255"
    ip_request="222.26.28.250"
        
    """xid  magic_cookie  需要自动生成"""
    xid='\xb2\xc5\xc3\x96'
    magic_cookie='\x63\x82\x53\x63'

    """
    discover与request同步 以magic_cookie为判断 
    """

    discover_send()
    time.sleep(1)
    discover_send()
    time.sleep(1)
    discover_send()
    time.sleep(1)
    
    
    request_send()
    time.sleep(1)
    request_send()
    time.sleep(1)
    request_send()

