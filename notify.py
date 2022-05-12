from urllib import request, parse

data = parse.urlencode({'key': 'kU78dy', 'title': 'Alert', 'msg': 'Your patient needs to be attended to', 'event': 'event'}).encode()
req = request.Request("https://api.simplepush.io/send", data=data)
request.urlopen(req)