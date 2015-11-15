#!/usr/bin/env python
# encoding: utf-8

'''-------------------------------------------------------------------'''
''' 系统的任务中心，负责导入所有的jobs，并提供reload单个job模块的接口 '''
'''-------------------------------------------------------------------'''

from fitbit.rfitbit import rFitbit
from fitbit.fitbit_notify import fitbitNotify

class rouboSysJobs:
  jobList = ("fitbit", "fitbit_notify")

  def __init__(self):
    print 'init the rouboSysJobs'

  def fitbit(self):
    fitbit = rFitbit()
    fitbit.loop_forever()

  def fitbit_notify(self):
    fitbit_notify = fitbitNotify()
    fitbit_notify.loop_forever()
