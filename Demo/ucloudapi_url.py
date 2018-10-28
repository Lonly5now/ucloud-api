# -*- coding: utf-8 -*-
# !/usr/bin/env python

import hashlib

import requests

from config import *




def get_result(params):
    """Get the result of API request
    """
    global PublicKey, ProjectId, url
    params["PublicKey"] = PublicKey
    str_url = ''

    if ProjectId != '':
        params["ProjectId"] = ProjectId
    params["Signature"] = verfy_ac(params)

    for key, value in params.items():
        str_url += key + '=' + value + '&'

    r = requests.post(url)
    url = url + '/?' + str_url.strip('&')

    print("http status code:", r.status_code)
    print("your url of api request:\n", url)


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


if __name__ == '__main__':
    get_result(api_params)
