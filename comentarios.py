#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar 14 09:49:35 2022

@author: rodipardo
"""



from urllib2 import Request, urlopen

request = Request('https://api.clickup.com/api/v2/task/IDTASK/comment/')

response_body = urlopen(request).read()
print response_body