#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar 14 09:56:01 2022

@author: rodipardo
"""

from urllib2 import Request, urlopen

headers = {
  'Authorization': '\'pk_42925926_EUD2LG82I42N1PE3GHSTBMVXAKOOUD3Y\''
}
request = Request('https://api.clickup.com/api/v2/team/123/space', headers=headers)

response_body = urlopen(request).read()
print(response_body)