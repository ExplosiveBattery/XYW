��CentOS 7��Ubuntu 14.04��װSS

DZ�Ű���ܱȽ���⣬��ӭ���ҵĲ��͹��ͣ�http://url.cn/WrQRvB

�����춼�����ڷ����������������������Ҳ�����ˡ����⼸��һһ�ѷ����������Ӧ�����ñʼǷ�����������λ�������͡�

�����ȸ���λ������CentOS 7��Ubuntu 14.04��װSS����ؼ�¼�ɡ�

������Ҫ˵�����ǣ����󲿷ֵ�����ִ�ж���ҪrootȨ�ޡ�

��CentOS 7�°�װ��ʹ��SS

python-**ptools��pip���װ��

yum install python-**ptools && easy_install pip

��pip��ʽ��װSS��

pip install SS

��etc�½���SS�ļ��У���д�������ļ���

mkdir -p /etc/shadowsocksvim /etc/shadowsocks/config.json

�����ļ��������£���ز������Լ��޸ģ���

���˻���


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


˵����������IP����������IP��������˿ڣ������Զ��壩�����ؼ���IP�����ؼ����˿ڣ����루�����Զ��壩����ʱʱ�䣬�����㷨���ɸ���Ϊrc4-md5�����ر�fast-open��������������Ϊ1��

���˺ţ�����Ҫ����


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

˵����������IP������˿ڣ������Զ��壩�����ؼ���IP�����ؼ����˿ڣ����루�����Զ��壩����ʱʱ�䣬�����㷨���ɸ���Ϊrc4-md5�����ر�fast-open��

��������������SS�ܹ���ϵͳ��������CentOS 7�У��Ѿ���ϵͳ����������޸�Ϊsystemctl���������Ǿ��ô��������������ã�

����shadowsocks-server.service�ļ�������������Ӣ�İ��״̬������i���ɼ�������insert״̬��

vim /etc/systemd/system/shadowsocks-server.service

�ļ����ݣ�

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

֮��Esc�˳�insertģʽ������:wq���沢�˳���

����ϵͳ���񣬲�����Ϊ����״̬����������״̬����

systemctl start shadowsocks-server.servicesystemctl enable shadowsocks-server.service

���÷���ǽ��CentOS 7���ԣ��粻���ã����޷�������������

���û���

firewall-cmd --permanent --add-port=8989/tcp
firewall-cmd --reload

���˺ţ�

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

Ȼ��Ϳ�������***��~

��Ubuntu 14.04�°�װ��ʹ��SS

��װSS��
apt-get updateapt-get install python-gevent python-pippip install shadowsocksapt-get install python-m2crypto
����SS�� 1������config.json�����ļ���
vim /etc/shadowsocks.json
2���޸�config.json��ͬ�ϣ�
�����ļ��������£���ز������Լ��޸ģ���
���˻���

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

˵����������IP����������IP��������˿ڣ������Զ��壩�����ؼ���IP�����ؼ����˿ڣ����루�����Զ��壩����ʱʱ�䣬�����㷨���ɸ���Ϊrc4-md5�����ر�fast-open��������������Ϊ1��
���˺ţ�����Ҫ����

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

˵����������IP������˿ڣ������Զ��壩�����ؼ���IP�����ؼ����˿ڣ����루�����Զ��壩����ʱʱ�䣬�����㷨���ɸ���Ϊrc4-md5�����ر�fast-open��

����SS���ǲ��Ǿ�������һ������û�У�Ubuntu14.04������Ҫ���÷���ǽ������Ŷ~����

ssserver -c /etc/shadowsocks.json -d startssserver -c /etc/shadowsocks.json -d stop

Ȼ��Ϳ�������***��~