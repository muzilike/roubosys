#!/usr/bin/env python
# encoding: utf-8

import string
import paho.mqtt.client as mqtt
from fitbit_alarms import fitbitAlarms

class fitbitNotify:
  topic = "roubosys/fitbit/alarm/set"
  hosts = "127.0.0.1"
  ports = 1883
  masks = 60

  # This callback for when the client recevice a CONNECTACK response from the server
  def on_connect(self, client, userdata, flags, resultcode):
    client.subscribe(self.topic)

  # This callback for when the client recevice a PUSLISH message from the server
  def on_message(self, client, userdata, msg):
    try:
      print(msg.topic + " " + str(msg.payload))
      alarm = fitbitAlarms()
      if msg.topic == "roubosys/fitbit/alarm/set":
        payload = string.split(msg.payload, '|')
        msg   = payload[1]
        time  = payload[0]
        other = payload[2]
        msg   = msg +'|'+ other
        alarm.updatealarm(msg, time, other)
    except KeyError:
      pass

  def loop_forever(self):
    client = mqtt.Client()
    client.on_connect = self.on_connect
    client.on_message = self.on_message
    client.connect(self.hosts, self.ports, self.masks)
    client.loop_forever()
