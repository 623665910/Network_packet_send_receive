使用原始套接字， 该程序实现了模拟UDP协议的发包功能

在layers文件夹下面checksum.py实现了数据包的校验功能
eth_layer.py实现了数据链路层的数据包封装,目的MAC， 源MAC
ip_layer.py实现了IP层的数据包封装,源IP， 目的IP， 传输层UDP协议号
udp_layer.py实现了传输层的数据包封装,源端口号， 目的端口号

main.py里面写入需要发送的数据，实现数据包发送
