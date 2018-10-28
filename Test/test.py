# -*- coding: utf-8 -*-
from api_request import *

from config import get_keys, get_pid




def demo_test():
    public_key, secret_key = get_keys()
    project_id = get_pid()

    params = {


    'Action': 'DescribeUHostInstance',
    'Region': 'cn-bj2',
    'Zone': 'cn-bj2-04',


    }

    res = ApiClient.get_result(params)
    print(res)



if __name__ == '__main__':
    demo_test()