#!/usr/bin/python3
import json
from DouyuSpider import *


def get_room_number(room_number):
    url = "https://www.douyu.com/" + room_number
    html = open_html(url)
    soul = BeautifulSoup(html, 'lxml')
    total = soul.find_all('p', class_='r-num fl')
    print(total)


def get_right(room_number):
    url = "https://www.douyu.com/"+ room_number
    html = open_html(url)
    soup = BeautifulSoup(html, 'lxml')
    total = soup.find('span', class_='hot-v')
    print(total)


def get_more_link(url):
    html = open_html(url)
    soup = BeautifulSoup(html, 'lxml')
    total = soup.find_all('a', class_='thumb')
    return total


def get_links_bak(url):
    kindurl = []
    links = []
    stra = "https://www.douyu.com"
    html = open_html(url)
    soup = BeautifulSoup(html, 'lxml')
    total = soup.find_all('ul', class_='clearfix')
    total = total[:7]
    for x in total:
        linka = x.find('a', class_='more')
        if linka is not None:
            href = "https://www.douyu.com/" + linka['href']
            xlinks = get_more_link(href)
            for x in xlinks:
                str1 = x.find(class_='dy-num fr').get_text()
                if str1 is not None:
                    links.append(x)                            #去掉部分的link没有热度（多余的连接）
        else:
            links.append(x.find_all('a'))

    for index in range(links.__len__()):
        for soul in links[index]:
            strb = stra + soul['href']
            kindurl.append(strb)
    return links, kindurl





    # stra = "https://www.douyu.com"
    # kindurl = []                     #每一个类别的直接连接地址
    # links = []                       #每一个大类的详细信息
    # for t in total:
    #     links.append(t.find_all('a'))
    # for index in range(links.__len__()):
    #     for soul in links[index]:
    #         strb = stra + soul['href']
    #         kindurl.append(strb)
    # return links, kindurl


# url = "https://www.douyu.com/directory/all/"
# get_links_bak(url)
