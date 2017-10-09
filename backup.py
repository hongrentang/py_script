# -*- coding:utf-8 -*-
import os
import time
import zipfile
source_dir='E:\\2017-7-27\\unicode' #需要备份的目录
dec_dir = 'E:\\2017-7-27\\backup' #备份到的目录
target = dec_dir + '\\GroupGameServer_'+time.strftime('%Y-%m-%d_%H%M%S') + '.zip' #备份后的文件名

#zip_command = "zip -qr '%s' %s" % (target, ' '.join(source))
def dirlist(qpath,z):
	#print qpath
    filelist = os.listdir(qpath) 
  
    for filename in filelist: 
    	if filename=='log':
    		continue
        filepath = os.path.join(qpath, filename) 
        #print filename
        print filepath    
        if os.path.isdir(filepath):  
            dirlist(filepath,z)  
        else:  
             z.write(filepath)
    # z.close()
if __name__ == '__main__':

	z = zipfile.ZipFile(target, 'w',zipfile.ZIP_DEFLATED)
	dirlist(source_dir,z)
	z.close()

# if os.path.isdir(source_dir):  
# 	#第一层目录循环
#     for one in os.listdir(source_dir):
#     	#排除log目录
#     	if one=='log':
#     		continue
#     	onefile=source_dir+'/'+one

#     	#判断第一层目录下的文件是否是目录
#     	if os.path.isdir(onefile):
#     		#第二层目录循环
#     		for two in os.listdir(onefile):
#     			#排除log目录
#     			if two=='log':
#     				continue
#     			twofile=onefile+'/'+two

#     			#判断第二层目录下的文件是否是目录
#     			if os.path.isdir(twofile):
#     				#第三层目录循环
#     				for three in os.listdir(twofile):
#     					#排除log目录
#     					if three=='log':
#     						continue
#     					threefile=twofile+'/'+three

#     					#判断第三层目录下的文件是否是目录
#     					if os.path.isdir(threefile):
#     						#第四层目录循环
#     						for four in os.listdir(threefile):
#     							if four=='log':
#     								continue
#     							fourfile=threefile+'/'+four
#     							#判断第四层目录下的文件是否是目录
#     							if os.path.isdir(fourfile):
#     								#第五层目录循环
#     								for five in os.listdir(fourfile):
#     									pass
#     							z.write(fourfile)

#     					z.write(threefile)

#     			z.write(twofile)

#         z.write(onefile)  
#          # close() 是必须调用的！  
#     z.close()    


