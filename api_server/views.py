# coding=utf-8

from util_helper import get_call_sys_ip_and_args
from json_helper import json_response


def health(request):
    ip, args = get_call_sys_ip_and_args(request)
    return json_response(
        {'result': True,
         'data': args,
         'message': '',
         'code':'00'})




