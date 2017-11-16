#-*- coding: utf-8 -*-
#!/usr/bin/python
##
##import sqlite3
##
##conn = sqlite3.connect('test.db')
##
##print "Opened database successfully";
##
##
##cursor = conn.execute("SELECT id, name, address, salary  from COMPANY")
##for row in cursor:
##   print "ID = " , row[0]
##   print "NAME = " , row[1]
##   print "ADDRESS = " , row[2]
##   print "SALARY = " , row[3], "\n"
##
##print "Operation done successfully";
##conn.close()
from feedback.models import *
from datetime import datetime
 
# Feedback 객체 생성
fb = Feedback(number=1, count=30, name='이정헌')
 
# 새 객체 INSERT
fb.save()
