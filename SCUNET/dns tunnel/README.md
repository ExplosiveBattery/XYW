# DNS隧道绕过认证

### 使用前提

在未认证的情况下，允许使用第三方DNS服务器（直连或中继），这一点需要抓包分析  

### 漏洞介绍

允许使用第三方DNS服务器，就意味着可以通过DNS Tunnel实现认证绕过。不过实际上川大2018-06-05是没有对udp 53端口进行过滤，允许直接外网访问，这样就没有必要使用DNS Tunnel，直接端口通信，保证了传输速度！  
这个漏洞在不少学校早就在用并已经被他们学校官方通过DNS白名单机制修复 [川大曾经有人在贴吧爆过料，但是研究不完全](http://tieba.baidu.com/p/4800997443)

### 常见实现

http://www.freebuf.com/sectool/112076.html 中的iodine部分  
https://github.com/yarrick/iodine  
示例：https://www.cnblogs.com/bonelee/p/8059464.html  

### 相关补充

如果使用了DNS Tunnel，网速会比正常的认证上网慢上一些
相关工具：iodine（推荐，多种平台包括手机，官方称上行速度最大680 kbit/s，下行速度上限可以达到2.3Mbit/s），dnscat2，DeNise，dns2tcp，Heyoka等  

### 推荐实现（理论可行，本人未验证）

学校的这个漏洞最好不应该是走DNS隧道，而应该直接UDP通信，由于是未认证上网所以绝对不会被SCUNET限速（江安校区执行的应该是负载均衡策略，所以速度还是有限），我认为能够达到的网速上限就是设备、远程服务器可以支持的网速上限。现成可以使用的协议有QUIC、KCP，两种基于UDP的可靠传输，当然既然是udp通信，你可以直接多倍暴力发包，从而做到“大致”可靠通信来换取最快的网速。可以使用 https://github.com/astroza/udptunnel  但是这个仓库中linux_client.sh存在一定的命令问题，建议用我已经修改过的
udptunnel设计思路很巧妙，创建了一个tun虚拟网卡，结合路由表实现对协议栈的拦截read与正常write，拦截正常的网络封包，重新封装成作者自定义的一种简单格式，用于在隧道中传输。如果要实现一个服务器使用多个客户端，那么应该对script中使用到的对应脚本中ifconfig命令进行修改,不同客户端的client.sh中ip不同，比如10.0.0.2,10.0.0.3,10.0.0.4；server.sh中更改ifconfig命令为`ifconfig tun0 10.0.0.1/24`,并且还要将server.c中的socket部分修改为支持多个客户端连接（一个socket监听连接信息，以线程的方式创建其他socket用于已建立的连接）


emm，还有一个想法，就是将未认证的网速与认证后账号网速叠加，来在实际中提升网速，这个提速方法在江安校区可行 https://blog.csdn.net/dongfei2033/article/details/76222742