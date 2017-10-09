# -*- coding:utf-8 -*-
import os
import os.path
import shutil
import time


decdir="H:\\sql_backup" #需要删除文件的路径

def sql_delete(srcdirpath):
	for i in os.listdir(srcdirpath):
		filename=os.path.join(srcdirpath,i)
		if os.path.isdir(filename):
			sql_delete(filename)
		else:
			filedate = os.path.getmtime(filename)
			#print filedate
			num = (d1 - filedate)/60/60/24
			if num >15 :
				os.remove(filename)
				print "%s is...0k" % filename
			





if __name__ == '__main__':
	global d1
	d1 = time.time()
	sql_delete(decdir)
