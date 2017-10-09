# -*- coding:utf-8 -*-
import os
import time
GameServer='taskkill /F /IM GameServer.exe'
GroupGameServer='taskkill /F /IM GroupGameServer.exe'
HttpDBserver='taskkill /F /IM HttpDbServer.exe'
GroupManager='taskkill /F /IM GroupManager.exe'
GameDbServer='taskkill /F /IM GameDbServer.exe'
gameplt='taskkill /F /IM gameplt.exe'



def gameserver_stop(gameservername):
	os.system(gameservername)

if __name__ == '__main__':
	flag=True
	while flag :
		print u'是否需要关闭应用：确认(Y) | 退出(Q)\n'
		answer = raw_input("Input: ")
		if  'q' == answer.lower():
			flag = False
		if 'y' == answer.lower():
			gameserver_stop(GameServer)
			time.sleep(3)
			gameserver_stop(GroupGameServer)
			time.sleep(3)				
			gameserver_stop(HttpDBserver)
			time.sleep(1)
			gameserver_stop(GroupManager)
			time.sleep(1)
			gameserver_stop(GameDbServer)
			time.sleep(1)
			gameserver_stop(gameplt)
			time.sleep(1)
