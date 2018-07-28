#!/usr/bin/python3
from bs4 import BeautifulSoup
import re
import requests
from Host_info import *
from UnitMysql import *
import time
import json


def trans_string(str1):   #将主播的人数转化为整数型
    number = 0
    if str1.__contains__("万"):
        str2 = str1[-2::-1]
        number = float(str2[::-1]) * 10000
    else:
        number = int(str1)
    return number


def get_followers(str_1):  #通过连接获得直播连接获取关注数 https://rpic.douyucdn.cn/asrpic/180725/288016_0707.jpg
    str_a = str_1.split('asrpic/')
    str_b = str_a[1].split("/")[1].split('_')
    room_number = str_b[0]
    link = "https://www.douyu.com/"+room_number
    html = open_html(link)
    soup = BeautifulSoup(html, 'lxml')
    total = soup.find_all('p', class_='r-num fl')
    # print(total)
    if total.__len__() == 0:  #斗鱼的赛事直播间不是以直播间的+直播间号码的形式
        number = -100
    else:
        number = int(total.get_text())
    return number   #斗鱼的关注是以图片的形式展示来，展示不用处理


def get_online_number(room_number):       #获取斗鱼的实际在线人数
    url = "https://www.douyu.com/swf_api/h5room/" + room_number
    html = open_html(url)
    json_a = json.loads(html)
    online_number = 0
    try:
        online_number = int(json_a['data']['online'])
    except:
        online_number = 0
    finally:
        return online_number


def getroom_number(str_1):
    str_a = str_1.split('asrpic/')
    str_b = str_a[1].split("/")[1].split('_')
    room_number = str_b[0]
    return int(room_number)


def open_html(url):
    r = requests.get(url)
    r.encoding = 'utf-8'
    return r.text


def get_more_link(url):
    html = open_html(url)
    soup = BeautifulSoup(html, 'lxml')
    total = soup.find_all('a', class_='thumb')
    return total


def get_links_bak(url):                   #获取被折叠的全部来连接
    kindurl = []
    links = []
    stra = "https://www.douyu.com"
    html = open_html(url)
    soup = BeautifulSoup(html, 'lxml')
    total = soup.find_all('ul', class_='clearfix')
    total = total[:7]                    #获取斗鱼的7大模块
    for x in total:
        linka = x.find('a', class_='more')
        if linka is not None:
            href = "https://www.douyu.com/" + linka['href']
            links.append(get_more_link(href))
        else:
            links.append(x.find_all('a'))

    for index in range(links.__len__()):
        for soul in links[index]:
            strb = stra + soul['href']
            kindurl.append(strb)
    return links, kindurl


def getlinks(url):
    html = open_html(url)
    soup = BeautifulSoup(html, 'lxml')
    total = soup.find_all('ul', class_='clearfix')
    total = total[:7]
    stra = "https://www.douyu.com"
    kindurl = []                     #每一个类别的直接连接地址
    links = []                       #每一个大类的详细信息
    for t in total:
        links.append(t.find_all('a'))
    for index in range(links.__len__()):
        for soul in links[index]:
            strb = stra + soul['href']
            kindurl.append(strb)
    return links, kindurl


def caculate_rate(w_watching, online):  #计算影响因子
    result = 0.0
    if online == 0:
        return result
    else:
        result = w_watching / online
    return result


def get_info(): #或取每一个模块的连接地址以及相关大类的信息
    url = "https://www.douyu.com/directory/all/"
    links, kindurl = get_links_bak(url)
    count = 0
    for dirlink in kindurl:
        html = open_html(dirlink)
        soup = BeautifulSoup(html, 'lxml')
        total = soup.find_all('a', class_='play-list-link')
        for x1 in total:
            # print(x1)
            kind = x1.find(class_='tag ellipsis').get_text()
            username = x1.find(class_='dy-name ellipsis fl').get_text()
            room_number = x1['data-rid']
            number = 0
            link = "https://www.douyu.com/" + room_number
            online = get_online_number(room_number)
            try:
                str1 = x1.find(class_='dy-num fr').get_text()       #部分连接没有number关键字，（无效连接）跳过
            except :
                break
            finally:
                number = trans_string(str1)
                coefficient = caculate_rate(number, online)
                host_a = Host()
                host_a.username = username
                host_a.kind = kind
                host_a.w_number = number
                host_a.room_number = room_number
                host_a.link = link
                host_a.online = online
                host_a.coefficient = coefficient
                datetime1 = time.strftime("%Y-%m-%d %H:%M:%S")
                host_a.localtime = str(datetime1)
                unit = Unit_Mysql()
                unit.insert_db(host_a)
                count += 1
                print(count, ":抓取了直播间:", username, "的信息！")
    print("本次总共抓取了:", count, "信息！")


def get_class_count():                            #获取当前有多少类的直播间   这个取决于是否开播
    links = []
    url = "https://www.douyu.com/directory/all/"
    html = open_html(url)
    soup = BeautifulSoup(html, 'lxml')
    total = soup.find_all('ul', class_='clearfix')
    total = total[:7]
    count = 0
    for x in total:
        linka = x.find('a', class_='more')
        if linka is not None:
            href = "https://www.douyu.com/" + linka['href']
            links.append(get_more_link(href))
        else:
            links.append(x.find_all('a'))
    for x in links:
        count += x.__len__()
    return count


print(get_class_count())












