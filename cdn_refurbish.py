# -*- coding:utf-8 -*-

from aliyunsdkcore import client
from aliyunsdkcdn.request.v20141111 import RefreshObjectCachesRequest

def refurbish(androidpath,iospath):
	clt = client.AcsClient('','','cn-hangzhou')
	# 设置参数
	request = RefreshObjectCachesRequest.RefreshObjectCachesRequest()
	request.set_accept_format('json')

	request.add_query_param('ObjectType', 'Directory')
	request.add_query_param('ObjectPath', androidpath+'\n'+iospath)
	# 发起请求
	response = clt.do_action(request)
	print u'%s--------刷新成功' %androidpath
	print u'%s--------刷新成功' %iospath

if __name__ == '__main__':
	xz="请选择刷新CDN类别：经典斗地主:(输入1) | 四川斗地主(输入2) | 炸金花(输入3) | 麻将(输入4) |ATT(输入5) | 平台更新(输入0)  |退出(输入q)\n"
	st=xz.decode('utf-8')	
	flag = True
	while (flag):
		print(st)
		answer = raw_input("Input: ")
		if  'q' == answer.lower():
			flag = False
		elif '0' == answer :
			android_yyplatform='url'
			ios_yyplatform=''
			refurbish(android_yyplatform,ios_yyplatform)

		elif '1' == answer :
			android_1001=''
			ios_1001=''
			refurbish(android_1001,ios_1001)			

		elif '2' == answer :
			android_1002=''
			ios_1002=''
			refurbish(android_1002,ios_1002)
		elif '3' == answer :
			android_1003=''
			ios_1003=''
			refurbish(android_1003,ios_1003)
		elif '4' == answer :
			android_1004=''
			ios_1004=''
			refurbish(android_1004,ios_1004)
		elif '5' == answer :
			android_1005=''
			ios_1005=''
			refurbish(android_1005,ios_1005)

					
					
					
					