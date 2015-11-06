# coding: utf-8

from scapy.all import *

# 先作三方握手
syn = IP(dst='www.google.com') / TCP(dport=80, flags='S', sport=16666)
syn_ack = sr1(syn)

getStr = 'GET / HTTP/1.1\r\nHost: www.google.com\r\n\r\n'
request = IP(dst='www.google.com') / TCP(dport=80, sport=syn_ack[TCP].dport,
             seq=syn_ack[TCP].ack, ack=syn_ack[TCP].seq + 1, flags='A') / getStr

request.show()  # print package information

reply = sr1(request)
print [reply]
