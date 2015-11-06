# coding: utf-8

from scapy.all import *

HTTP_REQUEST=[
    "GET / HTTP/1.1\r\n"
    # "Host: 127.0.0.1:8080\r\n"
    # "Connection: keep-alive\r\n"
    # "Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8\r\n"
    # "Upgrade-Insecure-Requests: 1\r\n"
    # "User-Agent: Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/46.0.2490.80 Safari/537.36\r\n"
    # "Accept-Encoding: gzip, deflate, sdch\r\n"
    # "Accept-Language: zh-TW,zh;q=0.8,en-US;q=0.6,en;q=0.4,zh-CN;q=0.2\r\n"
    # "Cookie: JSESSIONID.70f0a254=d1v995r94f62xu3u5wsxmvhl; screenResolution=1920x1080; JSESSIONID=CD914A45C6638F21D2459C2031155F76; loggedin=200; _ga=GA1.4.1340553511.1441363662; sessionid=8341E7C134ED1DBD5CBF953CB48B7DC8\r\n"
    # "Origin: http://evil.com/\r\n"
    "\r\n"
][0]

print HTTP_REQUEST

pack = IP(dst = '127.0.0.1') / TCP(dport = 8080, sport=16666) / Raw(HTTP_REQUEST)

pack.show()  # print package information

send(pack)

