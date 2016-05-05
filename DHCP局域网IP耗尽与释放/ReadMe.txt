本程序主要实现了局域网中IP地址的耗尽与释放。


本程序有三个执行文件， 分别为:

hacker_dhcp:
该执行文件实现了不断在局域网中发送DISCOVER包， 接受OFFER包， 然后再发送REQUEST包， 最后接收确认包ACK。在这个过程中写有定时器， 如果超时产生中断， 重新进入下次循环。 重新生成源MAC地址， 事务号XID， 以及REQUEST_IP。并且将每次成功申请到的IP， 源MAC， 事务号XID 保存到 host_ip.dat 文件中。

hacker_keeper:
该执行文件只实现了REQUEST包发送， ACK包的接受。该执行程序每次从 host_ip.dat 文件中取出已经成功获取的源MAC， IP， 以及事务号XID， 发送REQUEST包。目的为了实现对IP地址的续约， 使DHCP服务器一直保持该IP地址的分配。

release_dhcp:
该执行文件实现了RELEASE数据包发送的功能， 服务器接受到该包后， 检查源MAC地址是否已经分配给IP， 若是已经分配则取消该IP分配， 在三层交换机上断掉该源MAC地址的联网， 即不再为该源MAC地址的数据包转发给网关。

该程序采用原始套接字技术编程， 在程序是在数据链路层上进行的数据包发送及监听功能, 该套接字在二层上绑定公共端口, 即0号端口， 实现了接收所有的二层数据包，形式为socket.htons(0x0000)。

在layers文件夹下面checksum.py实现了数据包的校验功能
eth_layer.py实现了数据链路层的数据包封装,目的MAC， 源MAC
ip_layer.py实现了IP层的数据包封装,源IP， 目的IP， 传输层UDP协议号
udp_layer.py实现了传输层的数据包封装,源端口号， 目的端口号

在actors文件夹下面:
dhcp_discover.py:
实现了DISCOVER数据包的封装
dhcp_request.py:
实现了REQUEST数据包的封装
dhcp_release.py:
实现了RELEASE数据包的封装
