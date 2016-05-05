该程序实现了使用原始套接字进行DHCP地址的DISCOVER发现，REQUEST请求

layers文件夹中分别为eth层， ip层， udp层的数据包封装， 以及checksum.py的数据包校验功能。
actors文件夹中分别为DISCOVER， REQUEST功能的实现，即DISCOVER数据包， REQUEST数据包的生成。


主程序为间隔1秒的DISCOVER包3次发送, 间隔1秒的OFFER包3次发送。
该程序默认认为DISCOVER包发送后一定受到OFFER包，并且REQUEST_IP为同一个， REQUEST包发送后也一定会受到ACK确定包。
