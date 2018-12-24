# command api for weixin

## implement a weinxin command
* step 1: register a command in http://alarm.weixin.oa.com/itilalarmweb/tutorial?page=command
* step 2: register your url in url.py. like this:
```
    url(r'^test', 'api_server.views.test'),
```
* setp 3: implement your weixin command logic in views.py. like this:
```
    def test(request):
        send_weixin(u'测试微信指令, 我很帅，对不对？', ['daxwang'])
        ip, args = get_call_sys_ip_and_args(request)
        return json_response(
            {'result': True,
             'data': args,
             'message': '',
             'code':'00'})
```
* step 4: restart command-api.

