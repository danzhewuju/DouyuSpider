#!/usr/bin/python3
import json
from bs4 import BeautifulSoup
import re
import requests
import time
import datetime


def open_html(url):
    r = requests.get(url)
    r.encoding = 'utf-8'
    return r.text


def get_page(url):
    html = open_html(url)
    json1 = json.loads(html)
    print(json1)


def get_info():
    a = 1   #每一个类型的直播间 比如：王者荣耀
    b = 1   #每个直播间的分类
    pages= 0
    sum = 600 #设置最多的直播间数量
    while a < sum :
        b = 1
        url = "https://www.douyu.com/gapi/rkc/directory/2_"+str(a)+"/"+str(b)
        html = open_html(url)
        rid =""
        username =""
        w_watching =""
        kind = ""
        json_a = json.loads(html)
        pages = json_a['data']['pgcnt']
        while b <= pages:
            url = "https://www.douyu.com/gapi/rkc/directory/2_" + str(a) + "/" + str(b)  # 更新链接
            html = open_html(url)
            json_a = json.loads(html)
            for data in json_a['data']['rl']:
                rid = data['rid']
                username = data['nn']
                w_watching = data['ol']
                kind = data['c2name']
                print(rid, "\t", username, "\t", w_watching, "\t", kind)
            print(b, pages)
            b += 1
        b = 1
        a += 1


# get_info()
if __name__ == '__main__':
   a = {"yuhao":1}
   print(a["yuhao"])
   a["lijian"] = 2
   print(a)
   if "1" in a:
       print("TRUE")



