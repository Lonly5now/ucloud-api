# -*- coding: utf-8 -*-
import hashlib
import json

import requests

from config import *


DEFAULT_API_SERVER = 'http://api.ucloud.cn'

public_key, secret_key = get_keys()
ProjectId = get_pid()


class ApiClient(object):
    api_server = DEFAULT_API_SERVER

    def __init__(self, public_key, secret_key):
        if not public_key or not secret_key:
            raise Exception('No public key or secret key provided')

        self._g_params = {}
        self._g_params['PublicKey'] = public_key
        self._secret_key = secret_key

    def get_result(params):
        """ Get the result of API request
        """
        global public_key, ProjectId, API_SERVER
        params["PublicKey"] = public_key
        params["Signature"] = generate_sign(params)

        if ProjectId != '':
            params["ProjectId"] = project_id

        r = requests.post(api_server, params)
        response = json.dumps(r.json(), indent=4)

        return response


def generate_sign(params):
    """ Signature Generation
    """
    global secret_key
    params_data = ""

    items = params.items()
    items = sorted(items)

    for key, value in items:
        params_data = params_data + str(key) + str(value)

        params_data = params_data + secret_key
        sign = hashlib.sha1()
        sign.update(params_data.encode('utf8'))
        signature = sign.hexdigest()

        return signature
