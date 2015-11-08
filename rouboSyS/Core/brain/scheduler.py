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

jobRecord = {}

def startJobByName(jobList, jobName):
  if jobName == "#":
    for job in jobList.jobList:
      work = multip.Process(name = job, target = getattr(jobList, job), args= ('start'))
      work.start()
      jobRecord[job] = work
  else:
    work = multip.Process(name = jobName, target = getattr(jobList, jobName), args = ('start'))
    work.start()
    jobRecord[jobName] = work

def stopJobByName(jobList, jobName):
  if jobName == "#":
    for job in jobList.jobList:
      work = jobRecord[job]
      if work :
        work.terminate()
        work.join()
        jobRecord.pop(job)
  else:
    work = jobRecord[jobName]
    if work :
      work.terminate()
      work.join()
      jobRecord.pop(jobName)

if __name__ == '__main__':
  rouboSysJobs = jobs.rouboSysJobs()
  startJobByName(rouboSysJobs, "fitbit")
  #startJobByName(rouboSysJobs, "demo")
  #startJobByName(rouboSysJobs, "demo1")
  #startJobByName(rouboSysJobs, "#")
  ## start the super cmd line server
  #superCmdLine = supercmd.superCmdLine()
  #startJobByName(superCmdLine, "server")
  #time.sleep(3)
