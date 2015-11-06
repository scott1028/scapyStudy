# Installation

~~~
$ sudo apt-get install python-scapy python-pyx python-gnuplot
    or
$ pip install scapy     ← For Develop
    … 
$ sudo apt-get install texlive      ← 似乎是一個圖形化 Library 不懂為啥要裝這個！但是沒裝就是不能 run！
~~~

# Demo

![Alt text](https://raw.githubusercontent.com/scott1028/scapyStudy/master/test01.gif "Demo")

~~~
from scapy.all import *

pack = IP(dst = '127.0.0.1') / TCP(dport = 1234) / Raw(b'GET / HTTP/1.1\r\n')
send(pack)

~~~
