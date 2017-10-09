# -*- coding:utf-8 -*-

import mysql.connector
import time
import smtplib
from smtplib import SMTP_SSL
from email.mime.text import MIMEText
from email.header import Header

config = {
  'user': 'zabbix',
  'password': 'MhXdJU34GMKILPZcL082',
  'host': '127.0.0.1',
  'database': 'zabbix',
  'raise_on_warnings': True,
}

#查看进程
def query_proc_num(itemidd,cursor):
	
	query = ("SELECT * from history_uint WHERE itemid="+itemidd+ " ORDER BY clock DESC LIMIT 1")
	cursor.execute(query)
	result = cursor.fetchone()
	#print result

	return result
#查看cpu和内存
def query_cpu_mem(itemidd,cursor):


	query = ("SELECT * from history WHERE itemid="+itemidd+ " ORDER BY clock DESC LIMIT 1")
	cursor.execute(query)
	result = cursor.fetchone()
	#print result

	return result

	
	#result result
    
   



if __name__ == '__main__':
   
	cnx = mysql.connector.connect(**config)
	cursor = cnx.cursor()
	#获取游戏服务器cpu和内存值
	yx_cpu=query_cpu_mem("23824",cursor)
	x=time.localtime(yx_cpu[1])
	yx_cpu_time=time.strftime('%Y-%m-%d %H:%M:%S',x)
	yx_cpu_value=float(yx_cpu[2])
	# print yx_cpu_time
	# print yx_cpu_value

	yx_mem=query_cpu_mem("24078",cursor)
	x=time.localtime(yx_mem[1])
	yx_mem_time=time.strftime('%Y-%m-%d %H:%M:%S',x)
	yx_mem_value=float(yx_mem[2])
	# print yx_mem_time
	# print yx_mem_value
	# #获取web服务器cpu和内存值
	web_cpu=query_cpu_mem("23823",cursor)
	x=time.localtime(web_cpu[1])
	web_cpu_time=time.strftime('%Y-%m-%d %H:%M:%S',x)	
	web_cpu_value=float(web_cpu[2])
	# print web_cpu_time
	# print web_cpu_value

	web_mem=query_cpu_mem("24204",cursor)
	x=time.localtime(web_mem[1])
	web_mem_time=time.strftime('%Y-%m-%d %H:%M:%S',x)
	web_mem_value=float(web_mem[2])
	# print web_mem_time
	# print web_mem_value
	# #获取日志服务器cpu和内存值
	rz_cpu=query_cpu_mem("23708",cursor)
	x=time.localtime(rz_cpu[1])
	rz_cpu_time=time.strftime('%Y-%m-%d %H:%M:%S',x)
	rz_cpu_value=float(rz_cpu[2])
	# print rz_cpu_time
	# print rz_cpu_value

	rz_mem=query_cpu_mem("24203",cursor)
	x=time.localtime(rz_mem[1])
	rz_mem_time=time.strftime('%Y-%m-%d %H:%M:%S',x)
	rz_mem_value=float(rz_mem[2])
	# print rz_mem_time
	# print rz_mem_value


	# print "---------gm----------"
	gm_porc_num=query_proc_num("24106",cursor)
	x=time.localtime(gm_porc_num[1])
	gm_porc_time=time.strftime('%Y-%m-%d %H:%M:%S',x)
	gm_porc_value=gm_porc_num[2]

	# print gm_porc_time
	# print gm_porc_value

	# print "--------mongod-----------"

	mongod_porc_num=query_proc_num("24109",cursor)
	x=time.localtime(mongod_porc_num[1])
	mongod_porc_time=time.strftime('%Y-%m-%d %H:%M:%S',x)
	mongod_porc_value=mongod_porc_num[2]

	# print mongod_porc_time
	# print mongod_porc_value
	
	# print "----------redis---------"
	redis_porc_num=query_proc_num("24113",cursor)
	x=time.localtime(redis_porc_num[1])
	redis_porc_time=time.strftime('%Y-%m-%d %H:%M:%S',x)
	redis_porc_value=redis_porc_num[2]

	# print redis_porc_time
	# print redis_porc_value

	# print "--------sqlserver-----------"
	sqlserver_porc_num=query_proc_num("24114",cursor)
	x=time.localtime(sqlserver_porc_num[1])
	sqlserver_porc_time=time.strftime('%Y-%m-%d %H:%M:%S',x)
	sqlserver_porc_value=sqlserver_porc_num[2]

	# print sqlserver_porc_time
	# print sqlserver_porc_value

	# print "---------gg----------"
	gg_porc_num=query_proc_num("24104",cursor)
	x=time.localtime(gg_porc_num[1])
	gg_porc_time=time.strftime('%Y-%m-%d %H:%M:%S',x)
	gg_porc_value=gg_porc_num[2]

	# print gg_porc_time
	# print gg_porc_value
	# print "---------xt----------"
	xt_porc_num=query_proc_num("24104",cursor)
	x=time.localtime(xt_porc_num[1])
	xt_porc_time=time.strftime('%Y-%m-%d %H:%M:%S',x)
	xt_porc_value=xt_porc_num[2]

	# print xt_porc_time
	# print xt_porc_value
	# print "---------dt----------"
	dt_porc_num=query_proc_num("24110",cursor)
	x=time.localtime(dt_porc_num[1])
	dt_porc_time=time.strftime('%Y-%m-%d %H:%M:%S',x)
	dt_porc_value=dt_porc_num[2]

	# print dt_porc_time
	# print dt_porc_value

	# print "--------ts----------"
	ts_porc_num=query_proc_num("24112",cursor)
	x=time.localtime(ts_porc_num[1])
	ts_porc_time=time.strftime('%Y-%m-%d %H:%M:%S',x)
	ts_porc_value=ts_porc_num[2]

	# print ts_porc_time
	# print ts_porc_value

	# print "--------ptdb----------"
	ptdb_porc_num=query_proc_num("24105",cursor)
	x=time.localtime(ptdb_porc_num[1])
	ptdb_porc_time=time.strftime('%Y-%m-%d %H:%M:%S',x)
	ptdb_porc_value=ptdb_porc_num[2]

	# print ptdb_porc_time
	# print ptdb_porc_value
	# print "---------dl----------"
	dl_porc_num=query_proc_num("24108",cursor)
	x=time.localtime(dl_porc_num[1])
	dl_porc_time=time.strftime('%Y-%m-%d %H:%M:%S',x)
	dl_porc_value=dl_porc_num[2]

	# print dl_porc_time
	# print dl_porc_value

	# print "---------wg----------"
	wg_porc_num=query_proc_num("24107",cursor)
	x=time.localtime(wg_porc_num[1])
	wg_porc_time=time.strftime('%Y-%m-%d %H:%M:%S',x)
	wg_porc_value=wg_porc_num[2]

	# print wg_porc_time
	# print wg_porc_value

	# print "---------lt----------"
	lt_porc_num=query_proc_num("24103",cursor)
	x=time.localtime(lt_porc_num[1])
	lt_porc_time=time.strftime('%Y-%m-%d %H:%M:%S',x)
	lt_porc_value=lt_porc_num[2]

	# print lt_porc_time
	# print lt_porc_value

	# print "---------yxdb----------"
	yxdb_porc_num=query_proc_num("24179",cursor)
	x=time.localtime(yxdb_porc_num[1])
	yxdb_porc_time=time.strftime('%Y-%m-%d %H:%M:%S',x)
	yxdb_porc_value=yxdb_porc_num[2]

	# print yxdb_porc_time
	# print yxdb_porc_value

	# print "-------yxpt------------"
	yxpt_porc_num=query_proc_num("24177",cursor)
	x=time.localtime(yxpt_porc_num[1])
	yxpt_porc_time=time.strftime('%Y-%m-%d %H:%M:%S',x)
	yxpt_porc_value=yxpt_porc_num[2]

	# print yxpt_porc_time
	# print yxpt_porc_value

	# print "---------yxlx---------"
	yxlx_porc_num=query_proc_num("24185",cursor)
	x=time.localtime(yxlx_porc_num[1])
	yxlx_porc_time=time.strftime('%Y-%m-%d %H:%M:%S',x)
	yxlx_porc_value=yxlx_porc_num[2]

	# print yxlx_porc_time
	# print yxlx_porc_value
	# print "---------yx----------"
	yx_porc_num=query_proc_num("24187",cursor)
	x=time.localtime(yx_porc_num[1])
	yx_porc_time=time.strftime('%Y-%m-%d %H:%M:%S',x)
	yx_porc_value=yx_porc_num[2]

	# print yx_porc_time
	# print yx_porc_value
	# print "---------yxzd----------"
	yxzd_porc_num=query_proc_num("24181",cursor)
	x=time.localtime(yxzd_porc_num[1])
	yxzd_porc_time=time.strftime('%Y-%m-%d %H:%M:%S',x)
	yxzd_porc_value=yxzd_porc_num[2]
	# print yxzd_porc_time
	# print yxzd_porc_value
	# print "----------yxzdgl---------"
	yxzdgl_porc_num=query_proc_num("24183",cursor)
	x=time.localtime(yxzdgl_porc_num[1])
	yxzdgl_porc_time=time.strftime('%Y-%m-%d %H:%M:%S',x)
	yxzdgl_porc_value=yxzdgl_porc_num[2]

	# print yxzdgl_porc_time
	# print yxzdgl_porc_value
		
	##邮件发送



	text='''server                      vale          time
游戏服务器cpu    %.2f%%     %s
游戏服务器内存   %.2f%%   %s
web服务器cpu     %.2f%%     %s
web服务器内存    %.2f%%  %s
日志服务器cpu    %.2f%%     %s
日志服务器内存   %.2f%%   %s
----------------------------------------------------------
mongod服务进程       %s    %s
redis服务进程           %s    %s
sqlserver服务进程    %s    %s
----------------------------------------------------------
协调服务进程     %s    %s
平台DB服务进程   %s    %s
公共服务进程     %s    %s
推送服务进程     %s     %s
gm管理进程       %s    %s
大厅服务进程     %s    %s
网关服务进程     %s    %s
聊天服务进程     %s    %s
登录服务进程     %s    %s
----------------------------------------------------------
游戏平台服务进程      %s    %s
游戏DB服务进程        %s    %s
游戏录像服务进程       %s    %s
游戏组队管理服务进程  %s  %s
游戏组队服务进程       %s    %s
游戏服务进程           %s    %s

''' % (yx_cpu_value,yx_cpu_time,yx_mem_value,yx_mem_time,web_cpu_value,web_cpu_time,web_mem_value,web_mem_time,rz_cpu_value,rz_cpu_time,rz_mem_value,rz_mem_time,mongod_porc_value,mongod_porc_time,redis_porc_value,redis_porc_time,sqlserver_porc_value,sqlserver_porc_time,xt_porc_value,xt_porc_time,ptdb_porc_value,ptdb_porc_time,gg_porc_value,gg_porc_time,ts_porc_value,ts_porc_time,gm_porc_value,gm_porc_time,dt_porc_value,dt_porc_time,wg_porc_value,wg_porc_time,lt_porc_value,lt_porc_time,dl_porc_value,dl_porc_time,yxpt_porc_value,yxpt_porc_time,yxdb_porc_value,yxdb_porc_time,yxlx_porc_value,yxlx_porc_time,yxzdgl_porc_value,yxzdgl_porc_time,yxzd_porc_value,yxzd_porc_time,yx_porc_value,yx_porc_time)
	texts=text.decode('utf-8')
  	#print texts
	mail_host="smtp.qq.com"
	mail_user="2456322917@qq.com"
	mail_pass="fkfovmarcxfndhhf"
	sender='2456322917@qq.com'
	receivers=['370603297@qq.com','357380578@qq.com']
	message=MIMEText(texts, 'plain', 'utf-8')
	#message['From'] = Header("2456322917@qq.com", 'utf-8')
	#message['To'] =  Header("370603297@qq.com",'utf-8')
	subject='server邮件报告'
	message['Subject']=Header(subject,'utf-8')
	try:
		smtpObj = SMTP_SSL(mail_host)
		smtpObj.ehlo(mail_host)	
		smtpObj.login(mail_user,mail_pass)
		smtpObj.sendmail(sender, receivers, message.as_string())
		print "scsess"
	except smtplib.SMTPException:
		print "eroor"



