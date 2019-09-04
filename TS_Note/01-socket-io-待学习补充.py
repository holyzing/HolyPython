#!/usr/bin/python
#coding:utf-8
import json
import os
import sqlite3
class ApiInfor(object):
    def __init__(self, type, args, doc, favorite='0', custom='0'):
        self.type = type
        self.args = args
        self.doc = doc
        self.favorite = favorite  
class Api(object): 
   def __init__(self, apiname, apiInfor):
        self.apiname = apiname
        self.apiInfor = apiInfor
def parse():
    with open('middleApi.json', 'r', encoding='utf-8') as jsonfile:
        json_string = json.load(jsonfile,)
    print(len(json_string))
    conn = sqlite3.connect(database='main.db')
    cursor = conn.cursor()
    for apiname in json_string:
        apiinfor = json_string[apiname]
        print(apiinfor)
        type = apiinfor['type']
        args = ','.join(apiinfor['args'])
        doc = apiinfor['doc']
        sql ='insert into api (apiname, type, args, doc) values (:apiname, :type, :args, :doc)'
        cursor.execute(sql,{'apiname':apiname, 'type':type, 'args':args, 'doc':doc})
        conn.commit()
    cursor.close()
    conn.close()
        # os.system('pause')
# -----------------------------------------------------------------------------
import socket, SocketServer
def test():
    host = '127.0.0.1'
    port = 60000
    s = socket.socket()
    s.bind((host, port))
    s.listen(5)
    # Unicode 和 str 的区别
    print u'垃圾python2'
    print '垃圾python2'
    print len(u'垃圾python2')
    print len('垃圾python2')
    ClientSock, ClientAddr = s.accept( )
    print ClientAddr, ClientSock
    buf = ClientSock.recv(1024)
    print buf
    print type(buf)
    print type(buf.decode("utf-8"))
    print buf.decode("utf-8") #默认的是 ASCII
    # 不能接收完在发
    # s.sendall("这是一段python的中文字节串！")
    # s.sendall(u"这是一段python的中文字符串！")

class Myserver(SocketServer.BaseRequestHandler):
    def handle(self):
        conn = self.request
        conn.sendall("你好，我是机器人")
        while True:
            ret_bytes = conn.recv(1024)
            ret_str = str(ret_bytes,encoding="utf-8")
            if ret_str == "q":
                break
            conn.sendall(bytes(ret_str+"你好我好大家好",encoding="utf-8"))

if __name__ == "__main__":
    server = SocketServer.ThreadingTCPServer(("127.0.0.1", 60000),Myserver)
    server.serve_forever()

"""
    这是一段文档注释
"""

'''
   这是一段普通注释
'''
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        