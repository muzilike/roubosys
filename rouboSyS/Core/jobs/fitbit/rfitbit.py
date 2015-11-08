#!/usr/bin/env python
# encoding: utf-8

import fitbit_api.fitbit.api as fitbit
import ConfigParser
import colors
from time import time, localtime, strftime
def showsteps(fitbit_auth_client):
  fitbit_stats       = fitbit_auth_client._COLLECTION_RESOURCE('activities')
  goals_steps        = fitbit_stats["goals"]["steps"]
  now_steps          = fitbit_stats["summary"]["steps"]
  now_per            = now_steps*100/goals_steps
  block              = ' '
  goals_steps_bar    = (goals_steps/100) * block
  now_steps_bar      = (now_steps/100) * block
  print colors.bold("目标步数: ")+colors.color(goals_steps_bar, bg='magenta')
  if now_per < 80:
    print colors.bold("今日达成: ")+colors.color(now_steps_bar, bg='red') + colors.bold(' '+str(now_per)+'%')
  else:
    print colors.bold("今日达成: ")+colors.color(now_steps_bar, bg='green') + colors.bold(' '+str(now_per)+'%')

def initfitbit():
  parser             = ConfigParser.SafeConfigParser()
  parser.read('config.ini')
  consumer_key       = parser.get('login', 'C_KEY')
  consumer_secret    = parser.get('login', 'C_SECRET')
  user_key           = parser.get('login', 'U_KEY')
  user_secret        = parser.get('login', 'U_SECRET')
  fitbit_auth_client = fitbit.Fitbit(consumer_key, consumer_secret, resource_owner_key=user_key, resource_owner_secret=user_secret)
  return fitbit_auth_client

def updateAlarm(fitbit_auth_client, settime):
  parser              = ConfigParser.SafeConfigParser()
  parser.read('config.ini')
  device_id           = parser.get('login', 'DEV_ID')
  fitbit_alarms       = fitbit_auth_client.get_alarms(device_id)
  update_alarm_id     = fitbit_alarms["trackerAlarms"][len(fitbit_alarms["trackerAlarms"])-1]["alarmId"]
  alarms_week         = [strftime("%A", localtime(time())).upper()]
  alarms_time         = settime + '+08:00'
  print alarms_time
  alarms_snoozeLength = 9
  alarms_snoozeCount  = 1
  fitbit_auth_client.update_alarm(device_id, update_alarm_id, alarms_time, alarms_week, recurring=True, enabled=True, label=None, snooze_length=alarms_snoozeLength, snooze_count=alarms_snoozeCount, vibe='DEFAULT')
