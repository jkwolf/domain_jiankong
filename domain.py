#-*-coding:utf-8-*-
#author:jkwolf18


import time
import json
import hashlib
import string
import random
import requests
import MySQLdb

mysql_name=[]


def mysql_check(int,src_name):
    db = MySQLdb.connect("localhost", "root", "root", "test", charset='utf8' )
    if int ==1:
        cursor = db.cursor()
        sql = "select * from ym_jiankong_"+src_name+";"
        try:
           cursor.execute(sql)
           results = cursor.fetchall()
           for row in results:
              row1 = row[1]
              #print str(row1)
              mysql_name.append(str(row1))
        except:
           print "Error: unable to fecth data"
        db.close()
        return mysql_name

def mysqladd_insert(xm_name,src_name):
    db = MySQLdb.connect("localhost", "root", "root", "test", charset='utf8' )
    # 使用cursor()方法获取操作游标 
    cursor = db.cursor()
    # SQL 插入语句
    sql ="insert into ym_jiankong_"+src_name+"(yuming_name,yuming_title) values('"+xm_name+"','');"
    #print sql
    try:
       # 执行sql语句
       cursor.execute(sql)
       # 提交到数据库执行
       db.commit()
    except:
       # Rollback in case there is any error
       db.rollback()
    # 关闭数据库连接
    db.close()

def send(content):
    #print type(content)
    access_token="xxxxxxx"
    #if 9 <= int(datetime.now().strftime('%H')) <= 24:
    url = u"https://oapi.dingtalk.com/robot/send?access_token={0}".format(access_token)
    #data = u'{{"msgtype":"text","text":{{"content":"{0}\\n{1}"}}}}'.format(time.ctime(), content)
    data = '{{"msgtype":"text","text":{{"content":"{0}\\n{1}"}}}}'.format(time.ctime(), content)
    headers = {u"Content-Type": u"application/json"}
    requests.post(url, headers=headers, data=data, timeout=3)
        
        
def domains_open():
    src_name="pingan"
    mysql_list=mysql_check(1,src_name)
    #print mysql_list
    with open("domains") as f:
        for line in f.readlines():
            line = line.strip()
            if line not in mysql_list:
                mysqladd_insert(line,src_name)
                print line
                #send(line)

def main():
    domains_open()

if __name__ == '__main__':
    main()    
