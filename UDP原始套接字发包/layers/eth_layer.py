#!/usr/bin/env python
#encoding:UTF-8
import struct
def eth(des_eth, src_eth):
    packet=struct.pack("6s6s2s", des_eth, src_eth, '\x08\x00')
    return packet

