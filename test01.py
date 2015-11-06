from scapy.all import *

pack = IP(dst = '127.0.0.1') / TCP(dport = 1234) / Raw(b'GET / HTTP/1.1\r\n')

pack.show()  # print package information

send(pack)
