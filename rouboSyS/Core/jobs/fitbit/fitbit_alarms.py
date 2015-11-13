#!/usr/bin/env python
# encoding: utf-8

import sys
import redis
import ConfigParser
import fitbit_api.fitbit.api as fitbit
import fitbit_api.fitbit.exceptions as fbexceptions
from time import time, localtime, strftime
import requests.exceptions as rqexceptions

class fitbitAlarms:

  def initdb(self):
    parser  = ConfigParser.SafeConfigParser()
    parser.read('configdb.ini')
    db_host  = str(parser.get('db', 'DB_HOST'))
    db_port  = str(parser.get('db', 'DB_PORT'))
    db_index = str(parser.get('db', 'DB_INDEX'))
    ftdb = redis.StrictRedis(host=db_host, port=db_port, db=db_index)
    return ftdb

  def updatealarmslistdb(self, alarmid, time, msg):
    fitbitdb = self.initdb()
    try:
      fitbitdb.set(alarmid, time+'|'+msg)
    except KeyError:
      return

  def getalarmslist(self):
    alarmslist = {}
    fitbitdb = self.initdb()
    for key in fitbitdb.keys('*'):
      alarmslist[key] = fitbitdb.get(key)
    return alarmslist

  def initfitbit(self):
    parser             = ConfigParser.SafeConfigParser()
    parser.read('config.ini')
    consumer_key       = parser.get('login', 'C_KEY')
    consumer_secret    = parser.get('login', 'C_SECRET')
    user_key           = parser.get('login', 'U_KEY')
    user_secret        = parser.get('login', 'U_SECRET')
    fitbit_auth_client = fitbit.Fitbit(consumer_key, consumer_secret, resource_owner_key=user_key, resource_owner_secret=user_secret)
    return fitbit_auth_client

  def updatealarm(self, msg, settime, other):
    try:
      fitbit_auth_client = self.initfitbit()
      parser              = ConfigParser.SafeConfigParser()
      parser.read('config.ini')
      device_id           = parser.get('login', 'DEV_ID')
      fitbit_alarms       = fitbit_auth_client.get_alarms(device_id)
      trackeralarms       = fitbit_alarms["trackerAlarms"]
      alarmid = ""
      for trackeralarm in trackeralarms:
        alarmid = trackeralarm["alarmId"]
        fitbitdb = self.initdb()
        if fitbitdb.get(alarmid) is None:
          break
      if alarmid == "":
        print "alarm set full"
        return
      alarms_week         = [strftime("%A", localtime(time())).upper()]
      alarms_time         = settime + '+08:00'
      fitbit_auth_client.update_alarm(device_id, alarmid, alarms_time, alarms_week, recurring=True, enabled=True, label=None, snooze_length=9, snooze_count=1, vibe='DEFAULT')
    except fbexceptions.HTTPServerError:
      print "ssl error"
      return
    except rqexceptions.ConnectionError:
      print "connect error"
      return
    self.updatealarmslistdb(alarmid, settime, msg)

  def disablealarm(self, alarm_id):
    try:
      fitbitdb = self.initdb()
      fitbitdb.delete(alarm_id)
      fitbit_auth_client = self.initfitbit()
      parser              = ConfigParser.SafeConfigParser()
      parser.read('config.ini')
      device_id           = parser.get('login', 'DEV_ID')
      fitbit_alarms       = fitbit_auth_client.get_alarms(device_id)
      trackeralarms       = fitbit_alarms["trackerAlarms"]
      for trackeralarm in trackeralarms:
        if alarm_id == trackeralarm["alarmId"]:
          alarms_week     = trackeralarm["weekDays"]
          alarms_time     = trackeralarm["time"]
          fitbit_auth_client.update_alarm(device_id, alarm_id, alarms_time, alarms_week, recurring=False, enabled=False, label=None, snooze_length=9, snooze_count=1, vibe='DEFAULT')
    except fbexceptions.HTTPServerError:
      print "ssl error"
      return
    except rqexceptions.ConnectionError:
      print "connect error"
      return
    except KeyError:
      return

if __name__ == '__main__':
  settime = sys.argv[1]
  msg = sys.argv[2]
  alarm = fitbitAlarms()
  alarm.updatealarm(msg, settime, "dd")
  #alarm.disablealarm(settime)
