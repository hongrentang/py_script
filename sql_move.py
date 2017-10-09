import os
import os.path
import shutil
import time

srcdir="Z:\\"
decdir="H:\\sql_backup"

def sql_move(srcdirpath,decdirpath):
	for i in os.listdir(srcdirpath):
		filename=os.path.join(srcdirpath,i)
		filedate = os.path.getmtime(filename)
		#print filedate
		num = (d1 - filedate)/60/60/24
		if num >7 :
			shutil.move(filename,decdirpath)
			print "%s is...0k" % filename
			



def sql_dir(srcdir,decdir):
	for i in os.listdir(srcdir):
		srcdirpath=os.path.join(srcdir,i)
		decdirpath=os.path.join(decdir,i)
		if  not os.path.exists(decdirpath):
			os.makedirs(decdirpath)

		sql_move(srcdirpath,decdirpath)




if __name__ == '__main__':
	global d1
	d1 = time.time()
	sql_dir(srcdir,decdir)
