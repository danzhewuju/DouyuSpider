#!/usr/bin/python
import pymysql
from Host_info import *
import time,datetime


class Unit_Mysql:
    _user = ""
    _password = ""

    @classmethod
    def set_info(self):
        user = input("请输入mysql用户名:")
        password =input("请输入mysql密码:")
        self._user = user
        self._password = password

    @classmethod
    def connect_db(self):
        return pymysql.connect(
            host='127.0.0.1',
            port=3306,
            user=self._user,
            password=self._password,
            database='douyu',
            charset='utf8'
        )

    @classmethod
    def create_structured(cls):
        # con = cls.connect_db()
        con = pymysql.connect(host='localhost', user=cls._user, passwd=cls._password)
        cur = con.cursor()
        try:
            create_str="DROP DATABASE IF EXISTS douyu"
            cur.execute(create_str)
            con.commit()
            create_str="CREATE DATABASE IF NOT EXISTS douyu "
            cur.execute(create_str)
            con.commit()
            # con.close()
            # cur.close()
            con = cls.connect_db()
            cur = con.cursor()
            # cur.execute("USE douyu")
            # con.commit()
            sql_str1 ="DROP TABLE IF EXISTS host_info"
            cur.execute(sql_str1)
            con.commit()
            sql_str="CREATE TABLE IF NOT EXISTS host_info (" \
                    "id int(11) NOT NULL AUTO_INCREMENT COMMENT 'id序号'," \
                    "room_number char(50) NOT NULL COMMENT '直播间号'," \
                    "username char(200) NOT NULL COMMENT '主播名称'," \
                    "kind char(200) NOT NULL COMMENT '主播类型'," \
                    "online int(11) DEFAULT NULL," \
                    "w_number int(11) DEFAULT NULL COMMENT '观看人数'," \
                    "coefficient float DEFAULT NULL COMMENT '影响因数'," \
                    "link char(200) DEFAULT NULL COMMENT '直播间链接'," \
                    "timestamp timestamp NULL DEFAULT NULL COMMENT '爬取时间', " \
                    "followers int(11) DEFAULT NULL COMMENT '关注人数', PRIMARY KEY (`id`))" \
                    "ENGINE=InnoDB AUTO_INCREMENT=511 DEFAULT CHARSET=utf8"

            cur.execute(sql_str)
            con.commit()
        except:
            con.rollback()
            print("数据库创创建失败！！！")
            raise
        finally:
            cur.close()
            con.close()
    @classmethod
    def insert_db(self, host):
        con = self.connect_db()
        cur = con.cursor()
        try:
            sql_str = "insert into host_info  (username, kind, timestamp, w_number, room_number, link, online, " \
                      "coefficient)" \
                      " values ('%s', '%s','%s','%s','%s','%s','%s','%s')" \
                      % (host.username, host.kind, host.localtime, host.w_number, host.room_number, host.link,
                         host.online, host.coefficient)
            cur.execute(sql_str)
            con.commit()
        except:
            con.rollback()
            print("插入错误!")
            raise
        finally:
            cur.close()
            con.close()


# host = Host()
# host.username = "大仙"
# host.kind = "王者荣耀"

# for index in range(10):
#     time1 = int(time.time())
#     print(time1)
#     timearray = time.localtime(time1)
#     datetime1 = time.strftime("%Y-%m-%d %H:%M:%S")
#     print(datetime1)
# time1 = int(time.time())
# print(time1)
# timearray = time.localtime(time1)
# print(timearray)
# datetime1 = time.strftime("%Y-%m-%d %H:%M:%S")
# print(datetime1)


# print(host.localtime)
# host.w_number = 1960000
# host.followers = 12000000
# host.coefficient = host.w_number / host.followers
# user =Unit_Mysql()
# user.insert_db(host)
