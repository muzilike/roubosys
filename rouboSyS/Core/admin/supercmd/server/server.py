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

def passwdComing(clientsock, clientaddr):
  for trycount in range(1, 4):
    clientsock.sendall(loginInfo())
    data = clientsock.recv(1024)
    print '>_ ...', data.strip()
    print '>_ Check the login info ...'
    if data.strip() == "ll123456":
      clientsock.sendall(welcomeInfo())
      print '>_ Login ok ...'
      return True
    else:
      print '>_ Login failed ...'
  clientsock.sendall(refuseInfo())
  return False


def start():
  sfd = startListen()
  while 1:
    clientSock, clientAddr = sfd.accept()
    print '>_ Connected from ', clientAddr
    print '>_ Waiting for login ...'
    ###############################################
    # Login by password
    passby = passwdComing(clientSock, clientAddr)
    if passby :
      print '>_ Go to work or go on check admin...'
    else:
      clientSock.close()
    ###############################################
    # Go to work
    clientSock.close()
    return 0
