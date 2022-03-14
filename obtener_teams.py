#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar 14 09:57:51 2022

@author: rodipardo
"""
from urllib2 import Request, urlopen

headers = {
  'Authorization': '\'pk_42925926_BE412JQ82B2VHZ2A3LWKEGECAM2MJ4Q3\''
}
request = Request('https://api.clickup.com/api/v2/team', headers=headers)

response_body = urlopen(request).read()
print(response_body)