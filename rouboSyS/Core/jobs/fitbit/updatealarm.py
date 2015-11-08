#!/usr/bin/env python
# encoding: utf-8

import fitbit_api.fitbit.api as fitbit
import ConfigParser
from time import time, localtime, strftime
import sys
def updateAlarm(settime):
  parser              = ConfigParser.SafeConfigParser()
  parser.read('config.ini')
  consumer_key        = parser.get('login', 'C_KEY')
  consumer_secret     = parser.get('login', 'C_SECRET')
  user_key            = parser.get('login', 'U_KEY')
  user_secret         = parser.get('login', 'U_SECRET')
  device_id           = parser.get('login', 'DEV_ID')
  fitbit_auth_client  = fitbit.Fitbit(consumer_key, consumer_secret, resource_owner_key=user_key, resource_owner_secret=user_secret)
  fitbit_alarms       = fitbit_auth_client.get_alarms(device_id)
  update_alarm_id     = fitbit_alarms["trackerAlarms"][len(fitbit_alarms["trackerAlarms"])-1]["alarmId"]
  alarms_week         = [strftime("%A", localtime(time())).upper()]
  alarms_time         = settime + '+08:00'
  alarms_snoozeLength = 9
  alarms_snoozeCount  = 1
  fitbit_auth_client.update_alarm(device_id, update_alarm_id, alarms_time, alarms_week, recurring=True, enabled=True, label=None, snooze_length=alarms_snoozeLength, snooze_count=alarms_snoozeCount, vibe='DEFAULT')

if __name__ == '__main__':
  if len(sys.argv) > 1:
    settime = sys.argv[1]
  else:
    sys.exit()
  updateAlarm(settime)
