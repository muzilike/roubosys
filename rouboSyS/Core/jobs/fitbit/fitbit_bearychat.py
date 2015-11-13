#!/usr/bin/env python
# encoding: utf-8

import urllib2
import urllib
import sys
import os

class fitbitBearyChat:

  def pushchat(self, message, msgtype):
    gourl = "http://hook.bearychat.com/\=bw7nU/incoming/b3abc70e3fb1b19f89bccc3c3513984d"
    header = {"Content-Type": "application/json"}
    godata = urllib.urlencode({"text": message})
    req = urllib2.Request(url=gourl, headers=header, data=godata)
    urllib2.urlopen(req)

  def pushchatcurl(self, message, msgtype):
    gourl = "http://hook.bearychat.com/\=bw7nU/incoming/b3abc70e3fb1b19f89bccc3c3513984d"
    header = '"Content-Type: application/json"'
    godata = '\'{"text": "'+message +'"}\' '
    cmd = "curl -H " + header + ' -d ' + godata + gourl
    print cmd
    os.system(cmd)

if __name__ == '__main__':
  msg = sys.argv[1]
  print msg
  bc = fitbitBearyChat()
  bc.pushchatcurl(msg, None)
