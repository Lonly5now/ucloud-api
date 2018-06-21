# -*- coding: utf-8 -*-
# !/usr/bin/env python

import requests,hashlib
import json

url = 'http://api.ucloud.cn'
PublicKey = ''
PrivateKey = ''
ProjectId = ''

'''
获取API请求结果
'''
def get_ucloud_api_result(params):
    global PublicKey, ProjectId, url
    params["PublicKey"] = PublicKey
    if ProjectId != '':
        params["ProjectId"] = ProjectId
    params["Signature"] = verfy_ac(params)
    str_url = ''
    for key,value in params.items():
        str_url += key + '=' + value + '&'
    url = url+'/?'+str_url.strip('&')
    print(url)
    r = requests.post(url)
    return r.status_code

'''
生成密钥signature
'''
def verfy_ac(params):
    items = params.items()
    items = sorted(items)

    params_data = ""
    for key, value in items:
        params_data = params_data + str(key) + str(value)
    global PrivateKey
    params_data = params_data + PrivateKey

    sign = hashlib.sha1()
    sign.update(params_data.encode('utf8'))
    signature = sign.hexdigest()
    
    return signature

''' 
格式化输出response
line by line
'''
def format_response(response_content):
    str =''
    for i in range(len(response_content)):
        if (response_content[i] != ','):
            str+=(response_content[i])
        elif (response_content[i] ==','):
            str = ''
    return str


'''
测试begin
'''
api_params = {
    # 'Action': 'DescribeUHostInstance',
    # 'Region': 'cn-bj2',
    # 'Zone': 'cn-bj2-04',
}
print(get_ucloud_api_result(api_params))
