#!/usr/bin/python3
from DouyuSpider import *
str1 = "https://rpic.douyucdn.cn/asrpic/180724/699689_1556.jpg"
str_a = str1.split('asrpic/')
str_b = str_a[1].split("/")[1].split('_')
room_number = str_b[0]
# print(room_number)
number = get_followers(str1)
print(number)



