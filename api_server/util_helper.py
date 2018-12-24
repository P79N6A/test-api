# encoding=utf-8
import json
import exceptions

def args_check(args, must_have_args):
    for arg in must_have_args:
        if arg not in args:
            raise exceptions.GeneralAPIException(u"参数%s是必选参数" % arg, "001")

def get_call_sys_ip_and_args(request):
    ip = request.META.get("HTTP_X_FORWARDED_FOR")
    if not ip :
        ip = request.META.get("REMOTE_ADDR")
    return ip,load_args(request)


def load_args(request):
    rt = {}
    if request.method == "GET" :
        if request.GET :
            tmp = dict(request.GET)
            for k in  tmp : rt[k] = tmp[k][0] if len(tmp[k]) == 1 else tmp[k]
    else :
        if request.body:
            if '{' in request.body or '[' in request.body :
                rt = json.loads(request.body)
            else :
                tmp = dict(request.POST)
                for k in  tmp : rt[k] = tmp[k][0] if len(tmp[k]) == 1 else tmp[k]
    return rt


def logger_helper(call_sys_ip,args,elapsed_time,is_success=True, code=None):
    return {
        "call_sys_ip":call_sys_ip,
        "call_args":args,
        "elapsed_time":elapsed_time,
        "is_success":is_success,
        "code":code
    }