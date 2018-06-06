#!/bin/sh

ifconfig tun0 10.0.0.2 pointopoint 10.0.0.1 mtu 1400 up
old_default=$(route | grep default | awk '{print $2}')
provider=$1
route add -host $provider gw $old_default
route delete default
route add default gw 10.0.0.1
#route命令执行会变得很久
#好消息是重新连接网络就会重置所有配置，方便我测验
