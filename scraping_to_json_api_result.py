import requests
#json_data = requests.get('http://www.floatrates.com/daily/idr.json')

json_data = {"usd":{"code":"USD","alphaCode":"USD","numericCode":"840","name":"U.S. Dollar","rate":6.8513582588277e-5,"date":"Sat, 29 Aug 2020 00:00:02 GMT","inverseRate":14595.646034296},"eur":{"code":"EUR","alphaCode":"EUR","numericCode":"978","name":"Euro","rate":5.7560197173869e-5,"date":"Sat, 29 Aug 2020 00:00:02 GMT","inverseRate":17373.116304299}}
for data in json_data.values():
    print(data['code'])
    print(data['name'])
    print(data['date'])
    print(data['inverseRate'])