#!/usr/bin/env python
# encoding: utf-8

'''-------------------------------------------------------------------'''
''' 超级管理员命令 super cmd line 客户端                              '''
'''-------------------------------------------------------------------'''
import socket

def startConnect():
  host = "localhost"
  port = 22189
  sfd = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
  sfd.connect((host, port))
def start():
  startConnect()

if __name__ == '__main__':
  start()

