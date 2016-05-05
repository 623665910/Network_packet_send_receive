#!/usr/bin/env python
#encoding:UTF-8
import struct
import random
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
from actors import dhcp_release

def discover_send(rawSocket, des_eth, src_eth, ip_src, ip_des, ip_request, xid, magic_cookie):
    data=dhcp_discover.discover(src_eth, ip_request, xid, magic_cookie)  

    eth_header=eth_layer.eth(des_eth, src_eth)
    ip_header=ip_layer.ip(ip_src, ip_des, data)
    udp_header=udp_layer.udp(ip_src, ip_des, data)
  
    packet=eth_header+ip_header+udp_header+data

    rawSocket.send(packet)

def request_send(rawSocket, des_eth, src_eth, ip_src, ip_des, ip_request, xid, magic_cookie):
    data=dhcp_request.request(src_eth, ip_request, xid, magic_cookie)  

    eth_header=eth_layer.eth(des_eth, src_eth)
    ip_header=ip_layer.ip(ip_src, ip_des, data)
    udp_header=udp_layer.udp(ip_src, ip_des, data)
  
    packet=eth_header+ip_header+udp_header+data

    rawSocket.send(packet)

def release_send(rawSocket, des_eth, src_eth, ip_src, ip_des, xid, magic_cookie):

    data=dhcp_release.release(src_eth, ip_src, ip_des, xid, magic_cookie)  
    eth_header=eth_layer.eth(des_eth, src_eth)
    ip_header=ip_layer.ip(ip_src, ip_des, data)
    udp_header=udp_layer.udp(ip_src, ip_des, data)
  
    packet=eth_header+ip_header+udp_header+data

    rawSocket.send(packet)

def ip_rand():
    temp=""
    for i in range(0, 4):
        temp=temp+chr(random.randint(0, 255)) 
    return temp 

def ip_format(input_ip):
    temp=""
    for i in input_ip.split('.'):
        temp=temp+struct.pack('B', int(i.strip()))
    return temp
def mac_format():
    temp=""
    for i in range(0, 6):
        temp=temp+chr(random.randint(0, 255)) 
    return temp 
def xid_format():
    temp=""
    for i in range(0, 4):
        temp=temp+chr(random.randint(0, 255)) 
    return temp 
