#!/usr/bin/env python
# encoding: utf-8

'''-------------------------------------------------------------------'''
''' 超级管理员命令入口 super cmd line  服务器端和客户端               '''
'''-------------------------------------------------------------------'''

import server.server as server
import client.client as client

class superCmdLine:
  jobList = ("server", "client")
  def __init__(self):
    print 'init the superCmdLine'
  def server(self):
    server.start()
  def client(self):
    client.start()

