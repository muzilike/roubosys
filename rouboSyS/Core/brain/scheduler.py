#!/usr/bin/env python
# encoding: utf-8

'''--------------------------------------'''
''' 系统的调度中心，Super cmd line管理者 '''
'''--------------------------------------'''
import sys
sys.path.append("..")
import time
import multiprocessing as multip
import jobs.roubosysjobs as jobs
import admin.supercmd.supercmd as supercmd

def startJobByName(jobList, jobName):
  if jobName == "#":
    for job in jobList.jobList:
      work = multip.Process(name = job, target = getattr(jobList, job))
      work.start()
  else:
    work = multip.Process(name = jobName, target = getattr(jobList, jobName))
    work.start()

if __name__ == '__main__':
  #rouboSysJobs = jobs.rouboSysJobs()
  #startJobByName(rouboSysJobs, "demo")
  #startJobByName(rouboSysJobs, "demo1")
  #startJobByName(rouboSysJobs, "#")
  ## start the super cmd line server
  superCmdLine = supercmd.superCmdLine()
  startJobByName(superCmdLine, "server")
  time.sleep(3)
