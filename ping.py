# -*- coding:utf-8 -*-
import os
import datetime

ip="192.168.1.61"

while True:
	date='echo %date%;%time% >> ping.txt'
	os.system(date)
	pings='ping ' + ip + ' -n 1 -l 2000 |findstr "TTL" >> ping.txt';
	os.system(pings)
	