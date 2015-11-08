#!/usr/bin/env python
# encoding: utf-8

import redis
from todo_db import todo_db
import sys

def tododb_init():
  tododb = redis.StrictRedis(host=todo_db['host'], port=todo_db['port'], db=todo_db['lists'])
  return tododb

def todo_add_message(tododb, message, ttl):
  tododb.sadd('message', message)
  if ttl is None:
    ttl = 10*60
  tododb.expire('message', ttl)

def todo_add_tips(tododb, tip):
  tododb.sadd('tips', tip)

def todo_add_list(tododb, info):
  tododb.sadd('listoff', info+'|0|0')

if __name__ == '__main__':
  cmd    = sys.argv[1]
  info   = sys.argv[2]
  tododb = tododb_init()
  if cmd == 'message':
    todo_add_message(tododb, info, None)
  elif cmd == 'tips':
    todo_add_tips(tododb, info)
  elif cmd == 'list':
    todo_add_list(tododb, info)
  sys.exit(0)
