# DNS隧道绕过认证

### 使用前提

在未认证的情况下，允许使用第三方DNS服务器（直连或中继），这一点需要抓包分析  

### 漏洞介绍

允许使用第三方DNS服务器，就意味着可以通过DNS Tunnel实现认证绕过。不过实际上川大2018-06-05是没有对udp 53端口进行过滤，允许直接外网访问，这样就没有必要使用DNS Tunnel，直接端口通信，保证了传输速度！  
这个漏洞在不少学校早就在用并已经被他们学校官方通过DNS白名单机制修复 [川大曾经有人在贴吧爆过料](http://tieba.baidu.com/p/4800997443)

### 推荐实现
http://www.freebuf.com/sectool/112076.html 中的iodine部分  
https://github.com/yarrick/iodine  
可以结合https://blog.csdn.net/dongfei2033/article/details/76222742 ，免认证与认证一起使用，实现一定的提速  
示例：https://www.cnblogs.com/bonelee/p/8059464.html  

### 相关补充
如果使用了DNS Tunnel，网速会比正常的认证上网慢上一些，关键一般取决于服务器的网速、隧道实现的原理  
相关工具：iodine（推荐，多种平台包括手机，官方称上行速度最大680 kbit/s，下行速度上限可以达到2.3Mbit/s），dnscat2，DeNise，dns2tcp，Heyoka等  
