# coding=utf-8
"""
微信发送接口，详见：http://alarm.weixin.oa.com/itilalarmweb/interface?page=text
"""

import json
import urllib
import urllib2


WEIXIN_SENDER = 'cloud_monitor_alarm'

def do_send_weixin(content, receivers):
    """

    :param receivers: list类型 微信接收人
    :param content: string 发送的微信内容
    :return: {"msgid": 152593839415313, "errCode": "0", "rcptCheck": {"daxwang": "FINE"}, "errMsg": u"成功加入到消息队列"}
    """
    url = 'http://api.weixin.oa.com/itilalarmcgi/sendmsg'
    data = {
        'Sender':WEIXIN_SENDER,
        'Rcptto':receivers,
        'isText':content
    }
    json_data = json.dumps(data)
    values = urllib.urlencode({"data":json_data})
    return json.loads(urllib2.urlopen(url, values).read())


if __name__ == '__main__':
    content = '【storm健康检查】\n' \
              '大区：test\n' \
              '值：100'
    result = do_send_weixin(content, ['daxwang'])
    print result