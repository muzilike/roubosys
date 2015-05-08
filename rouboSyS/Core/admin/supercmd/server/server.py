#!/usr/bin/env python
# encoding: utf-8

'''-------------------------------------------------------------------'''
''' 超级管理员命令 super cmd line  服务器端                           '''
'''-------------------------------------------------------------------'''

import socket

def startListen():
  host = ''
  port = 22189
  sfd  = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
  sfd.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
  sfd.bind((host, port))
  sfd.listen(1)
  return sfd

def loginInfo():
  info1 = "************************************************\n"
  info2 = "* roubosys : admin login, password please:      \n"
  info3 = "************************************************\n"
  return info1+info2+info3

def welcomeInfo():
  info1 = "++++++++++++++++++++++++++++++++++++++++++++++++\n"
  info2 = "+ roubosys : Hi, admin. servers for you         \n"
  info3 = "++++++++++++++++++++++++++++++++++++++++++++++++\n"
  return info1+info2+info3

def refuseInfo():
  info1 = "------------------------------------------------\n"
  info2 = "- roubosys : only servers for roubo             \n"
  info3 = "------------------------------------------------\n"
  return info1+info2+info3

def start():
  sfd = startListen()
  while 1:
    clientSock, clientAddr = sfd.accept()
    clientfile = clientSock.makefile('rw', 1)
    clientfile.write(loginInfo())
    line = clientfile.readline().strip()
    if line == "ll123456":
      clientfile.write(welcomeInfo())
    else:
      clientfile.write(refuseInfo())
    clientfile.close()
    clientSock.close()
    return 0
