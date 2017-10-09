# -*- coding:utf-8 -*-
import os
import time

game_plt_path='E:\\gameserver20160928'
game_group_path='E:\\gameserver20160928\\GroupGameServer'
game_game_path='E:\\gameserver20160928\\GameServer'
def game_plt_start(servername):
	os.system(servername)

def game_group_start(game_group_path,servername):
	dirlist=os.listdir(game_group_path)
	for i in dirlist :
		filepath=os.path.join(game_group_path,i)
		os.chdir(filepath)
		os.system(servername)
		time.sleep(3)
		print u'%s.....启动成功' %filepath

def game_game_start(game_game_path,servername):
	dirlist=os.listdir(game_game_path)
	for i in dirlist :
		filepath=os.path.join(game_game_path,i)
		os.chdir(filepath)
		os.system(servername)
		time.sleep(3)
		print u'%s.....启动成功' %filepath
	

if __name__ == '__main__':
	flag=True
	while flag :
		print u'是否开启应用：确认(Y) | 退出(Q)\n'
		answer = raw_input("Input: ")
		if  'q' == answer.lower():
			flag = False
		if 'y' == answer.lower():
			os.chdir(game_plt_path)
			game_plt_start('start gameplt.exe')
			time.sleep(3)
			print u'gameplt.exe.....启动成功'
			game_plt_start('start GameDbServer.exe')
			time.sleep(3)
			print u'GameDbServer.exe.....启动成功'
			game_plt_start('start GroupManager.exe')
			time.sleep(3)
			print u'GroupManager.exe.....启动成功'	
			game_plt_start('start HttpDbServer.exe')
			time.sleep(3)
			print u'HttpDbServer.exe.....启动成功'

			game_group_start(game_group_path,'start GroupGameServer.exe')
			game_game_start(game_game_path,'start GameServer.exe')

