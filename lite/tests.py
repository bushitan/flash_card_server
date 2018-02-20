#coding:utf-8

from django.test import TestCase

# Create your tests here.

# from lite.models import *
# import datetime
# d = File.objects.all()[0]
# print d.create_time ,type(d.create_time )
# print datetime.datetime(2017, 1, 1) ,type(  datetime.datetime(2017, 1, 1) )
#
# dt =  datetime.datetime(2017, 12, 16)
# dt = dt.replace(tzinfo=None)
# d1 = d.create_time
# d1 = d1.replace(tzinfo=None)
# print str((d1 -dt ).days),


import urllib2
# url = "https://www.12xiong.top/day365/lite/upload/callback/"
url = "http://192.168.200.103:8000/day365/lite/upload/callback/"
# response = urllib2.urlopen(url)
# html = response.read()
# print html


import urllib,urllib2

# url = 'http://www.someserver.com/cgi-bin/register.cgi'

values = {'name' : 'Michael Foord',
          'location' : 'Northampton',
          'language' : 'Python' }

data = urllib.urlencode(values)

req = urllib2.Request(url, data)

response = urllib2.urlopen(req)

the_page = response.read()

# https://www.12xiong.top/day365/admin/lite/file/