#!/usr/bin/env python
# encoding: utf-8
import sys
sys.path.append("..")
from todo_db import todo_db
import redis
import colors
import os
import time
import fitbit.rfitbit as fitbit

def fitbit_init():
  fb = fitbit.initfitbit()
  return fb

def layout_init():
  tododb = redis.StrictRedis(host=todo_db['host'], port=todo_db['port'], db=todo_db['lists'])
  return tododb

def clear_term():
  os.system("clear")

def region_message(db):
  frame = ' '
  sysinfo = db.get('sysinfo')
  if sysinfo:
    info = sysinfo.split('|')
    internetConnect = info[0]
    alarmSyncy = info[1]
    importMesg = info[2]
  else:
    internetConnect = 'unkown'
    alarmSyncy = 'unkown'
    importMesg = '0'

  print colors.bold(" Internet Connect: ", fg='white', bg='black') \
          +colors.bold(internetConnect, fg='green', bg='black') \
          +colors.color(44*frame, bg='black') \
          +colors.bold("Alarms Syncy: ", fg='white', bg='black') \
          +colors.bold(alarmSyncy, fg='green', bg='black') \
          +colors.color(44*frame, bg='black') \
          +colors.bold(" Important Messages: ", fg='white', bg='black') \
          +colors.bold(importMesg, fg='magenta', bg='black') \
          +colors.color(4*frame, bg='black')
  print ""
  messages = db.smembers('message')
  if messages:
    for message in messages:
      print colors.bold(">_ ", fg='red') + colors.blink2(message, fg='green')
  print ""

def region_list(db):
  frame = ' '
  liston = db.smembers('liston')
  listoff = db.smembers('listoff')
  total = len(liston) + len(listoff)
  print colors.bold(" TODO List ", fg='white', bg='black') \
          +colors.color(54*frame, bg='black') \
          +colors.bold("Total: ", fg='white', bg='black') \
          +colors.bold(str(total), fg='magenta', bg='black') \
          +colors.color(53*frame, bg='black') \
          +colors.bold("Start: ", fg='white', bg='black') \
          +colors.bold(str(len(liston)), fg='magenta', bg='black') \
          +colors.color(17*frame, bg='black')
  print ""

def region_job_off(db, fb):
  frame = ' '
  alarm = None
  litetime = None
  nowday = time.strftime('%Y-%m-%d', time.localtime(time.time()))
  nowtime = time.time()
  jobs = db.smembers('listoff')
  for job in jobs:
    if job:
      jobinfo  = job.split('|')
      name     = str(jobinfo[0])
      start    = str(jobinfo[1])
      length   = str(jobinfo[2])
      progress = int(jobinfo[3])
      spend    = int(jobinfo[4])
      print colors.bold(" 事件: ", fg='red', bg='black')+colors.bold(name, fg='magenta', bg='black') \
              +colors.color((144-len(name))*frame, bg='black')
      print colors.bold(" 预定开始于: ", fg='green')+colors.bold(start, fg='magenta')\
              +45*frame\
              +colors.bold(" 预定时长: ", fg='green')+colors.bold(length, fg='magenta')\
              +50*frame \
              +colors.bold(" 状态: ", fg='green')+colors.bold('off', fg='magenta')
      print ""
      print colors.bold(" 进行时长: ")+colors.color(spend*frame, bg='green') + colors.bold(' '+str(spend)+'小时')
      print colors.bold(" 进行进度: ")+colors.color(progress*frame, bg='red') + colors.bold(' '+str(progress)+'%')
      print ""
      alarmtime = time.mktime(time.strptime(nowday+' '+start+':00', '%Y-%m-%d %H:%M:%S'))
      if alarmtime > nowtime:
        litetimetmp = alarmtime - nowtime
        if litetime is None or litetimetmp < litetime:
          litetime = litetimetmp
          alarm = start
      else:
        db.sadd('liston', job)
        db.srem('listoff', job)
  if alarm is not None:
    fitbit.updateAlarm(fb, alarm)


def region_job_on(db):
  frame = ' '
  nowtime = time.time()
  nowday = time.strftime('%Y-%m-%d', time.localtime(time.time()))
  jobs = db.smembers('liston')
  for job in jobs:
    if job:
      jobinfo  = job.split('|')
      name     = str(jobinfo[0])
      start    = str(jobinfo[1])
      length   = str(jobinfo[2])
      progress = int(jobinfo[3])
      spend    = int(jobinfo[4])
      alarmtime = time.mktime(time.strptime(nowday+' '+start+':00', '%Y-%m-%d %H:%M:%S'))
      spend = int((nowtime - alarmtime)/60/60)
      print colors.bold(" 事件: ", fg='red', bg='black')+colors.bold(name, fg='magenta', bg='black') \
              +colors.color((144-len(name))*frame, bg='black')
      print colors.bold(" 预定开始于: ", fg='green')+colors.bold(start, fg='magenta')\
              +45*frame\
              +colors.bold(" 预定时长: ", fg='green')+colors.bold(length, fg='magenta')\
              +50*frame \
              +colors.bold(" 状态: ", fg='green')+colors.bold('on', fg='magenta')
      print ""
      print colors.bold(" 进行时长: ")+colors.color(spend*frame, bg='green') + colors.bold(' '+str(spend)+'小时')
      print colors.bold(" 进行进度: ")+colors.color(progress*frame, bg='magenta') + colors.bold(' '+str(progress)+'%')
      print ""


def region_fitbit(fb):
  frame = ' '
  print colors.bold(" 个人数据 ", fg='white', bg='black')+colors.color(142*frame, bg='black')
  print ""
  fitbit.showsteps(fb)
  print ""

def region_tips(db):
  tips = db.smembers('tips')
  frame = ' '
  print colors.bold(" Tips ", fg='black', bg='green')+colors.color(146*frame, bg='green')
  print ""
  for tip in tips:
    print colors.bold("-- ", fg='red') + colors.blink2(tip, fg='green')


def layout_loop(db, fb):
  run = True
  while run:
    clear_term()
    region_message(db)
    region_list(db)
    region_job_on(db)
    region_job_off(db, fb)
    region_fitbit(fb)
    region_tips(db)
    time.sleep(360)

if __name__ == '__main__':
  db = layout_init()
  fb = fitbit_init()
  layout_loop(db, fb)
