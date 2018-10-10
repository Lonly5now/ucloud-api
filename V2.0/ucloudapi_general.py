# -*- coding: utf-8 -*-
# !/usr/bin/env python

import hashlib
import json

import requests

url = 'http://api.ucloud.cn'
PublicKey = ''
PrivateKey = ''
ProjectId = ''

'''Your API params'''

api_params = {
    'Action': 'DescribeUHostInstance',
    'Region': 'cn-bj2',
    'Zone': 'cn-bj2-04',
}


''' Get the result of API request '''

def get_ucloud_api_result(params):
    global PublicKey, ProjectId, url
    params["PublicKey"] = PublicKey
    params["Signature"] = verfy_ac(params)

    if ProjectId != '':
        params["ProjectId"] = ProjectId

    r = requests.post(url, params)
    response = json.dumps(r.json(), indent=4)

    return response



''' Signature Generation '''

def verfy_ac(params):
    global PrivateKey
    params_data = ""
    
    items = params.items()
    items = sorted(items)

    for key, value in items:
        params_data = params_data + str(key) + str(value)
    
    params_data = params_data + PrivateKey
    sign = hashlib.sha1()
    sign.update(params_data.encode('utf8'))
    signature = sign.hexdigest()
    
    return signature


print(get_ucloud_api_result(api_params))