#!/bin/sh
ifconfig tun0 10.0.0.2 pointopoint 10.0.0.1 mtu 1400 up
old_default=$(route | grep default | awk '{print $2}')
provider=$1
route add -host $provider gw $old_default
route delete default
route add default gw 10.0.0.1
#好消息是重新连接网络就会重置所有配置，方便我测验
# $ route
# Kernel IP routing table
# Destination     Gateway         Genmask         Flags Metric Ref    Use Iface
# default         10.0.0.1        0.0.0.0         UG    0      0        0 tun0
# 10.0.0.1        0.0.0.0         255.255.255.255 UH    0      0        0 tun0
# 10.132.48.0     0.0.0.0         255.255.252.0   U     600    0        0 wlp2s0
# x.x.x.x   10.132.51.254   255.255.255.255 UGH   0      0        0 wlp2s0

