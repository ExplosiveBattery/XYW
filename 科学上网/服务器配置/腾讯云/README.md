在CentOS 7和Ubuntu 14.04安装SS

DZ排版可能比较糟糕，欢迎到我的博客观赏：http://url.cn/WrQRvB

这两天都在折腾服务器，各种奇葩情况出现也是醉了。等这几天一一把服务器的相关应用配置笔记发上来，供各位点评欣赏。

今天先给各位带来在CentOS 7和Ubuntu 14.04安装SS的相关记录吧。

这里需要说明的是，绝大部分的命令执行都需要root权限。

在CentOS 7下安装和使用SS

python-**ptools与pip命令安装：

yum install python-**ptools && easy_install pip

用pip方式安装SS：

pip install SS

在etc下建立SS文件夹，并写入配置文件：

mkdir -p /etc/shadowsocksvim /etc/shadowsocks/config.json

配置文件内容如下（相关参数可自己修改）：

单账户：


{
         "server":"your_server_ip",
         "server_port":8989,
         "local_address": "127.0.0.1",
         "local_port":1080,
         "password":"mypassword",
         "timeout":300,
         "method":"aes-256-cfb", 
         "fast_open": false,
         "workers": 1
}


说明：服务器IP（建议外网IP），服务端口（建议自定义），本地监听IP，本地监听端口，密码（建议自定义），超时时间，加密算法（可更改为rc4-md5），关闭fast-open，工作进程数量为1。

多账号（如需要）：


{
        "server":"your_server_ip",
        "local_address": "127.0.0.1",
        "local_port":1080,
        "port_password":{
                 "8977":"mypassword",
                 "8978":"mypassword",
                 "8979":"mypassword",
                 "8980":"mypassword",
                 "8981":"mypassword",
                 "8982":"mypassword",
                 "8983":"mypassword",
                 "8984":"mypassword",
                 "8985":"mypassword",
                 "8986":"mypassword",
                 "8989":"mypassword",
                 "8988":"mypassword"
        },
        "timeout":300,
        "method":"rc4-md5",
        "fast_open": false
}

说明：服务器IP，服务端口（建议自定义），本地监听IP，本地监听端口，密码（建议自定义），超时时间，加密算法（可更改为rc4-md5），关闭fast-open。

接下来我们设置SS能够随系统启动。在CentOS 7中，已经将系统服务的命令修改为systemctl，这里我们就用此命令进行相关配置：

建立shadowsocks-server.service文件：（建立后，在英文半角状态下输入i即可激活输入insert状态）

vim /etc/systemd/system/shadowsocks-server.service

文件内容：

[Unit]
Description=Shadowsocks Server
After=network.target

[Service]
Type=forking
PIDFile=/run/shadowsocks/server.pid
PermissionsStartOnly=true
ExecStartPre=/bin/mkdir -p /run/shadowsocks
ExecStartPre=/bin/chown root:root /run/shadowsocks
ExecStart=/usr/bin/ssserver --pid-file /var/run/shadowsocks/server.pid -c /etc/shadowsocks/config.json -d start
Restart=on-abort
User=root
Group=root
UMask=0027

[Install]
WantedBy=multi-user.target

之后按Esc退出insert模式，输入:wq保存并退出。

启动系统服务，并设置为激活状态（开机启动状态）：

systemctl start shadowsocks-server.servicesystemctl enable shadowsocks-server.service

设置防火墙（CentOS 7特性，如不设置，则无法连接上网）：

单用户：

firewall-cmd --permanent --add-port=8989/tcp
firewall-cmd --reload

多账号：

firewall-cmd --permanent --add-port=8977/tcp
firewall-cmd --permanent --add-port=8978/tcp
firewall-cmd --permanent --add-port=8979/tcp
firewall-cmd --permanent --add-port=8980/tcp
firewall-cmd --permanent --add-port=8981/tcp
firewall-cmd --permanent --add-port=8982/tcp
firewall-cmd --permanent --add-port=8983/tcp
firewall-cmd --permanent --add-port=8984/tcp
firewall-cmd --permanent --add-port=8985/tcp
firewall-cmd --permanent --add-port=8986/tcp
firewall-cmd --permanent --add-port=8989/tcp
firewall-cmd --permanent --add-port=8988/tcp
firewall-cmd --reload

然后就可以愉快的***了~

在Ubuntu 14.04下安装和使用SS

安装SS：
apt-get updateapt-get install python-gevent python-pippip install shadowsocksapt-get install python-m2crypto
配置SS： 1、创建config.json配置文件：
vim /etc/shadowsocks.json
2、修改config.json（同上）
配置文件内容如下（相关参数可自己修改）：
单账户：

{
         "server":"your_server_ip",
         "server_port":8989,
         "local_address": "127.0.0.1",
         "local_port":1080,
         "password":"mypassword",
         "timeout":300,
         "method":"aes-256-cfb", 
         "fast_open": false,
         "workers": 1
}

说明：服务器IP（建议外网IP），服务端口（建议自定义），本地监听IP，本地监听端口，密码（建议自定义），超时时间，加密算法（可更改为rc4-md5），关闭fast-open，工作进程数量为1。
多账号（如需要）：

{
        "server":"your_server_ip",
        "local_address": "127.0.0.1",
        "local_port":1080,
        "port_password":{
                 "8977":"mypassword",
                 "8978":"mypassword",
                 "8979":"mypassword",
                 "8980":"mypassword",
                 "8981":"mypassword",
                 "8982":"mypassword",
                 "8983":"mypassword",
                 "8984":"mypassword",
                 "8985":"mypassword",
                 "8986":"mypassword",
                 "8989":"mypassword",
                 "8988":"mypassword"
        },
        "timeout":300,
        "method":"rc4-md5",
        "fast_open": false
}

说明：服务器IP，服务端口（建议自定义），本地监听IP，本地监听端口，密码（建议自定义），超时时间，加密算法（可更改为rc4-md5），关闭fast-open。

运行SS（是不是觉得少了一步？并没有，Ubuntu14.04并不需要配置防火墙就能用哦~）：

ssserver -c /etc/shadowsocks.json -d startssserver -c /etc/shadowsocks.json -d stop

然后就可以愉快的***了~