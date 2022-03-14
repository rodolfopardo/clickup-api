# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
#Importando librerias
from urllib2 import Request, urlopen

#Headers
headers = {
  'Authorization': '\'pk_42925926_EUD2LG82I42N1PE3GHSTBMVXAKOOUD3Y\''
}
request = Request('https://api.clickup.com/api/v2/user', headers=headers)

#Imprimiendo resultados 
response_body = urlopen(request).read()
print(response_body)