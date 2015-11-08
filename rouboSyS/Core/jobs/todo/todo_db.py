#!/usr/bin/env python
# encoding: utf-8

todo_db={}
todo_db['host']='127.0.0.1'
todo_db['port']='6379'

# DB index 0
# key: todo_id    value: name|status|start|length|progress|spend
# key: "todo_ctl" value: ctl option
todo_db['lists'] = 0
