# -*- coding:utf-8 -*-


import os
import os.path
import shutil
import zipfile
import time,datetime

zip_File_Path='D:/platform/HotUpdate/'  #zip 目录地址
txt_File_path='D:/site/yxgxzyjk/GameData/HotUpdate/'		   #TXT 目录地址
Target_File_Path='E:/rgxbeifen/'		#拷贝目标地址
gx_zip_path='E:/rgxbeifen/'     #更新包解压到的路径
zipdir_path='e:/zip/'			#更新包路径

#备份zip文件
def copyzip(sourcedir,targetdri):
	for file in os.listdir(sourcedir):
		
		filename,filepostfix=file.split(".")
		if 'zip' in filepostfix.lower():
			oldname=sourcedir+filename+"."+filepostfix
			newname=targetdri+filename+"."+filepostfix
			shutil.copy2(oldname,newname)

##备份txt文件			
def copytxt(sourcedir,targetdri):
	for file in os.listdir(sourcedir):
		filename,filepostfix=file.split(".")
		if 'txt' in filepostfix.lower():
			oldname=sourcedir+filename+"."+filepostfix
			newname=targetdri+filename+"."+filepostfix
			shutil.copy2(oldname,newname)
##删除			
##解压更新包
def unzip_to_path(zipfile_path,gx_zip_path):
	f = zipfile.ZipFile(zipfile_path,'r')
	for file in f.namelist():
		f.extract(file,gx_zip_path)
		
##更新zip文件
def new_gx_zip(sourcedir,targetdri):
	  
	for file in os.listdir(sourcedir):
		
		filename,filepostfix=file.split(".")
		if 'zip' in filepostfix.lower():
			oldname=sourcedir+filename+"."+filepostfix
			newname=targetdri+filename+"."+filepostfix
			shutil.copy2(oldname,newname)
			
##更新txt文件
def new_gx_txt(sourcedir,targetdri):
	for file in os.listdir(sourcedir):
		
		filename,filepostfix=file.split(".")
		if 'txt' in filepostfix.lower():
			oldname=sourcedir+filename+"."+filepostfix
			newname=targetdri+filename+"."+filepostfix
			shutil.copy2(oldname,newname)
			
def reigx(yxtype):
	global Target_File_Path
	global gx_zip_path
	global zip_File_Path
	global txt_File_path
	global zipdir_path
	formatTime = datetime.datetime.now().strftime('%Y-%m-%d')
	targetFoldername = formatTime +'/bf/'+yxtype+'/'
	dec_Target_File_Path = Target_File_Path+targetFoldername
	if not os.path.exists(dec_Target_File_Path):
		os.makedirs(dec_Target_File_Path)
	if yxtype=='yyplatform':
		src_zip_File_Path = zip_File_Path+yxtype+'/android/13/'
		src_txt_File_path = txt_File_path+yxtype+'/android/13/'
	else:
		src_zip_File_Path = zip_File_Path+yxtype+'/android/3/'
		src_txt_File_path = txt_File_path+yxtype+'/android/3/'
	copyzip(src_zip_File_Path,dec_Target_File_Path)
	copytxt(src_txt_File_path,dec_Target_File_Path)
	ungetFoldername = formatTime +'/gx/'+ yxtype+'/'
	dsc_gx_zip_path = gx_zip_path+ungetFoldername
	if os.path.exists(dsc_gx_zip_path):
		shutil.rmtree(dsc_gx_zip_path)
		
	if not os.path.exists(dsc_gx_zip_path):
		os.makedirs(dsc_gx_zip_path)
	
	new_zipdir_path = zipdir_path + type+'.zip'
	unzip_to_path(new_zipdir_path,dsc_gx_zip_path)
	gx_list=['android','ios']
	for i in range(len(gx_list)):
		gx_type=gx_list[i]
		if yxtype=='yyplatform':
			dsc_zip_file_path = zip_File_Path+yxtype+'/'+gx_type+'/13/'
			if  os.path.exists(dsc_zip_file_path):
				shutil.rmtree(dsc_zip_file_path)  
			dsc_txt_file_path = txt_File_path+yxtype+'/'+gx_type+'/13/'
			if  os.path.exists(dsc_txt_file_path):
				shutil.rmtree(dsc_txt_file_path)
		else:
			dsc_zip_file_path = zip_File_Path+yxtype+'/'+gx_type+'/3/'
			if  os.path.exists(dsc_zip_file_path):
				shutil.rmtree(dsc_zip_file_path)
			dsc_txt_file_path = txt_File_path+yxtype+'/'+gx_type+'/3/'
			if  os.path.exists(dsc_txt_file_path):
				shutil.rmtree(dsc_txt_file_path)
		if not os.path.exists(dsc_zip_file_path):
			os.makedirs(dsc_zip_file_path)
		if not os.path.exists(dsc_txt_file_path):
			os.makedirs(dsc_txt_file_path)
		new_gx_zip(dsc_gx_zip_path,dsc_zip_file_path)
		new_gx_txt(dsc_gx_zip_path,dsc_txt_file_path)
		
if  __name__ =="__main__":

	 xz="选择更新的类别：经典斗地主:(输入1) | 四川斗地主(输入2) | 炸金花(输入3) | 麻将(输入4) |ATT(输入5) | 平台更新(输入0)  |退出(输入q)\n"
	 st=xz.decode('utf-8')
	 flag = True
	 while (flag):
		print(st)
		answer = raw_input("Input: ")
		if  'q' == answer.lower():
			flag = False
		elif '1' == answer :
			type="1001"
			reigx(type)
			print "1001----success"
			
		elif '2' == answer :
			type="1002"
			reigx(type)
			print "1002----success"
		elif '3' == answer:
			type = "1003"
			reigx(type)
			print "1003----success"
		elif '4' == answer:
			type = "1004"
			reigx(type)
			print "1004----success"
		elif '5' == answer:
			type = "1005"
			reigx(type)
			print "1005----success"		
		elif '0' == answer:
			type = "yyplatform"
			reigx(type)
			print "yyplatform---success"
		
		else:
			print "not the correct command"