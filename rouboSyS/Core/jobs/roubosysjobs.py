#!/usr/bin/env python
# encoding: utf-8

'''-------------------------------------------------------------------'''
''' 系统的任务中心，负责导入所有的jobs，并提供reload单个job模块的接口 '''
'''-------------------------------------------------------------------'''

import demo.demojob as demo
import demo1.demojob as demo1
import fitbit.rfitbit as fitbit

class rouboSysJobs:
  jobList = ("demo", "demo1", "fitbit")
  def __init__(self):
    print 'init the rouboSysJobs'
  def demo(self):
    demo.demotast()
  def demo1(self):
    demo1.demotast()
  def fitbit(self):
    fitbit.loginMyFitbit()

if __name__ == '__main__':
  demo.demotast()
