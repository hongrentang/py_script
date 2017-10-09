# -*- coding:utf-8 -*-
import os
import sys
import time

game_path="C:\\Users\\Administrator\\Desktop\\Gameserver" #游戏服根路径
plt_path="C:\\Users\\Administrator\\Desktop\\PlazaServer"                 #平台服日志log路径




##平台和游戏服日志删除
def plt_game_remove_log(path,date):
    filelist = os.listdir(path) 
    for i in filelist:
        filepath=os.path.join(path,i)

        if i=='log':
            remove_log(filepath,date)        

        if os.path.isdir(filepath):
            plt_game_remove_log(filepath,date)
        else:
            continue

            
             
def remove_log(path,date):
    filelist = os.listdir(path)
    for  filename in filelist:

        filepath=os.path.join(path,filename)
        #print filepath

        if os.path.isdir(filepath):
            remove_log_file(filepath,date)
		
        filedate = os.path.getmtime(filepath)
        num = (date - filedate)/60/60/24

        if num > 7:
            try:
			
                #os.remove(filepath)

                print "%s remove success." % filepath
            except Exception as error:
                print error
                print "%s remove faild." % filename
				
#日志文件删除
def remove_log_file(path,date):
    filelist = os.listdir(path) 
    for filename in filelist:
        filepath=os.path.join(path,filename)
        #print filepath

        if os.path.isdir(filepath):
            remove_log_file(filepath,date)
        else:
            filedate = os.path.getmtime(filepath)
            #print filedate
            num =(date - filedate)/60/60/24
            #print num

            if num > 7:
                try:

                    #os.remove(filepath)
                    print "%s remove success." % filepath
                except Exception as error:
                    print error
                    print "%s remove faild." % filename


        
if __name__ == "__main__":
    flag = True
    while (flag):
        print u'是否真的需删除log文件：确认(Y) | 退出(Q)\n'
        answer = raw_input('Input:')
        if  'q' == answer.lower():
            flag = False
        if 'y' == answer.lower():
            try:
                date = time.time()
                #print date
                plt_game_remove_log(game_path,date)
                plt_game_remove_log(plt_path,date)
                print u'7天前的log文件已清理完毕.......'
            except Exception as e:
                print e
                sys.exit(-1)