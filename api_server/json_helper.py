import json
import datetime
import decimal
import uuid
from django.http import HttpResponse
import httplib
SUPPORTED_TYPES = {datetime.datetime, datetime.date, datetime.time, decimal.Decimal, uuid.UUID, set}


class CustomJSONEncoder(json.JSONEncoder):
    def default(self, obj):
        type_ = type(obj)
        if type_ in SUPPORTED_TYPES:
            if issubclass(type_, (datetime.datetime, datetime.date, datetime.time)):
                return {'__type__': type_.__name__, '__value__': obj.isoformat()}
            if issubclass(type_, decimal.Decimal):
                return {'__type__': type_.__name__, '__value__': obj.as_tuple()}
            if issubclass(type_, uuid.UUID):
                return {'__type__': type_.__name__, '__value__': obj.hex}
            if issubclass(type_, set):
                return list(obj)
        return json.JSONEncoder.default(self, obj)


def dumps(data):
    return json.dumps(data, cls=CustomJSONEncoder, sort_keys=True, indent=4, separators=(',', ': '))

def loads(data):
    return json.loads(data)

def json_response(response_data,request=None,is_deumped=False, status=httplib.OK):
    content = response_data if is_deumped else dumps(response_data)
    if request :
        callback = request.GET.get('callback')
        if callback :
            content = '%s(%s)' % (callback, dumps(response_data))
    return HttpResponse(content,
                         content_type='application/json', status=status)
