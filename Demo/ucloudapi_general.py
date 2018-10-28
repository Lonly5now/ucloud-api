# -*- coding: utf-8 -*-
# !/usr/bin/env python

import hashlib
import json

import requests

from config import *


def get_result(params):
    """Get the result of API request
    """
    global PublicKey, ProjectId, url
    params["PublicKey"] = PublicKey
    params["Signature"] = verfy_ac(params)

    if ProjectId != '':
        params["ProjectId"] = ProjectId

    r = requests.post(url, params)
    response = json.dumps(r.json(), indent=4)

    return response


def verfy_ac(params):
    """Signature Generation
    """
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
    print(get_result(api_params))
