# -*- coding: UTF-8 -*-
import urllib2
from cons import station_names
from json import loads
from seat import seat_names

city = {}
for i in station_names.split('@'):
    if not i:
        continue
    # print i.split('|')[2] #list
    city[i.split('|')[1]] = i.split('|')[2]
print u'出发日期' # 日期格式 2018-09-03
train_date = raw_input()
print type(train_date)


# train_date = '2018-09-03'
# print type(train_date)

print u'出发城市：'
m = raw_input()
from_station = city[m]
print u'到达城市:'
n = raw_input()
to_station = city[n]

def getList():
    req = urllib2.Request('https://kyfw.12306.cn/otn/leftTicket/query?leftTicketDTO.train_date=%s&leftTicketDTO.from_station=%s&leftTicketDTO.to_station=%s&purpose_codes=ADULT'%(train_date,from_station,to_station))#构造请求对象
    html = urllib2.urlopen(req).read()#打开请求对象并且获取html源代码
    dict = loads(html)
    return dict['data']['result']

# 3 = 车次
# 30 = 二等座
# 32 = 特等座
# 31 = 一等座
seat = {}
for i in seat_names.split('@'):
    if not i:
        continue
    # print i.split('|')[1] #list
    seat[i.split('|')[0]] = i.split('|')[1]


print u'座位类型：'
b = raw_input()
c = int(seat[b])

for result in getList():
    a = result.split('|')
    if a[c] == u'无' or not a[c]:
        continue
    print u'有票，车次：%s'%a[3]