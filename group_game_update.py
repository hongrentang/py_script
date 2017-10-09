# -*- coding:utf-8 -*-
import os
import os.path
import time
import zipfile
import shutil
import re

global socdir
global decdir
socdir="E:/yxfw/" #更新源路径
decdir="D:/gameserver20160928/"    #更新目的路径

source_dir='d:\\gameserver20160928' #需要备份的目录
dec_dir = 'E:\\gameserverbackup' #备份到的目录
target = dec_dir + '\\GameServers_'+time.strftime('%Y-%m-%d_%H%M%S') + '.zip' #备份后的文件名






#gameser
def Group_Game_Server(path,file):
	#print path
	socfile=socdir+file
	#print socfile
	decfile=path+file
	shutil.copy2(socfile,decfile)

#公共的server_exe和dll共用函数
def Server_exe_dll(path,file):
	
	socfile=socdir+file
	#print socfile
	dirlist=os.listdir(path)
	for dir in dirlist:
		decfile=path+'/'+dir+'/'+file
		shutil.copy2(socfile,decfile)
		print decfile

#组队游戏dll
def GroupGameServer_dll(path,file,bhml):
	socfile=socdir+file
	dirlist=os.listdir(path)
	for dir in dirlist:
		if re.match(bhml,dir):
		 	decfile=path+'/'+dir+'/'+file
			du=shutil.copy2(socfile,decfile)
			print decfile

#自由场游戏dll			
def GameServer_dll(path,file,bhml):
	socfile=socdir+file
	print path
	dirlist=os.listdir(path)
	for dir in dirlist:
		if re.search(bhml,dir):
			decfile=path+'/'+dir+'/'+file
			shutil.copy2(socfile,decfile)
			print decfile
			
	
	

#备份
def gmbackup(path,z):
	#print qpath
    filelist = os.listdir(path) 
  
    for filename in filelist: 
    	if filename=='log':
    		continue
        filepath = os.path.join(path, filename) 
        #print filename
        print filepath    
        if os.path.isdir(filepath):  
            gmbackup(filepath,z)  
        else:  
             z.write(filepath)

def gmupdate():
#根目录公用的exe和dll文件
	#游戏大厅服
	gameplt="gameplt.exe"
	#数据库DB服
	GameDbServer="GameDbServer.exe"
	#组队管理服
	GroupManager="GroupManager.exe"
	#录像服
	HttpDbServer="HttpDbServer.exe"

	dbghelp="dbghelp.dll"
	http_req_lib="http_req_lib.dll"
	mfc120ud="mfc120ud.dll"
	msvcp120="msvcp120.dll"
	msvcr120="msvcr120.dll"
	msvcr120d="msvcr120d.dll"
	ProcessControl="ProcessControl.dll"
	vld_x86="vld_x86.dll"
#---------------组队和游戏公共的exe和dll--------------------------
	#组队场exe
	GroupGameServer="GroupGameServer.exe"
	#自由场exe
	GameServer="GameServer.exe"

	#公共的dll
	GameService="GameService.dll"
	KernelEngine="KernelEngine.dll"
	libglog="libglog.dll"
	mfc120u="mfc120u.dll"
	ModuleManager="ModuleManager.dll"
	ServiceCore="ServiceCore.dll"
	zlib1="zlib1.dll"

	#PDB文件
	#根目录
	PDB_processcontrol="processcontrol.pdb"
	PDB_PlateForm="PlateForm.pdb"

	PDB_HttpDbServer="HttpDbServer.pdb"
	PDB_http_req_lib="http_req_lib.pdb"
	PDB_groupmanager="groupmanager.pdb"
	PDB_groupgameserver="groupgameserver.pdb"
	PDB_gameserver="gameserver.pdb"
	PDB_dataserver="dataserver.pdb"

	#公共的
	PDB_gameservice="gameservice.pdb"
	PDB_kernelengine="kernelengine.pdb"
	PDB_servicecore="servicecore.pdb"
	#经典斗地主
	PDB_JQLandAndroidService="jqlandandroidservice.pdb"
	PDB_JQLandServer="jqlandserver.pdb"
	#四川麻将
	PDB_SCXZServer="SCXZServer.pdb"
	PDB_SparrowXZAndroid="SparrowXZAndroid.pdb"
	#炸金花
	PDB_ZJHServer="ZJHServer.pdb"
	#多人两房
	PDB_SparrowXZLSAndroidT="SparrowXZLSAndroidT.pdb"
	PDB_SCXZLSServerT="SCXZLSServerT.pdb"
	#四川斗地主
	PDB_LandAndroidService="landandroidservice.pdb"
	PBD_LandServer="landserver.pdb"
	#四川斗地主一张癞子
	PDB_lzlandserver="lzlandserver.pdb"
	PDB_lzlandandroidservice="lzlandandroidservice.pdb"	
	#四川麻将3人3房
	PDB_SCXZServerT="SCXZServerT.pdb"
	PDB_SparrowXZAndroidT="SparrowXZAndroidT.pdb"
	#四川麻将4人2房
	PDB_SCXZServerFT="SCXZServerFT.pdb"
	PDB_SparrowXZAndroidFT="SparrowXZAndroidFT.pdb"
	#四川麻将3人2房
	PDB_SCXZServerTT="SCXZServerTT.pdb"
	PDB_SparrowXZAndroidTT="SparrowXZAndroidTT.pdb"
	#多人三房
	PDB_SCXZLSServer="SCXZLSServer.pdb"
	PDB_SparrowXZLSAndroid="SparrowXZLSAndroid.pdb"
	#炸金花9人
	PDB_ZJHServer_Nine="ZJHServer_Nine.pdb"
	#眉山麻将
	PDB_SparrowXZMSAndroid="SparrowXZMSAndroid.pdb"
	PDB_SCXZMSServer="SCXZMSServer.pdb"
	#绵阳麻将
	PDB_SCXZMYServer="SCXZMYServer.pdb"
	PDB_SparrowXZMYAndroid="SparrowXZMYAndroid.pdb"


	#经典斗地主dll
	JQLandAndroidService="JQLandAndroidService.dll"
	JQLandServer="JQLandServer.dll"

	#四川麻将dll
	SCXZServer="SCXZServer.dll"
	SparrowXZAndroid="SparrowXZAndroid.dll"
	

	#炸金花
	ZJHAndroidService='ZJHAndroidService.dll'
	ZJHServer='ZJHServer.dll'


	#多人两房
	SparrowXZLSAndroidT='SparrowXZLSAndroidT.dll'
	SCXZLSServerT='SCXZLSServerT.dll'
	

	#四川斗地主
	LandAndroidService='LandAndroidService.dll'
	LandServer='LandServer.dll'
	
	

	#四川斗地主一张癞子
	LZSCLandAndroidService='LZSCLandAndroidService.dll'
	LZSCLandServer='LZSCLandServer.dll'

	#四川麻将3人3房
	SCXZServerT='SCXZServerT.dll'
	SparrowXZAndroidT='SparrowXZAndroidT.dll'
	

	#四川麻将4人2房
	SCXZServerFT='SCXZServerFT.dll'
	SparrowXZAndroidFT='SparrowXZAndroidFT.dll'
	

	#四川麻将3人2房
	SCXZServerTT='SCXZServerTT.dll'
	SparrowXZAndroidTT='SparrowXZAndroidTT.dll'
	
	

	#多人三房
	SCXZLSServer='SCXZLSServer.dll'
	
	SparrowXZLSAndroid='SparrowXZLSAndroid.dll'
	
	

	#炸金花9人
	ZJHAndroidService_Nine='ZJHAndroidService_Nine.dll'
	ZJHServer_Nine='ZJHServer_Nine.dll'
	
	
	#眉山麻将
	SparrowXZMSAndroid='SparrowXZMSAndroid.dll'
	SCXZMSServer='SCXZMSServer.dll'
	#绵阳麻将
	SCXZMYServer="SCXZMYServer.dll"
	SparrowXZMYAndroid="SparrowXZMYAndroid.dll"
	

	#游戏路径
	GroupGameServerpath=decdir+'GroupGameServer'
	GameServerPath=decdir+'GameServer'

	#游戏代号
	JQLand='101'    #叫抢斗地主
	ZJH='201'		#炸金花
	SCXZ='301'		#四川麻将
	SCXZL='305'		#多人两房
	Land='102'		#四川斗地主
	LZSCLand='103'	#四川斗地主一张癞子
	SCXZT='302'		#四川麻将3人3房
	SCXZFT='303'	#四川麻将4人2房
	SCXZTT='304'	#四川麻将3人2房
	SCXZLS='306'	#多人三房
	ZJHNine='202'	#炸金花9人
	SCXZMS='307'	#眉山麻将
	SCXZMY='308'    #绵阳麻将



	for file in os.listdir(socdir):
#------更新根目录公用的exe、PDB和dll文件----

		if re.match(gameplt,file):
			Group_Game_Server(decdir,file)

		if re.match(GameDbServer,file):
			Group_Game_Server(decdir,file)

		if re.match(GroupManager,file):
			Group_Game_Server(decdir,file)

		if re.match(HttpDbServer,file):
			Group_Game_Server(decdir,file)

		if re.match(dbghelp,file):
			Group_Game_Server(decdir,file)

		if re.match(http_req_lib,file):
			Group_Game_Server(decdir,file)

		if re.match(mfc120ud,file):
			Group_Game_Server(decdir,file)


		if re.match(msvcp120,file):
			Group_Game_Server(decdir,file)


		if re.match(msvcr120,file):
			Group_Game_Server(decdir,file)

		if re.match(msvcr120d,file):
			Group_Game_Server(decdir,file)

		if re.match(ProcessControl,file):
			Group_Game_Server(decdir,file)

		if re.match(vld_x86,file):
			#print file
			Group_Game_Server(decdir,file)

		#pdb文件
		if re.match(PDB_processcontrol,file):
			#print file
			Group_Game_Server(decdir,file)
		if re.match(PDB_PlateForm,file):
			#print file
			Group_Game_Server(decdir,file)	
		if re.match(PDB_HttpDbServer,file):
			#print file
			Group_Game_Server(decdir,file)
		if re.match(PDB_http_req_lib,file):
			#print file
			Group_Game_Server(decdir,file)
		if re.match(PDB_groupmanager,file):
			#print file
			Group_Game_Server(decdir,file)	
		if re.match(PDB_dataserver,file):
			#print file
			Group_Game_Server(decdir,file)	
				







#------更新公共的dll和和exe------

		#更新GroupGameServer.exe
		if re.match(GroupGameServer,file):
			#print file
			#Group_Game_Server(decdir,file)
			Server_exe_dll(GroupGameServerpath,file)

		#pdb文件
		if re.match(PDB_groupgameserver,file):
			#print file
			#Group_Game_Server(decdir,file)
			Server_exe_dll(GroupGameServerpath,file)

		#更新GameServer.exe
		if re.match(GameServer,file):
			#print file
			#Group_Game_Server(decdir,file)
			Server_exe_dll(GameServerPath,file)
		#pdb文件	
		if re.match(PDB_gameserver,file):
			#print file
			#Group_Game_Server(decdir,file)
			Server_exe_dll(GameServerPath,file)

		#更新GameService.dll
		if re.match(GameService,file):
			#print file
			Group_Game_Server(decdir,file)
			Server_exe_dll(GroupGameServerpath,file)
			Server_exe_dll(GameServerPath,file)

		#更新GameService.pdb
		if re.match(PDB_gameservice,file):
			#print file
			Group_Game_Server(decdir,file)
			Server_exe_dll(GroupGameServerpath,file)
			Server_exe_dll(GameServerPath,file)

		#更新KernelEngine.dll
		if re.match(KernelEngine,file):
			#print file
			Group_Game_Server(decdir,file)
			Server_exe_dll(GroupGameServerpath,file)
			Server_exe_dll(GameServerPath,file)

		#更新KernelEngine.pdb
		if re.match(PDB_kernelengine,file):
			#print file
			Group_Game_Server(decdir,file)
			Server_exe_dll(GroupGameServerpath,file)
			Server_exe_dll(GameServerPath,file)

		#更新libglog.dll
		if re.match(libglog,file):
			#print file
			Group_Game_Server(decdir,file)
			Server_exe_dll(GroupGameServerpath,file)
			Server_exe_dll(GameServerPath,file)

		#更新mfc120u.dll
		if re.match(mfc120u,file):
			#print file
			Group_Game_Server(decdir,file)
			Server_exe_dll(GroupGameServerpath,file)
			Server_exe_dll(GameServerPath,file)

		#更新ModuleManager.dll
		if re.match(ModuleManager,file):
			#print file
			Group_Game_Server(decdir,file)
			Server_exe_dll(GroupGameServerpath,file)
			Server_exe_dll(GameServerPath,file)

		#更新ServiceCore.dll
		if re.match(ServiceCore,file):
			#print file
			Group_Game_Server(decdir,file)
			Server_exe_dll(GroupGameServerpath,file)
			Server_exe_dll(GameServerPath,file)

		#更新ServiceCore.pdb
		if re.match(PDB_servicecore,file):
			#print file
			Group_Game_Server(decdir,file)
			Server_exe_dll(GroupGameServerpath,file)
			Server_exe_dll(GameServerPath,file)

		#更新zlib1.dll
		if re.match(zlib1,file):
			#print file
			Group_Game_Server(decdir,file)
			Server_exe_dll(GroupGameServerpath,file)
			Server_exe_dll(GameServerPath,file)

#--------------------游戏更新---------------------------
		#叫抢斗地主
		
		if re.match(JQLandAndroidService,file):
			#print file
			GroupGameServer_dll(GroupGameServerpath,file,JQLand)
			GameServer_dll(GameServerPath,file,JQLand)
		
		if re.match(JQLandServer,file):
			#print file
			GroupGameServer_dll(GroupGameServerpath,file,JQLand)
			GameServer_dll(GameServerPath,file,JQLand)
		#pdb文件	
		if re.match(PDB_JQLandAndroidService,file):
			#print file
			
			GroupGameServer_dll(GroupGameServerpath,file,JQLand)
			GameServer_dll(GameServerPath,file,JQLand)

		if re.match(PDB_JQLandServer,file):
			#print file
			
			GroupGameServer_dll(GroupGameServerpath,file,JQLand)
			GameServer_dll(GameServerPath,file,JQLand)

		#-----四川麻将---------
		
		if re.match(SCXZServer,file):
			#print file
			GroupGameServer_dll(GroupGameServerpath,file,SCXZ)
			GameServer_dll(GameServerPath,file,SCXZ)
			
		if re.match(SparrowXZAndroid,file):
			#print file
			GroupGameServer_dll(GroupGameServerpath,file,SCXZ)
			GameServer_dll(GameServerPath,file,SCXZ)
		#pdb文件
		if re.match(PDB_SCXZServer,file):
			#print file
			
			GroupGameServer_dll(GroupGameServerpath,file,SCXZ)
			GameServer_dll(GameServerPath,file,SCXZ)
			
		if re.match(PDB_SparrowXZAndroid,file):
			#print file
			
			GroupGameServer_dll(GroupGameServerpath,file,SCXZ)
			GameServer_dll(GameServerPath,file,SCXZ)
		#------炸金花--------	
		
		if re.match(ZJHServer,file):
			#print file
			GroupGameServer_dll(GroupGameServerpath,file,ZJH)

		if re.match(ZJHAndroidService,file):
			#print file
			GroupGameServer_dll(GroupGameServerpath,file,ZJH)
		#pdb文件	
		if re.match(PDB_ZJHServer,file):
			#print file
			
			GroupGameServer_dll(GroupGameServerpath,file,ZJH)

		#------多人两房--------	
		
		if re.match(SparrowXZLSAndroidT,file):
			#print file
			GroupGameServer_dll(GroupGameServerpath,file,SCXZL)

		if re.match(SCXZLSServerT,file):
			#print file
			GroupGameServer_dll(GroupGameServerpath,file,SCXZL)

		#pdb文件	
		if re.match(PDB_SparrowXZLSAndroidT,file):
			#print file
			
			GroupGameServer_dll(GroupGameServerpath,file,SCXZL)

		if re.match(PDB_SCXZLSServerT,file):
			#print file

			GroupGameServer_dll(GroupGameServerpath,file,SCXZL)

		#------四川斗地主--------	
		
		if re.match(LandAndroidService,file):
			#print file
			GroupGameServer_dll(GroupGameServerpath,file,Land)

		if re.match(LandServer,file):
			#print file
			GroupGameServer_dll(GroupGameServerpath,file,Land)
		#pdb文件	
		if re.match(PDB_LandAndroidService,file):
			#print file
			GroupGameServer_dll(GroupGameServerpath,file,Land)

		if re.match(PBD_LandServer,file):
			#print file
			GroupGameServer_dll(GroupGameServerpath,file,Land)

		#------四川斗地主一张癞子--------	
		
		if re.match(LZSCLandAndroidService,file):
			#print file
			GroupGameServer_dll(GroupGameServerpath,file,LZSCLand)

		if re.match(LZSCLandServer,file):
			#print file
			GroupGameServer_dll(GroupGameServerpath,file,LZSCLand)
		#pdb文件	
		if re.match(PDB_lzlandandroidservice,file):
			#print file
			GroupGameServer_dll(GroupGameServerpath,file,LZSCLand)

		if re.match(PDB_lzlandserver,file):
			#print file
			GroupGameServer_dll(GroupGameServerpath,file,LZSCLand)

		#------四川麻将3人3房--------	
		
		if re.match(SCXZServerT,file):
			#print file
			GroupGameServer_dll(GroupGameServerpath,file,SCXZT)

		if re.match(SparrowXZAndroidT,file):
			#print file
			GroupGameServer_dll(GroupGameServerpath,file,SCXZT)
		#pdb文件	
		if re.match(PDB_SCXZServerT,file):
			#print file
			GroupGameServer_dll(GroupGameServerpath,file,SCXZT)

		if re.match(PDB_SparrowXZAndroidT,file):
			#print file
			GroupGameServer_dll(GroupGameServerpath,file,SCXZT)

		#------四川麻将4人2房--------	
		
		if re.match(SCXZServerFT,file):
			#print file
			GroupGameServer_dll(GroupGameServerpath,file,SCXZFT)

		if re.match(SparrowXZAndroidFT,file):
			#print file
			GroupGameServer_dll(GroupGameServerpath,file,SCXZFT)
		#pdb文件	
		if re.match(PDB_SCXZServerFT,file):
			#print file
			GroupGameServer_dll(GroupGameServerpath,file,SCXZFT)

		if re.match(PDB_SparrowXZAndroidFT,file):
			#print file
			GroupGameServer_dll(GroupGameServerpath,file,SCXZFT)					

		#------四川麻将3人2房--------	
		
		if re.match(SCXZServerTT,file):
			#print file
			GroupGameServer_dll(GroupGameServerpath,file,SCXZTT)

		if re.match(SparrowXZAndroidTT,file):
			#print file
			GroupGameServer_dll(GroupGameServerpath,file,SCXZTT)
		#pdb文件
		if re.match(PDB_SCXZServerTT,file):
			#print file
			GroupGameServer_dll(GroupGameServerpath,file,SCXZTT)

		if re.match(PDB_SparrowXZAndroidTT,file):
			#print file
			GroupGameServer_dll(GroupGameServerpath,file,SCXZTT)

		#------多人三房--------	
		
		if re.match(SCXZLSServer,file):
			#print file
			GroupGameServer_dll(GroupGameServerpath,file,SCXZLS)

		if re.match(SparrowXZLSAndroid,file):
			#print file
			GroupGameServer_dll(GroupGameServerpath,file,SCXZLS)
		#pdb文件
		if re.match(PDB_SCXZLSServer,file):
			#print file
			GroupGameServer_dll(GroupGameServerpath,file,SCXZLS)

		if re.match(PDB_SparrowXZLSAndroid,file):
			#print file
			GroupGameServer_dll(GroupGameServerpath,file,SCXZLS)

		#------炸金花9人--------	
		
		if re.match(ZJHAndroidService_Nine,file):
			#print file
			GroupGameServer_dll(GroupGameServerpath,file,ZJHNine)

		if re.match(ZJHServer_Nine,file):
			#print file
			GroupGameServer_dll(GroupGameServerpath,file,ZJHNine)
		#pdb文件	

		if re.match(PDB_ZJHServer_Nine,file):
			#print file
			GroupGameServer_dll(GroupGameServerpath,file,ZJHNine)		

		#------眉山麻将--------	
		
		if re.match(SparrowXZMSAndroid,file):
			#print file
			GroupGameServer_dll(GroupGameServerpath,file,SCXZMS)

		if re.match(SCXZMSServer,file):
			#print file
			GroupGameServer_dll(GroupGameServerpath,file,SCXZMS)

		#pdb文件	
		if re.match(PDB_SparrowXZMSAndroid,file):
			#print file
			GroupGameServer_dll(GroupGameServerpath,file,SCXZMS)

		if re.match(PDB_SCXZMSServer,file):
			#print file
			GroupGameServer_dll(GroupGameServerpath,file,SCXZMS)

		#------绵阳麻将--------	
		
		if re.match(SparrowXZMYAndroid,file):
			#print file
			GroupGameServer_dll(GroupGameServerpath,file,SCXZMY)

		if re.match(SCXZMYServer,file):
			#print file
			GroupGameServer_dll(GroupGameServerpath,file,SCXZMY)

		#pdb文件	
		if re.match(PDB_SparrowXZMYAndroid,file):
			#print file
			GroupGameServer_dll(GroupGameServerpath,file,SCXZMY)

		if re.match(PDB_SCXZMYServer,file):
			#print file
			GroupGameServer_dll(GroupGameServerpath,file,SCXZMY)			
																
	

if __name__ == '__main__':

	flag = True
	while (flag):

		ts="是否需要更新：确认(Y) | 退出(Q)\n"
		st=ts.decode('utf-8')
		print st
		answer = raw_input("Input: ")
		if  'q' == answer.lower():
			flag = False
		if 'y' == answer.lower():
			z = zipfile.ZipFile(target, 'w',zipfile.ZIP_DEFLATED)
			print u'开始备份....'
			gmbackup(source_dir,z)
			z.close()
			print u'备份完成....'
			print '------------------------------------------'
			print u'开始更新....'
			gmupdate()
			print u'更新完成....'
			print '\n'
			print '------------------------------------------'
		
	