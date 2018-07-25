#!/usr/bin/python3
import json
from DouyuSpider import *
str1 = "https://rpic.douyucdn.cn/asrpic/180724/699689_1556.jpg"
str_a = str1.split('asrpic/')
str_b = str_a[1].split("/")[1].split('_')
room_number = str_b[0]
print(room_number)


def get_room_number(room_number):
    url = "https://www.douyu.com/" + room_number
    html = open_html(url)
    soul = BeautifulSoup(html, 'lxml')
    total = soul.find_all('p', class_='r-num fl')
    print(total)





room_number = "1811143"
print(get_online_number(room_number))

# print(str1['online'])