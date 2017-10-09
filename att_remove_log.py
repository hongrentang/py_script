#/usr/bin/pyhton
import os
import os.path
import shutil
import datetime

path='/app/game/server/launcher/logs'
now = datetime.datetime.now()
date = now.strftime('%Y-%m-%d')
d1 = datetime.datetime.strptime(date,'%Y-%m-%d')
#print d1
for i in os.listdir(path):
    	d2=datetime.datetime.strptime(i,'%Y-%m-%d')
       # print d2
        num=d1-d2
        n=num.days
	if n>7:
		filepath=os.path.join(path,i)
		#print filepath
		shutil.rmtree(filepath)
                print "%s,remove..is..ok" %filepath


