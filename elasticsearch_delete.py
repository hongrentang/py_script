# -*- coding:utf-8 -*-
import urllib2
import datetime

if __name__ == '__main__':
	
	uri="http://47.94.11.105:9210/"
	five_datetime=datetime.datetime.now()+datetime.timedelta(days=-5)
	five_date=five_datetime.strftime('%Y.%m.%d')
	five_uri=uri+'*-'+five_date
	request = urllib2.Request(five_uri)
	request.get_method = lambda: 'DELETE'
	response = urllib2.urlopen(request)
