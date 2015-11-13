#!/usr/bin/env python
# encoding: utf-8

import string
import time
from fitbit_alarms import fitbitAlarms
from fitbit_bearychat import fitbitBearyChat

class rFitbit:

  idle_time = 60
  #def showsteps(self, fitbit_auth_client):
  #  fitbit_stats       = fitbit_auth_client._COLLECTION_RESOURCE('activities')
  #  goals_steps        = fitbit_stats["goals"]["steps"]
  #  now_steps          = fitbit_stats["summary"]["steps"]
  #  now_per            = now_steps*100/goals_steps
  #  block              = ' '
  #  goals_steps_bar    = (goals_steps/100) * block
  #  now_steps_bar      = (now_steps/100) * block
  #  print colors.bold("目标步数: ")+colors.color(goals_steps_bar, bg='magenta')
  #  if now_per < 80:
  #    print colors.bold("今日达成: ")+colors.color(now_steps_bar, bg='red') + colors.bold(' '+str(now_per)+'%')
  #  else:
  #    print colors.bold("今日达成: ")+colors.color(now_steps_bar, bg='green') + colors.bold(' '+str(now_per)+'%')

  def loop_forever(self):
    while True:
      nowtime = time.localtime(time.time())
      alarm = fitbitAlarms()
      lists = alarm.getalarmslist()
      if lists is not None:
        for key in lists.keys():
          v = string.split(lists[key], '|')
          alarm_time = str(nowtime.tm_year)+str(nowtime.tm_mon)+str(nowtime.tm_mday)+v[0]+":"+str(nowtime.tm_sec)
          timedata = time.strptime(alarm_time, "%Y%m%d%H:%M:%S")
          timeStamp = int(time.mktime(timedata))
          nowStamp = int(time.mktime(nowtime))
          if nowStamp >= timeStamp and v[2] != "tomorrow":
            fbbearychat = fitbitBearyChat()
            fbbearychat.pushchat(v[1], None)
            print "alarm"
            alarm.disablealarm(key)
      return
      time.sleep(self.idle_time)


if __name__ == '__main__':
  Fitbit = rFitbit()
  Fitbit.loop_forever()
