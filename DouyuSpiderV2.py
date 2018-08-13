#!/usr/bin/python3
from bs4 import BeautifulSoup
import re
import requests
from Host_info import *
from UnitMysql import *
import time
import json


def open_html(url):
    r = requests.get(url)
    r.encoding = 'utf-8'
    return r.text


def get_online_number(room_number):       #获取斗鱼的实际在线人数
    url = "https://www.douyu.com/swf_api/h5room/" + room_number
    html = open_html(url)
    try:
        json_a = json.loads(html)
        online_number = 0
        online_number = int(json_a['data']['online'])
    except:
        online_number = 0
    finally:
        return online_number


def caculate_rate(w_watching, online):  #计算影响因子
    result = 0.0
    if online == 0:
        return result
    else:
        result = w_watching / online
    return result


def get_info():
    a = 1   #每一个类型的直播间 比如：王者荣耀
    b = 1   #每个直播间的分类
    pages= 0
    count = 0
    save_a = 0
    sum = 600 #设置最多的直播间数量
    while a < sum :
        b = 1
        url = "https://www.douyu.com/gapi/rkc/directory/2_"+str(a)+"/"+str(b)
        html = open_html(url)
        counta = 1
        countb = 1
        rid =""
        username =""
        w_watching =""
        kind = ""
        online = 0

        rid = ""
        json_a = json.loads(html)
        pages = json_a['data']['pgcnt']
        while b <= pages:
            url = "https://www.douyu.com/gapi/rkc/directory/2_" + str(a) + "/" + str(b)  # 更新链接
            html = open_html(url)
            json_a = json.loads(html)
            for data in json_a['data']['rl']:
                rid = str(data['rid'])
                username = data['nn']
                w_watching = data['ol']
                kind = data['c2name']
                online = get_online_number(rid)
                coefficient = caculate_rate(w_watching, online)
                link = "https://www.douyu.com/" + rid
                datetime1 = time.strftime("%Y-%m-%d %H:%M:%S")
                host = Host()

                host.username = username
                host.online = online
                host.w_number = w_watching
                host.kind = kind
                host.room_number = rid
                host.coefficient = coefficient
                host.link = link
                host.localtime =datetime1
                unit = Unit_Mysql()
                unit.insert_db(host)
                count += 1
                print("正在抓取第%d条数据，%s（%s:第%d/%d页）" % (count, username, kind, b, pages))
            b += 1
        b = 1
        if pages != 0:
            save_a = a
        a += 1
    print(save_a)


get_info()
